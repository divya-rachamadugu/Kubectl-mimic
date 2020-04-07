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
        get_api_group=colors:get_api_group
        list_deployment=colors:list_deployment
        create_namespace=colors:create_namespace
        deamonset=colors:deamonset
        replicaset=colors:replicaset
        create_daemonset=colors:create_daemonset
        create_namespaced_pod=colors:create_namespaced_pod
        
    ''',
)