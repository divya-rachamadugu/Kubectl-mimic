from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

# lists configmaps

def list_configmaps():
    config.load_kube_config()
    v3 = client.CoreV1Api()
    print("Listing config maps with their IPs:")
    ret = v3.list_config_map_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.name)

# create namespaced configmap

def create_namespaced_configmap():
    
    config.load_kube_config()
    v18 = client.CoreV1Api()

    api_instance = kubernetes.client.CoreV1Api(v18.api_client)
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1ConfigMap()
    job_name= 'game-config2'
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name)
    body.data={
        "enemies": "aliens",
        "lives": "3",
        "enemies.cheat": "true",
        "enemies.cheat.level": "noGoodRotten",
        "secret.code.passphrase": "UUDDLRLRBABAS",
        "secret.code.allowed": "true",
        "secret.code.lives": "30"
    } 

    try:
        api_response = api_instance.create_namespaced_config_map(namespace, body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)

# delete namespaced configmap

def delete_namespaced_configmap():
    config.load_kube_config()
    v24 = client.CoreV1Api()

    api_instance = kubernetes.client.CoreV1Api(v24.api_client)
    name = 'game-config2' # str | name of the Pod
    
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespaced_config_map(name, namespace,body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespaced_configmap: %s\n" % e)