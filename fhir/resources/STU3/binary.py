# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import resource


class Binary(resource.Resource):
    """ Pure binary content defined by a format other than FHIR.

    A binary resource can contain any content, whether text, image, pdf, zip
    archive, etc.
    """

    resource_type = "Binary"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.content = None
        """ The actual content.
        Type `str`. """

        self.contentType = None
        """ MimeType of the binary content.
        Type `str`. """

        self.securityContext = None
        """ Access Control Management.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        super(Binary, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Binary, self).elementProperties()
        js.extend(
            [
                ("content", "content", str, "base64Binary", False, None, True),
                ("contentType", "contentType", str, "code", False, None, True),
                (
                    "securityContext",
                    "securityContext",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
