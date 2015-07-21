# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.common import ViewletBase

from abstract.pfgwizard.extenders import get_wizard_mode


WIZARD_VAR_TEMPLATE = ''.join([
    'pfg_wizard = {on: %(on)s};',
])


def to_js(val):
    if val is True:
        return 'true'
    if val is False or val is None:
        return 'false'


class JSVariables(ViewletBase):

    def js(self):
        mode = get_wizard_mode(self.context)
        template = WIZARD_VAR_TEMPLATE % {'on': to_js(mode)}
        return template
