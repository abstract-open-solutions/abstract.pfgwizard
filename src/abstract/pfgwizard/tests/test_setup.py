# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from abstract.pfgwizard.testing import ABSTRACT_PFGWIZARD_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that abstract.pfgwizard is properly installed."""

    layer = ABSTRACT_PFGWIZARD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if abstract.pfgwizard is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('abstract.pfgwizard'))

    def test_uninstall(self):
        """Test if abstract.pfgwizard is cleanly uninstalled."""
        self.installer.uninstallProducts(['abstract.pfgwizard'])
        self.assertFalse(self.installer.isProductInstalled('abstract.pfgwizard'))

    def test_browserlayer(self):
        """Test that IAbstractPfgwizardLayer is registered."""
        from abstract.pfgwizard.interfaces import IAbstractPfgwizardLayer
        from plone.browserlayer import utils
        self.assertIn(IAbstractPfgwizardLayer, utils.registered_layers())
