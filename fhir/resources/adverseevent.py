# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class AdverseEvent(domainresource.DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """

    resource_type = "AdverseEvent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actuality = None
        """ actual | potential.
        Type `str`. """

        self.category = None
        """ product-problem | product-quality | product-use-error | wrong-dose
        | incorrect-prescribing-information | wrong-technique | wrong-
        route-of-administration | wrong-rate | wrong-duration | wrong-time
        | expired-drug | medical-device-use-error | problem-different-
        manufacturer | unsafe-physical-environment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.contributor = None
        """ Who  was involved in the adverse event or the potential adverse
        event.
        List of `FHIRReference` items referencing `['Practitioner', 'PractitionerRole', 'Device']` (represented as `dict` in JSON). """

        self.date = None
        """ When the event occurred.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.detected = None
        """ When the event was detected.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.event = None
        """ Type of the event itself in relation to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier for the event.
        Type `Identifier` (represented as `dict` in JSON). """

        self.location = None
        """ Location where adverse event occurred.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.outcome = None
        """ resolved | recovering | ongoing | resolvedWithSequelae | fatal |
        unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.recordedDate = None
        """ When the event was recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.recorder = None
        """ Who recorded the adverse event.
        Type `FHIRReference` referencing `['Patient', 'Practitioner', 'PractitionerRole', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.referenceDocument = None
        """ AdverseEvent.referenceDocument.
        List of `FHIRReference` items referencing `['DocumentReference']` (represented as `dict` in JSON). """

        self.resultingCondition = None
        """ Effect on the subject due to this event.
        List of `FHIRReference` items referencing `['Condition']` (represented as `dict` in JSON). """

        self.seriousness = None
        """ Seriousness of the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.severity = None
        """ mild | moderate | severe.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.study = None
        """ AdverseEvent.study.
        List of `FHIRReference` items referencing `['ResearchStudy']` (represented as `dict` in JSON). """

        self.subject = None
        """ Subject impacted by event.
        Type `FHIRReference` referencing `['Patient', 'Group', 'Practitioner', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.subjectMedicalHistory = None
        """ AdverseEvent.subjectMedicalHistory.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'AllergyIntolerance', 'FamilyMemberHistory', 'Immunization', 'Procedure', 'Media', 'DocumentReference']` (represented as `dict` in JSON). """

        self.suspectEntity = None
        """ The suspected agent causing the adverse event.
        List of `AdverseEventSuspectEntity` items (represented as `dict` in JSON). """

        super(AdverseEvent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend(
            [
                ("actuality", "actuality", str, "code", False, None, True),
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "contributor",
                    "contributor",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                (
                    "detected",
                    "detected",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "event",
                    "event",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "location",
                    "location",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "outcome",
                    "outcome",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "recordedDate",
                    "recordedDate",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "recorder",
                    "recorder",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "referenceDocument",
                    "referenceDocument",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "resultingCondition",
                    "resultingCondition",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "seriousness",
                    "seriousness",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "severity",
                    "severity",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "study",
                    "study",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "subjectMedicalHistory",
                    "subjectMedicalHistory",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "suspectEntity",
                    "suspectEntity",
                    AdverseEventSuspectEntity,
                    "AdverseEventSuspectEntity",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """

    resource_type = "AdverseEventSuspectEntity"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.causality = None
        """ Information on the possible cause of the event.
        List of `AdverseEventSuspectEntityCausality` items (represented as `dict` in JSON). """

        self.instance = None
        """ Refers to the specific entity that caused the adverse event.
        Type `FHIRReference` referencing `['Immunization', 'Procedure', 'Substance', 'Medication', 'MedicationAdministration', 'MedicationStatement', 'Device']` (represented as `dict` in JSON). """

        super(AdverseEventSuspectEntity, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend(
            [
                (
                    "causality",
                    "causality",
                    AdverseEventSuspectEntityCausality,
                    "AdverseEventSuspectEntityCausality",
                    True,
                    None,
                    False,
                ),
                (
                    "instance",
                    "instance",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """ Information on the possible cause of the event.
    """

    resource_type = "AdverseEventSuspectEntityCausality"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assessment = None
        """ Assessment of if the entity caused the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.author = None
        """ AdverseEvent.suspectEntity.causalityAuthor.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.method = None
        """ ProbabilityScale | Bayesian | Checklist.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.productRelatedness = None
        """ AdverseEvent.suspectEntity.causalityProductRelatedness.
        Type `str`. """

        super(AdverseEventSuspectEntityCausality, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend(
            [
                (
                    "assessment",
                    "assessment",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "method",
                    "method",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "productRelatedness",
                    "productRelatedness",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
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
