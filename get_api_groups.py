from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

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