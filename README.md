# Python API for docker registry v2 API

I created this client because I have a private docker registry based on the docker image
and a CI process that builds images and places them into the registry.

As my system moves through versions images build up on the registry increasing storage costs.

I have created a script which uses the deleteNonWhitelistedTags api of the client to delete
images that I no longer need on the repository.


TODO
 - find out if garbage collection is run periodically in standard image or I need to run it
 - find out if there is an API to run the garbage collection process
 
```
registry garbage-collect /etc/docker/registry/config.yml
``` 

## Usage Examples

### List Catalogs on server:

```
import dockerRegistryPythonClient
client = dockerRegistryPythonClient.RegistryClient(baseURL="https://registryurl.com")

username="uu"
password="pp"
loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

loginSession.testValid()

catalogs = client.getCatalogIterator(loginSession=loginSession)
for catalog in catalogs:
  print(catalog)
```

The returned catalogs are just strings.

### List tags for a catalog on server:

```
import dockerRegistryPythonClient
client = dockerRegistryPythonClient.RegistryClient(baseURL="https://registryurl.com")

username="uu"
password="pp"
loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

tags = client.getTagsForCatalogIterator(loginSession=loginSession, catalogName="repourl/challengeapp")
for tag in tags:
  print(tag)

```

catalogName is just the name retrieved by the catalog iterator.

### Get a digest for an image

```
import dockerRegistryPythonClient
client = dockerRegistryPythonClient.RegistryClient(baseURL="https://registryurl.com")

username="uu"
password="pp"
loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

imageMetadata = client.getImageMetadata(loginSession, qualifiedImageName)

print(imageMetadata.getDigest())
```

### Delete an image

```
import dockerRegistryPythonClient
client = dockerRegistryPythonClient.RegistryClient(baseURL="https://registryurl.com")

username="uu"
password="pp"
loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

qualifiedImageName="imagename:tagname"
imageMetadata = client.getImageMetadata(loginSession, qualifiedImageName)

imageMetadata.delete(registryClient=client, loginSession=loginSession)
```
### Delete all images not on a whitelist 
```
import dockerRegistryPythonClient
client = dockerRegistryPythonClient.RegistryClient(baseURL="https://registryurl.com")

username="uu"
password="pp"
loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)


whiteList = [
  "myimage:0.1.19",
  "myotherimage:0.1.1"
]

client.deleteNonWhitelistedTags(loginSession=loginSession, whiteList=whiteList)
```
