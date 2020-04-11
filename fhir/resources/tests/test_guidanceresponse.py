# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import guidanceresponse
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class GuidanceResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("GuidanceResponse", js["resourceType"])
        return guidanceresponse.GuidanceResponse(js)

    def testGuidanceResponse1(self):
        inst = self.instantiate_from("guidanceresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a GuidanceResponse instance")
        self.implGuidanceResponse1(inst)

        js = inst.as_json()
        self.assertEqual("GuidanceResponse", js["resourceType"])
        inst2 = guidanceresponse.GuidanceResponse(js)
        self.implGuidanceResponse1(inst2)

    def implGuidanceResponse1(self, inst):
        self.assertEqual(
            force_bytes(inst.contained[0].id), force_bytes("outputParameters1")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("http://example.org")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("guidanceResponse1")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.moduleUri),
            force_bytes(
                "http://someguidelineprovider.org/radiology-appropriateness-guidelines.html"
            ),
        )
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2017-03-10T16:02:00Z").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2017-03-10T16:02:00Z")
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("Guideline Appropriate Ordering Assessment"),
        )
        self.assertEqual(
            force_bytes(inst.requestIdentifier.system),
            force_bytes("http://example.org"),
        )
        self.assertEqual(
            force_bytes(inst.requestIdentifier.value), force_bytes("guidanceRequest1")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("success"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
