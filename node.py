from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

def list_nodes():
    config.load_kube_config()
    v2 = client.CoreV1Api()
    print("Listing nodes with their IPs:")
    ret = v2.list_node()
    for i in ret.items:
        print(i.metadata.name)