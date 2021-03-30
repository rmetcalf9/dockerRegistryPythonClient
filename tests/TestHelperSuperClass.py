#Test helper functions
# defines a baseclass with extra functions
# https://docs.python.org/3/library/unittest.html
import unittest
import json
from baseapp_for_restapi_backend_with_swagger import AppObjBaseClass, from_iso8601

import datetime
import pytz

from nose.plugins.attrib import attr
def wipd(f):
  return attr('wip')(f)

class testHelperSuperClass(unittest.TestCase):
  pass