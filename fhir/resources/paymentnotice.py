# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import domainresource


class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    resource_type = "PaymentNotice"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amount = None
        """ Monetary amount of the payment.
        Type `Money` (represented as `dict` in JSON). """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.identifier = None
        """ Business Identifier for the payment noctice.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.payee = None
        """ Party being paid.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.payment = None
        """ Payment reference.
        Type `FHIRReference` referencing `['PaymentReconciliation']` (represented as `dict` in JSON). """

        self.paymentDate = None
        """ Payment or clearing date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.paymentStatus = None
        """ Issued or cleared Status of the payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.recipient = None
        """ Party being notified.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.response = None
        """ Response reference.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend(
            [
                ("amount", "amount", money.Money, "Money", False, None, True),
                (
                    "created",
                    "created",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    True,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                (
                    "payee",
                    "payee",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "payment",
                    "payment",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "paymentDate",
                    "paymentDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                (
                    "paymentStatus",
                    "paymentStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "provider",
                    "provider",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "recipient",
                    "recipient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "request",
                    "request",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "response",
                    "response",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + ".money"]
