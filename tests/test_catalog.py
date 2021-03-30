from TestHelperSuperClass import testHelperSuperClass
import dockerRegistryPythonClient
import base64
import json


class test_catalogAPI(testHelperSuperClass):
  def test_givenPaginatedCatalogResult_whenGetCatalog_returnThemAll(self):
    firstResult = ["1", "2", "ffff"]
    secondResult = ["221", "222", "22ffff"]
    thirdResult = ["331", "332", "33ffff"]


    baseUrl = "MOCK"
    client = dockerRegistryPythonClient.RegistryClient(baseURL=baseUrl)
    username = "U"
    password = "P"
    loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)

    def addMockResponse(entries, last=False):
      mockResponse = { "repositories": entries }
      contentHeaders = { "Link": "</v2/_catalog?n=100>; rel=\"next\""}
      if last:
        contentHeaders = {}
      client.mock.registerNextResponse(
        reqFnName="get",
        url="/v2/_catalog?n=100",
        data=None,
        status_code=200,
        contentBytes=base64.b64encode(json.dumps(mockResponse).encode()),
        contentHeaders=contentHeaders,
        ignoreData=True
      )

    # Mock responses must be added in reverse order!
    addMockResponse(thirdResult, last=True)
    addMockResponse(secondResult)
    addMockResponse(firstResult)

    catalogs = client.getCatalogIterator(loginSession=loginSession)
    recieved = []
    for catalog in catalogs:
      recieved.append(catalog)
      print("DCC", catalog)

    self.assertEqual(firstResult + secondResult + thirdResult, recieved)

