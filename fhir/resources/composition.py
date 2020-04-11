# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Composition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Composition(domainresource.DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.

    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. A Composition defines the structure
    and narrative content necessary for a document. However, a Composition
    alone does not constitute a document. Rather, the Composition must be the
    first entry in a Bundle where Bundle.type=document, and any other resources
    referenced from Composition must be included as subsequent entries in the
    Bundle (for example Patient, Practitioner, Encounter, etc.).
    """

    resource_type = "Composition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.attester = None
        """ Attests to accuracy of composition.
        List of `CompositionAttester` items (represented as `dict` in JSON). """

        self.author = None
        """ Who and/or what authored the composition.
        List of `FHIRReference` items referencing `['Practitioner', 'PractitionerRole', 'Device', 'Patient', 'RelatedPerson', 'Organization']` (represented as `dict` in JSON). """

        self.category = None
        """ Categorization of Composition.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.confidentiality = None
        """ As defined by affinity domain.
        Type `str`. """

        self.custodian = None
        """ Organization which maintains the composition.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.date = None
        """ Composition editing time.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.encounter = None
        """ Context of the Composition.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.event = None
        """ The clinical service(s) being documented.
        List of `CompositionEvent` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Version-independent identifier for the Composition.
        Type `Identifier` (represented as `dict` in JSON). """

        self.relatesTo = None
        """ Relationships to other compositions/documents.
        List of `CompositionRelatesTo` items (represented as `dict` in JSON). """

        self.section = None
        """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """

        self.status = None
        """ preliminary | final | amended | entered-in-error.
        Type `str`. """

        self.subject = None
        """ Who and/or what the composition is about.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.title = None
        """ Human Readable name/title.
        Type `str`. """

        self.type = None
        """ Kind of composition (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Composition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend(
            [
                (
                    "attester",
                    "attester",
                    CompositionAttester,
                    "CompositionAttester",
                    True,
                    None,
                    False,
                ),
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    True,
                ),
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("confidentiality", "confidentiality", str, "code", False, None, False),
                (
                    "custodian",
                    "custodian",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, True),
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
                    CompositionEvent,
                    "CompositionEvent",
                    True,
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
                    "relatesTo",
                    "relatesTo",
                    CompositionRelatesTo,
                    "CompositionRelatesTo",
                    True,
                    None,
                    False,
                ),
                (
                    "section",
                    "section",
                    CompositionSection,
                    "CompositionSection",
                    True,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("title", "title", str, "string", False, None, True),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """

    resource_type = "CompositionAttester"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.mode = None
        """ personal | professional | legal | official.
        Type `str`. """

        self.party = None
        """ Who attested the composition.
        Type `FHIRReference` referencing `['Patient', 'RelatedPerson', 'Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.time = None
        """ When the composition was attested.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(CompositionAttester, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend(
            [
                ("mode", "mode", str, "code", False, None, True),
                (
                    "party",
                    "party",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("time", "time", fhirdate.FHIRDate, "dateTime", False, None, False),
            ]
        )
        return js


class CompositionEvent(backboneelement.BackboneElement):
    """ The clinical service(s) being documented.

    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """

    resource_type = "CompositionEvent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Code(s) that apply to the event being documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.detail = None
        """ The event(s) being documented.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.period = None
        """ The period covered by the documentation.
        Type `Period` (represented as `dict` in JSON). """

        super(CompositionEvent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "detail",
                    "detail",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
            ]
        )
        return js


class CompositionRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other compositions/documents.

    Relationships that this composition has with other compositions or
    documents that already exist.
    """

    resource_type = "CompositionRelatesTo"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ replaces | transforms | signs | appends.
        Type `str`. """

        self.targetIdentifier = None
        """ Target of the relationship.
        Type `Identifier` (represented as `dict` in JSON). """

        self.targetReference = None
        """ Target of the relationship.
        Type `FHIRReference` referencing `['Composition']` (represented as `dict` in JSON). """

        super(CompositionRelatesTo, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionRelatesTo, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                (
                    "targetIdentifier",
                    "targetIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    "target",
                    True,
                ),
                (
                    "targetReference",
                    "targetReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "target",
                    True,
                ),
            ]
        )
        return js


class CompositionSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.

    The root of the sections that make up the composition.
    """

    resource_type = "CompositionSection"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.author = None
        """ Who and/or what authored the section.
        List of `FHIRReference` items referencing `['Practitioner', 'PractitionerRole', 'Device', 'Patient', 'RelatedPerson', 'Organization']` (represented as `dict` in JSON). """

        self.code = None
        """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.emptyReason = None
        """ Why the section is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.entry = None
        """ A reference to data that supports this section.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.focus = None
        """ Who/what the section is about, when it is not about the subject of
        composition.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.mode = None
        """ working | snapshot | changes.
        Type `str`. """

        self.orderedBy = None
        """ Order of section entries.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.section = None
        """ Nested Section.
        List of `CompositionSection` items (represented as `dict` in JSON). """

        self.text = None
        """ Text summary of the section, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """

        self.title = None
        """ Label for section (e.g. for ToC).
        Type `str`. """

        super(CompositionSection, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend(
            [
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "emptyReason",
                    "emptyReason",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "entry",
                    "entry",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "focus",
                    "focus",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("mode", "mode", str, "code", False, None, False),
                (
                    "orderedBy",
                    "orderedBy",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "section",
                    "section",
                    CompositionSection,
                    "CompositionSection",
                    True,
                    None,
                    False,
                ),
                ("text", "text", narrative.Narrative, "Narrative", False, None, False),
                ("title", "title", str, "string", False, None, False),
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
    from . import narrative
except ImportError:
    narrative = sys.modules[__package__ + ".narrative"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
