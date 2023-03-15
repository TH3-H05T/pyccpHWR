from setuptools import find_packages,setup

find_packages()

setup(
    name='pyccpHWR',
    version='0.1',
    packages=['pyccpHWR', 'pyccpHWR.tests'],
    url='https://github.com/TH3-H05T/pyccpHWR',
    license='',
    author='aryam',
    author_email='arya.mortazavi2004@gmail.com',
    description='ccp library for HWR'
)
install_requires = [
    'enum34',
    'mock',
    'future',
    'mako',

]
