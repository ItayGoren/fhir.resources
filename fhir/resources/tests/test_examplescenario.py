# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario
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

from .. import examplescenario
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ExampleScenarioTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ExampleScenario", js["resourceType"])
        return examplescenario.ExampleScenario(js)

    def testExampleScenario1(self):
        inst = self.instantiate_from("examplescenario-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExampleScenario instance")
        self.implExampleScenario1(inst)

        js = inst.as_json()
        self.assertEqual("ExampleScenario", js["resourceType"])
        inst2 = examplescenario.ExampleScenario(js)
        self.implExampleScenario1(inst2)

    def implExampleScenario1(self, inst):
        self.assertEqual(force_bytes(inst.actor[0].actorId), force_bytes("Nurse"))
        self.assertEqual(
            force_bytes(inst.actor[0].description), force_bytes("The Nurse")
        )
        self.assertEqual(force_bytes(inst.actor[0].name), force_bytes("Nurse"))
        self.assertEqual(force_bytes(inst.actor[0].type), force_bytes("person"))
        self.assertEqual(force_bytes(inst.actor[1].actorId), force_bytes("MAP"))
        self.assertEqual(
            force_bytes(inst.actor[1].description),
            force_bytes(
                "The entity that receives the Administration Requests to show the nurse to perform them"
            ),
        )
        self.assertEqual(force_bytes(inst.actor[1].name), force_bytes("Nurse's Tablet"))
        self.assertEqual(force_bytes(inst.actor[1].type), force_bytes("entity"))
        self.assertEqual(force_bytes(inst.actor[2].actorId), force_bytes("OP"))
        self.assertEqual(
            force_bytes(inst.actor[2].description),
            force_bytes("The Medication Administration Order Placer"),
        )
        self.assertEqual(
            force_bytes(inst.actor[2].name), force_bytes("MAR / Scheduler")
        )
        self.assertEqual(force_bytes(inst.actor[2].type), force_bytes("entity"))
        self.assertEqual(force_bytes(inst.actor[3].actorId), force_bytes("MAC"))
        self.assertEqual(
            force_bytes(inst.actor[3].description),
            force_bytes(
                "The entity that receives the Medication Administration reports"
            ),
        )
        self.assertEqual(force_bytes(inst.actor[3].name), force_bytes("MAR / EHR"))
        self.assertEqual(force_bytes(inst.actor[3].type), force_bytes("entity"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.instance[0].description),
            force_bytes(
                'The initial prescription which describes "medication X, 3 times per day" - the exact scheduling is not   in the initial prescription (it is left for the care teams to decide on the schedule).'
            ),
        )
        self.assertEqual(
            force_bytes(inst.instance[0].name), force_bytes("Initial Prescription")
        )
        self.assertEqual(
            force_bytes(inst.instance[0].resourceId), force_bytes("iherx001")
        )
        self.assertEqual(
            force_bytes(inst.instance[1].description),
            force_bytes("The administration request for day 1, morning"),
        )
        self.assertEqual(
            force_bytes(inst.instance[1].name),
            force_bytes("Request for day 1, morning"),
        )
        self.assertEqual(
            force_bytes(inst.instance[1].resourceId), force_bytes("iherx001.001")
        )
        self.assertEqual(
            force_bytes(inst.instance[2].description),
            force_bytes("The administration request for day 1, lunch"),
        )
        self.assertEqual(
            force_bytes(inst.instance[2].name), force_bytes("Request for day 1, lunch")
        )
        self.assertEqual(
            force_bytes(inst.instance[2].resourceId), force_bytes("iherx001.002")
        )
        self.assertEqual(
            force_bytes(inst.instance[3].description),
            force_bytes("The administration request for day 1, evening"),
        )
        self.assertEqual(
            force_bytes(inst.instance[3].name),
            force_bytes("Request for day 1, evening"),
        )
        self.assertEqual(
            force_bytes(inst.instance[3].resourceId), force_bytes("iherx001.003")
        )
        self.assertEqual(
            force_bytes(inst.instance[4].description),
            force_bytes("The administration request for day 2, morning"),
        )
        self.assertEqual(
            force_bytes(inst.instance[4].name),
            force_bytes("Request for day 2, morning"),
        )
        self.assertEqual(
            force_bytes(inst.instance[4].resourceId), force_bytes("iherx001.004")
        )
        self.assertEqual(
            force_bytes(inst.instance[5].description),
            force_bytes("The administration request for day 2, lunch"),
        )
        self.assertEqual(
            force_bytes(inst.instance[5].name), force_bytes("Request for day 2, lunch")
        )
        self.assertEqual(
            force_bytes(inst.instance[5].resourceId), force_bytes("iherx001.005")
        )
        self.assertEqual(
            force_bytes(inst.instance[6].description),
            force_bytes("The administration request for day 2, evening"),
        )
        self.assertEqual(
            force_bytes(inst.instance[6].name),
            force_bytes("Request for day 2, evening"),
        )
        self.assertEqual(
            force_bytes(inst.instance[6].resourceId), force_bytes("iherx001.006")
        )
        self.assertEqual(
            force_bytes(inst.instance[7].description),
            force_bytes("Administration report for day 1, morning: Taken"),
        )
        self.assertEqual(
            force_bytes(inst.instance[7].name), force_bytes("Morning meds - taken")
        )
        self.assertEqual(
            force_bytes(inst.instance[7].resourceId), force_bytes("iheadm001a")
        )
        self.assertEqual(
            force_bytes(inst.instance[8].description),
            force_bytes("Administration report for day 1, morning: NOT Taken"),
        )
        self.assertEqual(
            force_bytes(inst.instance[8].name), force_bytes("Morning meds - not taken")
        )
        self.assertEqual(
            force_bytes(inst.instance[8].resourceId), force_bytes("iheadm001b")
        )
        self.assertEqual(
            force_bytes(inst.instance[9].containedInstance[0].resourceId),
            force_bytes("iherx001.001"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].containedInstance[1].resourceId),
            force_bytes("iherx001.002"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].containedInstance[2].resourceId),
            force_bytes("iherx001.003"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].containedInstance[3].resourceId),
            force_bytes("iherx001.004"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].containedInstance[4].resourceId),
            force_bytes("iherx001.005"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].containedInstance[5].resourceId),
            force_bytes("iherx001.006"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].description),
            force_bytes("All the medication Requests for Day 1"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].name),
            force_bytes("Bundle of Medication Requests"),
        )
        self.assertEqual(
            force_bytes(inst.instance[9].resourceId), force_bytes("iherx001bundle")
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
            force_bytes(inst.process[0].postConditions),
            force_bytes(
                "Medication administration Reports are submitted, EHR is updated."
            ),
        )
        self.assertEqual(
            force_bytes(inst.process[0].preConditions),
            force_bytes(
                "Medication administration requests are in the EHR / MAR, scheduled for each individual intake."
            ),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[0].operation.initiator),
            force_bytes("Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[0].operation.name),
            force_bytes("1. Get today's schedule"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[0].operation.number), force_bytes("1")
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[0].operation.receiver), force_bytes("MAP")
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[1].process[0].description),
            force_bytes(
                "Query for medication administration orders,\\n- For today's shifts\\n- For today's patients"
            ),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[1].process[0].step[0].operation.initiator),
            force_bytes("MAP"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[1].process[0].step[0].operation.name),
            force_bytes(
                "2.Query for medication administration orders,\\n- For today's shifts\\n- For today's patients"
            ),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[1].process[0].step[0].operation.number),
            force_bytes("2"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[1].process[0].step[0].operation.receiver),
            force_bytes("OP"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0].step[1].process[0].step[0].operation.request.resourceId
            ),
            force_bytes("iherxqry"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0].step[1].process[0].step[0].operation.response.resourceId
            ),
            force_bytes("iherx001bundle"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[1].process[0].title),
            force_bytes("P1. Query Administration Requests"),
        )
        self.assertTrue(inst.process[0].step[2].pause)
        self.assertEqual(
            force_bytes(inst.process[0].step[3].operation.initiator), force_bytes("MAP")
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[3].operation.name),
            force_bytes("Notify (alert)"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[3].operation.number), force_bytes("4")
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[3].operation.receiver),
            force_bytes("Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[4].operation.initiator),
            force_bytes("Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[4].operation.name),
            force_bytes("Read orders"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[4].operation.number), force_bytes("5")
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[4].operation.receiver), force_bytes("MAP")
        )
        self.assertTrue(inst.process[0].step[5].pause)
        self.assertEqual(
            force_bytes(inst.process[0].step[6].operation.initiator),
            force_bytes("Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[6].operation.name),
            force_bytes("Ask if patient took meds"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[6].operation.number), force_bytes("5")
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[6].operation.receiver),
            force_bytes("Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[7].alternative[0].description),
            force_bytes("Invoke if patient took medications"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[0]
                .step[0]
                .process[0]
                .step[0]
                .operation.initiator
            ),
            force_bytes("Nurse"),
        )
        self.assertTrue(
            inst.process[0]
            .step[7]
            .alternative[0]
            .step[0]
            .process[0]
            .step[0]
            .operation.initiatorActive
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[0]
                .step[0]
                .process[0]
                .step[0]
                .operation.name
            ),
            force_bytes("Register Meds taken"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[0]
                .step[0]
                .process[0]
                .step[0]
                .operation.number
            ),
            force_bytes("1a"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[0]
                .step[0]
                .process[0]
                .step[0]
                .operation.receiver
            ),
            force_bytes("MAP"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0].step[7].alternative[0].step[0].process[0].title
            ),
            force_bytes("Register Meds taken"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[7].alternative[0].title),
            force_bytes("Patient took drugs"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[7].alternative[1].description),
            force_bytes("No, patient did not take drugs"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[1]
                .step[0]
                .process[0]
                .step[0]
                .operation.initiator
            ),
            force_bytes("Nurse"),
        )
        self.assertTrue(
            inst.process[0]
            .step[7]
            .alternative[1]
            .step[0]
            .process[0]
            .step[0]
            .operation.initiatorActive
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[1]
                .step[0]
                .process[0]
                .step[0]
                .operation.name
            ),
            force_bytes("Register Meds NOT taken"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[1]
                .step[0]
                .process[0]
                .step[0]
                .operation.number
            ),
            force_bytes("1b"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0]
                .step[7]
                .alternative[1]
                .step[0]
                .process[0]
                .step[0]
                .operation.receiver
            ),
            force_bytes("MAP"),
        )
        self.assertEqual(
            force_bytes(
                inst.process[0].step[7].alternative[1].step[0].process[0].title
            ),
            force_bytes("Register Meds NOT taken"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[7].alternative[1].title),
            force_bytes("No drugs"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[7].alternative[2].description),
            force_bytes("Unknown whether patient took medications or not"),
        )
        self.assertTrue(inst.process[0].step[7].alternative[2].step[0].pause)
        self.assertEqual(
            force_bytes(inst.process[0].step[7].alternative[2].title),
            force_bytes("Not clear"),
        )
        self.assertTrue(inst.process[0].step[8].pause)
        self.assertEqual(
            force_bytes(inst.process[0].step[9].operation.initiator),
            force_bytes("Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[9].operation.name),
            force_bytes("Administer drug"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[9].operation.number), force_bytes("6")
        )
        self.assertEqual(
            force_bytes(inst.process[0].step[9].operation.receiver),
            force_bytes("Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.process[0].title),
            force_bytes("Mobile Medication Administration"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
