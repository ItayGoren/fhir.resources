# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HumanName
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class HumanName(element.Element):
    """ Name of a human - parts and usage.

    A human's name with the ability to identify parts and usage.
    """

    resource_type = "HumanName"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.family = None
        """ Family name (often called 'Surname').
        Type `str`. """

        self.given = None
        """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """

        self.period = None
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """

        self.prefix = None
        """ Parts that come before the name.
        List of `str` items. """

        self.suffix = None
        """ Parts that come after the name.
        List of `str` items. """

        self.text = None
        """ Text representation of the full name.
        Type `str`. """

        self.use = None
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """

        super(HumanName, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend(
            [
                ("family", "family", str, "string", False, None, False),
                ("given", "given", str, "string", True, None, False),
                ("period", "period", period.Period, "Period", False, None, False),
                ("prefix", "prefix", str, "string", True, None, False),
                ("suffix", "suffix", str, "string", True, None, False),
                ("text", "text", str, "string", False, None, False),
                ("use", "use", str, "code", False, None, False),
            ]
        )
        return js


try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
