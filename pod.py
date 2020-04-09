from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

# lists pods
def list_pods():

    config.load_kube_config()
    v1 = client.CoreV1Api()

    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    elements=ret.items

    pods_names = [pod.metadata.name for pod in elements]
    pods_status = [pod.status.phase for pod in elements]  
    pods_namespace = [pod.metadata.namespace for pod in elements]
    pods_ip = [pod.status.pod_ip for pod in elements]

    table = PrettyTable(['POD NAME', 'STATUS', 'NAMESPACE', 'IP' ])
    for i in range(len(elements)):
        table.add_row(list(zip(pods_names, pods_status, pods_namespace, pods_ip))[i])
    print(table)


# create pod

def create_namespaced_pod():
    
    config.load_kube_config()
    v14 = client.CoreV1Api() 

    api_instance = kubernetes.client.CoreV1Api(v14.api_client)
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    job_name='test3'
    body = kubernetes.client.V1Pod() # V1Pod | 
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name)
    container = kubernetes.client.V1Container(name="busybox")
    container.image = "busybox"
    container.args = ["sleep", "10"]
    body.spec = client.V1PodSpec(containers=[container])
   
    try:
        api_response = api_instance.create_namespaced_pod(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)

# delete namspaced pod
def delete_namespaced_pod():
    config.load_kube_config()
    v21 = client.CoreV1Api()

    api_instance = kubernetes.client.CoreV1Api(v21.api_client)
    name = 'test' # str | name of the Pod
    
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespaced_pod(name, namespace,body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespaced_pod: %s\n" % e)