# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MessageDefinition(domainresource.DomainResource):
    """ A resource that defines a type of message that can be exchanged between
    systems.

    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    resource_type = "MessageDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.allowedResponse = None
        """ Responses to this message.
        List of `MessageDefinitionAllowedResponse` items (represented as `dict` in JSON). """

        self.base = None
        """ Definition this one is based on.
        Type `str` referencing `['MessageDefinition']`. """

        self.category = None
        """ consequence | currency | notification.
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the message definition.
        Type `str`. """

        self.eventCoding = None
        """ Event code  or link to the EventDefinition.
        Type `Coding` (represented as `dict` in JSON). """

        self.eventUri = None
        """ Event code  or link to the EventDefinition.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.focus = None
        """ Resource(s) that are the subject of the event.
        List of `MessageDefinitionFocus` items (represented as `dict` in JSON). """

        self.graph = None
        """ Canonical reference to a GraphDefinition.
        List of `str` items referencing `['GraphDefinition']`. """

        self.identifier = None
        """ Primary key for the message definition on a given server.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for message definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.name = None
        """ Name for this message definition (computer friendly).
        Type `str`. """

        self.parent = None
        """ Protocol/workflow this is part of.
        List of `str` items referencing `['ActivityDefinition', 'PlanDefinition']`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this message definition is defined.
        Type `str`. """

        self.replaces = None
        """ Takes the place of.
        List of `str` items referencing `['MessageDefinition']`. """

        self.responseRequired = None
        """ always | on-error | never | on-success.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.title = None
        """ Name for this message definition (human friendly).
        Type `str`. """

        self.url = None
        """ Business Identifier for a given MessageDefinition.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the message definition.
        Type `str`. """

        super(MessageDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageDefinition, self).elementProperties()
        js.extend(
            [
                (
                    "allowedResponse",
                    "allowedResponse",
                    MessageDefinitionAllowedResponse,
                    "MessageDefinitionAllowedResponse",
                    True,
                    None,
                    False,
                ),
                ("base", "base", str, "canonical", False, None, False),
                ("category", "category", str, "code", False, None, False),
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("copyright", "copyright", str, "markdown", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, True),
                ("description", "description", str, "markdown", False, None, False),
                (
                    "eventCoding",
                    "eventCoding",
                    coding.Coding,
                    "Coding",
                    False,
                    "event",
                    True,
                ),
                ("eventUri", "eventUri", str, "uri", False, "event", True),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                (
                    "focus",
                    "focus",
                    MessageDefinitionFocus,
                    "MessageDefinitionFocus",
                    True,
                    None,
                    False,
                ),
                ("graph", "graph", str, "canonical", True, None, False),
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
                ("name", "name", str, "string", False, None, False),
                ("parent", "parent", str, "canonical", True, None, False),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                ("replaces", "replaces", str, "canonical", True, None, False),
                (
                    "responseRequired",
                    "responseRequired",
                    str,
                    "code",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                ("title", "title", str, "string", False, None, False),
                ("url", "url", str, "uri", False, None, False),
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


class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.

    Indicates what types of messages may be sent as an application-level
    response to this message.
    """

    resource_type = "MessageDefinitionAllowedResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.message = None
        """ Reference to allowed message definition response.
        Type `str` referencing `['MessageDefinition']`. """

        self.situation = None
        """ When should this response be used.
        Type `str`. """

        super(MessageDefinitionAllowedResponse, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MessageDefinitionAllowedResponse, self).elementProperties()
        js.extend(
            [
                ("message", "message", str, "canonical", False, None, True),
                ("situation", "situation", str, "markdown", False, None, False),
            ]
        )
        return js


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ Resource(s) that are the subject of the event.

    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """

    resource_type = "MessageDefinitionFocus"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Type of resource.
        Type `str`. """

        self.max = None
        """ Maximum number of focuses of this type.
        Type `str`. """

        self.min = None
        """ Minimum number of focuses of this type.
        Type `int`. """

        self.profile = None
        """ Profile that must be adhered to by focus.
        Type `str` referencing `['StructureDefinition']`. """

        super(MessageDefinitionFocus, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageDefinitionFocus, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("max", "max", str, "string", False, None, False),
                ("min", "min", int, "unsignedInt", False, None, True),
                ("profile", "profile", str, "canonical", False, None, False),
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
