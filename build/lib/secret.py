from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

# lists secrets

def list_secrets():
    config.load_kube_config()
    v4 = client.CoreV1Api()
    print("Listing secrets with their IPs:")
    ret = v4.list_secret_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.name)

# create namespaced secret
def create_namespaced_secret():
    config.load_kube_config()
    v19 = client.CoreV1Api()

    api_instance = kubernetes.client.CoreV1Api(v19.api_client)
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1Secret()
    job_name= 'secret2'
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name)
    body.data={
        "username": "YWRtaW4=",
        "password": "ZGl2eWExMjM="
    }
    try:
        api_response = api_instance.create_namespaced_secret(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_secret: %s\n" % e)

# delete namespaced secret

def delete_namespaced_secret():
    config.load_kube_config()
    v25 = client.CoreV1Api()

    api_instance = kubernetes.client.CoreV1Api(v25.api_client)
    name = 'secret2' # str | name of the Pod
    
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespaced_secret(name, namespace,body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespaced_secret: %s\n" % e)