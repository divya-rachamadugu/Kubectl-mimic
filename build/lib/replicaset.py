from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

# lists replicasets
def list_replicasets():
    config.load_kube_config()
    v11 = client.CoreV1Api()

    api_instance = kubernetes.client.AppsV1Api(v11.api_client)
    namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
    pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
   
    try:
        api_response = api_instance.list_namespaced_replica_set(namespace, pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->list_namespaced_replica_set: %s\n" % e)

# create namespaced replicaset
def create_namespaced_replicaset():


    config.load_kube_config()
    v17 = client.CoreV1Api()

    api_instance = kubernetes.client.AppsV1Api(v17.api_client)
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1ReplicaSet() # V1ReplicaSet | 
    job_name= 'redis2'
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name) 
    replicas=3
    match_labels={
        "web": "component"
    }
    selector=kubernetes.client.V1LabelSelector(match_labels=match_labels)
    labels={
        "web": "component"
    }
    pod_name='redis'
    container = kubernetes.client.V1Container(name=pod_name)
    container.image = "redis"
 
    template = kubernetes.client.V1PodTemplateSpec()
    template.spec = kubernetes.client.V1PodSpec(containers=[container])
    template.metadata=kubernetes.client.V1ObjectMeta(labels=labels)
    body.spec=kubernetes.client.V1ReplicaSetSpec(template=template,replicas=replicas,selector=selector)

    try:
        api_response = api_instance.create_namespaced_replica_set(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->create_namespaced_replica_set: %s\n" % e)

# delete namespaced replicaset


def delete_namespaced_replicaset():
    config.load_kube_config()
    v26 = client.AppsV1Api()

    api_instance = kubernetes.client.AppsV1Api(v26.api_client)
    name = 'redis2' # str | name of the Deployment
    
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespaced_replica_set(name, namespace, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->delete_namespaced_replica-set: %s\n" % e)