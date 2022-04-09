"""Library for creating crash reports

Positional arguments
--------------------
etype: Optional[Type[BaseException]]
    The type of the exception. Ignored. For sys.excepthook
    compatibility mainly
value: Optional[BaseException]
    The exception object itself. If passed as None,
    it will default to sys.exc_info()[1]
tb: Optional[TracebackType]
    The traceback object. If passed as None,
    it will default to value.__traceback__

Keyword arguments
-----------------
"""

import io
import os
import pprint
import sys
import time
import traceback
from types import FrameType, TracebackType
from typing import Any, Callable, Dict, Optional, Set, TextIO, Type, Union

__author__ = 'Josiah (Gaming32) Glosson'

__license__ = 'MIT'
__version__ = '1.1.1'
__email__ = 'gaming32i64@gmail.com'

__all__ = [
    'dump_report_to_file',
    'dump_report',
    'format_report',
    'inject_excepthook'
]


def _get_main_name() -> str:
    import __main__
    return os.path.splitext(os.path.basename(__main__.__file__))[0]


def _write_separator(f: TextIO, count: int = 1) -> int:
    text = '\n'.join('='*75 for _ in range(count))
    return f.write('\n\n' + text + '\n\n')


def _exhaustive_vars(obj: Any) -> Dict[str, Any]:
    return {name: getattr(obj, name) for name in dir(obj)}


def _variable_summary(f: TextIO, vars: Dict[str, Any], indent: int = 0) -> None:
    for (name, value) in vars.items():
        label = f'{" "*indent}{name} => '
        total_indent = len(label)
        formatted = pprint.pformat(value)
        formatted = formatted.replace('\n', '\n' + ' '*total_indent)
        f.write(f'{label}{formatted}\n')


_RECURSIVE_CUTOFF = 3
def _trace_exchaustive(result: TextIO, exc: BaseException, tb: Optional[TracebackType], show_locals: bool, show_globals: bool, seen: Set[int]) -> None:
    if tb is None:
        return
    seen.add(id(exc))
    last_file = None
    last_line = None
    last_name = None
    count = 0
    cause = exc.__cause__
    if cause is not None and id(cause) not in seen:
        _trace_exchaustive(result, cause, cause.__traceback__, show_locals, show_globals, seen)
        result.write('The above exception was the direct cause of the following exception:\n')
    context = exc.__context__
    if context is not None and id(context) not in seen and not exc.__suppress_context__:
        _trace_exchaustive(result, context, context.__traceback__, show_locals, show_globals, seen)
        result.write('During handling of the above exception, another exception occurred:\n')
    result.write('Following is an exhaustive stack trace (most recent call last) for ')
    result.write(repr(exc))
    _write_separator(result)
    frame: FrameType
    for (frame, lineno) in traceback.walk_tb(tb):
        co = frame.f_code
        filename = co.co_filename
        name = co.co_name
        summary = traceback.FrameSummary(filename, lineno, name, lookup_line=True)
        if (last_file is None or last_file != filename or
            last_line is None or last_line != lineno or
            last_name is None or last_name != name):
            if count > _RECURSIVE_CUTOFF:
                count -= _RECURSIVE_CUTOFF
                result.write(
                    f'  [Previous frame repeated {count} more '
                    f'time{"s" if count > 1 else ""}]\n'
                )
            last_file = filename
            last_line = lineno
            last_name = name
            count = 0
        count += 1
        if count > _RECURSIVE_CUTOFF:
            _write_separator(result)
            continue
        result.write(f'File "{filename}", line {lineno}, in {name}\n')
        if summary.line:
            result.write(f'--->  {summary.line.strip()}\n\n')
        if frame.f_locals and show_locals:
            result.write('Local variables:\n')
            _variable_summary(result, frame.f_locals)
            if frame.f_globals and show_globals:
                result.write('\n')
        if frame.f_globals and show_globals:
            result.write('Global variables:\n')
            _variable_summary(result, frame.f_globals)
        _write_separator(result)
    if count > _RECURSIVE_CUTOFF:
        count -= _RECURSIVE_CUTOFF
        result.write(
            f'  [Previous frame repeated {count} more '
            f'time{"s" if count > 1 else ""}]\n'
        )


