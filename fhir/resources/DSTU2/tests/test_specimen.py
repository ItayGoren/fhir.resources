# -*- coding: utf-8 -*-
from datetime import datetime, timezone

from .. import fhirtypes  # noqa: F401
from .. import specimen


def test_Specimen_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "specimen-example-isolate.canonical.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type
    impl_Specimen_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_Specimen_1(inst2)


def impl_Specimen_1(inst):
    assert inst.accessionIdentifier.system == "http://lab.acme.org/specimens/2011"
    assert inst.accessionIdentifier.value == "X352356-ISO1"
    assert inst.collection.collectedDateTime == datetime(2015, 8, 16, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.collection.method.coding[0].code == "BAP"
    assert inst.collection.method.coding[0].system == "http://hl7.org/fhir/v2/0488"
    assert inst.contained[0].accessionIdentifier.system == "http://lab.acme.org/specimens/2015"
    assert inst.contained[0].accessionIdentifier.value == "X352356"
    assert inst.contained[0].collection.collectedDateTime == datetime(2011, 8, 16, 6, 15, 0, tzinfo=timezone.utc)
    assert inst.contained[0].collection.collector.display == "Patient"
    assert inst.contained[0].collection.comment[0] == "Patient dropped off specimen"
    assert inst.contained[0].collection.method.coding[0].code == "LNV"
    assert inst.contained[0].collection.method.coding[0].system == "http://hl7.org/fhir/v2/0488"
    assert inst.contained[0].id == "stool"
    assert inst.contained[0].receivedTime == datetime(2015, 8, 16, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.contained[0].status == "unavailable"
    assert inst.contained[0].subject.reference == "Patient/example"
    assert inst.contained[0].type.coding[0].code == "119339001"
    assert inst.contained[0].type.coding[0].display == "Stool specimen"
    assert inst.contained[0].type.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "isolate"
    assert inst.parent[0].reference == "#stool"
    assert inst.receivedTime == datetime(2015, 8, 18, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: isolate</p><p><b>contained</b>: </p><p><b>status</b>: available</p><p><b>type</b>: Bacterial isolate specimen <span>(Details : {SNOMED CT code '429951000124103' = '429951000124103', given as 'Bacterial isolate specimen'})</span></p><p><b>parent</b>: id: stool; status: unavailable; Stool specimen <span>(Details : {SNOMED CT code '119339001' = '119339001', given as 'Stool specimen'})</span>; Patient/example; X352356; receivedTime: 16/08/2015 5:03:00 PM</p><p><b>subject</b>: <a>Patient/example</a></p><p><b>accessionIdentifier</b>: X352356-ISO1</p><p><b>receivedTime</b>: 18/08/2015 5:03:00 PM</p><h3>Collections</h3><table><tr><td>-</td><td><b>Collector</b></td><td><b>Collected[x]</b></td><td><b>Method</b></td></tr><tr><td>*</td><td><a>Practitioner/f202</a></td><td>16/08/2015 5:03:00 PM</td><td>Plates, Blood Agar <span>(Details : {http://hl7.org/fhir/v2/0488 code 'BAP' = 'Plates, Blood Agar)</span></td></tr></table></div>"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "429951000124103"
    assert inst.type.coding[0].display == "Bacterial isolate specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"


def test_Specimen_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "specimen-example-urine.canonical.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type
    impl_Specimen_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_Specimen_2(inst2)


def impl_Specimen_2(inst):
    assert inst.accessionIdentifier.system == "http://lab.acme.org/specimens/2015"
    assert inst.accessionIdentifier.value == "X352356"
    assert inst.collection.collectedDateTime == datetime(2015, 8, 18, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.collection.collector.reference == "Practitioner/f202"
    assert inst.container[0].capacity.unit == "mls"
    assert inst.container[0].capacity.value == "50"
    assert inst.container[0].specimenQuantity.unit == "mls"
    assert inst.container[0].specimenQuantity.value == "10"
    assert inst.container[0].type.text == "Non-sterile specimen container"
    assert inst.id == "vma-urine"
    assert inst.receivedTime == datetime(2015, 8, 18, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.status == "available"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: vma-urine</p><p><b>status</b>: available</p><p><b>type</b>: Urine, Random <span>(Details : {http://hl7.org/fhir/v2/0487 code 'RANDU' = 'Urine, Random', given as 'Urine, Random'})</span></p><p><b>subject</b>: <a>Patient/example</a></p><p><b>accessionIdentifier</b>: X352356</p><p><b>receivedTime</b>: 18/08/2015 5:03:00 PM</p><h3>Collections</h3><table><tr><td>-</td><td><b>Collector</b></td><td><b>Collected[x]</b></td></tr><tr><td>*</td><td><a>Practitioner/f202</a></td><td>18/08/2015 5:03:00 PM</td></tr></table><h3>Treatments</h3><table><tr><td>-</td><td><b>Description</b></td><td><b>Procedure</b></td></tr><tr><td>*</td><td>Acidify to pH &lt; 3.0 with 6 N HCl.</td><td>Acidification <span>(Details : {http://hl7.org/fhir/v2/0373 code 'ACID' = 'Acidification)</span></td></tr></table><h3>Containers</h3><table><tr><td>-</td><td><b>Type</b></td><td><b>Capacity</b></td><td><b>SpecimenQuantity</b></td></tr><tr><td>*</td><td>Non-sterile specimen container <span>(Details )</span></td><td>50 mls</td><td>10 mls</td></tr></table></div>"
    assert inst.text.status == "generated"
    assert inst.treatment[0].description == "Acidify to pH < 3.0 with 6 N HCl."
    assert inst.treatment[0].procedure.coding[0].code == "ACID"
    assert inst.treatment[0].procedure.coding[0].system == "http://hl7.org/fhir/v2/0373"
    assert inst.type.coding[0].code == "RANDU"
    assert inst.type.coding[0].display == "Urine, Random"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/v2/0487"


def test_Specimen_3(base_settings):
    filename = base_settings["unittest_data_dir"] / "specimen-example.canonical.json"
    inst = specimen.Specimen.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Specimen" == inst.resource_type
    impl_Specimen_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Specimen" == data["resourceType"]

    inst2 = specimen.Specimen(**data)
    impl_Specimen_3(inst2)


def impl_Specimen_3(inst):
    assert inst.collection.collectedDateTime == datetime(2011, 3, 6, 6, 15, 0, tzinfo=timezone.utc)
    assert inst.collection.extension[0].url == "http://hl7.org/fhir/StructureDefinition/specimen-collectionPriority"
    assert inst.collection.extension[0].valueCodeableConcept.coding[0].code == "5"
    assert inst.collection.extension[0].valueCodeableConcept.coding[0].display == "ROUTINE"
    assert inst.collection.extension[0].valueCodeableConcept.coding[0].system == "http://example.com"
    assert inst.collection.extension[1].url == "http://hl7.org/fhir/StructureDefinition/specimen-specialHandling"
    assert inst.collection.extension[1].valueCodeableConcept.coding[0].code == "NOPERSISTP"
    assert inst.collection.extension[1].valueCodeableConcept.coding[0].display == "no collection beyond purpose of use"
    assert inst.collection.extension[1].valueCodeableConcept.coding[0].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.collection.quantity.extension[0].url == "http://hl7.org/fhir/StructureDefinition/specimen-isDryWeight"
    assert inst.collection.quantity.extension[0].valueBoolean == "False"
    assert inst.collection.quantity.unit == "mL"
    assert inst.collection.quantity.value == "6"
    assert inst.container[0].capacity.unit == "mL"
    assert inst.container[0].capacity.value == "10"
    assert inst.container[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/specimen-sequenceNumber"
    assert inst.container[0].extension[0].valueInteger == "1"
    assert inst.container[0].type.coding[0].code == "434746001"
    assert inst.container[0].type.coding[0].display == "Specimen vial"
    assert inst.container[0].type.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "specimen-example"
    assert inst.receivedTime == datetime(2011, 3, 4, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.subject.display == "Peter Patient"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: specimen-example</p><p><b>type</b>: Venous blood specimen <span>(Details : {SNOMED CT code '122555007' = '122555007', given as 'Venous blood specimen'})</span></p><p><b>subject</b>: <a>Peter Patient</a></p><p><b>receivedTime</b>: 04/03/2011 6:03:00 PM</p><h3>Collections</h3><table><tr><td>-</td><td><b>Extension</b></td><td><b>Collected[x]</b></td><td><b>Quantity</b></td></tr><tr><td>*</td><td>Extensions: Todo</td><td>06/03/2011 5:15:00 PM</td><td>6 mL</td></tr></table><h3>Treatments</h3><table><tr><td>-</td><td><b>Extension</b></td><td><b>Description</b></td><td><b>Additive</b></td></tr><tr><td>*</td><td>Extensions: Todo</td><td>Treated with anticoagulants.</td><td><a>Substance/example</a></td></tr></table><h3>Containers</h3><table><tr><td>-</td><td><b>Extension</b></td><td><b>Type</b></td><td><b>Capacity</b></td></tr><tr><td>*</td><td>Extensions: Todo</td><td>Specimen vial <span>(Details : {SNOMED CT code '434746001' = '434746001', given as 'Specimen vial'})</span></td><td>10 mL</td></tr></table></div>"
    assert inst.text.status == "generated"
    assert inst.treatment[0].additive[0].reference == "Substance/example"
    assert inst.treatment[0].description == "Treated with anticoagulants."
    assert inst.treatment[0].extension[0].url == "http://hl7.org/fhir/StructureDefinition/specimen-treatmentTime"
    assert inst.treatment[0].extension[0].valuePeriod.end == datetime(2011, 3, 4, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.treatment[0].extension[0].valuePeriod.start == datetime(2011, 3, 4, 7, 3, 0, tzinfo=timezone.utc)
    assert inst.type.coding[0].code == "122555007"
    assert inst.type.coding[0].display == "Venous blood specimen"
    assert inst.type.coding[0].system == "http://snomed.info/sct"
