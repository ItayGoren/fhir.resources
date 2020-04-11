#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-05-14.
#  2019, SMART Health IT.


import io
import json
import os
import unittest

from . import testscript
from .fhirdate import FHIRDate


class TestScriptTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("TestScript", js["resourceType"])
        return testscript.TestScript(js)

    def testTestScript1(self):
        inst = self.instantiate_from("testscript-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript1(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript1(inst2)

    def implTestScript1(self, inst):
        self.assertEqual(inst.contact[0].name, "Support")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].use, "temp")
        self.assertEqual(inst.contact[0].telecom[0].value, "support@gmail.com")
        self.assertEqual(inst.copyright, "© HL7.org 2011+")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-31").date)
        self.assertEqual(inst.date.as_json(), "2015-08-31")
        self.assertEqual(inst.description, "Example Test Script")
        self.assertTrue(inst.experimental)
        self.assertFalse(inst.fixture[0].autocreate)
        self.assertFalse(inst.fixture[0].autodelete)
        self.assertEqual(inst.fixture[0].id, "F1")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(
            inst.identifier.value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9876"
        )
        self.assertEqual(
            inst.metadata.capability[0].description,
            "Patient Create, Read, and Update Operations",
        )
        self.assertEqual(inst.metadata.capability[0].destination, 1)
        self.assertEqual(
            inst.metadata.capability[0].link[0],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#create",
        )
        self.assertEqual(
            inst.metadata.capability[0].link[1],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#read",
        )
        self.assertEqual(
            inst.metadata.capability[0].link[2],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#update",
        )
        self.assertTrue(inst.metadata.capability[0].required)
        self.assertEqual(inst.name, "Test Script 1")
        self.assertEqual(inst.publisher, "HL7")
        self.assertEqual(
            inst.requirements, "Patient Create, Read, and Update Operations"
        )
        self.assertEqual(inst.setup.action[0].operation.accept, "json")
        self.assertEqual(
            inst.setup.action[0].operation.description,
            "Create patient resource on test server",
        )
        self.assertEqual(inst.setup.action[0].operation.label, "SetupPatient")
        self.assertEqual(inst.setup.action[0].operation.responseId, "create-response")
        self.assertEqual(inst.setup.action[0].operation.sourceId, "F1")
        self.assertEqual(inst.setup.action[0].operation.type.code, "create")
        self.assertEqual(inst.setup.action[1].assert_fhir.direction, "request")
        self.assertEqual(inst.setup.action[1].assert_fhir.responseCode, "201")
        self.assertEqual(inst.status, "draft")
        self.assertFalse(inst.test[0].action[0].operation.encodeRequestUrl)
        self.assertEqual(inst.test[0].action[0].operation.responseId, "F1-read")
        self.assertEqual(inst.test[0].action[0].operation.targetId, "F1")
        self.assertEqual(inst.test[0].action[0].operation.type.code, "read")
        self.assertEqual(
            inst.test[0].action[1].assert_fhir.description, "Test for OK response"
        )
        self.assertEqual(inst.test[0].action[1].assert_fhir.direction, "request")
        self.assertEqual(inst.test[0].action[1].assert_fhir.label, "ReadOK")
        self.assertEqual(inst.test[0].action[1].assert_fhir.response, "okay")
        self.assertEqual(
            inst.test[0].action[2].assert_fhir.headerField, "Last-Modified"
        )
        self.assertEqual(inst.test[0].action[2].assert_fhir.operator, "notEmpty")
        self.assertTrue(inst.test[0].action[2].assert_fhir.warningOnly)
        self.assertEqual(inst.test[0].action[3].assert_fhir.resource, "Patient")
        self.assertEqual(
            inst.test[0].action[4].assert_fhir.validateProfileId, "patient-profile"
        )
        self.assertEqual(inst.test[0].action[5].assert_fhir.operator, "equals")
        self.assertEqual(
            inst.test[0].action[5].assert_fhir.path,
            "fhir:Patient/fhir:name/fhir:family/@value",
        )
        self.assertEqual(inst.test[0].action[5].assert_fhir.value, "Chalmers")
        self.assertEqual(inst.test[0].action[6].assert_fhir.operator, "equals")
        self.assertEqual(
            inst.test[0].action[6].assert_fhir.path,
            "fhir:Patient/fhir:name/fhir:family/@value",
        )
        self.assertEqual(inst.test[0].action[6].assert_fhir.sourceId, "F1")
        self.assertEqual(inst.test[0].action[6].assert_fhir.value, "Chalmers")
        self.assertEqual(
            inst.test[0].action[7].assert_fhir.compareToSourceId, "F1-read"
        )
        self.assertEqual(
            inst.test[0].action[7].assert_fhir.compareToSourcePath,
            "fhir:Patient/fhir:name/fhir:family/@value",
        )
        self.assertEqual(inst.test[0].action[7].assert_fhir.operator, "equals")
        self.assertEqual(
            inst.test[0].action[7].assert_fhir.path,
            "fhir:Patient/fhir:name/fhir:family/@value",
        )
        self.assertEqual(
            inst.test[0].action[8].assert_fhir.compareToSourceId, "F1-read"
        )
        self.assertEqual(
            inst.test[0].action[8].assert_fhir.compareToSourcePath,
            "fhir:Patient/fhir:name/fhir:family/@value",
        )
        self.assertEqual(
            inst.test[0].action[8].assert_fhir.path,
            "fhir:Patient/fhir:name/fhir:family/@value",
        )
        self.assertEqual(inst.test[0].action[8].assert_fhir.sourceId, "F1")
        self.assertEqual(inst.test[0].action[9].assert_fhir.minimumId, "F1-min")
        self.assertEqual(
            inst.test[0].description, "Read a patient and validate response."
        )
        self.assertEqual(inst.test[0].id, "READ01")
        self.assertEqual(inst.test[0].name, "Read Patient")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/TestScript/example")
        self.assertEqual(inst.useContext[0].coding[0].code, "US")
        self.assertEqual(
            inst.useContext[0].coding[0].display, "United States of America (the)"
        )
        self.assertEqual(inst.useContext[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.version, "1.0")

    def testTestScript2(self):
        inst = self.instantiate_from("testscript-example-multiserver.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript2(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript2(inst2)

    def implTestScript2(self, inst):
        self.assertEqual(inst.description, "Multiserver Test Script")
        self.assertEqual(inst.fixture[0].id, "F1")
        self.assertEqual(inst.id, "multiserver")
        self.assertTrue(inst.multiserver)
        self.assertEqual(inst.name, "Multiserver Test Script")
        self.assertEqual(inst.setup.action[0].operation.contentType, "xml")
        self.assertEqual(inst.setup.action[0].operation.destination, 0)
        self.assertEqual(inst.setup.action[0].operation.sourceId, "F1")
        self.assertEqual(inst.setup.action[0].operation.type.code, "create")
        self.assertEqual(
            inst.setup.metadata.capability[0].description, "Patient Create Operation"
        )
        self.assertEqual(
            inst.setup.metadata.capability[0].link[0],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#create",
        )
        self.assertTrue(inst.setup.metadata.capability[0].required)
        self.assertEqual(inst.setup.metadata.link[0].description, "FHIR Patient")
        self.assertEqual(
            inst.setup.metadata.link[0].url,
            "http://hl7.org/implement/standards/FHIR-Develop/patient.html",
        )
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.teardown.action[0].operation.destination, 0)
        self.assertEqual(inst.teardown.action[0].operation.targetId, "F1")
        self.assertEqual(inst.teardown.action[0].operation.type.code, "delete")
        self.assertEqual(inst.teardown.action[1].operation.destination, 1)
        self.assertEqual(inst.teardown.action[1].operation.targetId, "F1")
        self.assertEqual(inst.teardown.action[1].operation.type.code, "delete")
        self.assertEqual(inst.test[0].action[0].operation.destination, 0)
        self.assertEqual(inst.test[0].action[0].operation.responseId, "R1")
        self.assertEqual(inst.test[0].action[0].operation.targetId, "F1")
        self.assertEqual(inst.test[0].action[0].operation.type.code, "read")
        self.assertEqual(inst.test[0].action[1].assert_fhir.response, "okay")
        self.assertEqual(
            inst.test[0].action[2].assert_fhir.headerField, "Last-Modified"
        )
        self.assertEqual(inst.test[0].action[2].assert_fhir.operator, "notEmpty")
        self.assertEqual(inst.test[0].action[3].assert_fhir.resource, "Patient")
        self.assertEqual(inst.test[0].action[4].assert_fhir.minimumId, "F1")
        self.assertEqual(inst.test[0].description, "Read the patient from server 0.")
        self.assertEqual(inst.test[0].id, "READ01")
        self.assertEqual(
            inst.test[0].metadata.capability[0].description, "Patient Read Operation"
        )
        self.assertEqual(
            inst.test[0].metadata.capability[0].link[0],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#read",
        )
        self.assertTrue(inst.test[0].metadata.capability[0].validated)
        self.assertEqual(inst.test[0].name, "Read Patient")
        self.assertEqual(inst.test[1].action[0].operation.destination, 1)
        self.assertEqual(inst.test[1].action[0].operation.sourceId, "R1")
        self.assertEqual(inst.test[1].action[0].operation.type.code, "create")
        self.assertEqual(inst.test[1].action[1].assert_fhir.response, "okay")
        self.assertEqual(inst.test[1].action[2].operation.destination, 1)
        self.assertEqual(inst.test[1].action[2].operation.responseId, "R2")
        self.assertEqual(inst.test[1].action[2].operation.targetId, "R1")
        self.assertEqual(inst.test[1].action[2].operation.type.code, "read")
        self.assertEqual(inst.test[1].action[3].assert_fhir.response, "okay")
        self.assertEqual(
            inst.test[1].action[4].assert_fhir.headerField, "Last-Modified"
        )
        self.assertEqual(inst.test[1].action[4].assert_fhir.operator, "notEmpty")
        self.assertEqual(inst.test[1].action[5].assert_fhir.resource, "Patient")
        self.assertEqual(inst.test[1].action[6].assert_fhir.minimumId, "F1")
        self.assertEqual(inst.test[1].action[7].assert_fhir.minimumId, "R1")
        self.assertEqual(
            inst.test[1].description,
            "Write the patient read from server 0 to server 1.",
        )
        self.assertEqual(inst.test[1].id, "WRITE01")
        self.assertEqual(
            inst.test[1].metadata.capability[0].description, "Patient Create Operation"
        )
        self.assertEqual(
            inst.test[1].metadata.capability[0].link[0],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#create",
        )
        self.assertTrue(inst.test[1].metadata.capability[0].validated)
        self.assertEqual(
            inst.test[1].metadata.capability[1].description, "Patient Read Operation"
        )
        self.assertEqual(
            inst.test[1].metadata.capability[1].link[0],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#read",
        )
        self.assertTrue(inst.test[1].metadata.capability[1].validated)
        self.assertEqual(inst.test[1].name, "Write Patient")
        self.assertEqual(inst.test[2].action[0].operation.destination, 0)
        self.assertEqual(inst.test[2].action[0].operation.sourceId, "R2")
        self.assertEqual(inst.test[2].action[0].operation.targetId, "R1")
        self.assertEqual(inst.test[2].action[0].operation.type.code, "update")
        self.assertEqual(inst.test[2].action[1].assert_fhir.response, "okay")
        self.assertEqual(inst.test[2].action[2].operation.destination, 0)
        self.assertEqual(inst.test[2].action[2].operation.responseId, "R3")
        self.assertEqual(inst.test[2].action[2].operation.targetId, "R1")
        self.assertEqual(inst.test[2].action[2].operation.type.code, "read")
        self.assertEqual(inst.test[2].action[3].assert_fhir.response, "okay")
        self.assertEqual(
            inst.test[2].action[4].assert_fhir.headerField, "Last-Modified"
        )
        self.assertEqual(inst.test[2].action[4].assert_fhir.operator, "notEmpty")
        self.assertEqual(inst.test[2].action[5].assert_fhir.resource, "Patient")
        self.assertEqual(inst.test[2].action[6].assert_fhir.minimumId, "F1")
        self.assertEqual(inst.test[2].action[7].assert_fhir.minimumId, "R1")
        self.assertEqual(inst.test[2].action[8].assert_fhir.minimumId, "R2")
        self.assertEqual(
            inst.test[2].description,
            "Update the patient on server 0 with the one read from server 1.",
        )
        self.assertEqual(inst.test[2].id, "UPDATE01")
        self.assertEqual(
            inst.test[2].metadata.capability[0].description, "Patient Update Operation"
        )
        self.assertEqual(
            inst.test[2].metadata.capability[0].link[0],
            "http://hl7.org/implement/standards/FHIR-Develop/http.html#update",
        )
        self.assertTrue(inst.test[2].metadata.capability[0].validated)
        self.assertEqual(inst.test[2].name, "Update Patient")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/TestScript/multiserver")
