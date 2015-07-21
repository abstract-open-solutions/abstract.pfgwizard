# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import abstract.pfgwizard


class AbstractPfgwizardLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=abstract.pfgwizard)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'abstract.pfgwizard:default')


ABSTRACT_PFGWIZARD_FIXTURE = AbstractPfgwizardLayer()


ABSTRACT_PFGWIZARD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ABSTRACT_PFGWIZARD_FIXTURE,),
    name='AbstractPfgwizardLayer:IntegrationTesting'
)


ABSTRACT_PFGWIZARD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ABSTRACT_PFGWIZARD_FIXTURE,),
    name='AbstractPfgwizardLayer:FunctionalTesting'
)


ABSTRACT_PFGWIZARD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ABSTRACT_PFGWIZARD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='AbstractPfgwizardLayer:AcceptanceTesting'
)
