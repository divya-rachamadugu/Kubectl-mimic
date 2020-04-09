from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

#lists namespaces
def list_namespaces():
    config.load_kube_config()
    v6 = client.CoreV1Api()
    print("Listing namespaces with their IPs:")
    ret = v6.list_namespace()
    for i in ret.items:
        print(i.metadata.name)

# create namespace
def create_namespace():
    config.load_kube_config()
    v13 = client.CoreV1Api()
    job_name='test2'
    api_instance = kubernetes.client.CoreV1Api(v13.api_client)
    body = kubernetes.client.V1Namespace() # V1Namespace | 
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name)
    
    pretty = 'pretty_example'
    try:
        api_response = api_instance.create_namespace(body,pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)

# delete namespace
def delete_namespace():
    
    config.load_kube_config()
    v20 = client.CoreV1Api()
    api_instance = kubernetes.client.CoreV1Api(v20.api_client)
    name = 'test2'
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespace(name, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespace: %s\n" % e)