from setuptools import setup
import versioneer

#Dependancy lists maintained here and in tox.ini
sp_install_requires = [
  'requests==2.20.1',
  'pytz==2019.3',
  'python-dateutil==2.8.1',
  'PythonAPIClientBase==0.0.6'
]
sp_tests_require = [
  'nose==1.3.7',
  'python_Testing_Utilities==0.1.5'
]

all_require = sp_install_requires + sp_tests_require

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='dockerRegistryPythonClient',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Python package which provides Docker registry Client',
      url='https://github.com/rmetcalf9/dockerRegistryPythonClient',
      author='Robert Metcalf',
      author_email='rmetcalf9@googlemail.com',
      license='MIT',
      packages=['dockerRegistryPythonClient'],
      zip_safe=False,
      install_requires=sp_install_requires,
      tests_require=sp_tests_require,
      include_package_data=True)
