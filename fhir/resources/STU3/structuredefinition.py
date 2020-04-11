# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.

    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """

    resource_type = "StructureDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.abstract = None
        """ Whether the structure is abstract.
        Type `bool`. """

        self.baseDefinition = None
        """ Definition that this type is constrained/specialized from.
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.context = None
        """ Where the extension can be used in instances.
        List of `str` items. """

        self.contextInvariant = None
        """ FHIRPath invariants - when the extension can be used.
        List of `str` items. """

        self.contextType = None
        """ resource | datatype | extension.
        Type `str`. """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.derivation = None
        """ specialization | constraint - How relates to base definition.
        Type `str`. """

        self.description = None
        """ Natural language description of the structure definition.
        Type `str`. """

        self.differential = None
        """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.fhirVersion = None
        """ FHIR Version this StructureDefinition targets.
        Type `str`. """

        self.identifier = None
        """ Additional identifier for the structure definition.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for structure definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.keyword = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """

        self.kind = None
        """ primitive-type | complex-type | resource | logical.
        Type `str`. """

        self.mapping = None
        """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this structure definition (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this structure definition is defined.
        Type `str`. """

        self.snapshot = None
        """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.title = None
        """ Name for this structure definition (human friendly).
        Type `str`. """

        self.type = None
        """ Type defined or constrained by this structure.
        Type `str`. """

        self.url = None
        """ Logical URI to reference this structure definition (globally
        unique).
        Type `str`. """

        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the structure definition.
        Type `str`. """

        super(StructureDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend(
            [
                ("abstract", "abstract", bool, "boolean", False, None, True),
                ("baseDefinition", "baseDefinition", str, "uri", False, None, False),
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("context", "context", str, "string", True, None, False),
                (
                    "contextInvariant",
                    "contextInvariant",
                    str,
                    "string",
                    True,
                    None,
                    False,
                ),
                ("contextType", "contextType", str, "code", False, None, False),
                ("copyright", "copyright", str, "markdown", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("derivation", "derivation", str, "code", False, None, False),
                ("description", "description", str, "markdown", False, None, False),
                (
                    "differential",
                    "differential",
                    StructureDefinitionDifferential,
                    "StructureDefinitionDifferential",
                    False,
                    None,
                    False,
                ),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                ("fhirVersion", "fhirVersion", str, "id", False, None, False),
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
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("keyword", "keyword", coding.Coding, "Coding", True, None, False),
                ("kind", "kind", str, "code", False, None, True),
                (
                    "mapping",
                    "mapping",
                    StructureDefinitionMapping,
                    "StructureDefinitionMapping",
                    True,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, True),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                (
                    "snapshot",
                    "snapshot",
                    StructureDefinitionSnapshot,
                    "StructureDefinitionSnapshot",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                ("title", "title", str, "string", False, None, False),
                ("type", "type", str, "code", False, None, True),
                ("url", "url", str, "uri", False, None, True),
                (
                    "useContext",
                    "useContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
                    None,
                    False,
                ),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.

    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """

    resource_type = "StructureDefinitionDifferential"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """

        super(StructureDefinitionDifferential, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend(
            [
                (
                    "element",
                    "element",
                    elementdefinition.ElementDefinition,
                    "ElementDefinition",
                    True,
                    None,
                    True,
                ),
            ]
        )
        return js


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ External specification that the content is mapped to.

    An external specification that the content is mapped to.
    """

    resource_type = "StructureDefinitionMapping"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.comment = None
        """ Versions, Issues, Scope limitations etc..
        Type `str`. """

        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """

        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """

        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """

        super(StructureDefinitionMapping, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend(
            [
                ("comment", "comment", str, "string", False, None, False),
                ("identity", "identity", str, "id", False, None, True),
                ("name", "name", str, "string", False, None, False),
                ("uri", "uri", str, "uri", False, None, False),
            ]
        )
        return js


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.

    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """

    resource_type = "StructureDefinitionSnapshot"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """

        super(StructureDefinitionSnapshot, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend(
            [
                (
                    "element",
                    "element",
                    elementdefinition.ElementDefinition,
                    "ElementDefinition",
                    True,
                    None,
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import elementdefinition
except ImportError:
    elementdefinition = sys.modules[__package__ + ".elementdefinition"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
