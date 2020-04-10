# kubernetes.client

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/kubernetes-client/python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/kubernetes-client/python.git`)

Then import the package:
```python
import kubernetes.client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## List of Commands 

--
lists all pods

    list_pods

--
lists all nodes

    list_nodes

--
lists all services
	
	list_services   

--
lists all secrets

	list_secrets
	
--
lists  all configmaps
		
	list_configmaps  
    
--
lists all namespaces

	list_namespaces   

--	
lists all api groups

	get_api_group  

--	
lists all deployments

	list_deployments 

--
creates namespace

	create_namespace      

--
lists all daemonsets 

	list_daemonsets  
	
--
lists all replicasets

	list_replicasets    
	
--
creates namespaced daemonset

	create_namespaced_daemonset

--
creates namespaced pod 

	create_namespaced_pod   

--
creates namespaced service  

	create_namespaced_service    

--
creates namespaced deployment 

	create_namespaced_deployment      

--
creates namespaced replicaset 

	create_namespaced_replicaset 

--
creates namespaced configmap

	create_namespaced_configmap

--
creates namespaced secret     

	create_namespaced_secret      

--
deletes namespace     

	delete_namespace     

--
deletes namespaced pod

	delete_namespaced_pod    

--
deletes namespaced deployment 

	delete_namespaced_deployment 

--
deletes namespaced service  

	delete_namespaced_service       

--
deletes namespaced configmap   

	delete_namespaced_configmap   

--
deletes namespaced secret

	delete_namespaced_secret 

--
deletes namespaced replicaset

	delete_namespaced_replicaset
