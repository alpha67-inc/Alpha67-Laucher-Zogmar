

from crashreporter import CrashReporter
    
    class Person(object):
    
        def __init__(self, name, age=None):
            self.name = name
            self.age = age
    
    def combine_ages(person_a, person_b):
        a_local_variable = 134
        return person_a.age + person_b.age, Person.__name__
    
    if __name__ == '__main__':
        # Note I have used a configuration file for setting up SMTP and HQ accounts but you can also call functions
        # cr.setup_smtp() and cr.setup_hq() with your credentials to configure SMTP/HQ respectively.
        cr = CrashReporter(report_dir='/home/calvin/crashreporter',
                           check_interval=10,
                           config='./crashreporter.cfg')
    
        cr.application_name = 'My App'
        cr.application_version = '1.1.350'
    
        calvin = Person('calvin', age=25)
        bob = Person('bob')
        combine_ages(calvin, bob)
    
        while 1:
            pass


