from setuptools import setup, find_packages


packages = ['meeting.{}'.format(i)
            for i in find_packages('meeting', exclude=['tests'])]

setup(
    name='meeting',
    version=open('VERSION').read().strip(),
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
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    install_requires=[
        'django',
        # 'djangorestframework',
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
