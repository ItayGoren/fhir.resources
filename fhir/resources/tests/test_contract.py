# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
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

from .. import contract
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ContractTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Contract", js["resourceType"])
        return contract.Contract(js)

    def testContract1(self):
        inst = self.instantiate_from("pcd-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract1(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract1(inst2)

    def implContract1(self, inst):
        self.assertEqual(
            force_bytes(inst.friendly[0].contentAttachment.title),
            force_bytes("The terms of the consent in friendly consumer speak."),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notOrg"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.title),
            force_bytes("The terms of the consent in lawyer speak."),
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
            force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In")
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].display),
            force_bytes("Default Authorization with exceptions."),
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].system),
            force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.text),
            force_bytes(
                "Withhold this order and any results or related objects from any provider."
            ),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].code), force_bytes("withhold-from")
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].display),
            force_bytes("Withhold all data from specified actor entity."),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].system),
            force_bytes("http://example.org/fhir/consent-term-type-codes"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org")
        )

    def testContract2(self):
        inst = self.instantiate_from("contract-example-ins-policy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract2(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract2(inst2)

    def implContract2(self, inst):
        self.assertEqual(inst.applies.start.date, FHIRDate("2017-01-01").date)
        self.assertEqual(inst.applies.start.as_json(), "2017-01-01")
        self.assertEqual(force_bytes(inst.id), force_bytes("INS-101"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://xyz-insurance.com/forms"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("YCSCWLN(01-2017)")
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
            inst.term[0].asset[0].period[0].start.date, FHIRDate("2017-06-01").date
        )
        self.assertEqual(inst.term[0].asset[0].period[0].start.as_json(), "2017-06-01")
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].subtype[0].text), force_bytes("sample")
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].type[0].coding[0].code),
            force_bytes("RicardianContract"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].type[0].coding[0].system),
            force_bytes("urn:ietf:rfc:3986"),
        )
        self.assertEqual(
            inst.term[0].asset[0].valuedItem[0].effectiveTime.date,
            FHIRDate("1995").date,
        )
        self.assertEqual(
            inst.term[0].asset[0].valuedItem[0].effectiveTime.as_json(), "1995"
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].entityCodeableConcept.text),
            force_bytes("Ford Bobcat"),
        )
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].factor, 1.0)
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].identifier.system),
            force_bytes("http://somewhere.motor-vehicle.com/vin"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].identifier.value),
            force_bytes("XXSVT34-7665t952236"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].net.currency),
            force_bytes("CAD"),
        )
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].net.value, 200.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].points, 1.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].quantity.value, 1)
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].unitPrice.currency),
            force_bytes("CAD"),
        )
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].unitPrice.value, 200.0)
        self.assertEqual(
            force_bytes(inst.term[0].group[0].offer.text),
            force_bytes("Eligible Providers"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[1].offer.text),
            force_bytes("Responsibility for Payment"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[0].group[0].offer.text),
            force_bytes("Emergency Room Copay"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[0].group[1].offer.text),
            force_bytes("Professional Visit Copay"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[0].offer.text),
            force_bytes("Copays"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[1].offer.text),
            force_bytes("Calendar Year Deductible"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[2].offer.text),
            force_bytes("Out-Of-Pocket Maximum"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[3].group[0].offer.text),
            force_bytes("Ambulance Services"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[3].group[1].offer.text),
            force_bytes("Dental Services"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[3].group[2].offer.text),
            force_bytes("Diagnostic Services"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[3].group[3].offer.text),
            force_bytes("Emergency Room Services"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[3].group[4].offer.text),
            force_bytes("Hospital Inpatient Care"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].group[3].offer.text),
            force_bytes("Medical Services"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[2].offer.text),
            force_bytes("List of Benefits"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].code), force_bytes("healthinsurance")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].display), force_bytes("Health Insurance")
        )
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/contract-type"),
        )

    def testContract3(self):
        inst = self.instantiate_from("contract-example-42cfr-part2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract3(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract3(inst2)

    def implContract3(self, inst):
        self.assertEqual(
            inst.applies.start.date, FHIRDate("2013-11-01T21:18:27-04:00").date
        )
        self.assertEqual(inst.applies.start.as_json(), "2013-11-01T21:18:27-04:00")
        self.assertEqual(
            force_bytes(inst.contentDerivative.coding[0].code),
            force_bytes("registration"),
        )
        self.assertEqual(
            force_bytes(inst.contentDerivative.coding[0].system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/contract-content-derivative"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("C-2121"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-11-01T21:18:27-04:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-11-01T21:18:27-04:00")
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.contentType),
            force_bytes("application/pdf"),
        )
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.language), force_bytes("en-US")
        )
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.title),
            force_bytes("MDHHS-5515 Consent To Share Your Health Information"),
        )
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.url),
            force_bytes("http://org.mihin.ecms/ConsentDirective-2121"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2016-07-19T18:18:42.108-04:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2016-07-19T18:18:42.108-04:00"
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.meta.versionId), force_bytes("1"))
        self.assertEqual(
            force_bytes(inst.signer[0].signature[0].type[0].code),
            force_bytes("1.2.840.10065.1.12.1.1"),
        )
        self.assertEqual(
            force_bytes(inst.signer[0].signature[0].type[0].system),
            force_bytes("urn:iso-astm:E1762-95:2013"),
        )
        self.assertEqual(
            inst.signer[0].signature[0].when.date,
            FHIRDate("2017-02-08T10:57:34+01:00").date,
        )
        self.assertEqual(
            inst.signer[0].signature[0].when.as_json(), "2017-02-08T10:57:34+01:00"
        )
        self.assertEqual(force_bytes(inst.signer[0].type.code), force_bytes("SELF"))
        self.assertEqual(
            force_bytes(inst.signer[0].type.system),
            force_bytes("http://mdhhs.org/fhir/consent-signer-type"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("executed"))
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].code), force_bytes("hcd")
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/consentcategorycodes"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].intent.coding[0].code),
            force_bytes("HPRGRP"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].intent.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].status.text), force_bytes("Sample")
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[0].role.coding[0].code),
            force_bytes("IR"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[0].role.coding[0].display),
            force_bytes("Recipient"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[0].role.coding[0].system),
            force_bytes("http://mdhhs.org/fhir/consent-actor-type"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[0].role.text),
            force_bytes("Recipient of restricted health information"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[1].role.coding[0].code),
            force_bytes("IS"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[1].role.coding[0].display),
            force_bytes("Sender"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[1].role.coding[0].system),
            force_bytes("http://mdhhs.org/fhir/consent-actor-type"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].subject[1].role.text),
            force_bytes("Sender of restricted health information"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].type.coding[0].code),
            force_bytes("action-a"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].action[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/contractaction"),
        )
        self.assertEqual(
            inst.term[0].asset[0].period[0].end.date,
            FHIRDate("2019-11-01T21:18:27-04:00").date,
        )
        self.assertEqual(
            inst.term[0].asset[0].period[0].end.as_json(), "2019-11-01T21:18:27-04:00"
        )
        self.assertEqual(
            inst.term[0].asset[0].period[0].start.date,
            FHIRDate("2013-11-01T21:18:27-04:00").date,
        )
        self.assertEqual(
            inst.term[0].asset[0].period[0].start.as_json(), "2013-11-01T21:18:27-04:00"
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.decision.coding[0].code),
            force_bytes("OPTIN"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.decision.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.text), force_bytes("Can't refuse")
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.type.coding[0].code),
            force_bytes("statutory"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/contracttermtypecodes"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("OPTIN"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://mdhhs.org/fhir/consentdirective-type"),
        )
        self.assertEqual(
            force_bytes(inst.type.text), force_bytes("Opt-in consent directive")
        )

    def testContract4(self):
        inst = self.instantiate_from("pcd-example-notLabs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract4(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract4(inst2)

    def implContract4(self, inst):
        self.assertEqual(
            force_bytes(inst.friendly[0].contentAttachment.title),
            force_bytes("The terms of the consent in friendly consumer speak."),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notLabs"))
        self.assertEqual(inst.issued.date, FHIRDate("2014-08-17").date)
        self.assertEqual(inst.issued.as_json(), "2014-08-17")
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.title),
            force_bytes("The terms of the consent in lawyer speak."),
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
            force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In")
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].display),
            force_bytes("Default Authorization with exceptions."),
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].system),
            force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[0].offer.text),
            force_bytes("Withhold orders from any provider."),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[0].subType.coding[0].code),
            force_bytes("ServiceRequest"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[0].subType.coding[0].system),
            force_bytes("http://hl7.org/fhir/resource-types"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[0].type.coding[0].code),
            force_bytes("withhold-object-type"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[0].type.coding[0].system),
            force_bytes("http://example.org/fhir/consent-term-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[1].offer.text),
            force_bytes("Withhold order results from any provider."),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[1].subType.coding[0].code),
            force_bytes("DiagnosticReport"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[1].subType.coding[0].system),
            force_bytes("http://hl7.org/fhir/resource-types"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[1].type.coding[0].code),
            force_bytes("withhold-object-type"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].group[1].type.coding[0].system),
            force_bytes("http://example.org/fhir/consent-term-type-codes"),
        )
        self.assertEqual(force_bytes(inst.term[0].offer.text), force_bytes("sample"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org")
        )

    def testContract5(self):
        inst = self.instantiate_from("pcd-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract5(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract5(inst2)

    def implContract5(self, inst):
        self.assertEqual(
            force_bytes(inst.friendly[0].contentAttachment.title),
            force_bytes("The terms of the consent in friendly consumer speak."),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notThem"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.title),
            force_bytes("The terms of the consent in lawyer speak."),
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
            force_bytes(inst.signer[0].signature[0].type[0].code),
            force_bytes("1.2.840.10065.1.12.1.1"),
        )
        self.assertEqual(
            force_bytes(inst.signer[0].signature[0].type[0].system),
            force_bytes("urn:iso-astm:E1762-95:2013"),
        )
        self.assertEqual(
            inst.signer[0].signature[0].when.date,
            FHIRDate("2013-06-08T10:57:34-07:00").date,
        )
        self.assertEqual(
            inst.signer[0].signature[0].when.as_json(), "2013-06-08T10:57:34-07:00"
        )
        self.assertEqual(force_bytes(inst.signer[0].type.code), force_bytes("COVPTY"))
        self.assertEqual(
            force_bytes(inst.signer[0].type.system),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/contractsignertypecodes"
            ),
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In")
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].display),
            force_bytes("Default Authorization with exceptions."),
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].system),
            force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.text),
            force_bytes(
                "Withhold this order and any results or related objects from specified nurse provider."
            ),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].code), force_bytes("withhold-from")
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].display),
            force_bytes("Withhold all data from specified actor entity."),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].system),
            force_bytes("http://example.org/fhir/consent-term-type-codes"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org")
        )

    def testContract6(self):
        inst = self.instantiate_from("pcd-example-notAuthor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract6(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract6(inst2)

    def implContract6(self, inst):
        self.assertEqual(
            force_bytes(inst.friendly[0].contentAttachment.title),
            force_bytes("The terms of the consent in friendly consumer speak."),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notAuthor"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.title),
            force_bytes("The terms of the consent in lawyer speak."),
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
            force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In")
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].display),
            force_bytes("Default Authorization with exceptions."),
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].system),
            force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].offer.text),
            force_bytes("Withhold all data authored by Good Health provider."),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].code),
            force_bytes("withhold-authored-by"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].display),
            force_bytes("Withhold all data authored by specified actor entity."),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].system),
            force_bytes("http://example.org/fhir/consent-term-type-codes"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org")
        )

    def testContract7(self):
        inst = self.instantiate_from("contract-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract7(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract7(inst2)

    def implContract7(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("C-123"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyvalley.com/contract"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12347"))
        self.assertEqual(
            force_bytes(inst.legallyBindingAttachment.contentType),
            force_bytes("application/pdf"),
        )
        self.assertEqual(
            force_bytes(inst.legallyBindingAttachment.url),
            force_bytes("http://www.aws3.com/storage/doc.pdf"),
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
            force_bytes(inst.rule[0].contentAttachment.contentType),
            force_bytes("application/txt"),
        )
        self.assertEqual(
            force_bytes(inst.rule[0].contentAttachment.url),
            force_bytes("http://www.rfc-editor.org/bcp/bcp13.txt"),
        )
        self.assertEqual(
            inst.term[0].asset[0].period[0].start.date, FHIRDate("2017-06-01").date
        )
        self.assertEqual(inst.term[0].asset[0].period[0].start.as_json(), "2017-06-01")
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].subtype[0].text), force_bytes("sample")
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].type[0].coding[0].code),
            force_bytes("RicardianContract"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].type[0].coding[0].system),
            force_bytes("urn:ietf:rfc:3986"),
        )
        self.assertEqual(
            inst.term[0].asset[0].valuedItem[0].effectiveTime.date,
            FHIRDate("1995").date,
        )
        self.assertEqual(
            inst.term[0].asset[0].valuedItem[0].effectiveTime.as_json(), "1995"
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].entityCodeableConcept.text),
            force_bytes("Ford Bobcat"),
        )
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].factor, 1.0)
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].identifier.system),
            force_bytes("http://somewhere.motor-vehicle.com/vin"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].identifier.value),
            force_bytes("XXSVT34-7665t952236"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].net.currency),
            force_bytes("CAD"),
        )
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].net.value, 200.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].points, 1.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].quantity.value, 1)
        self.assertEqual(
            force_bytes(inst.term[0].asset[0].valuedItem[0].unitPrice.currency),
            force_bytes("CAD"),
        )
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].unitPrice.value, 200.0)
        self.assertEqual(
            force_bytes(inst.term[0].offer.text), force_bytes("Can't refuse")
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the contract</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testContract8(self):
        inst = self.instantiate_from("pcd-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract8(inst)

        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract8(inst2)

    def implContract8(self, inst):
        self.assertEqual(
            force_bytes(inst.friendly[0].contentAttachment.title),
            force_bytes("The terms of the consent in friendly consumer speak."),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("pcd-example-notThis"))
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(
            force_bytes(inst.legal[0].contentAttachment.title),
            force_bytes("The terms of the consent in lawyer speak."),
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
            force_bytes(inst.subType[0].coding[0].code), force_bytes("Opt-In")
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].display),
            force_bytes("Default Authorization with exceptions."),
        )
        self.assertEqual(
            force_bytes(inst.subType[0].coding[0].system),
            force_bytes("http://www.infoway-inforoute.ca.org/Consent-subtype-codes"),
        )
        self.assertEqual(inst.term[0].applies.start.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.term[0].applies.start.as_json(), "2015-11-18")
        self.assertEqual(
            force_bytes(inst.term[0].identifier.system),
            force_bytes("http://example.org/fhir/term-items"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].identifier.value), force_bytes("3347689")
        )
        self.assertEqual(inst.term[0].issued.date, FHIRDate("2015-11-01").date)
        self.assertEqual(inst.term[0].issued.as_json(), "2015-11-01")
        self.assertEqual(
            force_bytes(inst.term[0].offer.text),
            force_bytes(
                "Withhold this order and any results or related objects from any provider."
            ),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].code),
            force_bytes("withhold-identified-object-and-related"),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].display),
            force_bytes(
                "Withhold the identified object and any other resources that are related to this object."
            ),
        )
        self.assertEqual(
            force_bytes(inst.term[0].type.coding[0].system),
            force_bytes("http://example.org/fhir/consent-term-type-codes"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("57016-8"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org")
        )
