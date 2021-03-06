# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Basic
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Basic(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource for non-supported content.
    Basic is used for handling concepts not yet defined in FHIR, narrative-only
    resources that don't map to an existing resource, and custom resources not
    appropriate for inclusion in the FHIR specification.
    """

    resource_type = Field("Basic", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Who created",
        description="Indicates who was responsible for creating the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Patient",
            "RelatedPerson",
            "Organization",
        ],
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Kind of Resource",
        description=(
            "Identifies the 'type' of resource - equivalent to the resource name "
            "for other resources."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    created: fhirtypes.Date = Field(
        None,
        alias="created",
        title="When created",
        description="Identifies when the resource was first created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Identifier assigned to the resource for business purposes, outside the"
            " context of FHIR."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Identifies the focus of this resource",
        description=(
            "Identifies the patient, practitioner, device or any other resource "
            'that is the "focus" of this resource.'
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )
