from setuptools import setup, find_packages

from meeting.version import Version

setup(
    name='meeting',
    version=Version('1.0.0').number,
    description='Festival management application: '
    'Tickets E-Commerce, '
    'Tickets validation on Lobby (Web, Paper, Guest, '
    'Local Purchase) and '
    'Sells on Wristband/Card (Beverage, Food, Souvenir, etc).',
    long_description=open('README.rst').read().strip(),
    author='Paulo R',
    author_email='proberto.macedo@gmail.com',
    url='http://github.com/mauler/meeting',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'django',
        'djangorestframework',
    ],
    zip_safe=False,
    keywords='festival rfid qrcode barcode tickets',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: '
        'Python Modules'])
