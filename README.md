# Python API for docker registry v2 API

I needed this as a simple way to deal with API pagination 
and to give me the ability to delete images from my private registry.

I only use basic auth username/password on my registrey so I have only implemented that.

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

import dockerRegistryPythonClient
client = dockerRegistryPythonClient.RegistryClient(baseURL="https://registryurl.com")

username="uu"
password="pp"
loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

qualifiedImageName="imagename:tagname"
imageMetadata = client.getImageMetadata(loginSession, qualifiedImageName)

imageMetadata.delete(registryClient=client, loginSession=loginSession)

### Delete all images not on a whitelist TODO


