
def getSampleMetadata(catalogName, tagName, digest):
  return {
    'schemaVersion': 2,
    'mediaType': 'application/vnd.docker.distribution.manifest.v2+json',
    'config': {
      'mediaType': 'application/vnd.docker.container.image.v1+json',
      'size': 1111,
      'digest': digest
    },
    'layers': [
      {
        'mediaType': 'application/vnd.docker.image.rootfs.diff.tar.gzip', 'size': 123, 'digest': 'sha256:e6c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10'
      }, {
        'mediaType': 'application/vnd.docker.image.rootfs.diff.tar.gzip', 'size': 123, 'digest': 'sha256:8985e402e050840450bd9d60b20a9bec70d57a507b33a85e5c3b3caf2e0ada6e'
      }, {
        'mediaType': 'application/vnd.docker.image.rootfs.diff.tar.gzip', 'size': 23, 'digest': 'sha256:78986f489cfa0d72ea6e357ab3e81a9d5ebdb9cf4797a41eb49bdefe579f1b01'
      }
    ]
  }