def _recursive_exc_var_dump(file: TextIO, exc: BaseException, seen: Set[int], indent: int = 0) -> None:
    seen.add(id(exc))
    vars = _exhaustive_vars(exc)
    cause = vars.pop('__cause__')
    context = vars.pop('__context__')
    show_cause = cause is not None and id(cause) not in seen
    show_context = context is not None and id(context) not in seen and not exc.__suppress_context__
    _variable_summary(file, vars, indent)
    if show_cause:
        file.write(' '*indent + '__cause__ =>\n')
        _recursive_exc_var_dump(file, cause, seen, indent + 13)
    else:
        _variable_summary(file, {'__cause__': cause}, indent)
    if show_context:
        file.write(' '*indent + '__context__ =>\n')
        _recursive_exc_var_dump(file, context, seen, indent + 15)
    else:
        _variable_summary(file, {'__context__': context}, indent)


def dump_report_to_file(file: Union[TextIO, str],
        etype: Optional[Type[BaseException]], value: Optional[BaseException],
        tb: Optional[TracebackType], *, show_locals: bool = True,
        show_globals: bool = True, show_main_globals: bool = True,
        show_sys: bool = True, show_simple_tb: bool = True,
        show_exception_vars: bool = True,
        show_exc_vars_recur: bool = True,
        custom_values: Dict[str, Union[Any, Callable[[], Any]]] = None
    ) -> None:
    """Dumps an exception dump to the specified file-like object or file name

Arguments
---------
file: Union[TextIO, str]
    A file-like object or filename to dump the report to"""

    if isinstance(file, str):
        with open(file, 'w') as fp:
            dump_report_to_file(fp, etype, value, tb,
                show_locals=show_locals,
                show_globals=show_globals,
                show_main_globals=show_main_globals,
                show_sys=show_sys,
                show_simple_tb=show_simple_tb,
                show_exception_vars=show_exception_vars,
                show_exc_vars_recur=show_exc_vars_recur,
                custom_values=custom_values)
            return

    if value is None:
        value = sys.exc_info()[1]
    if value is None:
        return

    import __main__
    etype = type(value)

    if tb is None:
        tb = value.__traceback__

    # Write name and date and additional info
    file.write(f'"{__main__.__file__}" crashed at {time.strftime("%Y-%m-%dT%H:%M:%S%z")} ({time.strftime("%F %H:%M:%S %Z")})\n\n')
    if custom_values is None:
        custom_values = {
            'os.getcwd()': os.getcwd,
            'os.environ': (lambda: dict(os.environ)),
        }
    for (key, custom_value) in custom_values.items():
        if callable(custom_value):
            custom_values[key] = custom_value()
    _variable_summary(file, custom_values)
    _write_separator(file)

    # Write traceback
    if show_simple_tb:
        tb_lines = traceback.format_exception(etype, value, tb)
        file.write(''.join(tb_lines))
        _write_separator(file)

    # Write the contents of the exception
    if show_exception_vars:
        file.write('Summary of exception variables:\n')
        if show_exc_vars_recur:
            _recursive_exc_var_dump(file, value, set())
        else:
            _variable_summary(file, _exhaustive_vars(value))
        _write_separator(file)

    show_exhaustive = show_locals or show_globals

    # Write the contents of sys
    if show_sys:
        file.write('Summary of sys variables:\n')
        _variable_summary(file, _exhaustive_vars(sys))
        _write_separator(file, 3 if show_exhaustive else 1)

    # Write an exhaustive stack trace that shows all
    # locals and globals (configurable) of the entire stack
    if show_exhaustive:
        _trace_exchaustive(file, value, tb, show_locals, show_globals, set())

    # Write the main globals for the program
    # This is included in the exhaustive stack trace,
    # so we don't show it when we show an exhastive stack trace.
    elif show_main_globals:
        file.write('Summary of __main__ globals:\n')
        _variable_summary(file, _exhaustive_vars(__main__))
        _write_separator(file)


