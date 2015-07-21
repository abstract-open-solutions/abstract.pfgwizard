# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import atapi

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender

from Products.PloneFormGen.interfaces import IPloneFormGenForm

from .interfaces import IAbstractPfgwizardLayer
from . import _

WIZARD_MODE_FIELDNAME = "wizard_mode"


def get_wizard_mode(obj):
    field = obj.getField(WIZARD_MODE_FIELDNAME)
    return field and field.get(obj)


class _ExtensionBooleanField(ExtensionField, atapi.BooleanField):
    pass


class FormExtender(object):
    adapts(IPloneFormGenForm)
    implements(IOrderableSchemaExtender,
               IBrowserLayerAwareExtender,
               ISchemaModifier)

    layer = IAbstractPfgwizardLayer

    fields = [
        _ExtensionBooleanField(
            WIZARD_MODE_FIELDNAME,
            widget=atapi.BooleanWidget(
                label=_(u"Wizard mode"),
                description=_(u"Turn on wizard mode."),
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self): # noqa
        return self.fields

    def getOrder(self, original): # noqa
        """
        'original' is a dictionary where the keys are the names of
        schemata and the values are lists of field names, in order.
        """
        return original

    # def fiddle(object, schema):
    #     return schema
