#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-05-14.
#  2019, SMART Health IT.


import io
import json
import os
import unittest

from . import questionnaire
from .fhirdate import FHIRDate


class QuestionnaireTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Questionnaire", js["resourceType"])
        return questionnaire.Questionnaire(js)

    def testQuestionnaire1(self):
        inst = self.instantiate_from("questionnaire-example-gcs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire1(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire1(inst2)

    def implQuestionnaire1(self, inst):
        self.assertEqual(inst.contained[0].id, "motor")
        self.assertEqual(inst.contained[1].id, "verbal")
        self.assertEqual(inst.contained[2].id, "eye")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-03").date)
        self.assertEqual(inst.date.as_json(), "2015-08-03")
        self.assertEqual(inst.group.concept[0].code, "9269-2")
        self.assertEqual(inst.group.concept[0].system, "http://loinc.org")
        self.assertEqual(inst.group.linkId, "1")
        self.assertEqual(inst.group.question[0].concept[0].code, "9270-0")
        self.assertEqual(inst.group.question[0].concept[0].system, "http://loinc.org")
        self.assertEqual(inst.group.question[0].linkId, "1.1")
        self.assertEqual(inst.group.question[0].type, "choice")
        self.assertEqual(inst.group.question[1].concept[0].code, "9268-4")
        self.assertEqual(inst.group.question[1].concept[0].system, "http://loinc.org")
        self.assertEqual(inst.group.question[1].linkId, "1.2")
        self.assertEqual(inst.group.question[1].type, "choice")
        self.assertEqual(inst.group.question[2].concept[0].code, "9267-6")
        self.assertEqual(inst.group.question[2].concept[0].system, "http://loinc.org")
        self.assertEqual(inst.group.question[2].linkId, "1.3")
        self.assertEqual(inst.group.question[2].type, "choice")
        self.assertTrue(inst.group.required)
        self.assertEqual(inst.group.title, "Glasgow Coma Score")
        self.assertEqual(inst.id, "gcs")
        self.assertEqual(inst.publisher, "FHIR Project team")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")

    def testQuestionnaire2(self):
        inst = self.instantiate_from("questionnaire-example-f201-lifelines.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire2(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire2(inst2)

    def implQuestionnaire2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2010").date)
        self.assertEqual(inst.date.as_json(), "2010")
        self.assertEqual(inst.group.concept[0].code, "VL 1-1, 18-65_1.2.2")
        self.assertEqual(
            inst.group.concept[0].display, "Lifelines Questionnaire 1 part 1"
        )
        self.assertEqual(
            inst.group.concept[0].system, "http://example.org/system/code/lifelines/nl"
        )
        self.assertEqual(inst.group.group[0].linkId, "1")
        self.assertEqual(inst.group.group[0].question[0].linkId, "1.1")
        self.assertEqual(inst.group.group[0].question[0].text, "Do you have allergies?")
        self.assertEqual(inst.group.group[1].linkId, "2")
        self.assertEqual(inst.group.group[1].question[0].linkId, "2.1")
        self.assertEqual(inst.group.group[1].question[0].text, "What is your gender?")
        self.assertEqual(inst.group.group[1].question[1].linkId, "2.2")
        self.assertEqual(
            inst.group.group[1].question[1].text, "What is your date of birth?"
        )
        self.assertEqual(inst.group.group[1].question[2].linkId, "2.3")
        self.assertEqual(
            inst.group.group[1].question[2].text, "What is your country of birth?"
        )
        self.assertEqual(inst.group.group[1].question[3].linkId, "2.4")
        self.assertEqual(
            inst.group.group[1].question[3].text, "What is your marital status?"
        )
        self.assertEqual(inst.group.group[1].text, "General questions")
        self.assertEqual(inst.group.group[2].linkId, "3")
        self.assertEqual(inst.group.group[2].question[0].linkId, "3.1")
        self.assertEqual(inst.group.group[2].question[0].text, "Do you smoke?")
        self.assertEqual(inst.group.group[2].question[1].linkId, "3.2")
        self.assertEqual(inst.group.group[2].question[1].text, "Do you drink alchohol?")
        self.assertEqual(inst.group.group[2].title, "Intoxications")
        self.assertEqual(inst.group.linkId, "root")
        self.assertTrue(inst.group.required)
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.status, "published")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")

    def testQuestionnaire3(self):
        inst = self.instantiate_from("questionnaire-example-bluebook.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire3(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire3(inst2)

    def implQuestionnaire3(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-02-19").date)
        self.assertEqual(inst.date.as_json(), "2013-02-19")
        self.assertEqual(inst.group.group[0].group[0].question[0].linkId, "nameOfChild")
        self.assertEqual(inst.group.group[0].group[0].question[0].text, "Name of child")
        self.assertEqual(inst.group.group[0].group[0].question[1].linkId, "sex")
        self.assertEqual(inst.group.group[0].group[0].question[1].text, "Sex")
        self.assertEqual(inst.group.group[0].group[1].linkId, "neonatalInformation")
        self.assertEqual(inst.group.group[0].group[1].question[0].linkId, "birthWeight")
        self.assertEqual(
            inst.group.group[0].group[1].question[0].text, "Birth weight (kg)"
        )
        self.assertEqual(inst.group.group[0].group[1].question[1].linkId, "birthLength")
        self.assertEqual(
            inst.group.group[0].group[1].question[1].text, "Birth length (cm)"
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].group[0].extension[0].url,
            "http://example.org/Profile/questionnaire#visibilityCondition",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].group[0].extension[0].valueString,
            "HAS_VALUE(../choice/code) AND NEQ(../choice/code,'NO')",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].group[0].linkId,
            "vitaminKgivenDoses",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].group[0].question[0].linkId,
            "vitaminiKDose1",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].group[0].question[0].text,
            "1st dose",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].group[0].question[1].linkId,
            "vitaminiKDose2",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].group[0].question[1].text,
            "2nd dose",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].linkId, "vitaminKgiven"
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[2].text, "Vitamin K given"
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[3].group[0].question[0].linkId,
            "hepBgivenDate",
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[3].group[0].question[0].text,
            "Date given",
        )
        self.assertEqual(inst.group.group[0].group[1].question[3].linkId, "hepBgiven")
        self.assertEqual(
            inst.group.group[0].group[1].question[3].text, "Hep B given y / n"
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[4].linkId, "abnormalitiesAtBirth"
        )
        self.assertEqual(
            inst.group.group[0].group[1].question[4].text,
            "Abnormalities noted at birth",
        )
        self.assertEqual(inst.group.group[0].group[1].title, "Neonatal Information")
        self.assertEqual(inst.group.group[0].linkId, "birthDetails")
        self.assertEqual(
            inst.group.group[0].title,
            "Birth details - To be completed by health professional",
        )
        self.assertEqual(inst.group.linkId, "PHR")
        self.assertTrue(inst.group.required)
        self.assertEqual(inst.group.title, "NSW Government My Personal Health Record")
        self.assertEqual(inst.id, "bb")
        self.assertEqual(inst.publisher, "New South Wales Department of Health")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")

    def testQuestionnaire4(self):
        inst = self.instantiate_from("questionnaire-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire4(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire4(inst2)

    def implQuestionnaire4(self, inst):
        self.assertEqual(inst.contained[0].id, "yesno")
        self.assertEqual(inst.date.date, FHIRDate("2012-01").date)
        self.assertEqual(inst.date.as_json(), "2012-01")
        self.assertEqual(inst.group.group[0].concept[0].code, "COMORBIDITY")
        self.assertEqual(
            inst.group.group[0].concept[0].system,
            "http://example.org/system/code/sections",
        )
        self.assertEqual(inst.group.group[0].linkId, "1.1")
        self.assertEqual(inst.group.group[0].question[0].concept[0].code, "COMORB")
        self.assertEqual(
            inst.group.group[0].question[0].concept[0].system,
            "http://example.org/system/code/questions",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].concept[0].code, "CARDIAL"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].concept[0].system,
            "http://example.org/system/code/sections",
        )
        self.assertEqual(inst.group.group[0].question[0].group[0].linkId, "1.1.1.1")
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[0].concept[0].code,
            "COMORBCAR",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[0].concept[0].system,
            "http://example.org/system/code/questions",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[0].linkId, "1.1.1.1.1"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[0].type, "choice"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].concept[0].code,
            "COMCAR00",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].concept[0].display,
            "Angina Pectoris",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].concept[0].system,
            "http://example.org/system/code/questions",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].concept[1].code,
            "194828000",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].concept[1].display,
            "Angina (disorder)",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].concept[1].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].linkId, "1.1.1.1.2"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[1].type, "choice"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[2].concept[0].code,
            "22298006",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[2].concept[0].display,
            "Myocardial infarction (disorder)",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[2].concept[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[2].linkId, "1.1.1.1.3"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[0].question[2].type, "choice"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[1].concept[0].code, "VASCULAR"
        )
        self.assertEqual(
            inst.group.group[0].question[0].group[1].concept[0].system,
            "http://example.org/system/code/sections",
        )
        self.assertEqual(inst.group.group[0].question[0].group[1].linkId, "1.1.1.2")
        self.assertEqual(inst.group.group[0].question[0].linkId, "1.1.1")
        self.assertEqual(inst.group.group[0].question[0].type, "choice")
        self.assertEqual(inst.group.group[1].concept[0].code, "HISTOPATHOLOGY")
        self.assertEqual(
            inst.group.group[1].concept[0].system,
            "http://example.org/system/code/sections",
        )
        self.assertEqual(inst.group.group[1].group[0].concept[0].code, "ABDOMINAL")
        self.assertEqual(
            inst.group.group[1].group[0].concept[0].system,
            "http://example.org/system/code/sections",
        )
        self.assertEqual(inst.group.group[1].group[0].linkId, "1.2.1")
        self.assertEqual(
            inst.group.group[1].group[0].question[0].concept[0].code, "STADPT"
        )
        self.assertEqual(
            inst.group.group[1].group[0].question[0].concept[0].display, "pT category"
        )
        self.assertEqual(
            inst.group.group[1].group[0].question[0].concept[0].system,
            "http://example.org/system/code/questions",
        )
        self.assertEqual(inst.group.group[1].group[0].question[0].linkId, "1.2.1.2")
        self.assertEqual(inst.group.group[1].linkId, "1.2")
        self.assertEqual(inst.group.linkId, "1")
        self.assertTrue(inst.group.required)
        self.assertEqual(inst.group.title, "Cancer Quality Forum Questionnaire 2012")
        self.assertEqual(inst.id, "3141")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")
