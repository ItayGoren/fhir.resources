# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse
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

from .. import coverageeligibilityresponse
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CoverageEligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        return coverageeligibilityresponse.CoverageEligibilityResponse(js)

    def testCoverageEligibilityResponse1(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CoverageEligibilityResponse instance"
        )
        self.implCoverageEligibilityResponse1(inst)

        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse1(inst2)

    def implCoverageEligibilityResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Policy is currently in-force.")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("E2500"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("881234"))
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.purpose[0]), force_bytes("validation"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the CoverageEligibilityResponse.</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCoverageEligibilityResponse2(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example-error.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a CoverageEligibilityResponse instance"
        )
        self.implCoverageEligibilityResponse2(inst)

        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse2(inst2)

    def implCoverageEligibilityResponse2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(
            force_bytes(inst.disposition),
            force_bytes(
                "Eligibiliy request could not be processed, please address errors before submitting."
            ),
        )
        self.assertEqual(
            force_bytes(inst.error[0].code.coding[0].code), force_bytes("a001")
        )
        self.assertEqual(
            force_bytes(inst.error[0].code.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/adjudication-error"),
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("ELRSP/2017/01")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://national.org/form"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("E2503"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("8812343"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("error"))
        self.assertEqual(force_bytes(inst.purpose[0]), force_bytes("validation"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the CoverageEligibilityResponse.</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCoverageEligibilityResponse3(self):
        inst = self.instantiate_from(
            "coverageeligibilityresponse-example-benefits-2.json"
        )
        self.assertIsNotNone(
            inst, "Must have instantiated a CoverageEligibilityResponse instance"
        )
        self.implCoverageEligibilityResponse3(inst)

        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse3(inst2)

    def implCoverageEligibilityResponse3(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("coverage-1"))
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Policy is currently in-force.")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].code), force_bytes("ELRSP/2017/01")
        )
        self.assertEqual(
            force_bytes(inst.form.coding[0].system),
            force_bytes("http://national.org/form"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("E2502"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("8812342"))
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[0].allowedMoney.currency),
            force_bytes("USD"),
        )
        self.assertEqual(
            inst.insurance[0].item[0].benefit[0].allowedMoney.value, 500000
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[0].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[0].usedMoney.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.insurance[0].item[0].benefit[0].usedMoney.value, 3748.0)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[1].allowedMoney.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.value, 100)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[1].type.coding[0].code),
            force_bytes("copay-maximum"),
        )
        self.assertEqual(inst.insurance[0].item[0].benefit[2].allowedUnsignedInt, 20)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[2].type.coding[0].code),
            force_bytes("copay-percent"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].category.coding[0].code),
            force_bytes("30"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].category.coding[0].display),
            force_bytes("Health Benefit Plan Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].term.coding[0].code),
            force_bytes("annual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].benefit[0].allowedMoney.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.value, 15000)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].benefit[0].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].category.coding[0].code),
            force_bytes("69"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].category.coding[0].display),
            force_bytes("Maternity"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].term.coding[0].code),
            force_bytes("annual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].benefit[0].allowedMoney.currency),
            force_bytes("USD"),
        )
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.value, 2000)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].benefit[0].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].category.coding[0].code),
            force_bytes("F3"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].category.coding[0].display),
            force_bytes("Dental Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].term.coding[0].code),
            force_bytes("annual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].description),
            force_bytes(
                "Vision products and services such as exams, glasses and contact lenses."
            ),
        )
        self.assertTrue(inst.insurance[0].item[3].excluded)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].name), force_bytes("Vision")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.purpose[0]), force_bytes("validation"))
        self.assertEqual(force_bytes(inst.purpose[1]), force_bytes("benefits"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the CoverageEligibilityResponse.</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCoverageEligibilityResponse4(self):
        inst = self.instantiate_from(
            "coverageeligibilityresponse-example-benefits.json"
        )
        self.assertIsNotNone(
            inst, "Must have instantiated a CoverageEligibilityResponse instance"
        )
        self.implCoverageEligibilityResponse4(inst)

        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse4(inst2)

    def implCoverageEligibilityResponse4(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.disposition), force_bytes("Policy is currently in-force.")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("E2501"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.BenefitsInc.com/fhir/coverageeligibilityresponse"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("881234"))
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[0].allowedMoney.currency),
            force_bytes("SAR"),
        )
        self.assertEqual(
            inst.insurance[0].item[0].benefit[0].allowedMoney.value, 500000
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[0].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[1].allowedMoney.currency),
            force_bytes("SAR"),
        )
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.value, 100)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[1].type.coding[0].code),
            force_bytes("copay-maximum"),
        )
        self.assertEqual(inst.insurance[0].item[0].benefit[2].allowedUnsignedInt, 20)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].benefit[2].type.coding[0].code),
            force_bytes("copay-percent"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].category.coding[0].code),
            force_bytes("30"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].category.coding[0].display),
            force_bytes("Health Benefit Plan Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].term.coding[0].code),
            force_bytes("annual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[0].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].benefit[0].allowedMoney.currency),
            force_bytes("SAR"),
        )
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.value, 15000)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].benefit[0].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].category.coding[0].code),
            force_bytes("69"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].category.coding[0].display),
            force_bytes("Maternity"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].term.coding[0].code),
            force_bytes("annual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[1].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].benefit[0].allowedMoney.currency),
            force_bytes("SAR"),
        )
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.value, 2000)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].benefit[0].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].category.coding[0].code),
            force_bytes("F3"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].category.coding[0].display),
            force_bytes("Dental Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].term.coding[0].code),
            force_bytes("annual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[2].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].benefit[0].allowedMoney.currency),
            force_bytes("SAR"),
        )
        self.assertEqual(inst.insurance[0].item[3].benefit[0].allowedMoney.value, 400)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].benefit[0].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].category.coding[0].code),
            force_bytes("F6"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].category.coding[0].display),
            force_bytes("Vision Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].term.coding[0].code),
            force_bytes("annual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[3].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].benefit[0].allowedString),
            force_bytes("shared"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].benefit[0].type.coding[0].code),
            force_bytes("room"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].benefit[1].allowedMoney.currency),
            force_bytes("SAR"),
        )
        self.assertEqual(inst.insurance[0].item[4].benefit[1].allowedMoney.value, 600)
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].benefit[1].type.coding[0].code),
            force_bytes("benefit"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].category.coding[0].code),
            force_bytes("49"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].category.coding[0].display),
            force_bytes("Hospital Room and Board"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].category.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].network.coding[0].code),
            force_bytes("in"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].network.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-network"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].term.coding[0].code),
            force_bytes("day"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].term.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-term"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].unit.coding[0].code),
            force_bytes("individual"),
        )
        self.assertEqual(
            force_bytes(inst.insurance[0].item[4].unit.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-unit"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.outcome), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.purpose[0]), force_bytes("validation"))
        self.assertEqual(force_bytes(inst.purpose[1]), force_bytes("benefits"))
        self.assertEqual(inst.servicedDate.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the CoverageEligibilityResponse.</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
