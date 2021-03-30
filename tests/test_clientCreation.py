from TestHelperSuperClass import testHelperSuperClass
import dockerRegistryPythonClient

class test_apiClientCreation(testHelperSuperClass):
  def test_simple(self):
    baseUrl = "ABC"
    username = "U"
    password = "P"

    client = dockerRegistryPythonClient.RegistryClient(baseURL=baseUrl)
    loginSession = client.getLoginSessionBasedOnBasicAuth(username=username, password=password)


