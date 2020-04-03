from __future__ import print_function
import click
from kubernetes import client, config
from os import path

import yaml

import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable


def showpods():
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



def shownodes():
    config.load_kube_config()

    v2 = client.CoreV1Api()
    print("Listing nodes with their IPs:")
    ret = v2.list_node()
    for i in ret.items:
        print(i.metadata.name)
       # print("%s\t%s" % (i.metadata.name,i.status.type))


def configmaps():
    config.load_kube_config()

    v3 = client.CoreV1Api()
    print("Listing config maps with their IPs:")
    ret = v3.list_config_map_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.name)


def secrets():
    config.load_kube_config()

    v4 = client.CoreV1Api()
    print("Listing secrets with their IPs:")
    ret = v4.list_secret_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.name)


def services():
    config.load_kube_config()

    v5 = client.CoreV1Api()
    print("Listing services with their IPs:")
    ret = v5.list_service_for_all_namespaces()
    for i in ret.items:
        print(i.metadata.namespace, i.metadata.name, i.spec.ports[0].node_port, i.spec.ports[0].port, i.spec.type)

def namespaces():
    config.load_kube_config()
    v6 = client.CoreV1Api()
    print("Listing namespaces with their IPs:")
    ret = v6.list_namespace()
    for i in ret.items:
        print(i.metadata.name)

def create_deployment():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "nginx-deployment.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

