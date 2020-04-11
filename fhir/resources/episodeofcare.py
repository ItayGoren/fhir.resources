# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.

    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """

    resource_type = "EpisodeOfCare"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.account = None
        """ The set of accounts that may be used for billing for this
        EpisodeOfCare.
        List of `FHIRReference` items referencing `['Account']` (represented as `dict` in JSON). """

        self.careManager = None
        """ Care manager/care coordinator for the patient.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.diagnosis = None
        """ The list of diagnosis relevant to this episode of care.
        List of `EpisodeOfCareDiagnosis` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier(s) relevant for this EpisodeOfCare.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ Organization that assumes care.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.patient = None
        """ The patient who is the focus of this episode of care.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.period = None
        """ Interval during responsibility is assumed.
        Type `Period` (represented as `dict` in JSON). """

        self.referralRequest = None
        """ Originating Referral Request(s).
        List of `FHIRReference` items referencing `['ServiceRequest']` (represented as `dict` in JSON). """

        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled |
        entered-in-error.
        Type `str`. """

        self.statusHistory = None
        """ Past list of status codes (the current status may be included to
        cover the start date of the status).
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """

        self.team = None
        """ Other practitioners facilitating this episode of care.
        List of `FHIRReference` items referencing `['CareTeam']` (represented as `dict` in JSON). """

        self.type = None
        """ Type/class  - e.g. specialist referral, disease management.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(EpisodeOfCare, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend(
            [
                (
                    "account",
                    "account",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "careManager",
                    "careManager",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "diagnosis",
                    "diagnosis",
                    EpisodeOfCareDiagnosis,
                    "EpisodeOfCareDiagnosis",
                    True,
                    None,
                    False,
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
                    "managingOrganization",
                    "managingOrganization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "referralRequest",
                    "referralRequest",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "statusHistory",
                    "statusHistory",
                    EpisodeOfCareStatusHistory,
                    "EpisodeOfCareStatusHistory",
                    True,
                    None,
                    False,
                ),
                (
                    "team",
                    "team",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """

    resource_type = "EpisodeOfCareDiagnosis"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.condition = None
        """ Conditions/problems/diagnoses this episode of care is for.
        Type `FHIRReference` referencing `['Condition']` (represented as `dict` in JSON). """

        self.rank = None
        """ Ranking of the diagnosis (for each role type).
        Type `int`. """

        self.role = None
        """ Role that this diagnosis has within the episode of care (e.g.
        admission, billing, discharge …).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(EpisodeOfCareDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EpisodeOfCareDiagnosis, self).elementProperties()
        js.extend(
            [
                (
                    "condition",
                    "condition",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("rank", "rank", int, "positiveInt", False, None, False),
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).

    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """

    resource_type = "EpisodeOfCareStatusHistory"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.period = None
        """ Duration the EpisodeOfCare was in the specified status.
        Type `Period` (represented as `dict` in JSON). """

        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled |
        entered-in-error.
        Type `str`. """

        super(EpisodeOfCareStatusHistory, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend(
            [
                ("period", "period", period.Period, "Period", False, None, True),
                ("status", "status", str, "code", False, None, True),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
