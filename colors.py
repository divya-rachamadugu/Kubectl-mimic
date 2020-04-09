from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable


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



def list_nodes():
    config.load_kube_config()
    v2 = client.CoreV1Api()
    print("Listing nodes with their IPs:")
    ret = v2.list_node()
    for i in ret.items:
        print(i.metadata.name)
     


def list_configmaps():
    config.load_kube_config()
    v3 = client.CoreV1Api()
    print("Listing config maps with their IPs:")
    ret = v3.list_config_map_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.name)


def list_secrets():
    config.load_kube_config()
    v4 = client.CoreV1Api()
    print("Listing secrets with their IPs:")
    ret = v4.list_secret_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.name)


def list_services():
    config.load_kube_config()
    v5 = client.CoreV1Api()
    print("Listing services with their IPs:")
    ret = v5.list_service_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.namespace, i.metadata.name, i.spec.ports[0].node_port, i.spec.ports[0].port, i.spec.type)

def list_namespaces():
    config.load_kube_config()
    v6 = client.CoreV1Api()
    print("Listing namespaces with their IPs:")
    ret = v6.list_namespace()
    for i in ret.items:
        print(i.metadata.name)

def get_api_group():

    config.load_kube_config()
    v7 = client.CoreV1Api()

    # create an instance of the API class
    api_instance = kubernetes.client.AdmissionregistrationApi(v7.api_client)

    try:
        api_response = api_instance.get_api_group()
        print(api_response)
    except ApiException as e:
        print("Exception when calling AdmissionregistrationApi->get_api_group: %s\n" % e)

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


def list_daemonsets():
    config.load_kube_config()
    v10 = client.CoreV1Api()
    api_instance = kubernetes.client.AppsV1Api(v10.api_client)
    namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
    pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
  
    try:
        api_response = api_instance.list_namespaced_daemon_set(namespace,pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->list_namespaced_daemon_set: %s\n" % e)

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

def create_namespaced_pod():
    
    config.load_kube_config()
    v14 = client.CoreV1Api() 

    api_instance = kubernetes.client.CoreV1Api(v14.api_client)
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    job_name='test2'
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

def delete_namespaced_pod():
    config.load_kube_config()
    v21 = client.CoreV1Api()

    api_instance = kubernetes.client.CoreV1Api(v21.api_client)
    name = 'test2' # str | name of the Pod
    
    namespace = 'test' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

    try:
        api_response = api_instance.delete_namespaced_pod(name, namespace,body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespaced_pod: %s\n" % e)

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