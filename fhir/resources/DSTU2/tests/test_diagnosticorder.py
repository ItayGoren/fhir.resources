# -*- coding: utf-8 -*-
from datetime import date, datetime

from .. import fhirtypes  # noqa: F401
from .. import diagnosticorder


def test_DiagnosticOrder_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticorder-example-di.canonical.json"
    inst = diagnosticorder.DiagnosticOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticOrder" == inst.resource_type
    impl_DiagnosticOrder_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticOrder" == data["resourceType"]

    inst2 = diagnosticorder.DiagnosticOrder(**data)
    impl_DiagnosticOrder_1(inst2)


def impl_DiagnosticOrder_1(inst):
    assert inst.event[0].dateTime == datetime.fromisoformat("2013-05-08T09:33:27+07:00")
    assert inst.event[0].status == "requested"
    assert inst.id == "di"
    assert inst.item[0].bodySite.coding[0].code == "51185008"
    assert inst.item[0].bodySite.coding[0].display == "Thoracic structure"
    assert inst.item[0].bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.item[0].code.coding[0].code == "24627-2"
    assert inst.item[0].code.coding[0].system == "http://loinc.org"
    assert inst.item[0].code.text == "Chest CT"
    assert inst.orderer.display == "Dr. Adam Careful"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.reason[0].text == "Check for metastatic disease"
    assert inst.status == "requested"
    assert inst.subject.reference == "Patient/dicom"
    assert inst.text.div == """<div>
			<p>Chest CT - ordered May 8, 2013 by Dr. Adam Careful</p>
		</div>"""
    assert inst.text.status == "generated"


def test_DiagnosticOrder_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticorder-example-ft4.canonical.json"
    inst = diagnosticorder.DiagnosticOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticOrder" == inst.resource_type
    impl_DiagnosticOrder_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticOrder" == data["resourceType"]

    inst2 = diagnosticorder.DiagnosticOrder(**data)
    impl_DiagnosticOrder_2(inst2)


def impl_DiagnosticOrder_2(inst):
    assert inst.contained[0].accessionIdentifier.system == "http://acme.com/labs/accession-ids"
    assert inst.contained[0].accessionIdentifier.value == "20150816-00124"
    assert inst.contained[0].collection.collectedDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[0].collection.collector.reference == "Practitioner/f202"
    assert inst.contained[0].container[0].type.coding[0].code == "SST"
    assert inst.contained[0].container[0].type.coding[0].display == "Serum Separator Tube"
    assert inst.contained[0].container[0].type.coding[0].system == "http://acme.com/labs"
    assert inst.contained[0].id == "rtt"
    assert inst.contained[0].subject.reference == "Patient/pat2"
    assert inst.contained[0].type.coding[0].code == "119364003"
    assert inst.contained[0].type.coding[0].display == "Serum sample"
    assert inst.contained[0].type.coding[0].system == "http://snomed.info/sct"
    assert inst.event[0].dateTime == datetime.fromisoformat("2015-08-27T09:33:27+07:00")
    assert inst.event[0].status == "requested"
    assert inst.id == "ft4"
    assert inst.item[0].code.coding[0].code == "3024-7"
    assert inst.item[0].code.coding[0].system == "http://loinc.org"
    assert inst.item[0].code.text == "Free T4"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.specimen[0].display == "Red Top Tube"
    assert inst.specimen[0].reference == "#rtt"
    assert inst.status == "requested"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: ft4</p><p><b>contained</b>: </p><p><b>subject</b>: <a>Patient/pat2</a></p><p><b>orderer</b>: <a>Practitioner/example</a></p><p><b>specimen</b>: Red Top Tube. Generated Summary: id: rtt; Serum sample <span>(Details : {SNOMED CT code '119364003' = '119364003', given as 'Serum sample'})</span>; Patient/pat2; 20150816-00124</p><p><b>status</b>: requested</p><h3>Events</h3><table><tr><td>-</td><td><b>Status</b></td><td><b>DateTime</b></td></tr><tr><td>*</td><td>requested</td><td>27/08/2015 9:33:27 AM</td></tr></table><h3>Items</h3><table><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Free T4 <span>(Details : {LOINC code '3024-7' = 'Thyroxine (T4) free [Mass/volume] in Serum or Plasma)</span></td></tr></table></div>"
    assert inst.text.status == "generated"


def test_DiagnosticOrder_3(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticorder-example.canonical.json"
    inst = diagnosticorder.DiagnosticOrder.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticOrder" == inst.resource_type
    impl_DiagnosticOrder_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticOrder" == data["resourceType"]

    inst2 = diagnosticorder.DiagnosticOrder(**data)
    impl_DiagnosticOrder_3(inst2)


def impl_DiagnosticOrder_3(inst):
    assert inst.event[0].dateTime == datetime.fromisoformat("2013-05-02T16:16:00-07:00")
    assert inst.event[0].status == "requested"
    assert inst.event[1].dateTime == datetime.fromisoformat("2013-05-06T11:20:00-07:00")
    assert inst.event[1].status == "rejected"
    assert inst.extension[0].url == "http://hl7.org/fhir/StructureDefinition/diagnosticorder-reason"
    assert inst.extension[0].valueCodeableConcept.coding[0].code == "PHY"
    assert inst.extension[0].valueCodeableConcept.coding[0].display == "Physician request"
    assert inst.extension[0].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/v3/ActReason"
    assert inst.extension[1].url == "http://hl7.org/fhir/StructureDefinition/diagnosticorder-reasonRejected"
    assert inst.extension[1].valueCodeableConcept.coding[0].code == "NON-AVAIL"
    assert inst.extension[1].valueCodeableConcept.coding[0].display == "patient not-available"
    assert inst.extension[1].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/v3/ActReason"
    assert inst.id == "diagnosticorder-example"
    assert inst.identifier[0].system == "urn:oid:1.3.4.5.6.7"
    assert inst.identifier[0].type.text == "Placer"
    assert inst.identifier[0].value == "2345234234234"
    assert inst.item[0].code.coding[0].code == "57698-3"
    assert inst.item[0].code.coding[0].system == "http://loinc.org"
    assert inst.item[0].code.text == "Lipid panel with direct LDL - Serum or Plasma"
    assert inst.orderer.reference == "Practitioner/example"
    assert inst.status == "rejected"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == """<div>
        Example Diagnostic Order
        </div>"""
    assert inst.text.status == "generated"
