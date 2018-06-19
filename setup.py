import os
from setuptools import setup
from sys import version_info

NAME = 'leanpub'
VERSION = '0.1.2'


def readme():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst', format='md')
    except (IOError, ImportError):
        with open('README.md') as f:
            return f.read()

INSTALL_REQUIRES = (
    ['argh'] +
    ['watchdog']
)

setup(
    name=NAME,
    version=VERSION,
    description="Build leanpub books locally. Watch files and build a new "
                "pdf each time they change.",
    long_description=readme(),
    license='MIT License',
    author='Andy Hayden',
    author_email='andyhayden1@gmail.com',
    url='https://github.com/hayd/leanpub',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='automation, pdf, format',
    install_requires=INSTALL_REQUIRES,
    packages=['leanpub'],
    # test_suite='tests',
    entry_points={'console_scripts': ['leanpub = leanpub.__main__:main']},
)

