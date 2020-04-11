# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/UsageContext
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import element


class UsageContext(element.Element):
    """ Describes the context of use for a conformance or knowledge resource.

    Specifies clinical/business/etc metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """

    resource_type = "UsageContext"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Type of context being specified.
        Type `Coding` (represented as `dict` in JSON). """

        self.valueCodeableConcept = None
        """ Value that defines the context.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ Value that defines the context.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Value that defines the context.
        Type `Range` (represented as `dict` in JSON). """

        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend(
            [
                ("code", "code", coding.Coding, "Coding", False, None, True),
                (
                    "valueCodeableConcept",
                    "valueCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueQuantity",
                    "valueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueRange",
                    "valueRange",
                    range.Range,
                    "Range",
                    False,
                    "value",
                    True,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
