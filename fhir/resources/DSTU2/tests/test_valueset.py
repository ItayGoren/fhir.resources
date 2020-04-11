#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-05-14.
#  2019, SMART Health IT.


import io
import json
import os
import unittest

from . import valueset
from .fhirdate import FHIRDate


class ValueSetTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ValueSet", js["resourceType"])
        return valueset.ValueSet(js)

    def testValueSet1(self):
        inst = self.instantiate_from("valueset-example-inline.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet1(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet1(inst2)

    def implValueSet1(self, inst):
        self.assertTrue(inst.codeSystem.caseSensitive)
        self.assertEqual(inst.codeSystem.concept[0].code, "chol-mmol")
        self.assertEqual(
            inst.codeSystem.concept[0].definition, "Serum Cholesterol, in mmol/L"
        )
        self.assertEqual(
            inst.codeSystem.concept[0].designation[0].use.code, "internal-label"
        )
        self.assertEqual(
            inst.codeSystem.concept[0].designation[0].use.system,
            "http://acme.com/config/fhir/codesystems/internal",
        )
        self.assertEqual(
            inst.codeSystem.concept[0].designation[0].value, "From ACME POC Testing"
        )
        self.assertEqual(inst.codeSystem.concept[0].display, "SChol (mmol/L)")
        self.assertEqual(inst.codeSystem.concept[1].code, "chol-mass")
        self.assertEqual(
            inst.codeSystem.concept[1].definition, "Serum Cholesterol, in mg/L"
        )
        self.assertEqual(
            inst.codeSystem.concept[1].designation[0].use.code, "internal-label"
        )
        self.assertEqual(
            inst.codeSystem.concept[1].designation[0].use.system,
            "http://acme.com/config/fhir/codesystems/internal",
        )
        self.assertEqual(
            inst.codeSystem.concept[1].designation[0].value, "From Paragon Labs"
        )
        self.assertEqual(inst.codeSystem.concept[1].display, "SChol (mg/L)")
        self.assertEqual(inst.codeSystem.concept[2].code, "chol")
        self.assertEqual(inst.codeSystem.concept[2].definition, "Serum Cholesterol")
        self.assertEqual(
            inst.codeSystem.concept[2].designation[0].use.code, "internal-label"
        )
        self.assertEqual(
            inst.codeSystem.concept[2].designation[0].use.system,
            "http://acme.com/config/fhir/codesystems/internal",
        )
        self.assertEqual(
            inst.codeSystem.concept[2].designation[0].value,
            "Obdurate Labs uses this with both kinds of units...",
        )
        self.assertEqual(inst.codeSystem.concept[2].display, "SChol")
        self.assertEqual(
            inst.codeSystem.system,
            "http://acme.com/config/fhir/codesystems/cholesterol",
        )
        self.assertEqual(inst.codeSystem.version, "4.2.3")
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2015-06-22").date)
        self.assertEqual(inst.date.as_json(), "2015-06-22")
        self.assertEqual(
            inst.description,
            "This is an example value set that includes all the ACME codes for serum/plasma cholesterol from v2.36.",
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-inline")
        self.assertEqual(
            inst.identifier.system, "http://acme.com/identifiers/valuesets"
        )
        self.assertEqual(inst.identifier.value, "loinc-cholesterol-inl")
        self.assertEqual(
            inst.meta.profile[0],
            "http://hl7.org/fhir/StructureDefinition/valueset-shareable-definition",
        )
        self.assertEqual(inst.name, "ACME Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.publisher, "HL7 International")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-inline")
        self.assertEqual(inst.version, "20150622")

    def testValueSet2(self):
        inst = self.instantiate_from("valueset-example-intensional.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet2(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet2(inst2)

    def implValueSet2(self, inst):
        self.assertEqual(inst.compose.exclude[0].concept[0].code, "5932-9")
        self.assertEqual(
            inst.compose.exclude[0].concept[0].display,
            "Cholesterol [Presence] in Blood by Test strip",
        )
        self.assertEqual(inst.compose.exclude[0].system, "http://loinc.org")
        self.assertEqual(inst.compose.include[0].filter[0].op, "=")
        self.assertEqual(inst.compose.include[0].filter[0].property, "parent")
        self.assertEqual(inst.compose.include[0].filter[0].value, "LP43571-6")
        self.assertEqual(inst.compose.include[0].system, "http://loinc.org")
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(
            inst.copyright,
            "This content from LOINCÂ® is copyright Â© 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use",
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-06-22").date)
        self.assertEqual(inst.date.as_json(), "2015-06-22")
        self.assertEqual(
            inst.description,
            "This is an example value set that includes all the LOINC codes for serum/plasma cholesterol from v2.36.",
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-intensional")
        self.assertEqual(
            inst.identifier.system, "http://acme.com/identifiers/valuesets"
        )
        self.assertEqual(inst.identifier.value, "loinc-cholesterol-ext")
        self.assertEqual(
            inst.meta.profile[0],
            "http://hl7.org/fhir/StructureDefinition/valueset-shareable-definition",
        )
        self.assertEqual(inst.name, "LOINC Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.publisher, "HL7 International")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-intensional")
        self.assertEqual(inst.version, "20150622")

    def testValueSet3(self):
        inst = self.instantiate_from("valueset-example-expansion.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet3(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet3(inst2)

    def implValueSet3(self, inst):
        self.assertEqual(inst.compose.include[0].filter[0].op, "=")
        self.assertEqual(inst.compose.include[0].filter[0].property, "parent")
        self.assertEqual(inst.compose.include[0].filter[0].value, "LP43571-6")
        self.assertEqual(inst.compose.include[0].system, "http://loinc.org")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(
            inst.copyright,
            "This content from LOINC® is copyright © 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use.",
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-06-22").date)
        self.assertEqual(inst.date.as_json(), "2015-06-22")
        self.assertEqual(
            inst.description,
            "This is an example value set that includes all the LOINC codes for serum/plasma cholesterol from v2.36.",
        )
        self.assertEqual(inst.expansion.contains[0].code, "14647-2")
        self.assertEqual(
            inst.expansion.contains[0].display,
            "Cholesterol [Moles/volume] in Serum or Plasma",
        )
        self.assertEqual(inst.expansion.contains[0].system, "http://loinc.org")
        self.assertEqual(inst.expansion.contains[0].version, "2.50")
        self.assertTrue(inst.expansion.contains[1].abstract)
        self.assertEqual(inst.expansion.contains[1].contains[0].code, "2093-3")
        self.assertEqual(
            inst.expansion.contains[1].contains[0].display,
            "Cholesterol [Mass/volume] in Serum or Plasma",
        )
        self.assertEqual(
            inst.expansion.contains[1].contains[0].system, "http://loinc.org"
        )
        self.assertEqual(inst.expansion.contains[1].contains[0].version, "2.50")
        self.assertEqual(inst.expansion.contains[1].contains[1].code, "48620-9")
        self.assertEqual(
            inst.expansion.contains[1].contains[1].display,
            "Cholesterol [Mass/volume] in Serum or Plasma ultracentrifugate",
        )
        self.assertEqual(
            inst.expansion.contains[1].contains[1].system, "http://loinc.org"
        )
        self.assertEqual(inst.expansion.contains[1].contains[1].version, "2.50")
        self.assertEqual(inst.expansion.contains[1].contains[2].code, "9342-7")
        self.assertEqual(
            inst.expansion.contains[1].contains[2].display, "Cholesterol [Percentile]"
        )
        self.assertEqual(
            inst.expansion.contains[1].contains[2].system, "http://loinc.org"
        )
        self.assertEqual(inst.expansion.contains[1].contains[2].version, "2.50")
        self.assertEqual(inst.expansion.contains[1].display, "Cholesterol codes")
        self.assertTrue(inst.expansion.contains[2].abstract)
        self.assertEqual(inst.expansion.contains[2].contains[0].code, "2096-6")
        self.assertEqual(
            inst.expansion.contains[2].contains[0].display,
            "Cholesterol/Triglyceride [Mass Ratio] in Serum or Plasma",
        )
        self.assertEqual(
            inst.expansion.contains[2].contains[0].system, "http://loinc.org"
        )
        self.assertEqual(inst.expansion.contains[2].contains[0].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].contains[1].code, "35200-5")
        self.assertEqual(
            inst.expansion.contains[2].contains[1].display,
            "Cholesterol/Triglyceride [Mass Ratio] in Serum or Plasma",
        )
        self.assertEqual(
            inst.expansion.contains[2].contains[1].system, "http://loinc.org"
        )
        self.assertEqual(inst.expansion.contains[2].contains[1].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].contains[2].code, "48089-7")
        self.assertEqual(
            inst.expansion.contains[2].contains[2].display,
            "Cholesterol/Apolipoprotein B [Molar ratio] in Serum or Plasma",
        )
        self.assertEqual(
            inst.expansion.contains[2].contains[2].system, "http://loinc.org"
        )
        self.assertEqual(inst.expansion.contains[2].contains[2].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].contains[3].code, "55838-7")
        self.assertEqual(
            inst.expansion.contains[2].contains[3].display,
            "Cholesterol/Phospholipid [Molar ratio] in Serum or Plasma",
        )
        self.assertEqual(
            inst.expansion.contains[2].contains[3].system, "http://loinc.org"
        )
        self.assertEqual(inst.expansion.contains[2].contains[3].version, "2.50")
        self.assertEqual(inst.expansion.contains[2].display, "Cholesterol Ratios")
        self.assertEqual(
            inst.expansion.extension[0].url,
            "http://hl7.org/fhir/StructureDefinition/valueset-expansionSource",
        )
        self.assertEqual(
            inst.expansion.extension[0].valueUri,
            "http://hl7.org/fhir/ValueSet/example-extensional",
        )
        self.assertEqual(
            inst.expansion.identifier, "urn:uuid:42316ff8-2714-4680-9980-f37a6d1a71bc"
        )
        self.assertEqual(inst.expansion.offset, 0)
        self.assertEqual(inst.expansion.parameter[0].name, "version")
        self.assertEqual(inst.expansion.parameter[0].valueString, "2.50")
        self.assertEqual(
            inst.expansion.timestamp.date, FHIRDate("2015-06-22T13:56:07Z").date
        )
        self.assertEqual(inst.expansion.timestamp.as_json(), "2015-06-22T13:56:07Z")
        self.assertEqual(inst.expansion.total, 8)
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-expansion")
        self.assertEqual(
            inst.meta.profile[0],
            "http://hl7.org/fhir/StructureDefinition/valueset-shareable-definition",
        )
        self.assertEqual(inst.name, "LOINC Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.publisher, "FHIR Project team")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-expansion")
        self.assertEqual(inst.version, "20150622")

    def testValueSet4(self):
        inst = self.instantiate_from("valueset-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet4(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet4(inst2)

    def implValueSet4(self, inst):
        self.assertEqual(inst.compose.include[0].concept[0].code, "14647-2")
        self.assertEqual(
            inst.compose.include[0].concept[0].display, "Cholesterol [Moles/Volume]"
        )
        self.assertEqual(inst.compose.include[0].concept[1].code, "2093-3")
        self.assertEqual(
            inst.compose.include[0].concept[1].display, "Cholesterol [Mass/Volume]"
        )
        self.assertEqual(inst.compose.include[0].concept[2].code, "35200-5")
        self.assertEqual(
            inst.compose.include[0].concept[2].display,
            "Cholesterol [Mass Or Moles/Volume]",
        )
        self.assertEqual(inst.compose.include[0].concept[3].code, "9342-7")
        self.assertEqual(
            inst.compose.include[0].concept[3].display, "Cholesterol [Percentile]"
        )
        self.assertEqual(inst.compose.include[0].system, "http://loinc.org")
        self.assertEqual(inst.compose.include[0].version, "2.36")
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(
            inst.copyright,
            "This content from LOINCÂ® is copyright Â© 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use.",
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-06-22").date)
        self.assertEqual(inst.date.as_json(), "2015-06-22")
        self.assertEqual(
            inst.description,
            "This is an example value set that includes all the LOINC codes for serum/plasma cholesterol from v2.36.",
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example-extensional")
        self.assertEqual(
            inst.identifier.system, "http://acme.com/identifiers/valuesets"
        )
        self.assertEqual(inst.identifier.value, "loinc-cholesterol-int")
        self.assertEqual(inst.lockedDate.date, FHIRDate("2012-06-13").date)
        self.assertEqual(inst.lockedDate.as_json(), "2012-06-13")
        self.assertEqual(
            inst.meta.profile[0],
            "http://hl7.org/fhir/StructureDefinition/valueset-shareable-definition",
        )
        self.assertEqual(inst.name, "LOINC Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.publisher, "HL7 International")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/example-extensional")
        self.assertEqual(inst.version, "20150622")

    def testValueSet5(self):
        inst = self.instantiate_from("valueset-example-yesnodontknow.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet5(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet5(inst2)

    def implValueSet5(self, inst):
        self.assertEqual(
            inst.compose.import_fhir[0], "http://hl7.org/fhir/ValueSet/v2-0136"
        )
        self.assertEqual(inst.compose.include[0].concept[0].code, "asked")
        self.assertEqual(inst.compose.include[0].concept[0].display, "Don't know")
        self.assertEqual(
            inst.compose.include[0].system, "http://hl7.org/fhir/data-absent-reason"
        )
        self.assertEqual(
            inst.description, "For Capturing simple yes-no-don't know answers"
        )
        self.assertEqual(inst.expansion.contains[0].code, "Y")
        self.assertEqual(inst.expansion.contains[0].display, "Yes")
        self.assertEqual(
            inst.expansion.contains[0].system, "http://hl7.org/fhir/v2/0136"
        )
        self.assertEqual(inst.expansion.contains[1].code, "N")
        self.assertEqual(inst.expansion.contains[1].display, "No")
        self.assertEqual(
            inst.expansion.contains[1].system, "http://hl7.org/fhir/v2/0136"
        )
        self.assertEqual(inst.expansion.contains[2].code, "asked")
        self.assertEqual(inst.expansion.contains[2].display, "Don't know")
        self.assertEqual(
            inst.expansion.contains[2].system, "http://hl7.org/fhir/data-absent-reason"
        )
        self.assertEqual(
            inst.expansion.identifier, "urn:uuid:bf99fe50-2c2b-41ad-bd63-bee6919810b4"
        )
        self.assertEqual(
            inst.expansion.timestamp.date, FHIRDate("2015-07-14T10:00:00Z").date
        )
        self.assertEqual(inst.expansion.timestamp.as_json(), "2015-07-14T10:00:00Z")
        self.assertEqual(inst.id, "yesnodontknow")
        self.assertEqual(inst.name, "Yes/No/Don't Know")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/yesnodontknow")

    def testValueSet6(self):
        inst = self.instantiate_from("valueset-list-example-codes.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet6(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet6(inst2)

    def implValueSet6(self, inst):
        self.assertTrue(inst.codeSystem.caseSensitive)
        self.assertEqual(inst.codeSystem.concept[0].code, "alerts")
        self.assertEqual(
            inst.codeSystem.concept[0].definition, "A list of alerts for the patient."
        )
        self.assertEqual(inst.codeSystem.concept[0].display, "Alerts")
        self.assertEqual(inst.codeSystem.concept[1].code, "adverserxns")
        self.assertEqual(
            inst.codeSystem.concept[1].definition, "A list of part adverse reactions."
        )
        self.assertEqual(inst.codeSystem.concept[1].display, "Adverse Reactions")
        self.assertEqual(inst.codeSystem.concept[2].code, "allergies")
        self.assertEqual(
            inst.codeSystem.concept[2].definition,
            "A list of Allergies for the patient.",
        )
        self.assertEqual(inst.codeSystem.concept[2].display, "Allergies")
        self.assertEqual(inst.codeSystem.concept[3].code, "medications")
        self.assertEqual(
            inst.codeSystem.concept[3].definition,
            "A list of medication statements for the patient.",
        )
        self.assertEqual(inst.codeSystem.concept[3].display, "Medication List")
        self.assertEqual(inst.codeSystem.concept[4].code, "problems")
        self.assertEqual(
            inst.codeSystem.concept[4].definition,
            "A list of problems that the patient is known of have (or have had in the past).",
        )
        self.assertEqual(inst.codeSystem.concept[4].display, "Problem List")
        self.assertEqual(inst.codeSystem.concept[5].code, "worklist")
        self.assertEqual(
            inst.codeSystem.concept[5].definition,
            "A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list).",
        )
        self.assertEqual(inst.codeSystem.concept[5].display, "Worklist")
        self.assertEqual(inst.codeSystem.concept[6].code, "waiting")
        self.assertEqual(
            inst.codeSystem.concept[6].definition,
            "A list of items waiting for an event (perhaps a surgical patient waiting list).",
        )
        self.assertEqual(inst.codeSystem.concept[6].display, "Waiting List")
        self.assertEqual(inst.codeSystem.concept[7].code, "protocols")
        self.assertEqual(
            inst.codeSystem.concept[7].definition, "A set of protocols to be followed."
        )
        self.assertEqual(inst.codeSystem.concept[7].display, "Protocols")
        self.assertEqual(inst.codeSystem.concept[8].code, "plans")
        self.assertEqual(
            inst.codeSystem.concept[8].definition,
            "A set of care plans that apply in a particular context of care.",
        )
        self.assertEqual(inst.codeSystem.concept[8].display, "Care Plans")
        self.assertEqual(
            inst.codeSystem.extension[0].url,
            "http://hl7.org/fhir/StructureDefinition/valueset-oid",
        )
        self.assertEqual(
            inst.codeSystem.extension[0].valueUri,
            "urn:oid:2.16.840.1.113883.4.642.1.173",
        )
        self.assertEqual(
            inst.codeSystem.system, "http://hl7.org/fhir/list-example-use-codes"
        )
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2015-10-24T07:41:03+11:00").date)
        self.assertEqual(inst.date.as_json(), "2015-10-24T07:41:03+11:00")
        self.assertEqual(
            inst.description,
            "Example use codes for the List resource - typical kinds of use.",
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            inst.extension[0].url,
            "http://hl7.org/fhir/StructureDefinition/valueset-oid",
        )
        self.assertEqual(
            inst.extension[0].valueUri, "urn:oid:2.16.840.1.113883.4.642.2.173"
        )
        self.assertEqual(inst.id, "list-example-codes")
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2015-10-24T07:41:03.495+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2015-10-24T07:41:03.495+11:00"
        )
        self.assertEqual(
            inst.meta.profile[0],
            "http://hl7.org/fhir/StructureDefinition/valueset-shareable-definition",
        )
        self.assertEqual(inst.name, "Example Use Codes for List")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/list-example-codes")
        self.assertEqual(inst.version, "1.0.2")
