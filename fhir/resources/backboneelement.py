# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BackboneElement
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class BackboneElement(element.Element):
    """ Base for elements defined inside a resource.

    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """

    resource_type = "BackboneElement"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.modifierExtension = None
        """ Extensions that cannot be ignored even if unrecognized.
        List of `Extension` items (represented as `dict` in JSON). """

        super(BackboneElement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BackboneElement, self).elementProperties()
        js.extend(
            [
                (
                    "modifierExtension",
                    "modifierExtension",
                    extension.Extension,
                    "Extension",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import extension
except ImportError:
    extension = sys.modules[__package__ + ".extension"]
