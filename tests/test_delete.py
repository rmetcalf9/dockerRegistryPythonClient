from TestHelperSuperClass import testHelperSuperClass
import dockerRegistryPythonClient
import base64
import json
from SampleData import getSampleMetadata

class test_apiDelete(testHelperSuperClass):
  def test_simple(self):
    baseUrl = "MOCK"
    client = dockerRegistryPythonClient.RegistryClient(baseURL=baseUrl)

    catalogName = "testCatalogName"
    tagName = "testTag"
    digest = "testDigest"
    qualifiedImageName = catalogName + ":" + tagName
    dockerContentDigest = 'sha256:realditefdfddfdf'


    sampleDeleteResponse = {

    }
    client.mock.registerNextResponse(
      reqFnName="delete",
      url="/v2/" + catalogName + "/manifests/" + dockerContentDigest,
      data=None,
      status_code=202,
      contentBytes=base64.b64encode(json.dumps(sampleDeleteResponse).encode()),
      contentHeaders={ "x-remaining": "0"},
      ignoreData=True
    )

    sampleImageMetadata = getSampleMetadata(
      catalogName=catalogName,
      tagName=tagName,
      digest=digest
    )
    client.mock.registerNextResponse(
      reqFnName="get",
      url="/v2/" + catalogName + "/manifests/" + tagName,
      data=None,
      status_code=200,
      contentBytes=base64.b64encode(json.dumps(sampleImageMetadata).encode()),
      contentHeaders={ "x-remaining": "0", "Docker-Content-Digest": dockerContentDigest },
      ignoreData=True
    )

    username = "U"
    password = "P"
    loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

    imageMetadata = client.getImageMetadata(loginSession, qualifiedImageName)
    imageMetadata.delete(registryClient=client, loginSession=loginSession)



