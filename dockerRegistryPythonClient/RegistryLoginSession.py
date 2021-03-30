from PythonAPIClientBase import LoginSession

class RegistryLoginSessionBasedOnBasicAuth(LoginSession):
  username = None
  password = None
  apiClient = None

  def __init__(self, APIClient, username, password):
    self.apiClient = APIClient
    self.username = username
    self.password = password
