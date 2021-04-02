import PythonAPIClientBase
from .RegistryLoginSession import RegistryLoginSessionBasedOnBasicAuth
from .RegisteryIterator import RegisteryIterator, genFnCollectSinglePageFunction
import json
from .ImageMetadata import ImageMetadata

class RegistryClient(PythonAPIClientBase.APIClientBase):

  def __init__(self, baseURL, mock=None):
    super().__init__(baseURL=baseURL, mock=mock, forceOneRequestAtATime=True)

  def getLoginSessionBasedOnBasicAuth(self, username, password):
    return RegistryLoginSessionBasedOnBasicAuth(APIClient=self, username=username, password=password)

  def getBase(self, loginSession):
    result = self.sendGetRequest(
      url="/v2/",
      loginSession=loginSession
    )
    if result.status_code != 200:
      self.raiseResponseException(result)

    return json.loads(result.content)

  def getCatalogIterator(self, loginSession):
    def retrieveListFromResponse(responseJSON):
      return responseJSON["repositories"]

    def itemGeneratorFunction(responseFromAPI):
      # Each item is just a string
      return responseFromAPI

    return RegisteryIterator(
      itemGeneratorFunction=itemGeneratorFunction,
      collectSinglePageFunction=genFnCollectSinglePageFunction(
        apiClient=self, loginSession=loginSession, pageSize=100, baseAPI="/v2/_catalog",
        retrieveListFromResponseFn=retrieveListFromResponse
      )
    )

  def getTagsForCatalogIterator(self, loginSession, catalogName):
    def retrieveListFromResponse(responseJSON):
      return responseJSON["tags"]

    def itemGeneratorFunction(responseFromAPI):
      # Each item is just a string
      return responseFromAPI

    return RegisteryIterator(
      itemGeneratorFunction=itemGeneratorFunction,
      collectSinglePageFunction=genFnCollectSinglePageFunction(
        apiClient=self, loginSession=loginSession, pageSize=100, baseAPI="/v2/" + catalogName + "/tags/list",
        retrieveListFromResponseFn=retrieveListFromResponse
      )
    )

  def _getCatlogAndTag(self, qualifiedImageName):
    try:
      catalogName, tagName = qualifiedImageName.split(":")
    except:
      print("Invalid qualifiedImageName - must be two strings seperated by a colon:", qualifiedImageName)
      raise Exception("Invalid qualifiedImageName")
    return catalogName, tagName


  def getImageMetadata(self, loginSession, qualifiedImageName):
    catalogName, tagName = self._getCatlogAndTag(qualifiedImageName)
    def injectHeadersFn(headers):
      headers["Accept"] = "application/vnd.docker.distribution.manifest.v2+json"

    result = self.sendGetRequest(
      url="/v2/" + catalogName + "/manifests/" + tagName,
      loginSession=loginSession,
      injectHeadersFn=injectHeadersFn
    )
    if result.status_code != 200:
      self.raiseResponseException(result)

    return ImageMetadata(json.loads(result.content))

# TODO Investigate https://forums.docker.com/t/get-image-digest-from-remote-registry-via-api/9480
