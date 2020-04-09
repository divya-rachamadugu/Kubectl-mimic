from __future__ import print_function
import click
from kubernetes import client, config
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from prettytable import PrettyTable

# lists daemonsets
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