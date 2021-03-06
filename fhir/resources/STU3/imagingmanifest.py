# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImagingManifest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key Object Selection.
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """

    resource_type = Field("ImagingManifest", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Author (human or machine)",
        description=(
            "Author of ImagingManifest. It can be a human author or a device which "
            "made the decision of the SOP instances selected. For example, a "
            "radiologist selected a set of imaging SOP instances to attach in a "
            "diagnostic report, and a CAD application may author a selection to "
            "describe SOP instances it used to generate a detection conclusion."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Device",
            "Organization",
            "Patient",
            "RelatedPerson",
        ],
    )

    authoringTime: fhirtypes.DateTime = Field(
        None,
        alias="authoringTime",
        title="Time when the selection of instances was made",
        description=(
            "Date and time when the selection of the referenced instances were "
            "made. It is (typically) different from the creation date of the "
            "selection resource, and from dates associated with the referenced "
            "instances (e.g. capture time of the referenced image)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    authoringTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoringTime", title="Extension field for ``authoringTime``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description text",
        description=(
            "Free text narrative description of the ImagingManifest.   The value "
            "may be derived from the DICOM Standard Part 16, CID-7010 descriptions "
            "(e.g. Best in Set, Complete Study Content). Note that those values "
            "cover the wide range of uses of the DICOM Key Object Selection object,"
            " several of which are not supported by ImagingManifest. Specifically, "
            "there is no expected behavior associated with descriptions that "
            "suggest referenced images be removed or not used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="SOP Instance UID",
        description=(
            "Unique identifier of the DICOM Key Object Selection (KOS) that this "
            "resource represents."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Patient of the selected objects",
        description=(
            "A patient resource reference which is the patient subject of all DICOM"
            " SOP Instances in this ImagingManifest."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    study: ListType[fhirtypes.ImagingManifestStudyType] = Field(
        ...,
        alias="study",
        title="Study identity of the selected instances",
        description=(
            "Study identity and locating information of the DICOM SOP instances in "
            "the selection."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class ImagingManifestStudy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Study identity of the selected instances.
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = Field("ImagingManifestStudy", const=True)

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Study access service endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for the study. See implementation notes for information about using "
            "DICOM endpoints. A study-level endpoint applies to each series in the "
            "study, unless overridden by a series-level endpoint with the same "
            "Endpoint.type."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    imagingStudy: fhirtypes.ReferenceType = Field(
        None,
        alias="imagingStudy",
        title="Reference to ImagingStudy",
        description="Reference to the Imaging Study in FHIR form.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ImagingStudy"],
    )

    series: ListType[fhirtypes.ImagingManifestStudySeriesType] = Field(
        ...,
        alias="series",
        title="Series identity of the selected instances",
        description=(
            "Series identity and locating information of the DICOM SOP instances in"
            " the selection."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Study instance UID",
        description="Study instance UID of the SOP instances in the selection.",
        # if property is element of this resource.
        element_property=True,
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )


class ImagingManifestStudySeries(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Series identity of the selected instances.
    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """

    resource_type = Field("ImagingManifestStudySeries", const=True)

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Series access endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for this series. See implementation notes for information about using"
            " DICOM endpoints. A series-level endpoint, if present, has precedence "
            "over a study-level endpoint with the same Endpoint.type."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    instance: ListType[fhirtypes.ImagingManifestStudySeriesInstanceType] = Field(
        ...,
        alias="instance",
        title="The selected instance",
        description="Identity and locating information of the selected DICOM SOP instances.",
        # if property is element of this resource.
        element_property=True,
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Series instance UID",
        description="Series instance UID of the SOP instances in the selection.",
        # if property is element of this resource.
        element_property=True,
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )


class ImagingManifestStudySeriesInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The selected instance.
    Identity and locating information of the selected DICOM SOP instances.
    """

    resource_type = Field("ImagingManifestStudySeriesInstance", const=True)

    sopClass: fhirtypes.Oid = Field(
        ...,
        alias="sopClass",
        title="SOP class UID of instance",
        description="SOP class UID of the selected instance.",
        # if property is element of this resource.
        element_property=True,
    )
    sopClass__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sopClass", title="Extension field for ``sopClass``."
    )

    uid: fhirtypes.Oid = Field(
        ...,
        alias="uid",
        title="Selected instance UID",
        description="SOP Instance UID of the selected instance.",
        # if property is element of this resource.
        element_property=True,
    )
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )
