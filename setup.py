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
        list_pods=colors:list_pods
        list_nodes=colors:list_nodes
        list_services=colors:list_services
        list_secrets=colors:list_secrets
        list_configmaps=colors:list_configmaps
        list_namespaces=colors:list_namespaces
        get_api_group=colors:get_api_group
        list_deployments=colors:list_deployments
        create_namespace=colors:create_namespace
        list_daemonsets=colors:list_daemonsets
        list_replicasets=colors:list_replicasets
        create_namespaced_daemonset=colors:create_namespaced_daemonset
        create_namespaced_pod=colors:create_namespaced_pod
        create_namespaced_service=colors:create_namespaced_service
        create_namespaced_deployment=colors:create_namespaced_deployment
        create_namespaced_replicaset=colors:create_namespaced_replicaset
        create_namespaced_configmap=colors:create_namespaced_configmap
        create_namespaced_secret=colors:create_namespaced_secret
        delete_namespace=colors:delete_namespace
        delete_namespaced_pod=colors:delete_namespaced_pod
        delete_namespaced_deployment=colors:delete_namespaced_deployment
        delete_namespaced_service=colors:delete_namespaced_service
        delete_namespaced_configmap=colors:delete_namespaced_configmap
        delete_namespaced_secret=colors:delete_namespaced_secret
        delete_namespaced_replicaset=colors:delete_namespaced_replicaset

    ''',
)