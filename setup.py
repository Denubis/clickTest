from setuptools import setup

setup(
    name='yourscript',
    version='0.1',
    py_modules=['FactoryFactotum'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=FactoryFactotum:cli
    ''',
)