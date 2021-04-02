

class ImageMetadata():
  _jsonDict = None

  def __init__(self, jsonDict):
    self._jsonDict = jsonDict

  def getJson(self):
    return self._jsonDict

  def getDigest(self):
    return self._jsonDict["config"]["digest"]
