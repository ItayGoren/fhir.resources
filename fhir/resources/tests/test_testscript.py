# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TestScript
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

from .. import testscript
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class TestScriptTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("TestScript", js["resourceType"])
        return testscript.TestScript(js)

    def testTestScript1(self):
        inst = self.instantiate_from("testscript-example-multisystem.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript1(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript1(inst2)

    def implTestScript1(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("Support"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("support@HL7.org"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-01-18").date)
        self.assertEqual(inst.date.as_json(), "2017-01-18")
        self.assertEqual(inst.destination[0].index, 1)
        self.assertEqual(
            force_bytes(inst.destination[0].profile.code), force_bytes("FHIR-Server")
        )
        self.assertEqual(inst.destination[1].index, 2)
        self.assertEqual(
            force_bytes(inst.destination[1].profile.code), force_bytes("FHIR-Server")
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("testscript-example-multisystem")
        )
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9878"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America (the)"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].capabilities),
            force_bytes("CapabilityStatement/example"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].description),
            force_bytes("Patient Read Operation"),
        )
        self.assertEqual(inst.metadata.capability[0].destination, 1)
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[0]),
            force_bytes("http://hl7.org/fhir/http.html#read"),
        )
        self.assertEqual(inst.metadata.capability[0].origin[0], 1)
        self.assertTrue(inst.metadata.capability[0].required)
        self.assertFalse(inst.metadata.capability[0].validated)
        self.assertEqual(
            force_bytes(inst.metadata.capability[1].capabilities),
            force_bytes("CapabilityStatement/example"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[1].description),
            force_bytes("Patient Read Operation"),
        )
        self.assertEqual(inst.metadata.capability[1].destination, 2)
        self.assertEqual(
            force_bytes(inst.metadata.capability[1].link[0]),
            force_bytes("http://hl7.org/fhir/http.html#read"),
        )
        self.assertEqual(inst.metadata.capability[1].origin[0], 1)
        self.assertTrue(inst.metadata.capability[1].required)
        self.assertFalse(inst.metadata.capability[1].validated)
        self.assertEqual(
            force_bytes(inst.metadata.link[0].description),
            force_bytes(
                "Demographics and other administrative information about an individual or animal receiving care or other health-related services."
            ),
        )
        self.assertEqual(
            force_bytes(inst.metadata.link[0].url),
            force_bytes("http://hl7.org/fhir/patient.html"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("testscript-example-multisystem")
        )
        self.assertEqual(inst.origin[0].index, 1)
        self.assertEqual(
            force_bytes(inst.origin[0].profile.code), force_bytes("FHIR-Client")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7"))
        self.assertEqual(
            force_bytes(inst.purpose), force_bytes("Patient Read Operation")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.description),
            force_bytes(
                "Read a Patient from the first destination test system and perform basic validation."
            ),
        )
        self.assertEqual(inst.test[0].action[0].operation.destination, 1)
        self.assertTrue(inst.test[0].action[0].operation.encodeRequestUrl)
        self.assertEqual(inst.test[0].action[0].operation.origin, 1)
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.params),
            force_bytes("/${Dest1PatientResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.requestId),
            force_bytes("request-read-patient-01"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.description),
            force_bytes(
                "Confirm that the request method GET was sent by the client system under test."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.requestMethod),
            force_bytes("get"),
        )
        self.assertFalse(inst.test[0].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.description),
            force_bytes("Confirm that the client requested an Accept of xml."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.direction),
            force_bytes("request"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.headerField),
            force_bytes("Accept"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.operator),
            force_bytes("contains"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.value), force_bytes("xml")
        )
        self.assertFalse(inst.test[0].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[0].action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.description),
            force_bytes("Confirm that the returned format is XML."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertFalse(inst.test[0].action[4].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Patient."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.resource),
            force_bytes("Patient"),
        )
        self.assertFalse(inst.test[0].action[5].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].description),
            force_bytes(
                "Read a Patient from the first destination test system using the user defined dynamic variable ${Dest1PatientResourceId}. Perform basic validation."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].id), force_bytes("01-ReadPatient-Destination1")
        )
        self.assertEqual(
            force_bytes(inst.test[0].name), force_bytes("ReadPatient-Destination1")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.description),
            force_bytes(
                "Read a Patient from the second destination test system and perform basic validation."
            ),
        )
        self.assertEqual(inst.test[1].action[0].operation.destination, 2)
        self.assertTrue(inst.test[1].action[0].operation.encodeRequestUrl)
        self.assertEqual(inst.test[1].action[0].operation.origin, 1)
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.params),
            force_bytes("/${Dest2PatientResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.requestHeader[0].field),
            force_bytes("Accept-Charset"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.requestHeader[0].value),
            force_bytes("utf-8"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.description),
            force_bytes("Confirm that the client requested an Accept of xml."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.direction),
            force_bytes("request"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.headerField),
            force_bytes("Accept"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.operator),
            force_bytes("contains"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.value), force_bytes("xml")
        )
        self.assertFalse(inst.test[1].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[2].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[2].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[2].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[1].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[3].assert_fhir.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[3].assert_fhir.description),
            force_bytes("Confirm that the returned format is XML."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[3].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertFalse(inst.test[1].action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[4].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Patient."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[4].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[4].assert_fhir.resource),
            force_bytes("Patient"),
        )
        self.assertFalse(inst.test[1].action[4].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].description),
            force_bytes(
                "Read a Patient from the second destination test system using the user defined dynamic variable ${Dest2PatientResourceId}. Perform basic validation."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].id), force_bytes("02-ReadPatient-Destination2")
        )
        self.assertEqual(
            force_bytes(inst.test[1].name), force_bytes("ReadPatient-Destination2")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Multisystem Test Script")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/TestScript/testscript-example-multisystem"
            ),
        )
        self.assertEqual(
            force_bytes(inst.variable[0].defaultValue), force_bytes("example")
        )
        self.assertEqual(
            force_bytes(inst.variable[0].name), force_bytes("Dest1PatientResourceId")
        )
        self.assertEqual(
            force_bytes(inst.variable[1].defaultValue), force_bytes("example")
        )
        self.assertEqual(
            force_bytes(inst.variable[1].name), force_bytes("Dest2PatientResourceId")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0"))

    def testTestScript2(self):
        inst = self.instantiate_from("testscript-example-history.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript2(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript2(inst2)

    def implTestScript2(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("Support"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("support@HL7.org"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-01-18").date)
        self.assertEqual(inst.date.as_json(), "2017-01-18")
        self.assertTrue(inst.experimental)
        self.assertFalse(inst.fixture[0].autocreate)
        self.assertFalse(inst.fixture[0].autodelete)
        self.assertEqual(
            force_bytes(inst.fixture[0].id), force_bytes("fixture-patient-create")
        )
        self.assertFalse(inst.fixture[1].autocreate)
        self.assertFalse(inst.fixture[1].autodelete)
        self.assertEqual(
            force_bytes(inst.fixture[1].id), force_bytes("fixture-patient-update")
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("testscript-example-history")
        )
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9877"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America (the)"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].capabilities),
            force_bytes("CapabilityStatement/example"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].description),
            force_bytes("Patient Update, Delete and History (Instance) Operations"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[0]),
            force_bytes("http://hl7.org/fhir/http.html#update"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[1]),
            force_bytes("http://hl7.org/fhir/http.html#delete"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[2]),
            force_bytes("http://hl7.org/fhir/http.html#history"),
        )
        self.assertTrue(inst.metadata.capability[0].required)
        self.assertFalse(inst.metadata.capability[0].validated)
        self.assertEqual(
            force_bytes(inst.metadata.link[0].description),
            force_bytes(
                "Demographics and other administrative information about an individual or animal receiving care or other health-related services."
            ),
        )
        self.assertEqual(
            force_bytes(inst.metadata.link[0].url),
            force_bytes("http://hl7.org/fhir/patient.html"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("TestScript Example History")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7"))
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "Patient (Conditional) Create, Update, Delete and History (Instance) Operations"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.accept), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.description),
            force_bytes(
                "Execute a delete operation to insure the patient does not exist on the server."
            ),
        )
        self.assertTrue(inst.setup.action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.label),
            force_bytes("SetupDeletePatient"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.code), force_bytes("delete")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.description),
            force_bytes(
                "Confirm that the returned HTTP status is 200(OK) or 204(No Content)."
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.operator), force_bytes("in")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.responseCode),
            force_bytes("200,204"),
        )
        self.assertFalse(inst.setup.action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.accept), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.contentType), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.description),
            force_bytes(
                "Create patient resource on test server using the contents of fixture-patient-create"
            ),
        )
        self.assertTrue(inst.setup.action[2].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.label),
            force_bytes("SetupCreatePatient"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.sourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.type.code), force_bytes("update")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 201(Created)."),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.responseCode),
            force_bytes("201"),
        )
        self.assertFalse(inst.setup.action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.accept), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.contentType), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.description),
            force_bytes(
                "Update patient resource on test server using the contents of fixture-patient-update"
            ),
        )
        self.assertTrue(inst.setup.action[4].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.label),
            force_bytes("SetupUpdatePatient"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.sourceId),
            force_bytes("fixture-patient-update"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.type.code), force_bytes("update")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[5].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[5].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[5].assert_fhir.responseCode),
            force_bytes("200"),
        )
        self.assertFalse(inst.setup.action[5].assert_fhir.warningOnly)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.accept), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.contentType),
            force_bytes("json"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.description),
            force_bytes(
                "Get the Patient history on the test server using the id from fixture-patient-create."
            ),
        )
        self.assertTrue(inst.test[0].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.targetId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.code),
            force_bytes("history"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[0].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Bundle."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.resource),
            force_bytes("Bundle"),
        )
        self.assertFalse(inst.test[0].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Bundle conforms to the base FHIR specification."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.validateProfileId),
            force_bytes("bundle-profile"),
        )
        self.assertFalse(inst.test[0].action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.description),
            force_bytes("Confirm that the returned Bundle type equals 'history'."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.operator),
            force_bytes("equals"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.path),
            force_bytes("fhir:Bundle/fhir:type/@value"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.value),
            force_bytes("history"),
        )
        self.assertFalse(inst.test[0].action[4].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].description),
            force_bytes("Get the history for a known Patient and validate response."),
        )
        self.assertEqual(force_bytes(inst.test[0].id), force_bytes("01-HistoryPatient"))
        self.assertEqual(force_bytes(inst.test[0].name), force_bytes("History Patient"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/TestScript/testscript-example-history"),
        )
        self.assertEqual(
            force_bytes(inst.variable[0].name), force_bytes("createResourceId")
        )
        self.assertEqual(force_bytes(inst.variable[0].path), force_bytes("Patient/id"))
        self.assertEqual(
            force_bytes(inst.variable[0].sourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0"))

    def testTestScript3(self):
        inst = self.instantiate_from("testscript-example-update.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript3(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript3(inst2)

    def implTestScript3(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("Support"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("support@HL7.org"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-01-18").date)
        self.assertEqual(inst.date.as_json(), "2017-01-18")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "TestScript example resource with setup to delete if present and create a new instance of a Patient; and single test definition to update that Patient with various asserts."
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertFalse(inst.fixture[0].autocreate)
        self.assertFalse(inst.fixture[0].autodelete)
        self.assertEqual(
            force_bytes(inst.fixture[0].id), force_bytes("fixture-patient-create")
        )
        self.assertFalse(inst.fixture[1].autocreate)
        self.assertFalse(inst.fixture[1].autodelete)
        self.assertEqual(
            force_bytes(inst.fixture[1].id), force_bytes("fixture-patient-update")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("testscript-example-update"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9882"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America (the)"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].capabilities),
            force_bytes("CapabilityStatement/example"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].description),
            force_bytes("Patient Update and Delete Operations"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[0]),
            force_bytes("http://hl7.org/fhir/http.html#update"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[1]),
            force_bytes("http://hl7.org/fhir/http.html#delete"),
        )
        self.assertTrue(inst.metadata.capability[0].required)
        self.assertFalse(inst.metadata.capability[0].validated)
        self.assertEqual(
            force_bytes(inst.metadata.link[0].description),
            force_bytes(
                "Demographics and other administrative information about an individual or animal receiving care or other health-related services."
            ),
        )
        self.assertEqual(
            force_bytes(inst.metadata.link[0].url),
            force_bytes("http://hl7.org/fhir/patient.html"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("TestScript Example Update")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7"))
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes("Patient (Conditional) Create, Update, Delete Operations"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.description),
            force_bytes(
                "Execute a delete operation to insure the patient does not exist on the server."
            ),
        )
        self.assertTrue(inst.setup.action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.label),
            force_bytes("SetupDeletePatient"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.code), force_bytes("delete")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.description),
            force_bytes(
                "Confirm that the returned HTTP status is 200(OK) or 204(No Content)."
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.operator), force_bytes("in")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.responseCode),
            force_bytes("200,204"),
        )
        self.assertFalse(inst.setup.action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.contentType), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.description),
            force_bytes(
                "Create patient resource on test server using the contents of fixture-patient-create"
            ),
        )
        self.assertTrue(inst.setup.action[2].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.label),
            force_bytes("SetupCreatePatient"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.sourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.type.code), force_bytes("update")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 201(Created)."),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.responseCode),
            force_bytes("201"),
        )
        self.assertFalse(inst.setup.action[3].assert_fhir.warningOnly)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.description),
            force_bytes(
                "Update patient resource on test server using the contents of fixture-patient-update"
            ),
        )
        self.assertTrue(inst.test[0].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.label),
            force_bytes("SetupUpdatePatient"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.sourceId),
            force_bytes("fixture-patient-update"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.code),
            force_bytes("update"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[0].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.description),
            force_bytes("Confirm that the returned format is XML."),
        )
        self.assertFalse(inst.test[0].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.description),
            force_bytes(
                "Confirm that the returned HTTP Header Last-Modified is present. Warning only as the server might not support versioning."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.headerField),
            force_bytes("Last-Modified"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.operator),
            force_bytes("notEmpty"),
        )
        self.assertTrue(inst.test[0].action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].description),
            force_bytes("Update a Patient and validate response."),
        )
        self.assertEqual(force_bytes(inst.test[0].id), force_bytes("01-UpdatePatient"))
        self.assertEqual(force_bytes(inst.test[0].name), force_bytes("Update Patient"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/TestScript/testscript-example-update"),
        )
        self.assertEqual(
            force_bytes(inst.variable[0].name), force_bytes("createResourceId")
        )
        self.assertEqual(force_bytes(inst.variable[0].path), force_bytes("Patient/id"))
        self.assertEqual(
            force_bytes(inst.variable[0].sourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0"))

    def testTestScript4(self):
        inst = self.instantiate_from("testscript-example-search.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript4(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript4(inst2)

    def implTestScript4(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("Support"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("support@HL7.org"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-01-18").date)
        self.assertEqual(inst.date.as_json(), "2017-01-18")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "TestScript example resource with simple Patient search test. The read tests will utilize user defined dynamic variables that will hold the Patient search parameter values."
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertFalse(inst.fixture[0].autocreate)
        self.assertFalse(inst.fixture[0].autodelete)
        self.assertEqual(
            force_bytes(inst.fixture[0].id), force_bytes("fixture-patient-create")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("testscript-example-search"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9881"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America (the)"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].capabilities),
            force_bytes("CapabilityStatement/example"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].description),
            force_bytes("Patient Search Operation"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[0]),
            force_bytes("http://hl7.org/fhir/http.html#search"),
        )
        self.assertTrue(inst.metadata.capability[0].required)
        self.assertFalse(inst.metadata.capability[0].validated)
        self.assertEqual(
            force_bytes(inst.metadata.link[0].description),
            force_bytes(
                "Demographics and other administrative information about an individual or animal receiving care or other health-related services."
            ),
        )
        self.assertEqual(
            force_bytes(inst.metadata.link[0].url),
            force_bytes("http://hl7.org/fhir/patient.html"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("TestScript Example Search")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7"))
        self.assertEqual(
            force_bytes(inst.purpose), force_bytes("Patient Search Operation")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.description),
            force_bytes("Test simple search to verify server support."),
        )
        self.assertTrue(inst.setup.action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.params),
            force_bytes("?family=DONTEXPECTAMATCH&given=DONTEXPECTAMATCH"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.code), force_bytes("search")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.description),
            force_bytes(
                "Confirm that the request url contains the family search parameter."
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.direction),
            force_bytes("request"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.operator),
            force_bytes("contains"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.requestURL),
            force_bytes("family"),
        )
        self.assertFalse(inst.setup.action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[2].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].assert_fhir.responseCode),
            force_bytes("200"),
        )
        self.assertFalse(inst.setup.action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Bundle."),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.resource),
            force_bytes("Bundle"),
        )
        self.assertFalse(inst.setup.action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[4].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Bundle correctly defines the navigation links."
            ),
        )
        self.assertTrue(inst.setup.action[4].assert_fhir.navigationLinks)
        self.assertFalse(inst.setup.action[4].assert_fhir.warningOnly)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.description),
            force_bytes(
                "Create a Patient resource and capture the returned HTTP Header Location."
            ),
        )
        self.assertTrue(inst.test[0].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.responseId),
            force_bytes("PatientCreateResponse"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.sourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.code),
            force_bytes("create"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 201(Created)."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.response),
            force_bytes("created"),
        )
        self.assertFalse(inst.test[0].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP Header Location is present."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.headerField),
            force_bytes("Location"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.operator),
            force_bytes("notEmpty"),
        )
        self.assertFalse(inst.test[0].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[3].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].operation.description),
            force_bytes(
                "Read the created Patient using the captured Location URL value."
            ),
        )
        self.assertTrue(inst.test[0].action[3].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[0].action[3].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].operation.url),
            force_bytes("${PatientCreateLocation}"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[0].action[4].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Patient."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.resource),
            force_bytes("Patient"),
        )
        self.assertFalse(inst.test[0].action[5].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].description),
            force_bytes(
                "Create a Patient resource and capture the returned HTTP Header Location. Then search for (read) that Patient using the Location URL value and validate the response."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].id), force_bytes("01-PatientCreateSearch")
        )
        self.assertEqual(
            force_bytes(inst.test[0].name), force_bytes("Patient Create Search")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.description),
            force_bytes("Search for Patient resources on the destination test system."),
        )
        self.assertTrue(inst.test[1].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.params),
            force_bytes(
                "?family=${PatientSearchFamilyName}&given=${PatientSearchGivenName}"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.type.code),
            force_bytes("search"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[1].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[2].assert_fhir.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[2].assert_fhir.description),
            force_bytes("Confirm that the returned format is XML."),
        )
        self.assertFalse(inst.test[1].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[3].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Bundle."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[3].assert_fhir.resource),
            force_bytes("Bundle"),
        )
        self.assertFalse(inst.test[1].action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[4].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Bundle conforms to the base FHIR specification."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[4].assert_fhir.validateProfileId),
            force_bytes("bundle-profile"),
        )
        self.assertFalse(inst.test[1].action[4].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[5].assert_fhir.description),
            force_bytes("Confirm that the returned Bundle type equals 'searchset'."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[5].assert_fhir.operator),
            force_bytes("equals"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[5].assert_fhir.path),
            force_bytes("fhir:Bundle/fhir:type/@value"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[5].assert_fhir.value),
            force_bytes("searchset"),
        )
        self.assertFalse(inst.test[1].action[5].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].action[6].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Bundle total is greater than or equal to the number of returned entries."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[6].assert_fhir.expression),
            force_bytes("Bundle.total.toInteger() >= entry.count()"),
        )
        self.assertFalse(inst.test[1].action[6].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].description),
            force_bytes(
                "Search for Patient resources using the user defined dynamic variables ${PatientSearchFamilyName} and ${PatientSearchGivenName} and validate response."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].id), force_bytes("02-PatientSearchDynamic")
        )
        self.assertEqual(
            force_bytes(inst.test[1].name), force_bytes("Patient Search Dynamic")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/TestScript/testscript-example-search"),
        )
        self.assertEqual(
            force_bytes(inst.variable[0].headerField), force_bytes("Location")
        )
        self.assertEqual(
            force_bytes(inst.variable[0].name), force_bytes("PatientCreateLocation")
        )
        self.assertEqual(
            force_bytes(inst.variable[0].sourceId), force_bytes("PatientCreateResponse")
        )
        self.assertEqual(
            force_bytes(inst.variable[1].description),
            force_bytes(
                "Enter patient search criteria for a known family name on the target system"
            ),
        )
        self.assertEqual(
            force_bytes(inst.variable[1].hint), force_bytes("[Family name]")
        )
        self.assertEqual(
            force_bytes(inst.variable[1].name), force_bytes("PatientSearchFamilyName")
        )
        self.assertEqual(
            force_bytes(inst.variable[2].description),
            force_bytes(
                "Enter patient search criteria for a known given name on the target system"
            ),
        )
        self.assertEqual(
            force_bytes(inst.variable[2].hint), force_bytes("[Given name]")
        )
        self.assertEqual(
            force_bytes(inst.variable[2].name), force_bytes("PatientSearchGivenName")
        )
        self.assertEqual(
            force_bytes(inst.variable[3].description),
            force_bytes("Evaluate the returned Patient searchset Bundle.total value"),
        )
        self.assertEqual(
            force_bytes(inst.variable[3].expression),
            force_bytes("Bundle.total.toInteger()"),
        )
        self.assertEqual(
            force_bytes(inst.variable[3].name), force_bytes("PatientSearchBundleTotal")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0"))

    def testTestScript5(self):
        inst = self.instantiate_from("testscript-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript5(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript5(inst2)

    def implTestScript5(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("Support"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("support@HL7.org"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-01-18").date)
        self.assertEqual(inst.date.as_json(), "2017-01-18")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "TestScript example resource with setup to delete if present and create a new instance of a Patient; and single test definition to read the created Patient with various asserts."
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertFalse(inst.fixture[0].autocreate)
        self.assertFalse(inst.fixture[0].autodelete)
        self.assertEqual(
            force_bytes(inst.fixture[0].id), force_bytes("fixture-patient-create")
        )
        self.assertFalse(inst.fixture[1].autocreate)
        self.assertFalse(inst.fixture[1].autodelete)
        self.assertEqual(
            force_bytes(inst.fixture[1].id), force_bytes("fixture-patient-minimum")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("testscript-example"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9876"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America (the)"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].capabilities),
            force_bytes("CapabilityStatement/example"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].description),
            force_bytes("Patient Update, Read and Delete Operations"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[0]),
            force_bytes("http://hl7.org/fhir/http.html#delete"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[1]),
            force_bytes("http://hl7.org/fhir/http.html#read"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[2]),
            force_bytes("http://hl7.org/fhir/http.html#update"),
        )
        self.assertTrue(inst.metadata.capability[0].required)
        self.assertFalse(inst.metadata.capability[0].validated)
        self.assertEqual(
            force_bytes(inst.metadata.link[0].description),
            force_bytes(
                "Demographics and other administrative information about an individual or animal receiving care or other health-related services."
            ),
        )
        self.assertEqual(
            force_bytes(inst.metadata.link[0].url),
            force_bytes("http://hl7.org/fhir/patient.html"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("TestScript Example"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7"))
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "Patient Conditional Create (Update), Read and Delete Operations"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.accept), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.description),
            force_bytes(
                "Execute a delete operation to insure the patient does not exist on the server."
            ),
        )
        self.assertTrue(inst.setup.action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.label),
            force_bytes("SetupDeletePatient"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.code), force_bytes("delete")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.description),
            force_bytes(
                "Confirm that the returned HTTP status is 200(OK) or 204(No Content)."
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.operator), force_bytes("in")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[1].assert_fhir.responseCode),
            force_bytes("200,204"),
        )
        self.assertFalse(inst.setup.action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.accept), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.contentType), force_bytes("json")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.description),
            force_bytes(
                "Create patient resource on test server using the contents of fixture-patient-create"
            ),
        )
        self.assertTrue(inst.setup.action[2].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.label),
            force_bytes("SetupCreatePatient"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.params),
            force_bytes("/${createResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.sourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.type.code), force_bytes("update")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[2].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 201(Created)."),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[3].assert_fhir.responseCode),
            force_bytes("201"),
        )
        self.assertFalse(inst.setup.action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.description),
            force_bytes(
                "Read the created patient resource on the test server using the id from fixture-patient-create. Verify contents."
            ),
        )
        self.assertTrue(inst.setup.action[4].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.resource), force_bytes("Patient")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.targetId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.setup.action[4].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[5].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[5].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[5].assert_fhir.response), force_bytes("okay")
        )
        self.assertFalse(inst.setup.action[5].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.setup.action[6].assert_fhir.compareToSourceExpression),
            force_bytes("Patient.name.first().family"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[6].assert_fhir.compareToSourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[6].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Patient contains the expected family name 'Chalmers'. Uses explicit compareToSourceId reference to fixture-patient-create used to create the Patient."
            ),
        )
        self.assertEqual(
            force_bytes(inst.setup.action[6].assert_fhir.operator),
            force_bytes("equals"),
        )
        self.assertFalse(inst.setup.action[6].assert_fhir.warningOnly)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.teardown.action[0].operation.description),
            force_bytes(
                "Delete the patient resource on the test server using the id from fixture-patient-create."
            ),
        )
        self.assertTrue(inst.teardown.action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.teardown.action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.teardown.action[0].operation.targetId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.teardown.action[0].operation.type.code),
            force_bytes("delete"),
        )
        self.assertEqual(
            force_bytes(inst.teardown.action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.description),
            force_bytes(
                "Read the patient resource on the test server using the id from fixture-patient-create. Prevent URL encoding of the request."
            ),
        )
        self.assertFalse(inst.test[0].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.responseId),
            force_bytes("fixture-patient-read"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.targetId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.label),
            force_bytes("01-ReadPatientOK"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[0].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.description),
            force_bytes(
                "Confirm that the returned HTTP Header Last-Modified is present. Warning only as the server might not support versioning."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.direction),
            force_bytes("response"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.headerField),
            force_bytes("Last-Modified"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.operator),
            force_bytes("notEmpty"),
        )
        self.assertTrue(inst.test[0].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Patient."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.resource),
            force_bytes("Patient"),
        )
        self.assertFalse(inst.test[0].action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Patient conforms to the base FHIR specification."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.validateProfileId),
            force_bytes("patient-profile"),
        )
        self.assertFalse(inst.test[0].action[4].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Patient contains the expected family name 'Chalmers'. Uses explicit sourceId reference to read responseId fixture."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.operator),
            force_bytes("equals"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.path),
            force_bytes("fhir:Patient/fhir:name/fhir:family/@value"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.sourceId),
            force_bytes("fixture-patient-read"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.value),
            force_bytes("Chalmers"),
        )
        self.assertFalse(inst.test[0].action[5].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[6].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Patient contains the expected given name 'Peter'. Uses explicit sourceId reference to read responseId fixture."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[6].assert_fhir.operator),
            force_bytes("equals"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[6].assert_fhir.path),
            force_bytes("fhir:Patient/fhir:name/fhir:given/@value"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[6].assert_fhir.sourceId),
            force_bytes("fixture-patient-read"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[6].assert_fhir.value), force_bytes("Peter")
        )
        self.assertFalse(inst.test[0].action[6].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[7].assert_fhir.compareToSourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[7].assert_fhir.compareToSourcePath),
            force_bytes("fhir:Patient/fhir:name/fhir:family/@value"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[7].assert_fhir.operator),
            force_bytes("equals"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[7].assert_fhir.path),
            force_bytes("fhir:Patient/fhir:name/fhir:family/@value"),
        )
        self.assertFalse(inst.test[0].action[7].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[8].assert_fhir.compareToSourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[8].assert_fhir.compareToSourcePath),
            force_bytes("fhir:Patient/fhir:name/fhir:given/@value"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[8].assert_fhir.path),
            force_bytes("fhir:Patient/fhir:name/fhir:given/@value"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[8].assert_fhir.sourceId),
            force_bytes("fixture-patient-read"),
        )
        self.assertFalse(inst.test[0].action[8].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[9].assert_fhir.description),
            force_bytes(
                "Confirm that the returned resource contains the expected retained elements and values. Warning only to provide users with reviewable results."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[9].assert_fhir.minimumId),
            force_bytes("fixture-patient-minimum"),
        )
        self.assertTrue(inst.test[0].action[9].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].description),
            force_bytes("Read a Patient and validate response."),
        )
        self.assertEqual(force_bytes(inst.test[0].id), force_bytes("01-ReadPatient"))
        self.assertEqual(force_bytes(inst.test[0].name), force_bytes("Read Patient"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/TestScript/testscript-example"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("positive"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/variant-state"),
        )
        self.assertEqual(
            force_bytes(inst.variable[0].name), force_bytes("createResourceId")
        )
        self.assertEqual(force_bytes(inst.variable[0].path), force_bytes("Patient/id"))
        self.assertEqual(
            force_bytes(inst.variable[0].sourceId),
            force_bytes("fixture-patient-create"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0"))

    def testTestScript6(self):
        inst = self.instantiate_from("testscript-example-readtest.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestScript instance")
        self.implTestScript6(inst)

        js = inst.as_json()
        self.assertEqual("TestScript", js["resourceType"])
        inst2 = testscript.TestScript(js)
        self.implTestScript6(inst2)

    def implTestScript6(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("Support"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("support@HL7.org"),
        )
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© HL7.org 2011+"))
        self.assertEqual(inst.date.date, FHIRDate("2017-01-18").date)
        self.assertEqual(inst.date.as_json(), "2017-01-18")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "TestScript example resource with ported Sprinkler basic read tests R001, R002, R003, R004. The read tests will utilize user defined dynamic variables that will hold the Patient resource id values."
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("testscript-example-readtest")
        )
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.9879"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display),
            force_bytes("United States of America (the)"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].capabilities),
            force_bytes("CapabilityStatement/example"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].description),
            force_bytes("Patient Read Operation"),
        )
        self.assertEqual(
            force_bytes(inst.metadata.capability[0].link[0]),
            force_bytes("http://hl7.org/fhir/http.html#read"),
        )
        self.assertTrue(inst.metadata.capability[0].required)
        self.assertFalse(inst.metadata.capability[0].validated)
        self.assertEqual(
            force_bytes(inst.metadata.link[0].description),
            force_bytes(
                "Demographics and other administrative information about an individual or animal receiving care or other health-related services."
            ),
        )
        self.assertEqual(
            force_bytes(inst.metadata.link[0].url),
            force_bytes("http://hl7.org/fhir/patient.html"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("TestScript Example Read Test")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7"))
        self.assertEqual(
            force_bytes(inst.purpose), force_bytes("Patient Read Operation")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.description),
            force_bytes(
                "Read the known Patient resource on the destination test system using the user defined dynamic variable ${KnownPatientResourceId}."
            ),
        )
        self.assertTrue(inst.test[0].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.params),
            force_bytes("/${KnownPatientResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 200(OK)."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[1].assert_fhir.response),
            force_bytes("okay"),
        )
        self.assertFalse(inst.test[0].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.contentType),
            force_bytes("xml"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[2].assert_fhir.description),
            force_bytes("Confirm that the returned format is XML."),
        )
        self.assertFalse(inst.test[0].action[2].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.description),
            force_bytes(
                "Confirm that the returned HTTP Header Last-Modified is present. Warning only as the server might not support versioning."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.headerField),
            force_bytes("Last-Modified"),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[3].assert_fhir.operator),
            force_bytes("notEmpty"),
        )
        self.assertTrue(inst.test[0].action[3].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.description),
            force_bytes("Confirm that the returned resource type is Patient."),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[4].assert_fhir.resource),
            force_bytes("Patient"),
        )
        self.assertFalse(inst.test[0].action[4].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.description),
            force_bytes(
                "Confirm that the returned Patient conforms to the base FHIR specification."
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[0].action[5].assert_fhir.validateProfileId),
            force_bytes("patient-profile"),
        )
        self.assertFalse(inst.test[0].action[5].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[0].description),
            force_bytes("Read a known Patient and validate response."),
        )
        self.assertEqual(force_bytes(inst.test[0].id), force_bytes("R001"))
        self.assertEqual(
            force_bytes(inst.test[0].name), force_bytes("Sprinkler Read Test R001")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.accept), force_bytes("xml")
        )
        self.assertTrue(inst.test[1].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.params), force_bytes("/1")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 404(Not Found)."),
        )
        self.assertEqual(
            force_bytes(inst.test[1].action[1].assert_fhir.response),
            force_bytes("notFound"),
        )
        self.assertFalse(inst.test[1].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[1].description),
            force_bytes("Read an unknown Resource Type and validate response."),
        )
        self.assertEqual(force_bytes(inst.test[1].id), force_bytes("R002"))
        self.assertEqual(
            force_bytes(inst.test[1].name), force_bytes("Sprinkler Read Test R002")
        )
        self.assertEqual(
            force_bytes(inst.test[2].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[2].action[0].operation.description),
            force_bytes(
                "Attempt to read the non-existing Patient resource on the destination test system using the user defined dynamic variable ${NonExistsPatientResourceId}."
            ),
        )
        self.assertTrue(inst.test[2].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[2].action[0].operation.params),
            force_bytes("/${NonExistsPatientResourceId}"),
        )
        self.assertEqual(
            force_bytes(inst.test[2].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[2].action[0].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[2].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[2].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 404(Not Found)."),
        )
        self.assertEqual(
            force_bytes(inst.test[2].action[1].assert_fhir.response),
            force_bytes("notFound"),
        )
        self.assertFalse(inst.test[2].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[2].description),
            force_bytes("Read a known, non-existing Patient and validate response."),
        )
        self.assertEqual(force_bytes(inst.test[2].id), force_bytes("R003"))
        self.assertEqual(
            force_bytes(inst.test[2].name), force_bytes("Sprinkler Read Test R003")
        )
        self.assertEqual(
            force_bytes(inst.test[3].action[0].operation.accept), force_bytes("xml")
        )
        self.assertEqual(
            force_bytes(inst.test[3].action[0].operation.description),
            force_bytes(
                "Attempt to read a Patient resource on the destination test system using known bad formatted resource id."
            ),
        )
        self.assertTrue(inst.test[3].action[0].operation.encodeRequestUrl)
        self.assertEqual(
            force_bytes(inst.test[3].action[0].operation.params),
            force_bytes("/ID-may-not-contain-CAPITALS"),
        )
        self.assertEqual(
            force_bytes(inst.test[3].action[0].operation.resource),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.test[3].action[0].operation.type.code), force_bytes("read")
        )
        self.assertEqual(
            force_bytes(inst.test[3].action[0].operation.type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/testscript-operation-codes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.test[3].action[1].assert_fhir.description),
            force_bytes("Confirm that the returned HTTP status is 400(Bad Request)."),
        )
        self.assertEqual(
            force_bytes(inst.test[3].action[1].assert_fhir.response), force_bytes("bad")
        )
        self.assertFalse(inst.test[3].action[1].assert_fhir.warningOnly)
        self.assertEqual(
            force_bytes(inst.test[3].description),
            force_bytes(
                "Read a Patient using a known bad formatted resource id and validate response."
            ),
        )
        self.assertEqual(force_bytes(inst.test[3].id), force_bytes("R004"))
        self.assertEqual(
            force_bytes(inst.test[3].name), force_bytes("Sprinkler Read Test R004")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/TestScript/testscript-example-readtest"),
        )
        self.assertEqual(
            force_bytes(inst.variable[0].defaultValue), force_bytes("example")
        )
        self.assertEqual(
            force_bytes(inst.variable[0].name), force_bytes("KnownPatientResourceId")
        )
        self.assertEqual(
            force_bytes(inst.variable[1].defaultValue), force_bytes("does-not-exist")
        )
        self.assertEqual(
            force_bytes(inst.variable[1].name),
            force_bytes("NonExistsPatientResourceId"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0"))
