from TestHelperSuperClass import testHelperSuperClass
import dockerRegistryPythonClient
import base64
import json
from SampleData import getSampleMetadata

class test_apiClientCreation(testHelperSuperClass):
  def test_simple(self):
    baseUrl = "MOCK"
    client = dockerRegistryPythonClient.RegistryClient(baseURL=baseUrl)

    username = "U"
    password = "P"
    loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

    catalogName = "tmpCat"
    tagName = "testTag"
    digest = 'sha256:21914a3e0bafe8c5508a902b80972868934cae3559ec8359f5d1be7638d2d186'
    dockerContentDigest = 'sha256:realditefdfddfdf'

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

    imageMetadata = client.getImageMetadata(loginSession=loginSession, qualifiedImageName=catalogName + ":" + tagName)

    self.assertEqual(dockerContentDigest, imageMetadata.getDigest())

  def test_givenUnknownImage_whenGetImageMetadata_returnsNone(self):
    baseUrl = "MOCK"
    client = dockerRegistryPythonClient.RegistryClient(baseURL=baseUrl)

    username = "U"
    password = "P"
    loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

    catalogName = "tmpCat"
    tagName = "testTag"
    digest = 'sha256:21914a3e0bafe8c5508a902b80972868934cae3559ec8359f5d1be7638d2d186'
    dockerContentDigest = 'sha256:realditefdfddfdf'

    getImageResponse = {"errors":[{"code":"MANIFEST_UNKNOWN","message":"manifest unknown","detail":{"Tag":"tagname"}}]}

    client.mock.registerNextResponse(
      reqFnName="get",
      url="/v2/" + catalogName + "/manifests/" + tagName,
      data=None,
      status_code=404,
      contentBytes=base64.b64encode(json.dumps(getImageResponse).encode()),
      contentHeaders={ "x-remaining": "0", "Docker-Content-Digest": dockerContentDigest },
      ignoreData=True
    )

    imageMetadata = client.getImageMetadata(loginSession=loginSession, qualifiedImageName=catalogName + ":" + tagName)

    self.assertEqual(None, imageMetadata)


