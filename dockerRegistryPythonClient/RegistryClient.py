import PythonAPIClientBase
from .RegistryLoginSession import RegistryLoginSessionBasedOnBasicAuth

class RegistryClient(PythonAPIClientBase.APIClientBase):

  def __init__(self, baseURL, mock=None):
    super().__init__(baseURL=baseURL, mock=mock, forceOneRequestAtATime=True)

  def getLoginSessionBasedOnBasicAuth(self, username, password):
    return RegistryLoginSessionBasedOnBasicAuth(APIClient=self, username=username, password=password)
