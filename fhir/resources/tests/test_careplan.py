# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CarePlan
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

from .. import careplan
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CarePlanTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("CarePlan", js["resourceType"])
        return careplan.CarePlan(js)

    def testCarePlan1(self):
        inst = self.instantiate_from("careplan-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan1(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan1(inst2)

    def implCarePlan1(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].code),
            force_bytes("359615001"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].display),
            force_bytes("Partial lobectomy of lung"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertTrue(inst.activity[0].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.kind), force_bytes("ServiceRequest")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.scheduledString),
            force_bytes("2011-07-07T09:30:10+01:00"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("completed")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("careteam"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("goal"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/zorgportal/identifiers/careplans"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("CP2934"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.period.end.date, FHIRDate("2013-07-07").date)
        self.assertEqual(inst.period.end.as_json(), "2013-07-07")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-07-06").date)
        self.assertEqual(inst.period.start.as_json(), "2011-07-06")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCarePlan2(self):
        inst = self.instantiate_from("careplan-example-f202-malignancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan2(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan2(inst2)

    def implCarePlan2(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].code),
            force_bytes("367336001"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].display),
            force_bytes("Chemotherapy"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.kind), force_bytes("ServiceRequest")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("in-progress")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("doce"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("cisp"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("fluo"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("tpf"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("careteam"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("goal"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f202"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCarePlan3(self):
        inst = self.instantiate_from("careplan-example-obesity-narrative.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan3(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan3(inst2)

    def implCarePlan3(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("obesity-narrative"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))

    def testCarePlan4(self):
        inst = self.instantiate_from("careplan-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan4(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan4(inst2)

    def implCarePlan4(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].code),
            force_bytes("3141-9"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].display),
            force_bytes("Weight Measured"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[1].code),
            force_bytes("27113001"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[1].display),
            force_bytes("Body weight"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[1].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.frequency, 1)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.scheduledTiming.repeat.periodUnit),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("completed")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.statusReason.text),
            force_bytes("Achieved weight loss to mitigate diabetes risk."),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].outcomeCodeableConcept[0].coding[0].code),
            force_bytes("161832001"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].outcomeCodeableConcept[0].coding[0].display),
            force_bytes("Progressive weight loss"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].outcomeCodeableConcept[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].text), force_bytes("Weight management plan")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("p1"))
        self.assertEqual(inst.created.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.created.as_json(), "2016-01-01")
        self.assertEqual(
            force_bytes(inst.description), force_bytes("Manage obesity and weight loss")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(
            force_bytes(inst.instantiatesUri[0]),
            force_bytes("http://example.org/protocol-for-obesity"),
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.period.end.date, FHIRDate("2017-06-01").date)
        self.assertEqual(inst.period.end.as_json(), "2017-06-01")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))

    def testCarePlan5(self):
        inst = self.instantiate_from("careplan-example-f201-renal.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan5(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan5(inst2)

    def implCarePlan5(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].code),
            force_bytes("284093001"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].display),
            force_bytes("Potassium supplementation"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.dailyAmount.code),
            force_bytes("258718000"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.dailyAmount.system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.dailyAmount.unit), force_bytes("mmol")
        )
        self.assertEqual(inst.activity[0].detail.dailyAmount.value, 80)
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.kind), force_bytes("NutritionOrder")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.scheduledString), force_bytes("daily")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("completed")
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.coding[0].code),
            force_bytes("306005"),
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.coding[0].display),
            force_bytes("Echography of kidney"),
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[1].detail.kind), force_bytes("ServiceRequest")
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.status), force_bytes("completed")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("careteam"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("goal"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("proposal"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-13").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-13")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-11")
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCarePlan6(self):
        inst = self.instantiate_from("careplan-example-GPVisit.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan6(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan6(inst2)

    def implCarePlan6(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].code),
            force_bytes("nursecon"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].system),
            force_bytes("http://example.org/local"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.text),
            force_bytes("Nurse Consultation"),
        )
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.kind), force_bytes("Appointment")
        )
        self.assertEqual(
            inst.activity[0].detail.scheduledPeriod.end.date,
            FHIRDate("2013-01-01T10:50:00+00:00").date,
        )
        self.assertEqual(
            inst.activity[0].detail.scheduledPeriod.end.as_json(),
            "2013-01-01T10:50:00+00:00",
        )
        self.assertEqual(
            inst.activity[0].detail.scheduledPeriod.start.date,
            FHIRDate("2013-01-01T10:38:00+00:00").date,
        )
        self.assertEqual(
            inst.activity[0].detail.scheduledPeriod.start.as_json(),
            "2013-01-01T10:38:00+00:00",
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("completed")
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.coding[0].code),
            force_bytes("doccon"),
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.coding[0].system),
            force_bytes("http://example.org/local"),
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.text),
            force_bytes("Doctor Consultation"),
        )
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[1].detail.kind), force_bytes("Appointment")
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.status), force_bytes("scheduled")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("p1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("careteam"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("goal"))
        self.assertEqual(force_bytes(inst.id), force_bytes("gpvisit"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            inst.period.start.date, FHIRDate("2013-01-01T10:30:00+00:00").date
        )
        self.assertEqual(inst.period.start.as_json(), "2013-01-01T10:30:00+00:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))

    def testCarePlan7(self):
        inst = self.instantiate_from("careplan-example-integrated.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan7(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan7(inst2)

    def implCarePlan7(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.description),
            force_bytes(
                "Eve will review photos of high and low density foods and share with her parents"
            ),
        )
        self.assertFalse(inst.activity[0].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[0].detail.extension[0].valueDate.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[0].detail.extension[0].valueDate.as_json(), "2012-09-10"
        )
        self.assertEqual(
            inst.activity[0].detail.scheduledPeriod.start.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[0].detail.scheduledPeriod.start.as_json(), "2012-09-10"
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("not-started")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].progress[0].text),
            force_bytes("Eve eats one meal a day with her parents"),
        )
        self.assertEqual(
            inst.activity[0].progress[0].time.date, FHIRDate("2012-09-10").date
        )
        self.assertEqual(inst.activity[0].progress[0].time.as_json(), "2012-09-10")
        self.assertEqual(
            force_bytes(inst.activity[1].detail.description),
            force_bytes(
                "Eve will ask her dad to asist her to put the head of her bed on blocks"
            ),
        )
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[1].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[1].detail.extension[0].valueDate.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[1].detail.extension[0].valueDate.as_json(), "2012-09-10"
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.kind),
            force_bytes("CommunicationRequest"),
        )
        self.assertEqual(
            inst.activity[1].detail.scheduledPeriod.start.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[1].detail.scheduledPeriod.start.as_json(), "2012-09-10"
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.status), force_bytes("not-started")
        )
        self.assertEqual(
            force_bytes(inst.activity[1].progress[0].text),
            force_bytes("Eve will sleep in her bed more often than the couch"),
        )
        self.assertEqual(
            inst.activity[1].progress[0].time.date, FHIRDate("2012-09-10").date
        )
        self.assertEqual(inst.activity[1].progress[0].time.as_json(), "2012-09-10")
        self.assertEqual(
            force_bytes(inst.activity[2].detail.description),
            force_bytes("Eve will reduce her intake of coffee and chocolate"),
        )
        self.assertFalse(inst.activity[2].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[2].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[2].detail.extension[0].valueDate.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[2].detail.extension[0].valueDate.as_json(), "2012-09-10"
        )
        self.assertEqual(
            inst.activity[2].detail.scheduledPeriod.start.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[2].detail.scheduledPeriod.start.as_json(), "2012-09-10"
        )
        self.assertEqual(
            force_bytes(inst.activity[2].detail.status), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.activity[3].detail.description),
            force_bytes(
                "Eve will walk her friend's dog up and down a big hill 15-30 minutes 3 days a week"
            ),
        )
        self.assertFalse(inst.activity[3].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[3].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[3].detail.extension[0].valueDate.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[3].detail.extension[0].valueDate.as_json(), "2012-09-10"
        )
        self.assertEqual(
            inst.activity[3].detail.scheduledPeriod.start.date,
            FHIRDate("2012-08-27").date,
        )
        self.assertEqual(
            inst.activity[3].detail.scheduledPeriod.start.as_json(), "2012-08-27"
        )
        self.assertEqual(
            force_bytes(inst.activity[3].detail.status), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.activity[3].progress[0].text),
            force_bytes("Eve would like to try for 5 days a week."),
        )
        self.assertEqual(
            inst.activity[3].progress[0].time.date, FHIRDate("2012-08-27").date
        )
        self.assertEqual(inst.activity[3].progress[0].time.as_json(), "2012-08-27")
        self.assertEqual(
            force_bytes(inst.activity[3].progress[1].text),
            force_bytes("Eve is still walking the dogs."),
        )
        self.assertEqual(
            inst.activity[3].progress[1].time.date, FHIRDate("2012-09-10").date
        )
        self.assertEqual(inst.activity[3].progress[1].time.as_json(), "2012-09-10")
        self.assertEqual(
            force_bytes(inst.activity[4].detail.description),
            force_bytes("Eve will walk 3 blocks to her parents house twice a week"),
        )
        self.assertFalse(inst.activity[4].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[4].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[4].detail.extension[0].valueDate.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[4].detail.extension[0].valueDate.as_json(), "2012-09-10"
        )
        self.assertEqual(
            inst.activity[4].detail.scheduledPeriod.start.date,
            FHIRDate("2012-07-23").date,
        )
        self.assertEqual(
            inst.activity[4].detail.scheduledPeriod.start.as_json(), "2012-07-23"
        )
        self.assertEqual(
            force_bytes(inst.activity[4].detail.status), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.activity[4].progress[0].text),
            force_bytes("Eve walked 4 times the last week."),
        )
        self.assertEqual(
            inst.activity[4].progress[0].time.date, FHIRDate("2012-08-13").date
        )
        self.assertEqual(inst.activity[4].progress[0].time.as_json(), "2012-08-13")
        self.assertEqual(
            force_bytes(inst.activity[4].progress[1].text),
            force_bytes(
                "Eve did not walk to her parents the last week, but has plans to start again"
            ),
        )
        self.assertEqual(
            inst.activity[4].progress[1].time.date, FHIRDate("2012-09-10").date
        )
        self.assertEqual(inst.activity[4].progress[1].time.as_json(), "2012-09-10")
        self.assertEqual(
            force_bytes(inst.activity[5].detail.description),
            force_bytes(
                "Eve will use a calendar to check off after medications are taken"
            ),
        )
        self.assertFalse(inst.activity[5].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[5].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[5].detail.extension[0].valueDate.date,
            FHIRDate("2012-08-13").date,
        )
        self.assertEqual(
            inst.activity[5].detail.extension[0].valueDate.as_json(), "2012-08-13"
        )
        self.assertEqual(
            inst.activity[5].detail.scheduledPeriod.start.date,
            FHIRDate("2012-07-23").date,
        )
        self.assertEqual(
            inst.activity[5].detail.scheduledPeriod.start.as_json(), "2012-07-23"
        )
        self.assertEqual(
            force_bytes(inst.activity[5].detail.status), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.activity[6].detail.description),
            force_bytes("Eve will use her lights MWF after her shower for 3 minutes"),
        )
        self.assertFalse(inst.activity[6].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[6].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[6].detail.extension[0].valueDate.date,
            FHIRDate("2012-08-27").date,
        )
        self.assertEqual(
            inst.activity[6].detail.extension[0].valueDate.as_json(), "2012-08-27"
        )
        self.assertEqual(
            inst.activity[6].detail.scheduledPeriod.start.date,
            FHIRDate("2012-07-23").date,
        )
        self.assertEqual(
            inst.activity[6].detail.scheduledPeriod.start.as_json(), "2012-07-23"
        )
        self.assertEqual(
            force_bytes(inst.activity[6].detail.status), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.activity[6].progress[0].text),
            force_bytes(
                "After restarting the vinegar soaks the psoriasis is improved and Eve plans to treat the remainder with light treatments.  She plans to start this week."
            ),
        )
        self.assertEqual(
            inst.activity[6].progress[0].time.date, FHIRDate("2012-08-13").date
        )
        self.assertEqual(inst.activity[6].progress[0].time.as_json(), "2012-08-13")
        self.assertEqual(
            force_bytes(inst.activity[6].progress[1].text),
            force_bytes(
                "Since her skin is improved Eve has not been using the light treatment as often, maybe once a week.  She would like to increase to 3 times a week again"
            ),
        )
        self.assertEqual(
            inst.activity[6].progress[1].time.date, FHIRDate("2012-08-27").date
        )
        self.assertEqual(inst.activity[6].progress[1].time.as_json(), "2012-08-27")
        self.assertEqual(
            force_bytes(inst.activity[7].detail.description),
            force_bytes(
                "Eve will use a calendar of a chart to help her remember when to take her medications"
            ),
        )
        self.assertFalse(inst.activity[7].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[7].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[7].detail.extension[0].valueDate.date,
            FHIRDate("2012-09-10").date,
        )
        self.assertEqual(
            inst.activity[7].detail.extension[0].valueDate.as_json(), "2012-09-10"
        )
        self.assertEqual(
            inst.activity[7].detail.scheduledPeriod.start.date,
            FHIRDate("2012-07-10").date,
        )
        self.assertEqual(
            inst.activity[7].detail.scheduledPeriod.start.as_json(), "2012-07-10"
        )
        self.assertEqual(
            force_bytes(inst.activity[7].detail.status), force_bytes("in-progress")
        )
        self.assertEqual(
            force_bytes(inst.activity[7].progress[0].text),
            force_bytes(
                "Eve created a chart as a reminer to take the medications that do not fit in her pill box"
            ),
        )
        self.assertEqual(
            inst.activity[7].progress[0].time.date, FHIRDate("2012-07-23").date
        )
        self.assertEqual(inst.activity[7].progress[0].time.as_json(), "2012-07-23")
        self.assertEqual(
            force_bytes(inst.activity[8].detail.description),
            force_bytes(
                "Eve will start using stretch bands and one step 2 days a week Mon/Wed 6-7am and maybe Friday afternoon"
            ),
        )
        self.assertFalse(inst.activity[8].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[8].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[8].detail.extension[0].valueDate.date,
            FHIRDate("2012-08-23").date,
        )
        self.assertEqual(
            inst.activity[8].detail.extension[0].valueDate.as_json(), "2012-08-23"
        )
        self.assertEqual(
            inst.activity[8].detail.scheduledPeriod.start.date,
            FHIRDate("2012-07-23").date,
        )
        self.assertEqual(
            inst.activity[8].detail.scheduledPeriod.start.as_json(), "2012-07-23"
        )
        self.assertEqual(
            force_bytes(inst.activity[8].detail.status), force_bytes("on-hold")
        )
        self.assertEqual(
            force_bytes(inst.activity[8].progress[0].text),
            force_bytes("Will be able to esume exercise."),
        )
        self.assertEqual(
            inst.activity[8].progress[0].time.date, FHIRDate("2012-07-30").date
        )
        self.assertEqual(inst.activity[8].progress[0].time.as_json(), "2012-07-30")
        self.assertEqual(
            force_bytes(inst.activity[8].progress[1].text),
            force_bytes("Eve prefers to focus on walking at this time"),
        )
        self.assertEqual(
            inst.activity[8].progress[1].time.date, FHIRDate("2012-08-13").date
        )
        self.assertEqual(inst.activity[8].progress[1].time.as_json(), "2012-08-13")
        self.assertEqual(
            force_bytes(inst.activity[9].detail.description),
            force_bytes(
                "Eve will match a printed medication worksheet with the medication bottles at home"
            ),
        )
        self.assertFalse(inst.activity[9].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[9].detail.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/RevisionDate"),
        )
        self.assertEqual(
            inst.activity[9].detail.extension[0].valueDate.date,
            FHIRDate("2012-07-23").date,
        )
        self.assertEqual(
            inst.activity[9].detail.extension[0].valueDate.as_json(), "2012-07-23"
        )
        self.assertEqual(
            inst.activity[9].detail.scheduledPeriod.start.date,
            FHIRDate("2012-07-10").date,
        )
        self.assertEqual(
            inst.activity[9].detail.scheduledPeriod.start.as_json(), "2012-07-10"
        )
        self.assertEqual(
            force_bytes(inst.activity[9].detail.status), force_bytes("completed")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("p1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("p2"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("p3"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("g1"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("g2"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("g3"))
        self.assertEqual(force_bytes(inst.contained[6].id), force_bytes("g4"))
        self.assertEqual(force_bytes(inst.contained[7].id), force_bytes("g5"))
        self.assertEqual(force_bytes(inst.id), force_bytes("integrate"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.note[0].text),
            force_bytes(
                "Patient family is not ready to commit to goal setting at this time.  Goal setting will be addressed in the future"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCarePlan8(self):
        inst = self.instantiate_from("careplan-example-f003-pharynx.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan8(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan8(inst2)

    def implCarePlan8(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].code),
            force_bytes("172960003"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].display),
            force_bytes("Incision of retropharyngeal abscess"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertTrue(inst.activity[0].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.kind), force_bytes("ServiceRequest")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.scheduledString),
            force_bytes("2011-06-27T09:30:10+01:00"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("completed")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("careteam"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("goal"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f003"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/zorgportal/identifiers/careplans"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("CP3953"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            inst.period.end.date, FHIRDate("2013-03-08T09:30:10+01:00").date
        )
        self.assertEqual(inst.period.end.as_json(), "2013-03-08T09:30:10+01:00")
        self.assertEqual(
            inst.period.start.date, FHIRDate("2013-03-08T09:00:10+01:00").date
        )
        self.assertEqual(inst.period.start.as_json(), "2013-03-08T09:00:10+01:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCarePlan9(self):
        inst = self.instantiate_from("careplan-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan9(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan9(inst2)

    def implCarePlan9(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].code),
            force_bytes("64915003"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].display),
            force_bytes("Operation on heart"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertTrue(inst.activity[0].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[0].detail.kind), force_bytes("ServiceRequest")
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.scheduledString),
            force_bytes("2011-06-27T09:30:10+01:00"),
        )
        self.assertEqual(
            force_bytes(inst.activity[0].detail.status), force_bytes("completed")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("careteam"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("goal"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.bmc.nl/zorgportal/identifiers/careplans"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("CP2903"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.period.end.date, FHIRDate("2011-06-27").date)
        self.assertEqual(inst.period.end.as_json(), "2011-06-27")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-06-26").date)
        self.assertEqual(inst.period.start.as_json(), "2011-06-26")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testCarePlan10(self):
        inst = self.instantiate_from("careplan-example-pregnancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan10(inst)

        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan10(inst2)

    def implCarePlan10(self, inst):
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.coding[0].code), force_bytes("1an")
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.coding[0].system),
            force_bytes("http://example.org/mySystem"),
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.code.text),
            force_bytes("First Antenatal encounter"),
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.description),
            force_bytes(
                "The first antenatal encounter. This is where a detailed physical examination is performed.             and the pregnanacy discussed with the mother-to-be."
            ),
        )
        self.assertFalse(inst.activity[1].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[1].detail.kind), force_bytes("Appointment")
        )
        self.assertEqual(
            inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.end.date,
            FHIRDate("2013-02-28").date,
        )
        self.assertEqual(
            inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.end.as_json(),
            "2013-02-28",
        )
        self.assertEqual(
            inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.start.date,
            FHIRDate("2013-02-14").date,
        )
        self.assertEqual(
            inst.activity[1].detail.scheduledTiming.repeat.boundsPeriod.start.as_json(),
            "2013-02-14",
        )
        self.assertEqual(
            force_bytes(inst.activity[1].detail.status), force_bytes("scheduled")
        )
        self.assertEqual(
            force_bytes(inst.activity[1].extension[0].url),
            force_bytes(
                "http://example.org/fhir/StructureDefinition/careplan#andetails"
            ),
        )
        self.assertEqual(
            force_bytes(inst.activity[1].extension[0].valueUri),
            force_bytes("http://orionhealth.com/fhir/careplan/1andetails"),
        )
        self.assertEqual(
            force_bytes(inst.activity[2].detail.code.coding[0].code), force_bytes("an")
        )
        self.assertEqual(
            force_bytes(inst.activity[2].detail.code.coding[0].system),
            force_bytes("http://example.org/mySystem"),
        )
        self.assertEqual(
            force_bytes(inst.activity[2].detail.code.text),
            force_bytes("Follow-up Antenatal encounter"),
        )
        self.assertEqual(
            force_bytes(inst.activity[2].detail.description),
            force_bytes(
                "The second antenatal encounter. Discuss any issues that arose from the first antenatal encounter"
            ),
        )
        self.assertFalse(inst.activity[2].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[2].detail.kind), force_bytes("Appointment")
        )
        self.assertEqual(
            inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.end.date,
            FHIRDate("2013-03-14").date,
        )
        self.assertEqual(
            inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.end.as_json(),
            "2013-03-14",
        )
        self.assertEqual(
            inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.start.date,
            FHIRDate("2013-03-01").date,
        )
        self.assertEqual(
            inst.activity[2].detail.scheduledTiming.repeat.boundsPeriod.start.as_json(),
            "2013-03-01",
        )
        self.assertEqual(
            force_bytes(inst.activity[2].detail.status), force_bytes("not-started")
        )
        self.assertEqual(
            force_bytes(inst.activity[3].detail.code.coding[0].code), force_bytes("del")
        )
        self.assertEqual(
            force_bytes(inst.activity[3].detail.code.coding[0].system),
            force_bytes("http://example.org/mySystem"),
        )
        self.assertEqual(
            force_bytes(inst.activity[3].detail.code.text), force_bytes("Delivery")
        )
        self.assertEqual(
            force_bytes(inst.activity[3].detail.description),
            force_bytes("The delivery."),
        )
        self.assertFalse(inst.activity[3].detail.doNotPerform)
        self.assertEqual(
            force_bytes(inst.activity[3].detail.kind), force_bytes("Appointment")
        )
        self.assertEqual(
            inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.end.date,
            FHIRDate("2013-09-14").date,
        )
        self.assertEqual(
            inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.end.as_json(),
            "2013-09-14",
        )
        self.assertEqual(
            inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.start.date,
            FHIRDate("2013-09-01").date,
        )
        self.assertEqual(
            inst.activity[3].detail.scheduledTiming.repeat.boundsPeriod.start.as_json(),
            "2013-09-01",
        )
        self.assertEqual(
            force_bytes(inst.activity[3].detail.status), force_bytes("not-started")
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("p1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("pr1"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("pr2"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("careteam"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("goal"))
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes("http://example.org/fhir/StructureDefinition/careplan#lmp"),
        )
        self.assertEqual(
            inst.extension[0].valueDateTime.date, FHIRDate("2013-01-01").date
        )
        self.assertEqual(inst.extension[0].valueDateTime.as_json(), "2013-01-01")
        self.assertEqual(force_bytes(inst.id), force_bytes("preg"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.period.end.date, FHIRDate("2013-10-01").date)
        self.assertEqual(inst.period.end.as_json(), "2013-10-01")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2013-01-01")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
