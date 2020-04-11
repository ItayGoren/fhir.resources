# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Provenance
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

from .. import provenance
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ProvenanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Provenance", js["resourceType"])
        return provenance.Provenance(js)

    def testProvenance1(self):
        inst = self.instantiate_from("provenance-example-sig.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance1(inst)

        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance1(inst2)

    def implProvenance1(self, inst):
        self.assertEqual(force_bytes(inst.activity.code), force_bytes("AU"))
        self.assertEqual(
            force_bytes(inst.activity.display), force_bytes("authenticated")
        )
        self.assertEqual(
            force_bytes(inst.activity.system),
            force_bytes("http://hl7.org/fhir/v3/DocumentCompletion"),
        )
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].code), force_bytes("VERF")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].system),
            force_bytes("http://www.hl7.org/fhir/contractsignertypecodes"),
        )
        self.assertEqual(
            force_bytes(inst.agent[0].whoUri), force_bytes("mailto://hhd@ssa.gov")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("signature"))
        self.assertEqual(force_bytes(inst.reason[0].code), force_bytes("TREAT"))
        self.assertEqual(force_bytes(inst.reason[0].display), force_bytes("treatment"))
        self.assertEqual(
            force_bytes(inst.reason[0].system),
            force_bytes("http://hl7.org/fhir/v3/ActReason"),
        )
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-27T08:39:24+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-27T08:39:24+10:00")
        self.assertEqual(force_bytes(inst.signature[0].blob), force_bytes("Li4u"))
        self.assertEqual(
            force_bytes(inst.signature[0].contentType),
            force_bytes("application/signature+xml"),
        )
        self.assertEqual(
            force_bytes(inst.signature[0].type[0].code),
            force_bytes("1.2.840.10065.1.12.1.5"),
        )
        self.assertEqual(
            force_bytes(inst.signature[0].type[0].display),
            force_bytes("Verification Signature"),
        )
        self.assertEqual(
            force_bytes(inst.signature[0].type[0].system),
            force_bytes("urn:iso-astm:E1762-95:2013"),
        )
        self.assertEqual(
            inst.signature[0].when.date, FHIRDate("2015-08-27T08:39:24+10:00").date
        )
        self.assertEqual(inst.signature[0].when.as_json(), "2015-08-27T08:39:24+10:00")
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">procedure record authored on 27-June 2015 by Harold Hippocrates, MD Content extracted from Referral received 26-June</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProvenance2(self):
        inst = self.instantiate_from("provenance-consent-signature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance2(inst)

        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance2(inst2)

    def implProvenance2(self, inst):
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].code), force_bytes("AUT")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/ParticipationType"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-signature"))
        self.assertEqual(inst.recorded.date, FHIRDate("2016-05-26T00:41:10-04:00").date)
        self.assertEqual(inst.recorded.as_json(), "2016-05-26T00:41:10-04:00")
        self.assertEqual(
            force_bytes(inst.signature[0].blob),
            force_bytes("dGhpcyBibG9iIGlzIHNuaXBwZWQ="),
        )
        self.assertEqual(
            force_bytes(inst.signature[0].contentType),
            force_bytes("application/signature+xml"),
        )
        self.assertEqual(
            force_bytes(inst.signature[0].type[0].code),
            force_bytes("1.2.840.10065.1.12.1.1"),
        )
        self.assertEqual(
            force_bytes(inst.signature[0].type[0].display),
            force_bytes("Author's Signature"),
        )
        self.assertEqual(
            force_bytes(inst.signature[0].type[0].system),
            force_bytes("urn:iso-astm:E1762-95:2013"),
        )
        self.assertEqual(
            inst.signature[0].when.date, FHIRDate("2016-05-26T00:41:10-04:00").date
        )
        self.assertEqual(inst.signature[0].when.as_json(), "2016-05-26T00:41:10-04:00")
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProvenance3(self):
        inst = self.instantiate_from("provenance-example-cwl.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance3(inst)

        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance3(inst2)

    def implProvenance3(self, inst):
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].code), force_bytes("AUT")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/ParticipationType"),
        )
        self.assertEqual(force_bytes(inst.entity[0].role), force_bytes("source"))
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.type.coding[0].code),
            force_bytes("CWL"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.type.coding[0].display),
            force_bytes("lobSTR"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.type.coding[0].system),
            force_bytes("https://github.com/common-workflow-language/workflows"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.value),
            force_bytes(
                "https://github.com/common-workflow-language/workflows/blob/master/workflows/lobSTR/lobSTR-workflow.cwl"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-cwl"))
        self.assertEqual(inst.period.start.date, FHIRDate("2016-11-30").date)
        self.assertEqual(inst.period.start.as_json(), "2016-11-30")
        self.assertEqual(
            force_bytes(inst.reason[0].display),
            force_bytes(
                "profiling Short Tandem Repeats (STRs) from high throughput sequencing data."
            ),
        )
        self.assertEqual(inst.recorded.date, FHIRDate("2016-12-01T08:12:14+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2016-12-01T08:12:14+10:00")
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProvenance4(self):
        inst = self.instantiate_from("provenance-example-biocompute-object.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance4(inst)

        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance4(inst2)

    def implProvenance4(self, inst):
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].code), force_bytes("AUT")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/ParticipationType"),
        )
        self.assertEqual(force_bytes(inst.entity[0].role), force_bytes("source"))
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.type.coding[0].code),
            force_bytes("biocompute"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.type.coding[0].display),
            force_bytes("obj.1001"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.type.coding[0].system),
            force_bytes("https://hive.biochemistry.gwu.edu"),
        )
        self.assertEqual(
            force_bytes(inst.entity[0].whatIdentifier.value),
            force_bytes(
                "https://hive.biochemistry.gwu.edu/cgi-bin/prd/htscsrs/servlet.cgi?pageid=bcoexample_1"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-biocompute-object"))
        self.assertEqual(inst.period.start.date, FHIRDate("2017-06-06").date)
        self.assertEqual(inst.period.start.as_json(), "2017-06-06")
        self.assertEqual(
            force_bytes(inst.reason[0].display),
            force_bytes("antiviral resistance detection"),
        )
        self.assertEqual(inst.recorded.date, FHIRDate("2016-06-09T08:12:14+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2016-06-09T08:12:14+10:00")
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProvenance5(self):
        inst = self.instantiate_from("provenance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance5(inst)

        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance5(inst2)

    def implProvenance5(self, inst):
        self.assertEqual(force_bytes(inst.agent[0].onBehalfOfUri), force_bytes("#a1"))
        self.assertEqual(
            force_bytes(inst.agent[0].relatedAgentType.text), force_bytes("used")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].code), force_bytes("AUT")
        )
        self.assertEqual(
            force_bytes(inst.agent[0].role[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/ParticipationType"),
        )
        self.assertEqual(force_bytes(inst.agent[1].id), force_bytes("a1"))
        self.assertEqual(
            force_bytes(inst.agent[1].role[0].coding[0].code), force_bytes("DEV")
        )
        self.assertEqual(
            force_bytes(inst.agent[1].role[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/ParticipationType"),
        )
        self.assertEqual(force_bytes(inst.entity[0].role), force_bytes("source"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(inst.period.end.date, FHIRDate("2015-06-28").date)
        self.assertEqual(inst.period.end.as_json(), "2015-06-28")
        self.assertEqual(inst.period.start.date, FHIRDate("2015-06-27").date)
        self.assertEqual(inst.period.start.as_json(), "2015-06-27")
        self.assertEqual(
            force_bytes(inst.policy[0]), force_bytes("http://acme.com/fhir/Consent/25")
        )
        self.assertEqual(force_bytes(inst.reason[0].code), force_bytes("3457005"))
        self.assertEqual(force_bytes(inst.reason[0].display), force_bytes("Referral"))
        self.assertEqual(
            force_bytes(inst.reason[0].system), force_bytes("http://snomed.info/sct")
        )
        self.assertEqual(inst.recorded.date, FHIRDate("2015-06-27T08:39:24+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2015-06-27T08:39:24+10:00")
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">procedure record authored on 27-June 2015 by Harold Hippocrates, MD Content extracted from XDS managed CDA Referral received 26-June</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
