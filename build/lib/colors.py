from __future__ import print_function
import click
from kubernetes import client, config


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

def get_api_group():

    config.load_kube_config()
    v7 = client.CoreV1Api()
    
    # Configure API key authorization: BearerToken
    #configuration = kubernetes.client.Configuration()
    #configuration.api_key['authorization'] = 'YOUR_API_KEY'
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['authorization'] = 'Bearer'

    # create an instance of the API class
    api_instance = kubernetes.client.AdmissionregistrationApi(v7.api_client)

    try:
        api_response = api_instance.get_api_group()
        print(api_response)
    except ApiException as e:
        print("Exception when calling AdmissionregistrationApi->get_api_group: %s\n" % e)

def list_deployment():

    config.load_kube_config()
    v8 = client.CoreV1Api()
    #configuration = kubernetes.client.Configuration()
    #configuration.api_key['authorization'] = 'YOUR_API_KEY'
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['authorization'] = 'Bearer'

    # create an instance of the API class
    api_instance = kubernetes.client.AppsV1Api(v8.api_client)
   # allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.  This field is alpha and can be changed or removed without notice. (optional)
    #_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    #field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    #label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    #limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
    #resource_version = 'resource_version_example' # str | Wh7en specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
   # timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
   # watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    try:
        api_response = api_instance.list_deployment_for_all_namespaces(pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->list_deployment_for_all_namespaces: %s\n" % e)


def deamonset():
    config.load_kube_config()
    v10 = client.CoreV1Api()
    api_instance = kubernetes.client.AppsV1Api(v10.api_client)
    namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
    pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
   # allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.  This field is alpha and can be changed or removed without notice. (optional)
    #_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    #field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    #label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    #limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    #resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
    #timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    #watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    try:
        api_response = api_instance.list_namespaced_daemon_set(namespace,pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->list_namespaced_daemon_set: %s\n" % e)

def replicaset():
    config.load_kube_config()
    v11 = client.CoreV1Api()


    api_instance = kubernetes.client.AppsV1Api(v11.api_client)
    namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
    pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
   # allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.  This field is alpha and can be changed or removed without notice. (optional)
    #_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    #field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    #label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    #limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    #resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
    #timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    #watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    try:
        api_response = api_instance.list_namespaced_replica_set(namespace, pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->list_namespaced_replica_set: %s\n" % e)

def create_daemonset():
    config.load_kube_config()
    v12 = client.CoreV1Api()
    job_name='test'
    api_instance = kubernetes.client.AppsV1Api(v12.api_client)
    namespace = 'kubectl-mimic' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1DaemonSet()# V1DaemonSet | 
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name)
    template = kubernetes.client.V1PodTemplate()
    template.template = kubernetes.client.V1PodTemplateSpec()
    container = kubernetes.client.V1Container(name="busybox")
    container.image = "busybox"
    container.args = ["sleep", "10"]
    container.restart_policy = 'Never'
    template.template.spec = kubernetes.client.V1PodSpec(restart_policy='Never', containers=[container])
    #body.spec = kubernetes.client.V1JobSpec(template=template, backoff_limit=0)
     
    pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
    # dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    #field_manager = 'daemonset' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    try:
        api_response = api_instance.create_namespaced_daemon_set(namespace, body, pretty=pretty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->create_namespaced_daemon_set: %s\n" % e)

def create_namespace():
    config.load_kube_config()
    v13 = client.CoreV1Api()
    job_name='test'
    api_instance = kubernetes.client.CoreV1Api(v13.api_client)
    body = kubernetes.client.V1Namespace() # V1Namespace | 
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name)
    
    pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
    #dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    #field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

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
    job_name='test'
    body = kubernetes.client.V1Pod() # V1Pod | 
    body.metadata = kubernetes.client.V1ObjectMeta(name=job_name)
    #template = kubernetes.client.V1PodTemplate()
    #template.template = kubernetes.client.V1PodTemplateSpec()
    container = kubernetes.client.V1Container(name="busybox")
    container.image = "busybox"
    container.args = ["sleep", "10"]
  
    
    body.spec = client.V1PodSpec(containers=[container])
    #pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
    #dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    #field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    try:
        api_response = api_instance.create_namespaced_pod(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)

