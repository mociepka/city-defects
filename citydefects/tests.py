from django.test import TestCase
from distutils.version import StrictVersion


class VersionTest(TestCase):

    def test_version_pep_compatible(self):
        'Version is compatible with PEP 386'
        from . import __version__ as version
        StrictVersion(version)
