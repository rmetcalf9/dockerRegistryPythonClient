from TestHelperSuperClass import testHelperSuperClass
import dockerRegistryPythonClient
import base64
import json

class test_apiClientCreation(testHelperSuperClass):
  def test_simple(self):
    baseUrl = "MOCK"
    client = dockerRegistryPythonClient.RegistryClient(baseURL=baseUrl)

    mockResponse = {}
    client.mock.registerNextResponse(
      reqFnName="get",
      url="/v2/",
      data=None,
      status_code=200,
      contentBytes=base64.b64encode(json.dumps(mockResponse).encode()),
      contentHeaders={ "x-remaining": "0"},
      ignoreData=True
    )

    username = "U"
    password = "P"
    loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

    self.assertTrue(loginSession.testValid())

  def test_givenBasPass_whenTestLoginSession_returnFalse(self):
    baseUrl = "MOCK"
    client = dockerRegistryPythonClient.RegistryClient(baseURL=baseUrl)

    mockResponse = {}
    client.mock.registerNextResponse(
      reqFnName="get",
      url="/v2/",
      data=None,
      status_code=401,
      contentBytes=base64.b64encode(json.dumps(mockResponse).encode()),
      contentHeaders={ "x-remaining": "0"},
      ignoreData=True
    )

    username = "U"
    password = "P"
    loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

    self.assertFalse(loginSession.testValid())

