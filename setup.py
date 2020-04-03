from setuptools import setup

setup(
    name='click-example-colors',
    version='1.0',
    py_modules=['colors','colorssss'],
    
    include_package_data=True,
    install_requires=[
        'click',
        'kubernetes',
        'future',
        'pprint',
        'prettytable'
        
    ],
    entry_points='''
        [console_scripts]
        colors=colors:cli
        hello=colorssss:hello
        showpods=colors:showpods
        shownodes=colors:shownodes
        services=colors:services
        secrets=colors:secrets
        configmaps=colors:configmaps
        namespaces=colors:namespaces
        
    ''',
)