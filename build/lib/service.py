from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

#lists services

def list_services():
    config.load_kube_config()
    v5 = client.CoreV1Api()
    print("Listing services with their IPs:")
    ret = v5.list_service_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.namespace, i.metadata.name, i.spec.ports[0].node_port, i.spec.ports[0].port, i.spec.type)


# create namespaced_service

def create_namespaced_service():

    config.load_kube_config()
    v15 = client.CoreV1Api()
    api_instance = kubernetes.client.CoreV1Api(v15.api_client)
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1Service() # V1Service |
    job_name='my-nginx2'
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name) 
    ports=kubernetes.client.V1ServicePort(port=80,target_port=80)
    selector={
        "run": "my-nginx"
    }
    body.spec=client.V1ServiceSpec(ports=[ ports ],selector=selector)
     
    try:
        api_response = api_instance.create_namespaced_service(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

# delete namespaced service

def delete_namespaced_service():
    config.load_kube_config()
    v23 = client.CoreV1Api()

    api_instance = kubernetes.client.CoreV1Api(v23.api_client)
    name = 'my-nginx2' # str | name of the Pod
    
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespaced_service(name, namespace,body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespaced_service: %s\n" % e)