from setuptools import setup


with open('README.md') as fp:
    long_description = fp.read()


setup(
    name = 'crashreport',
    version = '1.1.1',
    description = 'Python crash reporting library',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Josiah (Gaming32) Glosson',
    author_email = 'gaming32i64@gmail.com',
    url = 'https://github.com/Gaming32/crashreport',
    project_urls = {
        'Source': 'https://github.com/Gaming32/crashreport',
    },
    py_modules = [
        'crashreport',
    ],
    license = 'License :: OSI Approved :: MIT License'
)
