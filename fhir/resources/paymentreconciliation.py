# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class PaymentReconciliation(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    PaymentReconciliation resource.
    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """

    resource_type = Field("PaymentReconciliation", const=True)

    created: fhirtypes.DateTime = Field(
        ...,
        alias="created",
        title="Creation date",
        description="The date when the resource was created.",
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    detail: ListType[fhirtypes.PaymentReconciliationDetailType] = Field(
        None,
        alias="detail",
        title="Settlement particulars",
        description=(
            "Distribution of the payment amount for a previously acknowledged "
            "payable."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition message",
        description=(
            "A human readable description of the status of the request for the "
            "reconciliation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    formCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="formCode",
        title="Printed form identifier",
        description="A code for the form to be used for printing the content.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for a payment reconciliation",
        description="A unique identifier assigned to this payment reconciliation.",
        # if property is element of this resource.
        element_property=True,
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="queued | complete | error | partial",
        description="The outcome of a request for a reconciliation.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["queued", "complete", "error", "partial"],
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    paymentAmount: fhirtypes.MoneyType = Field(
        ...,
        alias="paymentAmount",
        title="Total amount of Payment",
        description="Total payment amount as indicated on the financial instrument.",
        # if property is element of this resource.
        element_property=True,
    )

    paymentDate: fhirtypes.Date = Field(
        ...,
        alias="paymentDate",
        title="When payment issued",
        description="The date of payment as indicated on the financial instrument.",
        # if property is element of this resource.
        element_property=True,
    )
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_paymentDate", title="Extension field for ``paymentDate``."
    )

    paymentIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="paymentIdentifier",
        title="Business identifier for the payment",
        description="Issuer's unique identifier for the payment instrument.",
        # if property is element of this resource.
        element_property=True,
    )

    paymentIssuer: fhirtypes.ReferenceType = Field(
        None,
        alias="paymentIssuer",
        title="Party generating payment",
        description="The party who generated the payment.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period covered",
        description=(
            "The period of time for which payments have been gathered into this "
            "bulk payment for settlement."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    processNote: ListType[fhirtypes.PaymentReconciliationProcessNoteType] = Field(
        None,
        alias="processNote",
        title="Note concerning processing",
        description=(
            "A note that describes or explains the processing in a human readable "
            "form."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Reference to requesting resource",
        description="Original request resource reference.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Task"],
    )

    requestor: fhirtypes.ReferenceType = Field(
        None,
        alias="requestor",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Settlement particulars.
    Distribution of the payment amount for a previously acknowledged payable.
    """

    resource_type = Field("PaymentReconciliationDetail", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Amount allocated to this payable",
        description="The monetary amount allocated from the total payment to the payable.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="Date of commitment to pay",
        description="The date from the response resource containing a commitment to pay.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Business identifier of the payment detail",
        description=(
            "Unique identifier for the current payment item for the referenced "
            "payable."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    payee: fhirtypes.ReferenceType = Field(
        None,
        alias="payee",
        title="Recipient of the payment",
        description="The party which is receiving the payment.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    predecessor: fhirtypes.IdentifierType = Field(
        None,
        alias="predecessor",
        title="Business identifier of the prior payment detail",
        description=(
            "Unique identifier for the prior payment item for the referenced "
            "payable."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Request giving rise to the payment",
        description=(
            "A resource, such as a Claim, the evaluation of which could lead to "
            "payment."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    response: fhirtypes.ReferenceType = Field(
        None,
        alias="response",
        title="Response committing to a payment",
        description=(
            "A resource, such as a ClaimResponse, which contains a commitment to "
            "payment."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    responsible: fhirtypes.ReferenceType = Field(
        None,
        alias="responsible",
        title="Contact for the response",
        description=(
            "A reference to the individual who is responsible for inquiries "
            "regarding the response and its payment."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PractitionerRole"],
    )

    submitter: fhirtypes.ReferenceType = Field(
        None,
        alias="submitter",
        title="Submitter of the request",
        description="The party which submitted the claim or financial transaction.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Category of payment",
        description="Code to indicate the nature of the payment.",
        # if property is element of this resource.
        element_property=True,
    )


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Note concerning processing.
    A note that describes or explains the processing in a human readable form.
    """

    resource_type = Field("PaymentReconciliationProcessNote", const=True)

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Note explanatory text",
        description="The explanation or description associated with the processing.",
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="display | print | printoper",
        description="The business purpose of the note text.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["display", "print", "printoper"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