def dump_report(etype: Optional[Type[BaseException]],
        value: Optional[BaseException], tb: Optional[TracebackType], *,
        show_locals: bool = True, show_globals: bool = True,
        show_main_globals: bool = True, show_sys: bool = True,
        show_simple_tb: bool = True, show_exception_vars: bool = True,
        show_exc_vars_recur: bool = True,
        custom_values: Dict[str, Union[Any, Callable[[], Any]]] = None
    ) -> str:
    """Dumps a report to a file named "{main_filename}-%Y-%m-%d-%H-%M-%S.dump

Returns
-------
The filename the report was dumped to"""
    filename = f'{_get_main_name()}-{time.strftime("%Y-%m-%d-%H-%M-%S")}.dump'

    dump_report_to_file(filename, etype, value, tb,
        show_locals=show_locals,
        show_globals=show_globals,
        show_main_globals=show_main_globals,
        show_sys=show_sys,
        show_simple_tb=show_simple_tb,
        show_exception_vars=show_exception_vars,
        show_exc_vars_recur=show_exc_vars_recur,
        custom_values=custom_values)

    return filename


def format_report(etype: Optional[Type[BaseException]],
        value: Optional[BaseException], tb: Optional[TracebackType], *,
        show_locals: bool = True, show_globals: bool = True,
        show_main_globals: bool = True, show_sys: bool = True,
        show_simple_tb: bool = True, show_exception_vars: bool = True,
        show_exc_vars_recur: bool = True,
        custom_values: Dict[str, Union[Any, Callable[[], Any]]] = None
    ) -> str:
    """Returns a report in string form

Returns
-------
The string value of the report"""
    result = io.StringIO()

    dump_report_to_file(result, etype, value, tb,
        show_locals=show_locals,
        show_globals=show_globals,
        show_main_globals=show_main_globals,
        show_sys=show_sys,
        show_simple_tb=show_simple_tb,
        show_exception_vars=show_exception_vars,
        show_exc_vars_recur=show_exc_vars_recur,
        custom_values=custom_values)

    return result.getvalue()


def inject_excepthook(
        callback: Optional[Callable[[Type[BaseException], BaseException, TracebackType, str], Any]] = None, *,
        show_locals: bool = True, show_globals: bool = True,
        show_main_globals: bool = True, show_sys: bool = True,
        show_simple_tb: bool = True, show_exception_vars: bool = True,
        show_exc_vars_recur: bool = True,
        custom_values: Dict[str, Union[Any, Callable[[], Any]]] = None
    ) -> Callable[[Type[BaseException], BaseException, TracebackType], Any]:
    """Inject dump_report into sys.excepthook. This allows you to specify
configuration, which is not possible if you inject the excepthook directly

Arguments
---------
callback: Callable[[Type[BaseException], BaseException, TracebackType, str], Any]
    Called with (etype, value, tb, dumped_filename) when exception passed
    through sys.excepthook. If the the exception was not a subclass of Exception
    (such as SystemExit or KeyboardInterrupt), dumped_filename will be None, and
    the old excepthook will be called.

Returns
-------
The old excepthook"""
    old_excepthook = sys.excepthook

    def excepthook(etype, value, tb):
        if issubclass(etype, Exception):
            dest = dump_report(etype, value, tb,
                show_locals=show_locals,
                show_globals=show_globals,
                show_main_globals=show_main_globals,
                show_sys=show_sys,
                show_simple_tb=show_simple_tb,
                show_exception_vars=show_exception_vars,
                show_exc_vars_recur=show_exc_vars_recur,
                custom_values=custom_values)
            if callback is not None:
                callback(etype, value, tb, dest)
            sys.exit(1)
        elif callback is not None:
            callback(etype, value, tb, None)
        old_excepthook(etype, value, tb)

    sys.excepthook = excepthook
    return old_excepthook
