
from setuptools import setup, find_packages, Command
try:
    import pytest
    class PyTest(Command):
        user_options=[]
        def initialize_options(self):pass
        def finalize_options(self):pass
        def run(self):
            args = ['--doctest-modules', '-q', 'granpa']
            pytest.main(args)
except ImportError:
    class PyTest(Command):pass

setup(
    name='granpa',
    scripts=['scripts/granpa_info'],
    entry_points={
        'console_scripts':[
            'granpa = granpa.core:main_func',
            ]
        },
    install_requires=[
        'pytest',
        'python-daemon',
        'ini_parse==dev',
        'meta==dev',
        'doctest_utils==dev',
        ],
    dependency_links=[
        'https://github.com/danse/ini_parse/raw/master/ini_parse.py#egg=ini_parse-dev',
        'https://github.com/danse/meta/raw/master/meta.py#egg=meta-dev',
        'https://github.com/danse/doctest_utils/raw/master/doctest_utils.py#egg=doctest_utils-dev',
        ],
    packages=find_packages(),
    cmdclass={'test':PyTest},
)
