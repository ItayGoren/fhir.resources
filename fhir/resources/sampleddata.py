# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SampledData
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class SampledData(element.Element):
    """ A series of measurements taken by a device.

    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    resource_type = "SampledData"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.data = None
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """

        self.dimensions = None
        """ Number of sample points at each time point.
        Type `int`. """

        self.factor = None
        """ Multiply data by this before adding to origin.
        Type `float`. """

        self.lowerLimit = None
        """ Lower limit of detection.
        Type `float`. """

        self.origin = None
        """ Zero value and units.
        Type `Quantity` (represented as `dict` in JSON). """

        self.period = None
        """ Number of milliseconds between samples.
        Type `float`. """

        self.upperLimit = None
        """ Upper limit of detection.
        Type `float`. """

        super(SampledData, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend(
            [
                ("data", "data", str, "string", False, None, False),
                ("dimensions", "dimensions", int, "positiveInt", False, None, True),
                ("factor", "factor", float, "decimal", False, None, False),
                ("lowerLimit", "lowerLimit", float, "decimal", False, None, False),
                ("origin", "origin", quantity.Quantity, "Quantity", False, None, True),
                ("period", "period", float, "decimal", False, None, True),
                ("upperLimit", "upperLimit", float, "decimal", False, None, False),
            ]
        )
        return js


try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
