# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import plandefinition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class PlanDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("PlanDefinition", js["resourceType"])
        return plandefinition.PlanDefinition(js)

    def testPlanDefinition1(self):
        inst = self.instantiate_from("plandefinition-example-kdn5-simplified.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition1(inst2)

    def implPlanDefinition1(self, inst):
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[0]
                .extension[0]
                .extension[0]
                .url
            ),
            force_bytes("day"),
        )
        self.assertEqual(
            inst.action[0]
            .action[0]
            .action[0]
            .action[0]
            .action[0]
            .extension[0]
            .extension[0]
            .valueInteger,
            1,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[0]
                .extension[0]
                .extension[1]
                .url
            ),
            force_bytes("day"),
        )
        self.assertEqual(
            inst.action[0]
            .action[0]
            .action[0]
            .action[0]
            .action[0]
            .extension[0]
            .extension[1]
            .valueInteger,
            8,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[0].extension[0].url
            ),
            force_bytes("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].action[0].id),
            force_bytes("action-1"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[0].textEquivalent
            ),
            force_bytes("Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[1]
                .extension[0]
                .extension[0]
                .url
            ),
            force_bytes("day"),
        )
        self.assertEqual(
            inst.action[0]
            .action[0]
            .action[0]
            .action[0]
            .action[1]
            .extension[0]
            .extension[0]
            .valueInteger,
            1,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[1].extension[0].url
            ),
            force_bytes("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].action[1].id),
            force_bytes("action-2"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[1]
                .relatedAction[0]
                .actionId
            ),
            force_bytes("action-1"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .action[1]
                .relatedAction[0]
                .relationship
            ),
            force_bytes("concurrent-with-start"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[0].action[0].action[0].action[1].textEquivalent
            ),
            force_bytes("CARBOplatin AUC 5 IV over 30 minutes on Day 1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].id),
            force_bytes("cycle-definition-1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].action[0].textEquivalent),
            force_bytes("21-day cycle for 6 cycles"),
        )
        self.assertEqual(
            inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count, 6
        )
        self.assertEqual(
            inst.action[0].action[0].action[0].action[0].timingTiming.repeat.duration,
            21,
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[0]
                .action[0]
                .action[0]
                .timingTiming.repeat.durationUnit
            ),
            force_bytes("d"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].groupingBehavior),
            force_bytes("sentence-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].selectionBehavior),
            force_bytes("exactly-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].selectionBehavior), force_bytes("all")
        )
        self.assertEqual(
            force_bytes(inst.action[0].selectionBehavior), force_bytes("exactly-one")
        )
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-07-27").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-07-27")
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("1111"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("2222"))
        self.assertEqual(
            force_bytes(inst.contributor[0].name), force_bytes("Lee Surprenant")
        )
        self.assertEqual(force_bytes(inst.contributor[0].type), force_bytes("author"))
        self.assertEqual(
            force_bytes(inst.copyright), force_bytes("All rights reserved.")
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("KDN5"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://example.org/ordertemplates"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("KDN5"))
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-07-27").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-07-27")
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("National Comprehensive Cancer Network, Inc."),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("NCCN Guidelines for Kidney Cancer. V.2.2016"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "http://www.example.org/professionals/physician_gls/PDF/kidney.pdf"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].citation),
            force_bytes("Oudard S, et al. J Urol. 2007;177(5):1698-702"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("citation")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].url),
            force_bytes("http://www.ncbi.nlm.nih.gov/pubmed/17437788"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Gemcitabine/CARBOplatin")
        )
        self.assertEqual(
            force_bytes(inst.type.text), force_bytes("Chemotherapy Order Template")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code),
            force_bytes("treamentSetting-or-diseaseStatus"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].extension[0].valueString), force_bytes("A")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.text),
            force_bytes("Metastatic"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code),
            force_bytes("disease-or-histology"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].extension[0].valueString), force_bytes("A")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.text),
            force_bytes("Collecting Duct/Medullary Subtypes"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].extension[0].valueString), force_bytes("A")
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.text),
            force_bytes("Kidney Cancer"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.code),
            force_bytes("treatmentSetting-or-diseaseStatus"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].extension[0].valueString), force_bytes("B")
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.text),
            force_bytes("Relapsed"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.code),
            force_bytes("disease-or-histology"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.system),
            force_bytes("http://example.org/fhir/CodeSystem/indications"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].extension[0].valueString), force_bytes("B")
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.text),
            force_bytes("Collecting Duct/Medullary Subtypes"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].extension[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/usagecontext-group"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].extension[0].valueString), force_bytes("B")
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.text),
            force_bytes(
                "Kidney Cancer – Collecting Duct/Medullary Subtypes - Metastatic"
            ),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1"))

    def testPlanDefinition2(self):
        inst = self.instantiate_from("plandefinition-options-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition2(inst2)

    def implPlanDefinition2(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].id), force_bytes("medication-action-1")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Administer Medication 1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].id), force_bytes("medication-action-2")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].relatedAction[0].actionId),
            force_bytes("medication-action-1"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].relatedAction[0].offsetDuration.unit),
            force_bytes("h"),
        )
        self.assertEqual(
            inst.action[0].action[1].relatedAction[0].offsetDuration.value, 1
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].relatedAction[0].relationship),
            force_bytes("after-end"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].title),
            force_bytes("Administer Medication 2"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].groupingBehavior), force_bytes("logical-group")
        )
        self.assertEqual(
            force_bytes(inst.action[0].selectionBehavior), force_bytes("all")
        )
        self.assertEqual(
            force_bytes(inst.contained[0].id),
            force_bytes("activitydefinition-medicationrequest-1"),
        )
        self.assertEqual(
            force_bytes(inst.contained[1].id),
            force_bytes("activitydefinition-medicationrequest-2"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("options-example"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("This example illustrates relationships between actions."),
        )

    def testPlanDefinition3(self):
        inst = self.instantiate_from(
            "plandefinition-exclusive-breastfeeding-intervention-02.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition3(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition3(inst2)

    def implPlanDefinition3(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression),
            force_bytes("Communication Request to Provider"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].textEquivalent),
            force_bytes(
                "A Breastfeeding Readiness Assessment is recommended, please authorize or reject the order."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Notify the provider to sign the order."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].type.code), force_bytes("create")
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression),
            force_bytes("Should Notify Provider to Sign Assessment Order"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Mother should be administered a breastfeeding readiness assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].eventName),
            force_bytes("Admission"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[1].eventName),
            force_bytes("Birth"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[1].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[2].eventName),
            force_bytes("Infant Transfer to Recovery"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[2].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[3].eventName),
            force_bytes("Transfer to Post-Partum"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[3].type),
            force_bytes("named-event"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-03-08").date)
        self.assertEqual(inst.date.as_json(), "2015-03-08")
        self.assertEqual(
            force_bytes(inst.id), force_bytes("exclusive-breastfeeding-intervention-02")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("exclusive-breastfeeding-intervention-02"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Exclusive Breastfeeding Intervention-02"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition4(self):
        inst = self.instantiate_from(
            "plandefinition-exclusive-breastfeeding-intervention-03.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition4(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition4(inst2)

    def implPlanDefinition4(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression),
            force_bytes("Communication Request to Charge Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].textEquivalent),
            force_bytes(
                "A Breastfeeding Readiness Assessment is recommended, please administer the assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Notify the charge nurse to perform the assessment."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].type.code), force_bytes("create")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].dynamicValue[0].expression),
            force_bytes("Communication Request to Bedside Nurse"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].textEquivalent),
            force_bytes(
                "A Breastfeeding Readiness Assessment is recommended, please administer the assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].title),
            force_bytes("Notify the bedside nurse to perform the assessment."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].type.code), force_bytes("create")
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression),
            force_bytes("Should Notify Nurse to Perform Assessment"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Mother should be administered a breastfeeding readiness assessment."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].eventName),
            force_bytes("Admission"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[1].eventName),
            force_bytes("Birth"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[1].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[2].eventName),
            force_bytes("Infant Transfer to Recovery"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[2].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[3].eventName),
            force_bytes("Transfer to Post-Partum"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[3].type),
            force_bytes("named-event"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-03-08").date)
        self.assertEqual(inst.date.as_json(), "2015-03-08")
        self.assertEqual(
            force_bytes(inst.id), force_bytes("exclusive-breastfeeding-intervention-03")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("exclusive-breastfeeding-intervention-03"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Exclusive Breastfeeding Intervention-03"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition5(self):
        inst = self.instantiate_from("plandefinition-protocol-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition5(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition5(inst2)

    def implPlanDefinition5(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].cardinalityBehavior), force_bytes("single")
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression),
            force_bytes(
                "exists ([Condition: Obesity]) or not exists ([Observation: BMI] O where O.effectiveDateTime 2 years or less before Today())"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].language), force_bytes("text/cql")
        )
        self.assertEqual(
            force_bytes(inst.action[0].goalId[0]), force_bytes("reduce-bmi-ratio")
        )
        self.assertEqual(force_bytes(inst.action[0].label), force_bytes("Measure BMI"))
        self.assertEqual(
            force_bytes(inst.action[0].requiredBehavior),
            force_bytes("must-unless-documented"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes("Measure, Weight, Height, Waist, Circumference; Calculate BMI"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("procedure"))
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].system),
            force_bytes("url"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].value),
            force_bytes("https://www.nhlbi.nih.gov/health-pro/guidelines"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].name),
            force_bytes("National Heart, Lung, and Blood Institute"),
        )
        self.assertEqual(force_bytes(inst.contributor[0].type), force_bytes("author"))
        self.assertEqual(
            force_bytes(inst.goal[0].addresses[0].coding[0].code),
            force_bytes("414916001"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].addresses[0].coding[0].display),
            force_bytes("Obesity (disorder)"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].addresses[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].category.text), force_bytes("Treatment")
        )
        self.assertEqual(
            force_bytes(inst.goal[0].description.text),
            force_bytes("Reduce BMI to below 25"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].documentation[0].display),
            force_bytes("Evaluation and Treatment Strategy"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].documentation[0].type),
            force_bytes("justification"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].documentation[0].url),
            force_bytes(
                "https://www.nhlbi.nih.gov/health-pro/guidelines/current/obesity-guidelines/e_textbook/txgd/42.htm"
            ),
        )
        self.assertEqual(force_bytes(inst.goal[0].id), force_bytes("reduce-bmi-ratio"))
        self.assertEqual(
            force_bytes(inst.goal[0].priority.text), force_bytes("medium-priority")
        )
        self.assertEqual(
            force_bytes(inst.goal[0].start.text),
            force_bytes("When the patient's BMI Ratio is at or above 25"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].detailRange.high.unit),
            force_bytes("kg/m2"),
        )
        self.assertEqual(inst.goal[0].target[0].detailRange.high.value, 24.9)
        self.assertEqual(force_bytes(inst.goal[0].target[0].due.unit), force_bytes("a"))
        self.assertEqual(inst.goal[0].target[0].due.value, 1)
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].measure.coding[0].code),
            force_bytes("39156-5"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].measure.coding[0].display),
            force_bytes("Body mass index (BMI) [Ratio]"),
        )
        self.assertEqual(
            force_bytes(inst.goal[0].target[0].measure.coding[0].system),
            force_bytes("http://loinc.org"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("protocol-example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("http://acme.org")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("example-1")
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "Example of A medical algorithm for assessment and treatment of overweight and obesity"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes("Overweight and Obesity Treatment Guidelines"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "http://www.nhlbi.nih.gov/health-pro/guidelines/current/obesity-guidelines/e_textbook/txgd/algorthm/algorthm.htm"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Obesity Assessment Protocol")
        )
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("protocol"))
        self.assertEqual(
            force_bytes(inst.useContext[0].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("414916001"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Obesity (disorder)"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )

    def testPlanDefinition6(self):
        inst = self.instantiate_from("plandefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition6(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition6(inst2)

    def implPlanDefinition6(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[0].expression),
            force_bytes("Now()"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[0].path),
            force_bytes("timing.event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[1].expression),
            force_bytes(
                "Code '261QM0850X' from SuicideRiskLogic.\"NUCC Provider Taxonomy\" display 'Adult Mental Health'"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[1].path),
            force_bytes("specialty"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[2].expression),
            force_bytes("SuicideRiskLogic.ReferralRequestFulfillmentTime"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[2].path),
            force_bytes("occurrenceDateTime"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[3].expression),
            force_bytes("SuicideRiskLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[3].path),
            force_bytes("subject"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[4].expression),
            force_bytes("SuicideRiskLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[4].path),
            force_bytes("requester.agent"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[5].expression),
            force_bytes("SuicideRiskLogic.RiskAssessmentScore"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[5].path),
            force_bytes("reasonCode"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[6].expression),
            force_bytes("SuicideRiskLogic.RiskAssessment"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].dynamicValue[6].path),
            force_bytes("reasonReference"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].action[0].textEquivalent),
            force_bytes(
                "Refer to outpatient mental health program for evaluation and treatment of mental health conditions now"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].selectionBehavior), force_bytes("any")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Consults and Referrals"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[0]
                .expression
            ),
            force_bytes("'draft'"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[0]
                .path
            ),
            force_bytes("status"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[1]
                .expression
            ),
            force_bytes("SuicideRiskLogic.Patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[1]
                .path
            ),
            force_bytes("patient"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[2]
                .expression
            ),
            force_bytes("SuicideRiskLogic.Practitioner"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[2]
                .path
            ),
            force_bytes("prescriber"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[3]
                .expression
            ),
            force_bytes("SuicideRiskLogic.RiskAssessmentScore"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[3]
                .path
            ),
            force_bytes("reasonCode"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[4]
                .expression
            ),
            force_bytes("SuicideRiskLogic.RiskAssessment"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .action[0]
                .dynamicValue[4]
                .path
            ),
            force_bytes("reasonReference"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[0].textEquivalent
            ),
            force_bytes(
                "citalopram 20 mg tablet 1 tablet oral 1 time daily now (30 table; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[1].textEquivalent
            ),
            force_bytes(
                "escitalopram 10 mg tablet 1 tablet oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[2].textEquivalent
            ),
            force_bytes(
                "fluoxetine 20 mg capsule 1 capsule oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[3].textEquivalent
            ),
            force_bytes(
                "paroxetine 20 mg tablet 1 tablet oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].action[4].textEquivalent
            ),
            force_bytes(
                "sertraline 50 mg tablet 1 tablet oral 1 time daily now (30 tablet; 3 refills)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .documentation[0]
                .document.contentType
            ),
            force_bytes("text/html"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .documentation[0]
                .document.title
            ),
            force_bytes(
                "National Library of Medicine. DailyMed website. CITALOPRAM- citalopram hydrobromide tablet, film coated."
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .action[0]
                .documentation[0]
                .document.url
            ),
            force_bytes(
                "http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6daeb45c-451d-b135-bf8f-2d6dff4b6b01"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].action[0].documentation[0].type
            ),
            force_bytes("citation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[0].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[0].title),
            force_bytes(
                "Selective Serotonin Reuptake Inhibitors (Choose a mazimum of one or document reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[1].textEquivalent),
            force_bytes(
                "Dopamine Norepinephrine Reuptake Inhibitors (Choose a maximum of one or document reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[2].textEquivalent),
            force_bytes(
                "Serotonin Norepinephrine Reuptake Inhibitors (Choose a maximum of one or doument reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].action[3].textEquivalent),
            force_bytes(
                "Norepinephrine-Serotonin Modulators (Choose a maximum of one or document reasons for exception)"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].documentation[0].document.contentType
            ),
            force_bytes("text/html"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .url
            ),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/cqif-qualityOfEvidence"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("high"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/evidence-quality"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0]
                .action[1]
                .action[0]
                .documentation[0]
                .document.extension[0]
                .valueCodeableConcept.text
            ),
            force_bytes("High Quality"),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].documentation[0].document.title
            ),
            force_bytes(
                "Practice Guideline for the Treatment of Patients with Major Depressive Disorder"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.action[0].action[1].action[0].documentation[0].document.url
            ),
            force_bytes(
                "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].documentation[0].type),
            force_bytes("citation"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].action[0].title),
            force_bytes("First-Line Antidepressants"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].groupingBehavior),
            force_bytes("logical-group"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].selectionBehavior),
            force_bytes("at-most-one"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].title), force_bytes("Medications")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes("Suicide Risk Assessment and Outpatient Management"),
        )
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-03-12").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-03-12")
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("415-362-4007")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].use), force_bytes("work")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("info@motivemi.com"),
        )
        self.assertEqual(
            force_bytes(inst.contained[0].id), force_bytes("referralToMentalHealthCare")
        )
        self.assertEqual(
            force_bytes(inst.contained[1].id), force_bytes("citalopramPrescription")
        )
        self.assertEqual(
            force_bytes(inst.contained[2].id), force_bytes("citalopramMedication")
        )
        self.assertEqual(
            force_bytes(inst.contained[3].id), force_bytes("citalopramSubstance")
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].system),
            force_bytes("phone"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].use),
            force_bytes("work"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[0].value),
            force_bytes("415-362-4007"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[1].system),
            force_bytes("email"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[1].use),
            force_bytes("work"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].contact[0].telecom[1].value),
            force_bytes("info@motivemi.com"),
        )
        self.assertEqual(
            force_bytes(inst.contributor[0].name),
            force_bytes("Motive Medical Intelligence"),
        )
        self.assertEqual(force_bytes(inst.contributor[0].type), force_bytes("author"))
        self.assertEqual(
            force_bytes(inst.copyright),
            force_bytes(
                "© Copyright 2016 Motive Medical Intelligence. All rights reserved."
            ),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-08-15").date)
        self.assertEqual(inst.date.as_json(), "2015-08-15")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Orders to be applied to a patient characterized as low suicide risk."
            ),
        )
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2016-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("low-suicide-risk-order-set")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://motivemi.com/artifacts"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("mmi:low-suicide-risk-order-set"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("urn:iso:std:iso:3166"),
        )
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-08-15").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-08-15")
        self.assertEqual(force_bytes(inst.name), force_bytes("LowSuicideRiskOrderSet"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Motive Medical Intelligence")
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes(
                "This order set helps ensure consistent application of appropriate orders for the care of low suicide risk patients."
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].display),
            force_bytes(
                "Practice Guideline for the Treatment of Patients with Major Depressive Disorder"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("composed-of")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[2].type), force_bytes("composed-of")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Low Suicide Risk Order Set")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Suicide risk assessment")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://motivemi.com/artifacts/PlanDefinition/low-suicide-risk-order-set"
            ),
        )
        self.assertEqual(
            force_bytes(inst.usage),
            force_bytes(
                "This order set should be applied after assessing a patient for suicide risk, when the findings of that assessment indicate the patient has low suicide risk."
            ),
        )
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("age"))
        self.assertEqual(
            force_bytes(inst.useContext[0].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code),
            force_bytes("D000328"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display),
            force_bytes("Adult"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system),
            force_bytes("https://meshb.nlm.nih.gov"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code),
            force_bytes("87512008"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display),
            force_bytes("Mild major depression"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].code),
            force_bytes("40379007"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].display),
            force_bytes("Major depression, recurrent, mild"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].code),
            force_bytes("394687007"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].display),
            force_bytes("Low suicide risk"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.code), force_bytes("focus")
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].code),
            force_bytes("225337009"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].display),
            force_bytes("Suicide risk assessment"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.useContext[5].code.code), force_bytes("user"))
        self.assertEqual(
            force_bytes(inst.useContext[5].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].code),
            force_bytes("309343006"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].display),
            force_bytes("Physician"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].code.code), force_bytes("venue")
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].code.system),
            force_bytes("http://hl7.org/fhir/usage-context-type"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].code),
            force_bytes("440655000"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].display),
            force_bytes("Outpatient environment"),
        )
        self.assertEqual(
            force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition7(self):
        inst = self.instantiate_from(
            "plandefinition-exclusive-breastfeeding-intervention-04.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition7(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition7(inst2)

    def implPlanDefinition7(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].expression),
            force_bytes("Create Lactation Consult Request"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].dynamicValue[0].path), force_bytes("/")
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].textEquivalent),
            force_bytes("Create a lactation consult request"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].title),
            force_bytes("Create a lactation consult request."),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].type.code), force_bytes("create")
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression),
            force_bytes("Should Create Lactation Consult"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Mother should be referred to a lactation specialist for consultation."
            ),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].eventName),
            force_bytes("Admission"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[1].eventName),
            force_bytes("Birth"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[1].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[2].eventName),
            force_bytes("Infant Transfer to Recovery"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[2].type),
            force_bytes("named-event"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[3].eventName),
            force_bytes("Transfer to Post-Partum"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[3].type),
            force_bytes("named-event"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-03-08").date)
        self.assertEqual(inst.date.as_json(), "2015-03-08")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Exclusive breastfeeding intervention intended to improve outcomes for exclusive breastmilk feeding of newborns by creating a lactation consult for the mother if appropriate."
            ),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("exclusive-breastfeeding-intervention-04")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("exclusive-breastfeeding-intervention-04"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Exclusive Breastfeeding Intervention-04"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition8(self):
        inst = self.instantiate_from("plandefinition-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition8(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition8(inst2)

    def implPlanDefinition8(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].condition[0].expression),
            force_bytes("Should Administer Zika Virus Exposure Assessment"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].condition[0].expression),
            force_bytes("Should Order Serum + Urine rRT-PCR Test"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[2].condition[0].expression),
            force_bytes("Should Order Serum Zika Virus IgM + Dengue Virus IgM"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[2].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[3].condition[0].expression),
            force_bytes("Should Consider IgM Antibody Testing"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[3].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[4].condition[0].expression),
            force_bytes("Should Provide Mosquito Prevention and Contraception Advice"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[4].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression),
            force_bytes("Is Patient Pregnant"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title), force_bytes("Zika Virus Assessment")
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].eventName),
            force_bytes("patient-view"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].type),
            force_bytes("named-event"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2016-11-14").date)
        self.assertEqual(inst.date.as_json(), "2016-11-14")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Zika Virus Management intervention describing the CDC Guidelines for Zika Virus Reporting and Management."
            ),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("zika-virus-intervention-initial")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("zika-virus-intervention"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm6539e1_w"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("successor")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Example Zika Virus Intervention")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Zika Virus Management")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://example.org/PlanDefinition/zika-virus-intervention"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))

    def testPlanDefinition9(self):
        inst = self.instantiate_from("plandefinition-zika-virus-intervention.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition9(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition9(inst2)

    def implPlanDefinition9(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].action[0].condition[0].expression),
            force_bytes("Should Administer Zika Virus Exposure Assessment"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[0].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].condition[0].expression),
            force_bytes("Should Order Serum + Urine rRT-PCR Test"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[1].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[2].condition[0].expression),
            force_bytes("Should Order Serum Zika Virus IgM + Dengue Virus IgM"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[2].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[3].condition[0].expression),
            force_bytes("Should Consider IgM Antibody Testing"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[3].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[4].condition[0].expression),
            force_bytes("Should Provide Mosquito Prevention and Contraception Advice"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].action[4].condition[0].kind),
            force_bytes("applicability"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression),
            force_bytes("Is Patient Pregnant"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title), force_bytes("Zika Virus Assessment")
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].eventName),
            force_bytes("patient-view"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].triggerDefinition[0].type),
            force_bytes("named-event"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-01-12").date)
        self.assertEqual(inst.date.as_json(), "2017-01-12")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Zika Virus Management intervention describing the CDC Guidelines for Zika Virus Reporting and Management."
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("zika-virus-intervention"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("zika-virus-intervention"),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].type), force_bytes("derived-from")
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[0].url),
            force_bytes(
                "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm6539e1_w"
            ),
        )
        self.assertEqual(
            force_bytes(inst.relatedArtifact[1].type), force_bytes("predecessor")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Example Zika Virus Intervention")
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Zika Virus Management")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://example.org/PlanDefinition/zika-virus-intervention"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("2.0.0"))

    def testPlanDefinition10(self):
        inst = self.instantiate_from(
            "plandefinition-chlamydia-screening-intervention.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition10(inst)

        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition10(inst2)

    def implPlanDefinition10(self, inst):
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].expression),
            force_bytes("NoScreening"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].condition[0].kind), force_bytes("applicability")
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].expression),
            force_bytes("ChlamydiaScreeningRequest"),
        )
        self.assertEqual(
            force_bytes(inst.action[0].dynamicValue[0].path), force_bytes("~")
        )
        self.assertEqual(
            force_bytes(inst.action[0].title),
            force_bytes(
                "Patient has not had chlamydia screening within the recommended timeframe..."
            ),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Chlamydia Screening CDS Example Using Common"),
        )
        self.assertEqual(
            force_bytes(inst.id), force_bytes("chlamydia-screening-intervention")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("ChlamydiaScreening_CDS_UsingCommon"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Chalmydia Screening CDS Example Using Common"),
        )
        self.assertEqual(
            force_bytes(inst.topic[0].text), force_bytes("Chlamydia Screeening")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("2.0.0"))
