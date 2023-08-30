import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='kb-django-dramatiq',
    packages=['tests', 'tests.testapp2', 'tests.testapp2.migrations', 'tests.testapp1', 'tests.testapp1.migrations', 'tests.testapp3', 'tests.testapp3.tasks', 'tests.testapp3.tasks.utils', 'tests.testapp3.migrations', 'django_dramatiq', 'django_dramatiq.migrations', 'django_dramatiq.management', 'django_dramatiq.management.commands'],
    version='0.0.08',
    description='django_dramatiq',
    author='Patrick Kimber',
    author_email='patrick@kbsoftware.co.uk',
    url='git@github.com:pkimber/django_dramatiq.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 1.8',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)