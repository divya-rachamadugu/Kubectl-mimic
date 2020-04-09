from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

# lists deployments

def list_deployments():
    config.load_kube_config()
    v8 = client.CoreV1Api()

    # create an instance of the API class
    api_instance = kubernetes.client.AppsV1Api(v8.api_client)
    pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
    
    try:
        api_response = api_instance.list_deployment_for_all_namespaces(pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->list_deployment_for_all_namespaces: %s\n" % e)

# create namespaced deployment

def create_namespaced_deployment():

    config.load_kube_config()
    v16 = client.CoreV1Api()

    api_instance = kubernetes.client.AppsV1Api(v16.api_client)
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1Deployment() # V1Deployment | 
    job_name= 'my-nginx2'
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name) 
    replicas=3
    match_labels={
        "web": "component"
    }
    selector=kubernetes.client.V1LabelSelector(match_labels=match_labels)
    labels={
        "web": "component"
    }
    pod_name='my-nginx'
    container = kubernetes.client.V1Container(name=pod_name)
    container.image = "nginx"
 
    template = kubernetes.client.V1PodTemplateSpec()
    template.spec = kubernetes.client.V1PodSpec(containers=[container])
    template.metadata=kubernetes.client.V1ObjectMeta(labels=labels)


    body.spec=kubernetes.client.V1DeploymentSpec(template=template,replicas=replicas,selector=selector)
    
    
    try:
        api_response = api_instance.create_namespaced_deployment(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)

# delete namespaced deployments

def delete_namespaced_deployment():
    config.load_kube_config()
    v22 = client.AppsV1Api()

    api_instance = kubernetes.client.AppsV1Api(v22.api_client)
    name = 'my-nginx2' # str | name of the Deployment
    
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespaced_deployment(name, namespace, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->delete_namespaced_deployment: %s\n" % e)