# -*- coding: utf-8 -*-
from datetime import date, datetime
from decimal import Decimal

from .. import fhirtypes  # noqa: F401
from .. import diagnosticreport


def test_DiagnosticReport_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-dxa.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_1(inst2)


def impl_DiagnosticReport_1(inst):
    assert inst.code.coding[0].code == "38269-7"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "DXA BONE DENSITOMETRY"
    assert inst.codedDiagnosis[0].coding[0].code == "391040000"
    assert inst.codedDiagnosis[0].coding[0].display == "At risk of osteoporotic fracture"
    assert inst.codedDiagnosis[0].coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].bodySite.coding[0].code == "71341001:272741003=7771000"
    assert inst.contained[0].bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].code.coding[0].code == "24701-5"
    assert inst.contained[0].code.coding[0].display == "Femur DXA Bone density"
    assert inst.contained[0].code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].id == "r1"
    assert inst.contained[0].performer[0].display == "Acme Imaging Diagnostics"
    assert inst.contained[0].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[0].status == "final"
    assert inst.contained[0].subject.reference == "Patient/pat2"
    assert inst.contained[0].valueQuantity.code == "g/cm-2"
    assert inst.contained[0].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[0].valueQuantity.unit == "g/cm²"
    assert inst.contained[0].valueQuantity.value == Decimal("0.887")
    assert inst.effectiveDateTime == date.fromisoformat("2008-06-17")
    assert inst.id == "102"
    assert inst.issued == datetime.fromisoformat("2008-06-18T09:23:00+10:00")
    assert inst.performer.display == "Acme Imaging Diagnostics"
    assert inst.performer.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.result[0].reference == "#r1"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.div == """<div>
			
      
      <h2>DXA BONE DENSITOMETRY</h2>
			
      
      <table>
				
        
        <tr>
					
          
          <td>NAME</td>
					
          
          <td>XXXXXXX</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>DOB</td>
					
          
          <td>10/02/1974</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>REFERRING DR</td>
					
          
          <td>Smith, Jane</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>INDICATIONS</td>
					
          
          <td>Early menopause on estrogen levels. No period  for 18 months</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>PROCEDURE</td>
					
          
          <td>Dual energy x-ray absorptiometry (DEXA)</td>
				
        
        </tr>
			
      
      </table>
			
      
      <h3>Bone Mineral Density</h3>
			
      
      <table>
				
        
        <tr>
					
          
          <td>Scan Type</td>
					
          
          <td>Region</td>
					
          
          <td>Measured</td>
					
          
          <td>Age</td>
					
          
          <td>BMD</td>
					
          
          <td>T-Score</td>
					
          
          <td>Z-Score</td>
					
          
          <td>?BMD(g/cm2)</td>
					
          
          <td>?BMD(%)</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>AP Spine</td>
					
          
          <td>L1-L4</td>
					
          
          <td>17/06/2008</td>
					
          
          <td>34.4</td>
					
          
          <td>1.148 g/cm²</td>
					
          
          <td>-0.4</td>
					
          
          <td>-0.5</td>
					
          
          <td>-</td>
					
          
          <td>-</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>Left Femur</td>
					
          
          <td>Neck</td>
					
          
          <td>17/06/2008</td>
					
          
          <td>34.4</td>
					
          
          <td>0.891 g/cm²</td>
					
          
          <td>-1.0</td>
					
          
          <td>-0.9</td>
					
          
          <td>-</td>
					
          
          <td>-</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>Left Femur</td>
					
          
          <td>Total</td>
					
          
          <td>17/06/2008</td>
					
          
          <td>34.4</td>
					
          
          <td>0.887 g/cm²</td>
					
          
          <td>-1.2</td>
					
          
          <td>-1.3</td>
					
          
          <td>-</td>
					
          
          <td>-</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>Right Femur</td>
					
          
          <td>Neck</td>
					
          
          <td>17/06/2008</td>
					
          
          <td>34.4</td>
					
          
          <td>0.885 g/cm²</td>
					
          
          <td>-1.0</td>
					
          
          <td>-1.0</td>
					
          
          <td>-</td>
					
          
          <td>-</td>
				
        
        </tr>
				
        
        <tr>
					
          
          <td>Right Femur</td>
					
          
          <td>Total</td>
					
          
          <td>17/06/2008</td>
					
          
          <td>34.4</td>
					
          
          <td>0.867 g/cm²</td>
					
          
          <td>-1.4</td>
					
          
          <td>-1.4</td>
					
          
          <td>-</td>
					
          
          <td>-</td>
				
        
        </tr>
			
      
      </table>
			
      
      <p>Assessment:</p>
			
      
      <ul>
				
        
        <li>The Spine L1-L4 BMD is normal.</li>
				
        
        <li>The Left Femur Neck BMD is in the osteopenic range. Relative fracture risk is about 2.</li>
				
        
        <li>The Left Femur Total BMD is in the osteopenic range. Relative fracture risk is about 2.</li>
				
        
        <li>The Right Femur Neck BMD is in the osteopenic range. Relative fracture risk is about 2.</li>
				
        
        <li>The Right Femur Total BMD is in the osteopenic range. Relative fracture risk is about 2.</li>
			
      
      </ul>
			
      
      <p>
				
        
        <b>COMMENT</b>
			
      
      </p>
			
      
      <p>Osteopenia on measured BMD. The estimated 10-year probability of fracture based on present age, gender and measured BMD is less than 10%. This absolute fracture risk remains low. A follow-up assessment may be considered in 2 to 3 years to monitor the trend in BMD.</p>
			
      
      <p>Thank you for your referral.  Dr Peter Ng  17/06/2008</p>
			
      
      <pre>
Note:
WHO classification of osteoporosis (WHO Technical Report Series 1994: 843)
- Normal: T-score equal to -1.0 s.d. or higher
- Osteopenia: T-score  between -1.0 and -2.5 s.d.
- Osteoporosis: T-score equal to -2.5 s.d. or lower
- Severe/Established osteoporosis: Osteoporosis with one or more fragility fracture.
T-score: The number of s.d. from the mean BMD for a gender-matched young adult population.
Z-score: The number of s.d. from the mean BMD for an age-, weight- and gender-matched population.
Reference for 10-year probability of fracture risk: Kanis JA, Johnell O, Oden A, Dawson A,  De Laet C, Jonsson B. Ten year probabilities of osteoporotic fractures according to BMD and diagnostic thresholds. Osteoporos.Int. 2001;12(12):989-995.
GE LUNAR PRODIGY DENSITOMETER
</pre>
		
    
    </div>"""
    assert inst.text.status == "generated"


def test_DiagnosticReport_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-f001-bloodexam.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_2(inst2)


def impl_DiagnosticReport_2(inst):
    assert inst.category.coding[0].code == "252275004"
    assert inst.category.coding[0].display == "Haematology test"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "HM"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "58410-2"
    assert inst.code.coding[0].display == "Complete blood count (hemogram) panel - Blood by Automated count"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.conclusion == "Core lab"
    assert inst.contained[0].encounter.reference == "Encounter/f001"
    assert inst.contained[0].id == "req"
    assert inst.contained[0].identifier[0].system == "http://www.bmc.nl/zorgportal/identifiers/labresults"
    assert inst.contained[0].identifier[0].use == "official"
    assert inst.contained[0].identifier[0].value == "L2381"
    assert inst.contained[0].item[0].bodySite.coding[0].code == "14975008"
    assert inst.contained[0].item[0].bodySite.coding[0].display == "Forearm structure"
    assert inst.contained[0].item[0].bodySite.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[0].item[0].code.coding[0].code == "58410-2"
    assert inst.contained[0].item[0].code.coding[0].display == "Complete blood count (hemogram) panel - Blood by Automated count"
    assert inst.contained[0].item[0].code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].orderer.display == "E.van den Broek"
    assert inst.contained[0].orderer.reference == "Practitioner/f001"
    assert inst.contained[0].reason[0].text == "patient almost fainted during procedure"
    assert inst.contained[0].subject.display == "P. van den Heuvel"
    assert inst.contained[0].subject.reference == "Patient/f001"
    assert inst.effectiveDateTime == date.fromisoformat("2013-04-02")
    assert inst.id == "f001"
    assert inst.identifier[0].system == "http://www.bmc.nl/zorgportal/identifiers/reports"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "nr1239044"
    assert inst.issued == datetime.fromisoformat("2013-05-15T19:32:52+01:00")
    assert inst.performer.display == "Burgers University Medical Centre"
    assert inst.performer.reference == "Organization/f001"
    assert inst.request[0].reference == "#req"
    assert inst.result[0].reference == "Observation/f001"
    assert inst.result[1].reference == "Observation/f002"
    assert inst.result[2].reference == "Observation/f003"
    assert inst.result[3].reference == "Observation/f004"
    assert inst.result[4].reference == "Observation/f005"
    assert inst.status == "final"
    assert inst.subject.display == "P. van den Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f001</p><p><b>contained</b>: </p><p><b>identifier</b>: nr1239044 (OFFICIAL)</p><p><b>status</b>: final</p><p><b>category</b>: Haematology test <span>(Details : {SNOMED CT code '252275004' = '252275004', given as 'Haematology test'}; {http://hl7.org/fhir/v2/0074 code 'HM' = 'Hematology)</span></p><p><b>code</b>: Complete blood count (hemogram) panel - Blood by Automated count <span>(Details : {LOINC code '58410-2' = 'Complete blood count (hemogram) panel - Blood by Automated count', given as 'Complete blood count (hemogram) panel - Blood by Automated count'})</span></p><p><b>subject</b>: <a>P. van den Heuvel</a></p><p><b>effective</b>: 02/04/2013</p><p><b>issued</b>: 15/05/2013 7:32:52 PM</p><p><b>performer</b>: <a>Burgers University Medical Centre</a></p><p><b>request</b>: id: req; P. van den Heuvel; L2381 (OFFICIAL); patient almost fainted during procedure <span>(Details )</span></p><p><b>result</b>: </p><ul><li><a>Observation/f001</a></li><li><a>Observation/f002</a></li><li><a>Observation/f003</a></li><li><a>Observation/f004</a></li><li><a>Observation/f005</a></li></ul><p><b>conclusion</b>: Core lab</p></div>"
    assert inst.text.status == "generated"


def test_DiagnosticReport_3(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-f201-brainct.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_3(inst2)


def impl_DiagnosticReport_3(inst):
    assert inst.category.coding[0].code == "394914008"
    assert inst.category.coding[0].display == "Radiology"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "RAD"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "429858000"
    assert inst.code.coding[0].display == "Computed tomography (CT) of head and neck"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "CT of head-neck"
    assert inst.codedDiagnosis[0].coding[0].code == "188340000"
    assert inst.codedDiagnosis[0].coding[0].display == "Malignant tumor of craniopharyngeal duct"
    assert inst.codedDiagnosis[0].coding[0].system == "http://snomed.info/sct"
    assert inst.conclusion == "CT brains: large tumor sphenoid/clivus."
    assert inst.effectiveDateTime == datetime.fromisoformat("2012-12-01T12:00:00+01:00")
    assert inst.id == "f201"
    assert inst.imagingStudy[0].display == "HEAD and NECK CT DICOM imaging study"
    assert inst.issued == datetime.fromisoformat("2012-12-01T12:00:00+01:00")
    assert inst.performer.display == "Blijdorp MC"
    assert inst.performer.reference == "Organization/f203"
    assert inst.status == "final"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f201</p><p><b>status</b>: final</p><p><b>category</b>: Radiology <span>(Details : {SNOMED CT code '394914008' = '394914008', given as 'Radiology'}; {http://hl7.org/fhir/v2/0074 code 'RAD' = 'Radiology)</span></p><p><b>code</b>: CT of head-neck <span>(Details : {SNOMED CT code '429858000' = '429858000', given as 'Computed tomography (CT) of head and neck'})</span></p><p><b>subject</b>: <a>Roel</a></p><p><b>effective</b>: 01/12/2012 12:00:00 PM</p><p><b>issued</b>: 01/12/2012 12:00:00 PM</p><p><b>performer</b>: <a>Blijdorp MC</a></p><p><b>imagingStudy</b>: HEAD and NECK CT DICOM imaging study</p><p><b>conclusion</b>: CT brains: large tumor sphenoid/clivus.</p><p><b>codedDiagnosis</b>: Malignant tumor of craniopharyngeal duct <span>(Details : {SNOMED CT code '188340000' = '188340000', given as 'Malignant tumor of craniopharyngeal duct'})</span></p></div>"
    assert inst.text.status == "generated"


def test_DiagnosticReport_4(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-f202-bloodculture.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_4(inst2)


def impl_DiagnosticReport_4(inst):
    assert inst.category.coding[0].code == "15220000"
    assert inst.category.coding[0].display == "Laboratory test"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "LAB"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "104177005"
    assert inst.code.coding[0].display == "Blood culture for bacteria, including anaerobic screen"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.codedDiagnosis[0].coding[0].code == "428763004"
    assert inst.codedDiagnosis[0].coding[0].display == "Bacteremia due to staphylococcus"
    assert inst.codedDiagnosis[0].coding[0].system == "http://snomed.info/sct"
    assert inst.conclusion == "Blood culture tested positive on staphylococcus aureus"
    assert inst.contained[0].encounter.display == "Roel's encounter on March eleventh 2013"
    assert inst.contained[0].encounter.reference == "Encounter/f203"
    assert inst.contained[0].id == "req"
    assert inst.contained[0].orderer.display == "Dokter Bronsig"
    assert inst.contained[0].orderer.reference == "Practitioner/f201"
    assert inst.contained[0].subject.display == "Roel"
    assert inst.contained[0].subject.reference == "Patient/f201"
    assert inst.effectiveDateTime == datetime.fromisoformat("2013-03-11T03:45:00+01:00")
    assert inst.id == "f202"
    assert inst.issued == datetime.fromisoformat("2013-03-11T10:28:00+01:00")
    assert inst.performer.display == "AUMC"
    assert inst.performer.reference == "Organization/f201"
    assert inst.request[0].reference == "#req"
    assert inst.result[0].display == "Results for staphylococcus analysis on Roel's blood culture"
    assert inst.result[0].reference == "Observation/f206"
    assert inst.status == "final"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f202</p><p><b>contained</b>: </p><p><b>status</b>: final</p><p><b>category</b>: Laboratory test <span>(Details : {SNOMED CT code '15220000' = '15220000', given as 'Laboratory test'}; {http://hl7.org/fhir/v2/0074 code 'LAB' = 'Laboratory)</span></p><p><b>code</b>: Blood culture for bacteria, including anaerobic screen <span>(Details : {SNOMED CT code '104177005' = '104177005', given as 'Blood culture for bacteria, including anaerobic screen'})</span></p><p><b>subject</b>: <a>Roel</a></p><p><b>effective</b>: 11/03/2013 3:45:00 AM</p><p><b>issued</b>: 11/03/2013 10:28:00 AM</p><p><b>performer</b>: <a>AUMC</a></p><p><b>request</b>: id: req; Roel</p><p><b>result</b>: <a>Results for staphylococcus analysis on Roel's blood culture</a></p><p><b>conclusion</b>: Blood culture tested positive on staphylococcus aureus</p><p><b>codedDiagnosis</b>: Bacteremia due to staphylococcus <span>(Details : {SNOMED CT code '428763004' = '428763004', given as 'Bacteremia due to staphylococcus'})</span></p></div>"
    assert inst.text.status == "generated"


def test_DiagnosticReport_5(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-ghp.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_5(inst2)


def impl_DiagnosticReport_5(inst):
    assert inst.code.coding[0].code == "GHP"
    assert inst.code.coding[0].display == "General Health Profile"
    assert inst.code.coding[0].system == "http://acme.com/labs/reports"
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
    assert inst.contained[1].accessionIdentifier.system == "http://acme.com/labs/accession-ids"
    assert inst.contained[1].accessionIdentifier.value == "20150816-00124"
    assert inst.contained[1].collection.collectedDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[1].collection.collector.reference == "Practitioner/f202"
    assert inst.contained[1].container[0].type.coding[0].code == "LTT"
    assert inst.contained[1].container[0].type.coding[0].display == "Lavender Top Tube"
    assert inst.contained[1].container[0].type.coding[0].system == "http://acme.com/labs"
    assert inst.contained[1].id == "ltt"
    assert inst.contained[1].subject.reference == "Patient/pat2"
    assert inst.contained[1].type.coding[0].code == "445295009"
    assert inst.contained[1].type.coding[0].display == "Blood specimen with EDTA"
    assert inst.contained[1].type.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[2].accessionIdentifier.system == "http://acme.com/labs/accession-ids"
    assert inst.contained[2].accessionIdentifier.value == "20150816-00124"
    assert inst.contained[2].collection.collectedDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[2].collection.collector.reference == "Practitioner/f202"
    assert inst.contained[2].container[0].type.coding[0].code == "UCUP"
    assert inst.contained[2].container[0].type.coding[0].display == "100mL sterile cup"
    assert inst.contained[2].container[0].type.coding[0].system == "http://acme.com/labs"
    assert inst.contained[2].id == "urine"
    assert inst.contained[2].subject.reference == "Patient/pat2"
    assert inst.contained[2].type.coding[0].code == "122575003"
    assert inst.contained[2].type.coding[0].display == "Urine specimen"
    assert inst.contained[2].type.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[3].code.coding[0].code == "58410-2"
    assert inst.contained[3].code.coding[0].display == "Complete blood count (hemogram) panel - Blood by Automated count"
    assert inst.contained[3].code.coding[0].system == "http://loinc.org"
    assert inst.contained[3].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[3].id == "p2"
    assert inst.contained[3].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[3].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[3].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[3].related[0].target.reference == "#r1"
    assert inst.contained[3].related[0].type == "has-member"
    assert inst.contained[3].related[1].target.reference == "#r2"
    assert inst.contained[3].related[1].type == "has-member"
    assert inst.contained[3].related[2].target.reference == "#r3"
    assert inst.contained[3].related[2].type == "has-member"
    assert inst.contained[3].related[3].target.reference == "#r4"
    assert inst.contained[3].related[3].type == "has-member"
    assert inst.contained[3].related[4].target.reference == "#r5"
    assert inst.contained[3].related[4].type == "has-member"
    assert inst.contained[3].related[5].target.reference == "#r6"
    assert inst.contained[3].related[5].type == "has-member"
    assert inst.contained[3].related[6].target.reference == "#r7"
    assert inst.contained[3].related[6].type == "has-member"
    assert inst.contained[3].related[7].target.reference == "#r8"
    assert inst.contained[3].related[7].type == "has-member"
    assert inst.contained[3].related[8].target.reference == "#r9"
    assert inst.contained[3].related[8].type == "has-member"
    assert inst.contained[3].related[9].target.reference == "#r10"
    assert inst.contained[3].related[9].type == "has-member"
    assert inst.contained[3].related[10].target.reference == "#r11"
    assert inst.contained[3].related[10].type == "has-member"
    assert inst.contained[3].related[11].target.reference == "#r12"
    assert inst.contained[3].related[11].type == "has-member"
    assert inst.contained[3].related[12].target.reference == "#r13"
    assert inst.contained[3].related[12].type == "has-member"
    assert inst.contained[3].related[13].target.reference == "#r14"
    assert inst.contained[3].related[13].type == "has-member"
    assert inst.contained[3].related[14].target.reference == "#r15"
    assert inst.contained[3].related[14].type == "has-member"
    assert inst.contained[3].related[15].target.reference == "#r16"
    assert inst.contained[3].related[15].type == "has-member"
    assert inst.contained[3].related[16].target.reference == "#r17"
    assert inst.contained[3].related[16].type == "has-member"
    assert inst.contained[3].specimen.display == "Lavender Top Tube"
    assert inst.contained[3].specimen.reference == "#ltt"
    assert inst.contained[3].status == "final"
    assert inst.contained[4].code.coding[0].code == "718-7"
    assert inst.contained[4].code.coding[0].display == "Hemoglobin [Mass/volume] in Blood"
    assert inst.contained[4].code.coding[0].system == "http://loinc.org"
    assert inst.contained[4].code.text == "Haemoglobin"
    assert inst.contained[4].id == "r1"
    assert inst.contained[4].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[4].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[4].referenceRange[0].high.code == "g/L"
    assert inst.contained[4].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[4].referenceRange[0].high.unit == "g/L"
    assert inst.contained[4].referenceRange[0].high.value == Decimal("180")
    assert inst.contained[4].referenceRange[0].low.code == "g/L"
    assert inst.contained[4].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[4].referenceRange[0].low.unit == "g/L"
    assert inst.contained[4].referenceRange[0].low.value == Decimal("135")
    assert inst.contained[4].status == "final"
    assert inst.contained[4].subject.reference == "Patient/pat2"
    assert inst.contained[4].valueQuantity.code == "g/L"
    assert inst.contained[4].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[4].valueQuantity.unit == "g/L"
    assert inst.contained[4].valueQuantity.value == Decimal("176")
    assert inst.contained[5].code.coding[0].code == "789-8"
    assert inst.contained[5].code.coding[0].display == "Erythrocytes [#/volume] in Blood by Automated count"
    assert inst.contained[5].code.coding[0].system == "http://loinc.org"
    assert inst.contained[5].code.text == "Red Cell Count"
    assert inst.contained[5].id == "r2"
    assert inst.contained[5].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[5].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[5].referenceRange[0].high.code == "10*12/L"
    assert inst.contained[5].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[5].referenceRange[0].high.unit == "x10*12/L"
    assert inst.contained[5].referenceRange[0].high.value == Decimal("6.0")
    assert inst.contained[5].referenceRange[0].low.code == "10*12/L"
    assert inst.contained[5].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[5].referenceRange[0].low.unit == "x10*12/L"
    assert inst.contained[5].referenceRange[0].low.value == Decimal("4.2")
    assert inst.contained[5].status == "final"
    assert inst.contained[5].subject.reference == "Patient/pat2"
    assert inst.contained[5].valueQuantity.code == "10*12/L"
    assert inst.contained[5].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[5].valueQuantity.unit == "x10*12/L"
    assert inst.contained[5].valueQuantity.value == Decimal("5.9")
    assert inst.contained[6].code.coding[0].code == "4544-3"
    assert inst.contained[6].code.coding[0].display == "Hematocrit [Volume Fraction] of Blood by Automated count"
    assert inst.contained[6].code.coding[0].system == "http://loinc.org"
    assert inst.contained[6].code.text == "Haematocrit"
    assert inst.contained[6].id == "r3"
    assert inst.contained[6].interpretation.coding[0].code == "H"
    assert inst.contained[6].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[6].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[6].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[6].referenceRange[0].high.unit == "%"
    assert inst.contained[6].referenceRange[0].high.value == Decimal("52")
    assert inst.contained[6].referenceRange[0].low.unit == "%"
    assert inst.contained[6].referenceRange[0].low.value == Decimal("38")
    assert inst.contained[6].status == "final"
    assert inst.contained[6].subject.reference == "Patient/pat2"
    assert inst.contained[6].valueQuantity.unit == "%"
    assert inst.contained[6].valueQuantity.value == Decimal("55")
    assert inst.contained[7].code.coding[0].code == "787-2"
    assert inst.contained[7].code.coding[0].display == "Erythrocyte mean corpuscular volume [Entitic volume] by Automated count"
    assert inst.contained[7].code.coding[0].system == "http://loinc.org"
    assert inst.contained[7].code.text == "Mean Cell Volume"
    assert inst.contained[7].id == "r4"
    assert inst.contained[7].interpretation.coding[0].code == "H"
    assert inst.contained[7].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[7].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[7].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[7].referenceRange[0].high.code == "fL"
    assert inst.contained[7].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[7].referenceRange[0].high.unit == "fL"
    assert inst.contained[7].referenceRange[0].high.value == Decimal("98")
    assert inst.contained[7].referenceRange[0].low.code == "fL"
    assert inst.contained[7].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[7].referenceRange[0].low.unit == "fL"
    assert inst.contained[7].referenceRange[0].low.value == Decimal("80")
    assert inst.contained[7].status == "final"
    assert inst.contained[7].subject.reference == "Patient/pat2"
    assert inst.contained[7].valueQuantity.code == "fL"
    assert inst.contained[7].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[7].valueQuantity.unit == "fL"
    assert inst.contained[7].valueQuantity.value == Decimal("99")
    assert inst.contained[8].code.coding[0].code == "785-6"
    assert inst.contained[8].code.coding[0].display == "Erythrocyte mean corpuscular hemoglobin [Entitic mass] by Automated count"
    assert inst.contained[8].code.coding[0].system == "http://loinc.org"
    assert inst.contained[8].code.text == "Mean Cell Haemoglobin"
    assert inst.contained[8].id == "r5"
    assert inst.contained[8].interpretation.coding[0].code == "H"
    assert inst.contained[8].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[8].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[8].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[8].referenceRange[0].high.code == "pg"
    assert inst.contained[8].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[8].referenceRange[0].high.unit == "pg"
    assert inst.contained[8].referenceRange[0].high.value == Decimal("35")
    assert inst.contained[8].referenceRange[0].low.code == "pg"
    assert inst.contained[8].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[8].referenceRange[0].low.unit == "pg"
    assert inst.contained[8].referenceRange[0].low.value == Decimal("27")
    assert inst.contained[8].status == "final"
    assert inst.contained[8].subject.reference == "Patient/pat2"
    assert inst.contained[8].valueQuantity.code == "pg"
    assert inst.contained[8].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[8].valueQuantity.unit == "pg"
    assert inst.contained[8].valueQuantity.value == Decimal("36")
    assert inst.contained[9].code.coding[0].code == "777-3"
    assert inst.contained[9].code.coding[0].display == "Platelets [#/volume] in Blood by Automated count"
    assert inst.contained[9].code.coding[0].system == "http://loinc.org"
    assert inst.contained[9].code.text == "Platelet Count"
    assert inst.contained[9].id == "r6"
    assert inst.contained[9].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[9].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[9].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[9].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[9].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[9].referenceRange[0].high.value == Decimal("450")
    assert inst.contained[9].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[9].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[9].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[9].referenceRange[0].low.value == Decimal("150")
    assert inst.contained[9].status == "final"
    assert inst.contained[9].subject.reference == "Patient/pat2"
    assert inst.contained[9].valueQuantity.code == "10*9/L"
    assert inst.contained[9].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[9].valueQuantity.unit == "x10*9/L"
    assert inst.contained[9].valueQuantity.value == Decimal("444")
    assert inst.contained[10].code.coding[0].code == "6690-2"
    assert inst.contained[10].code.coding[0].display == "Leukocytes [#/volume] in Blood by Automated count"
    assert inst.contained[10].code.coding[0].system == "http://loinc.org"
    assert inst.contained[10].code.text == "White Cell Count"
    assert inst.contained[10].id == "r7"
    assert inst.contained[10].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[10].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[10].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[10].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[10].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[10].referenceRange[0].high.value == Decimal("11.0")
    assert inst.contained[10].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[10].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[10].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[10].referenceRange[0].low.value == Decimal("4.0")
    assert inst.contained[10].status == "final"
    assert inst.contained[10].subject.reference == "Patient/pat2"
    assert inst.contained[10].valueQuantity.code == "10*9/L"
    assert inst.contained[10].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[10].valueQuantity.unit == "x10*9/L"
    assert inst.contained[10].valueQuantity.value == Decimal("4.6")
    assert inst.contained[11].code.coding[0].code == "770-8"
    assert inst.contained[11].code.coding[0].display == "Neutrophils/100 leukocytes in Blood by Automated count"
    assert inst.contained[11].code.coding[0].system == "http://loinc.org"
    assert inst.contained[11].code.text == "Neutrophils"
    assert inst.contained[11].id == "r8"
    assert inst.contained[11].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[11].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[11].status == "final"
    assert inst.contained[11].subject.reference == "Patient/pat2"
    assert inst.contained[11].valueQuantity.code == "%"
    assert inst.contained[11].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[11].valueQuantity.unit == "%"
    assert inst.contained[11].valueQuantity.value == Decimal("20")
    assert inst.contained[12].code.coding[0].code == "751-8"
    assert inst.contained[12].code.coding[0].display == "Neutrophils [#/volume] in Blood by Automated count"
    assert inst.contained[12].code.coding[0].system == "http://loinc.org"
    assert inst.contained[12].code.text == "Neutrophils"
    assert inst.contained[12].id == "r9"
    assert inst.contained[12].interpretation.coding[0].code == "LL"
    assert inst.contained[12].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[12].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[12].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[12].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[12].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[12].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[12].referenceRange[0].high.value == Decimal("7.5")
    assert inst.contained[12].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[12].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[12].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[12].referenceRange[0].low.value == Decimal("2.0")
    assert inst.contained[12].status == "final"
    assert inst.contained[12].subject.reference == "Patient/pat2"
    assert inst.contained[12].valueQuantity.code == "10*9/L"
    assert inst.contained[12].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[12].valueQuantity.unit == "x10*9/L"
    assert inst.contained[12].valueQuantity.value == Decimal("0.9")
    assert inst.contained[13].code.coding[0].code == "736-9"
    assert inst.contained[13].code.coding[0].display == "Lymphocytes/100 leukocytes in Blood by Automated count"
    assert inst.contained[13].code.coding[0].system == "http://loinc.org"
    assert inst.contained[13].code.text == "Lymphocytes"
    assert inst.contained[13].id == "r10"
    assert inst.contained[13].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[13].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[13].status == "final"
    assert inst.contained[13].subject.reference == "Patient/pat2"
    assert inst.contained[13].valueQuantity.code == "%"
    assert inst.contained[13].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[13].valueQuantity.unit == "%"
    assert inst.contained[13].valueQuantity.value == Decimal("20")
    assert inst.contained[14].code.coding[0].code == "731-0"
    assert inst.contained[14].code.coding[0].display == "Lymphocytes [#/volume] in Blood by Automated count"
    assert inst.contained[14].code.coding[0].system == "http://loinc.org"
    assert inst.contained[14].code.text == "Lymphocytes"
    assert inst.contained[14].id == "r11"
    assert inst.contained[14].interpretation.coding[0].code == "L"
    assert inst.contained[14].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[14].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[14].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[14].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[14].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[14].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[14].referenceRange[0].high.value == Decimal("4.0")
    assert inst.contained[14].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[14].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[14].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[14].referenceRange[0].low.value == Decimal("1.1")
    assert inst.contained[14].status == "final"
    assert inst.contained[14].subject.reference == "Patient/pat2"
    assert inst.contained[14].valueQuantity.code == "10*9/L"
    assert inst.contained[14].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[14].valueQuantity.unit == "x10*9/L"
    assert inst.contained[14].valueQuantity.value == Decimal("0.9")
    assert inst.contained[15].code.coding[0].code == "5905-5"
    assert inst.contained[15].code.coding[0].display == "Monocytes/100 leukocytes in Blood by Automated count"
    assert inst.contained[15].code.coding[0].system == "http://loinc.org"
    assert inst.contained[15].code.text == "Monocytes"
    assert inst.contained[15].id == "r12"
    assert inst.contained[15].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[15].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[15].status == "final"
    assert inst.contained[15].subject.reference == "Patient/pat2"
    assert inst.contained[15].valueQuantity.code == "%"
    assert inst.contained[15].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[15].valueQuantity.unit == "%"
    assert inst.contained[15].valueQuantity.value == Decimal("20")
    assert inst.contained[16].code.coding[0].code == "742-7"
    assert inst.contained[16].code.coding[0].display == "Monocytes [#/volume] in Blood by Automated count"
    assert inst.contained[16].code.coding[0].system == "http://loinc.org"
    assert inst.contained[16].code.text == "Monocytes"
    assert inst.contained[16].id == "r13"
    assert inst.contained[16].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[16].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[16].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[16].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[16].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[16].referenceRange[0].high.value == Decimal("1.0")
    assert inst.contained[16].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[16].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[16].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[16].referenceRange[0].low.value == Decimal("0.2")
    assert inst.contained[16].status == "final"
    assert inst.contained[16].subject.reference == "Patient/pat2"
    assert inst.contained[16].valueQuantity.code == "10*9/L"
    assert inst.contained[16].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[16].valueQuantity.unit == "x10*9/L"
    assert inst.contained[16].valueQuantity.value == Decimal("0.9")
    assert inst.contained[17].code.coding[0].code == "713-8"
    assert inst.contained[17].code.coding[0].display == "Eosinophils/100 leukocytes in Blood by Automated count"
    assert inst.contained[17].code.coding[0].system == "http://loinc.org"
    assert inst.contained[17].code.text == "Eosinophils"
    assert inst.contained[17].id == "r14"
    assert inst.contained[17].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[17].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[17].status == "final"
    assert inst.contained[17].subject.reference == "Patient/pat2"
    assert inst.contained[17].valueQuantity.code == "%"
    assert inst.contained[17].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[17].valueQuantity.unit == "%"
    assert inst.contained[17].valueQuantity.value == Decimal("20")
    assert inst.contained[18].code.coding[0].code == "711-2"
    assert inst.contained[18].code.coding[0].display == "Eosinophils [#/volume] in Blood by Automated count"
    assert inst.contained[18].code.coding[0].system == "http://loinc.org"
    assert inst.contained[18].code.text == "Eosinophils"
    assert inst.contained[18].id == "r15"
    assert inst.contained[18].interpretation.coding[0].code == "HH"
    assert inst.contained[18].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[18].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[18].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[18].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[18].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[18].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[18].referenceRange[0].high.value == Decimal("0.4")
    assert inst.contained[18].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[18].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[18].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[18].referenceRange[0].low.value == Decimal("0.04")
    assert inst.contained[18].status == "final"
    assert inst.contained[18].subject.reference == "Patient/pat2"
    assert inst.contained[18].valueQuantity.code == "10*9/L"
    assert inst.contained[18].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[18].valueQuantity.unit == "x10*9/L"
    assert inst.contained[18].valueQuantity.value == Decimal("0.92")
    assert inst.contained[19].code.coding[0].code == "706-2"
    assert inst.contained[19].code.coding[0].display == "Basophils/100 leukocytes in Blood by Automated count"
    assert inst.contained[19].code.coding[0].system == "http://loinc.org"
    assert inst.contained[19].code.text == "Basophils"
    assert inst.contained[19].id == "r16"
    assert inst.contained[19].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[19].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[19].status == "final"
    assert inst.contained[19].subject.reference == "Patient/pat2"
    assert inst.contained[19].valueQuantity.code == "%"
    assert inst.contained[19].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[19].valueQuantity.unit == "%"
    assert inst.contained[19].valueQuantity.value == Decimal("20")
    assert inst.contained[20].code.coding[0].code == "704-7"
    assert inst.contained[20].code.coding[0].display == "Basophils [#/volume] in Blood by Automated count"
    assert inst.contained[20].code.coding[0].system == "http://loinc.org"
    assert inst.contained[20].code.text == "Basophils"
    assert inst.contained[20].id == "r17"
    assert inst.contained[20].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[20].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[20].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[20].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[20].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[20].referenceRange[0].high.value == Decimal("0.21")
    assert inst.contained[20].status == "final"
    assert inst.contained[20].subject.reference == "Patient/pat2"
    assert inst.contained[20].valueQuantity.code == "10*9/L"
    assert inst.contained[20].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[20].valueQuantity.unit == "x10*9/L"
    assert inst.contained[20].valueQuantity.value == Decimal("0.92")
    assert inst.contained[21].code.coding[0].code == "24323-8"
    assert inst.contained[21].code.coding[0].display == "Comprehensive metabolic 2000 panel - Serum or Plasma"
    assert inst.contained[21].code.coding[0].system == "http://loinc.org"
    assert inst.contained[21].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[21].id == "p1"
    assert inst.contained[21].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[21].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[21].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[21].related[0].target.reference == "#o1"
    assert inst.contained[21].related[0].type == "has-member"
    assert inst.contained[21].related[1].target.reference == "#o2"
    assert inst.contained[21].related[1].type == "has-member"
    assert inst.contained[21].related[2].target.reference == "#o3"
    assert inst.contained[21].related[2].type == "has-member"
    assert inst.contained[21].related[3].target.reference == "#o4"
    assert inst.contained[21].related[3].type == "has-member"
    assert inst.contained[21].related[4].target.reference == "#o5"
    assert inst.contained[21].related[4].type == "has-member"
    assert inst.contained[21].related[5].target.reference == "#o6"
    assert inst.contained[21].related[5].type == "has-member"
    assert inst.contained[21].related[6].target.reference == "#o7"
    assert inst.contained[21].related[6].type == "has-member"
    assert inst.contained[21].related[7].target.reference == "#o8"
    assert inst.contained[21].related[7].type == "has-member"
    assert inst.contained[21].related[8].target.reference == "#o9"
    assert inst.contained[21].related[8].type == "has-member"
    assert inst.contained[21].related[9].target.reference == "#o10"
    assert inst.contained[21].related[9].type == "has-member"
    assert inst.contained[21].related[10].target.reference == "#o11"
    assert inst.contained[21].related[10].type == "has-member"
    assert inst.contained[21].related[11].target.reference == "#o12"
    assert inst.contained[21].related[11].type == "has-member"
    assert inst.contained[21].related[12].target.reference == "#o13"
    assert inst.contained[21].related[12].type == "has-member"
    assert inst.contained[21].related[13].target.reference == "#o14"
    assert inst.contained[21].related[13].type == "has-member"
    assert inst.contained[21].related[14].target.reference == "#o15"
    assert inst.contained[21].related[14].type == "has-member"
    assert inst.contained[21].related[15].target.reference == "#o16"
    assert inst.contained[21].related[15].type == "has-member"
    assert inst.contained[21].related[16].target.reference == "#o17"
    assert inst.contained[21].related[16].type == "has-member"
    assert inst.contained[21].related[17].target.reference == "#o18"
    assert inst.contained[21].related[17].type == "has-member"
    assert inst.contained[21].related[18].target.reference == "#o19"
    assert inst.contained[21].related[18].type == "has-member"
    assert inst.contained[21].related[19].target.reference == "#o20"
    assert inst.contained[21].related[19].type == "has-member"
    assert inst.contained[21].related[20].target.reference == "#o21"
    assert inst.contained[21].related[20].type == "has-member"
    assert inst.contained[21].related[21].target.reference == "#o22"
    assert inst.contained[21].related[21].type == "has-member"
    assert inst.contained[21].specimen.display == "Red Top Tube"
    assert inst.contained[21].specimen.reference == "#rtt"
    assert inst.contained[21].status == "final"
    assert inst.contained[22].code.coding[0].code == "2951-2"
    assert inst.contained[22].code.coding[0].display == "Sodium [Moles/volume] in Serum or Plasma"
    assert inst.contained[22].code.coding[0].system == "http://loinc.org"
    assert inst.contained[22].code.coding[1].code == "104934005"
    assert inst.contained[22].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[22].id == "o1"
    assert inst.contained[22].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[22].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[22].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[22].referenceRange[0].high.value == Decimal("147")
    assert inst.contained[22].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[22].referenceRange[0].low.value == Decimal("137")
    assert inst.contained[22].status == "final"
    assert inst.contained[22].subject.reference == "Patient/pat2"
    assert inst.contained[22].valueQuantity.unit == "mmol/L"
    assert inst.contained[22].valueQuantity.value == Decimal("140")
    assert inst.contained[23].code.coding[0].code == "2823-3"
    assert inst.contained[23].code.coding[0].display == "Potassium [Moles/volume] in Serum or Plasma"
    assert inst.contained[23].code.coding[0].system == "http://loinc.org"
    assert inst.contained[23].code.coding[1].code == "59573005"
    assert inst.contained[23].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[23].id == "o2"
    assert inst.contained[23].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[23].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[23].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[23].referenceRange[0].high.value == Decimal("5.0")
    assert inst.contained[23].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[23].referenceRange[0].low.value == Decimal("3.5")
    assert inst.contained[23].status == "final"
    assert inst.contained[23].subject.reference == "Patient/pat2"
    assert inst.contained[23].valueQuantity.unit == "mmol/L"
    assert inst.contained[23].valueQuantity.value == Decimal("4.2")
    assert inst.contained[24].code.coding[0].code == "2075-0"
    assert inst.contained[24].code.coding[0].display == "Chloride [Moles/volume] in Serum or Plasma"
    assert inst.contained[24].code.coding[0].system == "http://loinc.org"
    assert inst.contained[24].code.coding[1].code == "46511006"
    assert inst.contained[24].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[24].id == "o3"
    assert inst.contained[24].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[24].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[24].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[24].referenceRange[0].high.value == Decimal("109")
    assert inst.contained[24].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[24].referenceRange[0].low.value == Decimal("96")
    assert inst.contained[24].status == "final"
    assert inst.contained[24].subject.reference == "Patient/pat2"
    assert inst.contained[24].valueQuantity.unit == "mmol/L"
    assert inst.contained[24].valueQuantity.value == Decimal("105")
    assert inst.contained[25].code.coding[0].code == "1963-8"
    assert inst.contained[25].code.coding[0].display == "Bicarbonate [Moles/volume] in Serum"
    assert inst.contained[25].code.coding[0].system == "http://loinc.org"
    assert inst.contained[25].code.coding[1].code == "88645003"
    assert inst.contained[25].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[25].id == "o4"
    assert inst.contained[25].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[25].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[25].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[25].referenceRange[0].high.value == Decimal("33")
    assert inst.contained[25].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[25].referenceRange[0].low.value == Decimal("25")
    assert inst.contained[25].status == "final"
    assert inst.contained[25].subject.reference == "Patient/pat2"
    assert inst.contained[25].valueQuantity.unit == "mmol/L"
    assert inst.contained[25].valueQuantity.value == Decimal("26")
    assert inst.contained[26].code.coding[0].code == "1863-0"
    assert inst.contained[26].code.coding[0].display == "Anion gap 4 in Serum or Plasma"
    assert inst.contained[26].code.coding[0].system == "http://loinc.org"
    assert inst.contained[26].code.coding[1].code == "271057005"
    assert inst.contained[26].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[26].id == "o5"
    assert inst.contained[26].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[26].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[26].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[26].referenceRange[0].high.value == Decimal("17")
    assert inst.contained[26].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[26].referenceRange[0].low.value == Decimal("4")
    assert inst.contained[26].status == "final"
    assert inst.contained[26].subject.reference == "Patient/pat2"
    assert inst.contained[26].valueQuantity.unit == "mmol/L"
    assert inst.contained[26].valueQuantity.value == Decimal("13")
    assert inst.contained[27].code.coding[0].code == "14749-6"
    assert inst.contained[27].code.coding[0].display == "Glucose [Moles/volume] in Serum or Plasma"
    assert inst.contained[27].code.coding[0].system == "http://loinc.org"
    assert inst.contained[27].code.coding[1].code == "36048009"
    assert inst.contained[27].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[27].id == "o6"
    assert inst.contained[27].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[27].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[27].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[27].referenceRange[0].high.value == Decimal("7.7")
    assert inst.contained[27].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[27].referenceRange[0].low.value == Decimal("3.0")
    assert inst.contained[27].status == "final"
    assert inst.contained[27].subject.reference == "Patient/pat2"
    assert inst.contained[27].valueQuantity.unit == "mmol/L"
    assert inst.contained[27].valueQuantity.value == Decimal("7.4")
    assert inst.contained[28].code.coding[0].code == "14937-7"
    assert inst.contained[28].code.coding[0].display == "Urea nitrogen [Moles/volume] in Serum or Plasma"
    assert inst.contained[28].code.coding[0].system == "http://loinc.org"
    assert inst.contained[28].code.coding[1].code == "273967009"
    assert inst.contained[28].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[28].id == "o7"
    assert inst.contained[28].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[28].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[28].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[28].referenceRange[0].high.value == Decimal("7.0")
    assert inst.contained[28].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[28].referenceRange[0].low.value == Decimal("2.0")
    assert inst.contained[28].status == "final"
    assert inst.contained[28].subject.reference == "Patient/pat2"
    assert inst.contained[28].valueQuantity.unit == "mmol/L"
    assert inst.contained[28].valueQuantity.value == Decimal("4.7")
    assert inst.contained[29].code.coding[0].code == "14682-9"
    assert inst.contained[29].code.coding[0].display == "Creatinine [Moles/volume] in Serum or Plasma"
    assert inst.contained[29].code.coding[0].system == "http://loinc.org"
    assert inst.contained[29].code.coding[1].code == "70901006"
    assert inst.contained[29].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[29].id == "o8"
    assert inst.contained[29].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[29].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[29].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[29].referenceRange[0].high.value == Decimal("0.11")
    assert inst.contained[29].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[29].referenceRange[0].low.value == Decimal("0.04")
    assert inst.contained[29].status == "final"
    assert inst.contained[29].subject.reference == "Patient/pat2"
    assert inst.contained[29].valueQuantity.unit == "mmol/L"
    assert inst.contained[29].valueQuantity.value == Decimal("0.09")
    assert inst.contained[30].code.coding[0].code == "14933-6"
    assert inst.contained[30].code.coding[0].display == "Urate [Moles/volume] in Serum or Plasma"
    assert inst.contained[30].code.coding[0].system == "http://loinc.org"
    assert inst.contained[30].code.coding[1].code == "86228006"
    assert inst.contained[30].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[30].id == "o9"
    assert inst.contained[30].interpretation.coding[0].code == "H"
    assert inst.contained[30].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[30].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[30].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[30].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[30].referenceRange[0].high.value == Decimal("0.35")
    assert inst.contained[30].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[30].referenceRange[0].low.value == Decimal("0.14")
    assert inst.contained[30].status == "final"
    assert inst.contained[30].subject.reference == "Patient/pat2"
    assert inst.contained[30].valueQuantity.unit == "mmol/L"
    assert inst.contained[30].valueQuantity.value == Decimal("0.39")
    assert inst.contained[31].code.coding[0].code == "14631-6"
    assert inst.contained[31].code.coding[0].display == "Bilirubin.total [Moles/volume] in Serum or Plasma"
    assert inst.contained[31].code.coding[0].system == "http://loinc.org"
    assert inst.contained[31].code.coding[1].code == "27171005"
    assert inst.contained[31].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[31].id == "o10"
    assert inst.contained[31].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[31].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[31].referenceRange[0].high.unit == "umol/L"
    assert inst.contained[31].referenceRange[0].high.value == Decimal("20")
    assert inst.contained[31].referenceRange[0].low.unit == "umol/L"
    assert inst.contained[31].referenceRange[0].low.value == Decimal("2")
    assert inst.contained[31].status == "final"
    assert inst.contained[31].subject.reference == "Patient/pat2"
    assert inst.contained[31].valueQuantity.unit == "umol/L"
    assert inst.contained[31].valueQuantity.value == Decimal("7")
    assert inst.contained[32].code.coding[0].code == "14629-0"
    assert inst.contained[32].code.coding[0].display == "Bilirubin.direct [Moles/volume] in Serum or Plasma"
    assert inst.contained[32].code.coding[0].system == "http://loinc.org"
    assert inst.contained[32].code.coding[1].code == "39748002"
    assert inst.contained[32].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[32].id == "o11"
    assert inst.contained[32].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[32].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[32].referenceRange[0].high.unit == "umol/L"
    assert inst.contained[32].referenceRange[0].high.value == Decimal("8")
    assert inst.contained[32].referenceRange[0].low.unit == "umol/L"
    assert inst.contained[32].referenceRange[0].low.value == Decimal("0")
    assert inst.contained[32].status == "final"
    assert inst.contained[32].subject.reference == "Patient/pat2"
    assert inst.contained[32].valueQuantity.unit == "umol/L"
    assert inst.contained[32].valueQuantity.value == Decimal("3")
    assert inst.contained[33].code.coding[0].code == "6768-6"
    assert inst.contained[33].code.coding[0].display == "Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma"
    assert inst.contained[33].code.coding[0].system == "http://loinc.org"
    assert inst.contained[33].code.coding[1].code == "88810008"
    assert inst.contained[33].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[33].id == "o12"
    assert inst.contained[33].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[33].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[33].referenceRange[0].high.unit == "U/L"
    assert inst.contained[33].referenceRange[0].high.value == Decimal("115")
    assert inst.contained[33].referenceRange[0].low.unit == "U/L"
    assert inst.contained[33].referenceRange[0].low.value == Decimal("30")
    assert inst.contained[33].status == "final"
    assert inst.contained[33].subject.reference == "Patient/pat2"
    assert inst.contained[33].valueQuantity.unit == "U/L"
    assert inst.contained[33].valueQuantity.value == Decimal("108")
    assert inst.contained[34].code.coding[0].code == "2324-2"
    assert inst.contained[34].code.coding[0].display == "Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma"
    assert inst.contained[34].code.coding[0].system == "http://loinc.org"
    assert inst.contained[34].code.coding[1].code == "69480007"
    assert inst.contained[34].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[34].id == "o13"
    assert inst.contained[34].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[34].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[34].referenceRange[0].high.unit == "U/L"
    assert inst.contained[34].referenceRange[0].high.value == Decimal("45")
    assert inst.contained[34].referenceRange[0].low.unit == "U/L"
    assert inst.contained[34].referenceRange[0].low.value == Decimal("0")
    assert inst.contained[34].status == "final"
    assert inst.contained[34].subject.reference == "Patient/pat2"
    assert inst.contained[34].valueQuantity.unit == "U/L"
    assert inst.contained[34].valueQuantity.value == Decimal("35")
    assert inst.contained[35].code.coding[0].code == "1742-6"
    assert inst.contained[35].code.coding[0].display == "Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma"
    assert inst.contained[35].code.coding[0].system == "http://loinc.org"
    assert inst.contained[35].code.coding[1].code == "34608000"
    assert inst.contained[35].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[35].id == "o14"
    assert inst.contained[35].interpretation.coding[0].code == "H"
    assert inst.contained[35].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[35].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[35].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[35].referenceRange[0].high.unit == "U/L"
    assert inst.contained[35].referenceRange[0].high.value == Decimal("45")
    assert inst.contained[35].referenceRange[0].low.unit == "U/L"
    assert inst.contained[35].referenceRange[0].low.value == Decimal("0")
    assert inst.contained[35].status == "final"
    assert inst.contained[35].subject.reference == "Patient/pat2"
    assert inst.contained[35].valueQuantity.unit == "U/L"
    assert inst.contained[35].valueQuantity.value == Decimal("54")
    assert inst.contained[36].code.coding[0].code == "1920-8"
    assert inst.contained[36].code.coding[0].display == "Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma"
    assert inst.contained[36].code.coding[0].system == "http://loinc.org"
    assert inst.contained[36].code.coding[1].code == "45896001"
    assert inst.contained[36].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[36].id == "o15"
    assert inst.contained[36].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[36].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[36].referenceRange[0].high.unit == "U/L"
    assert inst.contained[36].referenceRange[0].high.value == Decimal("41")
    assert inst.contained[36].referenceRange[0].low.unit == "U/L"
    assert inst.contained[36].referenceRange[0].low.value == Decimal("0")
    assert inst.contained[36].status == "final"
    assert inst.contained[36].subject.reference == "Patient/pat2"
    assert inst.contained[36].valueQuantity.unit == "U/L"
    assert inst.contained[36].valueQuantity.value == Decimal("30")
    assert inst.contained[37].code.coding[0].code == "2532-0"
    assert inst.contained[37].code.coding[0].display == "Lactate dehydrogenase [Enzymatic activity/volume] in Serum or Plasma"
    assert inst.contained[37].code.coding[0].system == "http://loinc.org"
    assert inst.contained[37].code.coding[1].code == "11274001"
    assert inst.contained[37].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[37].id == "o16"
    assert inst.contained[37].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[37].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[37].referenceRange[0].high.unit == "U/L"
    assert inst.contained[37].referenceRange[0].high.value == Decimal("250")
    assert inst.contained[37].referenceRange[0].low.unit == "U/L"
    assert inst.contained[37].referenceRange[0].low.value == Decimal("80")
    assert inst.contained[37].status == "final"
    assert inst.contained[37].subject.reference == "Patient/pat2"
    assert inst.contained[37].valueQuantity.unit == "U/L"
    assert inst.contained[37].valueQuantity.value == Decimal("131")
    assert inst.contained[38].code.coding[0].code == "2000-8"
    assert inst.contained[38].code.coding[0].display == "Calcium [Moles/volume] in Serum or Plasma"
    assert inst.contained[38].code.coding[0].system == "http://loinc.org"
    assert inst.contained[38].code.coding[1].code == "71878006"
    assert inst.contained[38].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[38].id == "o17"
    assert inst.contained[38].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[38].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[38].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[38].referenceRange[0].high.value == Decimal("2.65")
    assert inst.contained[38].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[38].referenceRange[0].low.value == Decimal("2.25")
    assert inst.contained[38].status == "final"
    assert inst.contained[38].subject.reference == "Patient/pat2"
    assert inst.contained[38].valueQuantity.unit == "mmol/L"
    assert inst.contained[38].valueQuantity.value == Decimal("2.38")
    assert inst.contained[39].code.coding[0].code == "13959-2"
    assert inst.contained[39].code.coding[0].display == "Calcium.ionized [Moles/volume] in Serum or Plasma by calculation"
    assert inst.contained[39].code.coding[0].system == "http://loinc.org"
    assert inst.contained[39].code.coding[1].code == "166708003"
    assert inst.contained[39].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[39].id == "o18"
    assert inst.contained[39].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[39].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[39].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[39].referenceRange[0].high.value == Decimal("2.65")
    assert inst.contained[39].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[39].referenceRange[0].low.value == Decimal("2.25")
    assert inst.contained[39].status == "final"
    assert inst.contained[39].subject.reference == "Patient/pat2"
    assert inst.contained[39].valueQuantity.unit == "mmol/L"
    assert inst.contained[39].valueQuantity.value == Decimal("2.39")
    assert inst.contained[40].code.coding[0].code == "14879-1"
    assert inst.contained[40].code.coding[0].display == "Phosphate [Moles/volume] in Serum or Plasma"
    assert inst.contained[40].code.coding[0].system == "http://loinc.org"
    assert inst.contained[40].code.coding[1].code == "104866001"
    assert inst.contained[40].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[40].id == "o19"
    assert inst.contained[40].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[40].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[40].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[40].referenceRange[0].high.value == Decimal("1.5")
    assert inst.contained[40].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[40].referenceRange[0].low.value == Decimal("0.8")
    assert inst.contained[40].status == "final"
    assert inst.contained[40].subject.reference == "Patient/pat2"
    assert inst.contained[40].valueQuantity.unit == "mmol/L"
    assert inst.contained[40].valueQuantity.value == Decimal("1.5")
    assert inst.contained[41].code.coding[0].code == "2885-2"
    assert inst.contained[41].code.coding[0].display == "Protein [Mass/volume] in Serum or Plasma"
    assert inst.contained[41].code.coding[0].system == "http://loinc.org"
    assert inst.contained[41].code.coding[1].code == "74040009"
    assert inst.contained[41].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[41].id == "o20"
    assert inst.contained[41].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[41].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[41].referenceRange[0].high.unit == "g/L"
    assert inst.contained[41].referenceRange[0].high.value == Decimal("82")
    assert inst.contained[41].referenceRange[0].low.unit == "g/L"
    assert inst.contained[41].referenceRange[0].low.value == Decimal("60")
    assert inst.contained[41].status == "final"
    assert inst.contained[41].subject.reference == "Patient/pat2"
    assert inst.contained[41].valueQuantity.unit == "g/L"
    assert inst.contained[41].valueQuantity.value == Decimal("67")
    assert inst.contained[42].code.coding[0].code == "1751-7"
    assert inst.contained[42].code.coding[0].display == "Albumin [Mass/volume] in Serum or Plasma"
    assert inst.contained[42].code.coding[0].system == "http://loinc.org"
    assert inst.contained[42].code.coding[1].code == "104485008"
    assert inst.contained[42].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[42].id == "o21"
    assert inst.contained[42].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[42].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[42].referenceRange[0].high.unit == "g/L"
    assert inst.contained[42].referenceRange[0].high.value == Decimal("50")
    assert inst.contained[42].referenceRange[0].low.unit == "g/L"
    assert inst.contained[42].referenceRange[0].low.value == Decimal("35")
    assert inst.contained[42].status == "final"
    assert inst.contained[42].subject.reference == "Patient/pat2"
    assert inst.contained[42].valueQuantity.unit == "g/L"
    assert inst.contained[42].valueQuantity.value == Decimal("42")
    assert inst.contained[43].code.coding[0].code == "10834-0"
    assert inst.contained[43].code.coding[0].display == "Globulin [Mass/volume] in Serum by calculation"
    assert inst.contained[43].code.coding[0].system == "http://loinc.org"
    assert inst.contained[43].code.coding[1].code == "104979009"
    assert inst.contained[43].code.coding[1].system == "http://snomed.info/sct"
    assert inst.contained[43].id == "o22"
    assert inst.contained[43].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[43].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[43].referenceRange[0].high.unit == "g/L"
    assert inst.contained[43].referenceRange[0].high.value == Decimal("40")
    assert inst.contained[43].referenceRange[0].low.unit == "g/L"
    assert inst.contained[43].referenceRange[0].low.value == Decimal("20")
    assert inst.contained[43].status == "final"
    assert inst.contained[43].subject.reference == "Patient/pat2"
    assert inst.contained[43].valueQuantity.unit == "g/L"
    assert inst.contained[43].valueQuantity.value == Decimal("25")
    assert inst.contained[44].code.coding[0].code == "24357-6"
    assert inst.contained[44].code.coding[0].display == "Urinalysis macro (dipstick) panel - Urine"
    assert inst.contained[44].code.coding[0].system == "http://loinc.org"
    assert inst.contained[44].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[44].id == "p3"
    assert inst.contained[44].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[44].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[44].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[44].related[0].target.reference == "#u1"
    assert inst.contained[44].related[0].type == "has-member"
    assert inst.contained[44].related[1].target.reference == "#u2"
    assert inst.contained[44].related[1].type == "has-member"
    assert inst.contained[44].related[2].target.reference == "#u3"
    assert inst.contained[44].related[2].type == "has-member"
    assert inst.contained[44].related[3].target.reference == "#u4"
    assert inst.contained[44].related[3].type == "has-member"
    assert inst.contained[44].related[4].target.reference == "#u5"
    assert inst.contained[44].related[4].type == "has-member"
    assert inst.contained[44].related[5].target.reference == "#u6"
    assert inst.contained[44].related[5].type == "has-member"
    assert inst.contained[44].related[6].target.reference == "#u7"
    assert inst.contained[44].related[6].type == "has-member"
    assert inst.contained[44].related[7].target.reference == "#u8"
    assert inst.contained[44].related[7].type == "has-member"
    assert inst.contained[44].related[8].target.reference == "#u9"
    assert inst.contained[44].related[8].type == "has-member"
    assert inst.contained[44].specimen.display == "Urine Sample"
    assert inst.contained[44].specimen.reference == "#urine"
    assert inst.contained[44].status == "final"
    assert inst.contained[45].code.coding[0].code == "2756-5"
    assert inst.contained[45].code.coding[0].display == "pH of Urine"
    assert inst.contained[45].code.coding[0].system == "http://loinc.org"
    assert inst.contained[45].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[45].id == "u1"
    assert inst.contained[45].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[45].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[45].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[45].specimen.display == "Urine Sample"
    assert inst.contained[45].specimen.reference == "#urine"
    assert inst.contained[45].status == "final"
    assert inst.contained[45].subject.reference == "Patient/pat2"
    assert inst.contained[45].valueQuantity.unit == "pH"
    assert inst.contained[45].valueQuantity.value == Decimal("5.0")
    assert inst.contained[46].code.coding[0].code == "2887-8"
    assert inst.contained[46].code.coding[0].display == "Protein [Presence] in Urine"
    assert inst.contained[46].code.coding[0].system == "http://loinc.org"
    assert inst.contained[46].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[46].id == "u2"
    assert inst.contained[46].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[46].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[46].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[46].specimen.display == "Urine Sample"
    assert inst.contained[46].specimen.reference == "#urine"
    assert inst.contained[46].status == "final"
    assert inst.contained[46].subject.reference == "Patient/pat2"
    assert inst.contained[46].valueCodeableConcept.coding[0].code == "260385009"
    assert inst.contained[46].valueCodeableConcept.coding[0].display == "Negative"
    assert inst.contained[46].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[47].code.coding[0].code == "2965-2"
    assert inst.contained[47].code.coding[0].display == "Specific gravity of Urine"
    assert inst.contained[47].code.coding[0].system == "http://loinc.org"
    assert inst.contained[47].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[47].id == "u3"
    assert inst.contained[47].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[47].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[47].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[47].specimen.display == "Urine Sample"
    assert inst.contained[47].specimen.reference == "#urine"
    assert inst.contained[47].status == "final"
    assert inst.contained[47].subject.reference == "Patient/pat2"
    assert inst.contained[47].valueQuantity.value == Decimal("1.009")
    assert inst.contained[48].code.coding[0].code == "33051-4"
    assert inst.contained[48].code.coding[0].display == "Erythrocytes [Presence] in Urine"
    assert inst.contained[48].code.coding[0].system == "http://loinc.org"
    assert inst.contained[48].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[48].id == "u4"
    assert inst.contained[48].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[48].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[48].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[48].specimen.display == "Urine Sample"
    assert inst.contained[48].specimen.reference == "#urine"
    assert inst.contained[48].status == "final"
    assert inst.contained[48].subject.reference == "Patient/pat2"
    assert inst.contained[48].valueCodeableConcept.coding[0].code == "260385009"
    assert inst.contained[48].valueCodeableConcept.coding[0].display == "Negative"
    assert inst.contained[48].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[49].code.coding[0].code == "2349-9"
    assert inst.contained[49].code.coding[0].display == "Glucose [Presence] in Urine"
    assert inst.contained[49].code.coding[0].system == "http://loinc.org"
    assert inst.contained[49].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[49].id == "u5"
    assert inst.contained[49].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[49].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[49].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[49].specimen.display == "Urine Sample"
    assert inst.contained[49].specimen.reference == "#urine"
    assert inst.contained[49].status == "final"
    assert inst.contained[49].subject.reference == "Patient/pat2"
    assert inst.contained[49].valueCodeableConcept.coding[0].code == "260385009"
    assert inst.contained[49].valueCodeableConcept.coding[0].display == "Negative"
    assert inst.contained[49].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[50].code.coding[0].code == "33052-2"
    assert inst.contained[50].code.coding[0].display == "Leukocytes [Presence] in Urine"
    assert inst.contained[50].code.coding[0].system == "http://loinc.org"
    assert inst.contained[50].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[50].id == "u6"
    assert inst.contained[50].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[50].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[50].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[50].specimen.display == "Urine Sample"
    assert inst.contained[50].specimen.reference == "#urine"
    assert inst.contained[50].status == "final"
    assert inst.contained[50].subject.reference == "Patient/pat2"
    assert inst.contained[50].valueCodeableConcept.coding[0].code == "260385009"
    assert inst.contained[50].valueCodeableConcept.coding[0].display == "Negative"
    assert inst.contained[50].valueCodeableConcept.coding[0].system == "http://snomed.info/sct"
    assert inst.contained[51].code.coding[0].code == "30405-5"
    assert inst.contained[51].code.coding[0].display == "Leukocytes [#/volume] in Urine"
    assert inst.contained[51].code.coding[0].system == "http://loinc.org"
    assert inst.contained[51].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[51].id == "u7"
    assert inst.contained[51].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[51].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[51].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[51].specimen.display == "Urine Sample"
    assert inst.contained[51].specimen.reference == "#urine"
    assert inst.contained[51].status == "final"
    assert inst.contained[51].subject.reference == "Patient/pat2"
    assert inst.contained[51].valueQuantity.unit == "/uL"
    assert inst.contained[51].valueQuantity.value == Decimal("1")
    assert inst.contained[52].code.coding[0].code == "30391-7"
    assert inst.contained[52].code.coding[0].display == "Erythocytes [#/volume] in Urine"
    assert inst.contained[52].code.coding[0].system == "http://loinc.org"
    assert inst.contained[52].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[52].id == "u8"
    assert inst.contained[52].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[52].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[52].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[52].specimen.display == "Urine Sample"
    assert inst.contained[52].specimen.reference == "#urine"
    assert inst.contained[52].status == "final"
    assert inst.contained[52].subject.reference == "Patient/pat2"
    assert inst.contained[52].valueQuantity.comparator == "<"
    assert inst.contained[52].valueQuantity.unit == "/uL"
    assert inst.contained[52].valueQuantity.value == Decimal("1")
    assert inst.contained[53].code.coding[0].code == "13654-9"
    assert inst.contained[53].code.coding[0].display == "Epithelial cells.squamous [#/volume] in Urine sediment"
    assert inst.contained[53].code.coding[0].system == "http://loinc.org"
    assert inst.contained[53].effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.contained[53].id == "u9"
    assert inst.contained[53].issued == "2015-08-17T06:40:17Z"
    assert inst.contained[53].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[53].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[53].specimen.display == "Urine Sample"
    assert inst.contained[53].specimen.reference == "#urine"
    assert inst.contained[53].status == "final"
    assert inst.contained[53].subject.reference == "Patient/pat2"
    assert inst.contained[53].valueQuantity.comparator == "<"
    assert inst.contained[53].valueQuantity.unit == "/mL"
    assert inst.contained[53].valueQuantity.value == Decimal("1")
    assert inst.effectiveDateTime == "2015-08-16T06:40:17Z"
    assert inst.id == "ghp"
    assert inst.identifier[0].system == "http://acme.com/lab/reports"
    assert inst.identifier[0].value == "ghp-example"
    assert inst.issued == "2015-08-17T06:40:17Z"
    assert inst.meta.lastUpdated == "2015-08-16T10:35:23Z"
    assert inst.performer.display == "Acme Laboratory, Inc"
    assert inst.performer.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.result[0].display == "Chemistry Panel"
    assert inst.result[0].reference == "#p1"
    assert inst.result[1].display == "CBC"
    assert inst.result[1].reference == "#p2"
    assert inst.result[2].display == "Urinalysis"
    assert inst.result[2].reference == "#p3"
    assert inst.specimen[0].display == "Red Top Tube"
    assert inst.specimen[0].reference == "#rtt"
    assert inst.specimen[1].display == "Lavender Top Tube"
    assert inst.specimen[1].reference == "#ltt"
    assert inst.specimen[2].display == "Urine Sample"
    assert inst.specimen[2].reference == "#urine"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: ghp</p><p><b>meta</b>: </p><p><b>contained</b>: , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , </p><p><b>identifier</b>: ghp-example</p><p><b>status</b>: final</p><p><b>code</b>: General Health Profile <span>(Details : {http://acme.com/labs/reports code 'GHP' = '??', given as 'General Health Profile'})</span></p><p><b>subject</b>: <a>Patient/pat2</a></p><p><b>effective</b>: 16/08/2015 4:40:17 PM</p><p><b>issued</b>: 17/08/2015 4:40:17 PM</p><p><b>performer</b>: <a>Acme Laboratory, Inc</a></p><p><b>specimen</b>: </p><ul><li>Red Top Tube. Generated Summary: id: rtt; Serum sample <span>(Details : {SNOMED CT code '119364003' = '119364003', given as 'Serum sample'})</span>; Patient/pat2; 20150816-00124</li><li>Lavender Top Tube. Generated Summary: id: ltt; Blood specimen with EDTA <span>(Details : {SNOMED CT code '445295009' = '445295009', given as 'Blood specimen with EDTA'})</span>; Patient/pat2; 20150816-00124</li><li>Urine Sample. Generated Summary: id: urine; Urine specimen <span>(Details : {SNOMED CT code '122575003' = '122575003', given as 'Urine specimen'})</span>; Patient/pat2; 20150816-00124</li></ul><p><b>result</b>: </p><ul><li>Chemistry Panel. Generated Summary: id: p1; status: final; Comprehensive metabolic 2000 panel - Serum or Plasma <span>(Details : {LOINC code '24323-8' = 'Comprehensive metabolic 2000 panel - Serum or Plasma', given as 'Comprehensive metabolic 2000 panel - Serum or Plasma'})</span>; effective: 16/08/2015 4:40:17 PM; issued: 17/08/2015 4:40:17 PM; Acme Laboratory, Inc</li><li>CBC. Generated Summary: id: p2; status: final; Complete blood count (hemogram) panel - Blood by Automated count <span>(Details : {LOINC code '58410-2' = 'Complete blood count (hemogram) panel - Blood by Automated count', given as 'Complete blood count (hemogram) panel - Blood by Automated count'})</span>; effective: 16/08/2015 4:40:17 PM; issued: 17/08/2015 4:40:17 PM; Acme Laboratory, Inc</li><li>Urinalysis. Generated Summary: id: p3; status: final; Urinalysis macro (dipstick) panel - Urine <span>(Details : {LOINC code '24357-6' = 'Urinalysis macro (dipstick) panel - Urine', given as 'Urinalysis macro (dipstick) panel - Urine'})</span>; effective: 16/08/2015 4:40:17 PM; issued: 17/08/2015 4:40:17 PM; Acme Laboratory, Inc</li></ul></div>"
    assert inst.text.status == "generated"


def test_DiagnosticReport_6(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-lipids.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_6(inst2)


def impl_DiagnosticReport_6(inst):
    assert inst.category.coding[0].code == "HM"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "57698-3"
    assert inst.code.coding[0].display == "Lipid panel with direct LDL - Serum or Plasma"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Lipid Panel"
    assert inst.contained[0].code.coding[0].code == "35200-5"
    assert inst.contained[0].code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].code.text == "Cholesterol"
    assert inst.contained[0].id == "cholesterol"
    assert inst.contained[0].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[0].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[0].referenceRange[0].high.code == "mmol/L"
    assert inst.contained[0].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[0].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[0].referenceRange[0].high.value == Decimal("4.5")
    assert inst.contained[0].status == "final"
    assert inst.contained[0].subject.reference == "Patient/pat2"
    assert inst.contained[0].valueQuantity.code == "mmol/L"
    assert inst.contained[0].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[0].valueQuantity.unit == "mmol/L"
    assert inst.contained[0].valueQuantity.value == Decimal("6.3")
    assert inst.contained[1].code.coding[0].code == "35217-9"
    assert inst.contained[1].code.coding[0].system == "http://loinc.org"
    assert inst.contained[1].code.text == "Triglyceride"
    assert inst.contained[1].id == "triglyceride"
    assert inst.contained[1].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[1].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[1].referenceRange[0].high.code == "mmol/L"
    assert inst.contained[1].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[1].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[1].referenceRange[0].high.value == Decimal("2.0")
    assert inst.contained[1].status == "final"
    assert inst.contained[1].subject.reference == "Patient/pat2"
    assert inst.contained[1].valueQuantity.code == "mmol/L"
    assert inst.contained[1].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[1].valueQuantity.unit == "mmol/L"
    assert inst.contained[1].valueQuantity.value == Decimal("1.3")
    assert inst.contained[2].code.coding[0].code == "2085-9"
    assert inst.contained[2].code.coding[0].system == "http://loinc.org"
    assert inst.contained[2].code.text == "Cholesterol in HDL"
    assert inst.contained[2].id == "hdlcholesterol"
    assert inst.contained[2].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[2].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[2].referenceRange[0].low.code == "mmol/L"
    assert inst.contained[2].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[2].referenceRange[0].low.unit == "mmol/L"
    assert inst.contained[2].referenceRange[0].low.value == Decimal("1.5")
    assert inst.contained[2].status == "final"
    assert inst.contained[2].subject.reference == "Patient/pat2"
    assert inst.contained[2].valueQuantity.code == "mmol/L"
    assert inst.contained[2].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[2].valueQuantity.unit == "mmol/L"
    assert inst.contained[2].valueQuantity.value == Decimal("1.3")
    assert inst.contained[3].code.coding[0].code == "13457-7"
    assert inst.contained[3].code.coding[0].system == "http://loinc.org"
    assert inst.contained[3].code.text == "LDL Chol. (Calc)"
    assert inst.contained[3].id == "ldlcholesterol"
    assert inst.contained[3].performer[0].display == "Acme Laboratory, Inc"
    assert inst.contained[3].performer[0].reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.contained[3].referenceRange[0].high.code == "mmol/L"
    assert inst.contained[3].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[3].referenceRange[0].high.unit == "mmol/L"
    assert inst.contained[3].referenceRange[0].high.value == Decimal("3.0")
    assert inst.contained[3].status == "final"
    assert inst.contained[3].subject.reference == "Patient/pat2"
    assert inst.contained[3].valueQuantity.code == "mmol/L"
    assert inst.contained[3].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[3].valueQuantity.unit == "mmol/L"
    assert inst.contained[3].valueQuantity.value == Decimal("4.6")
    assert inst.effectiveDateTime == datetime.fromisoformat("2011-03-04T08:30:00+11:00")
    assert inst.id == "lipids"
    assert inst.identifier[0].system == "http://acme.com/lab/reports"
    assert inst.identifier[0].value == "5234342"
    assert inst.issued == datetime.fromisoformat("2013-01-27T11:45:33+11:00")
    assert inst.performer.display == "Acme Laboratory, Inc"
    assert inst.performer.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.result[0].reference == "#cholesterol"
    assert inst.result[1].reference == "#triglyceride"
    assert inst.result[2].reference == "#hdlcholesterol"
    assert inst.result[3].reference == "#ldlcholesterol"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.div == """<div>
      
      
      <h3>Lipid Report for Wile. E. COYOTE (MRN: 23453) issued 3-Mar 2009 14:26</h3>
      
      
      <pre>
Test                  Units       Value       Reference Range
Cholesterol           mmol/L      6.3         &lt;4.5
Triglyceride          mmol/L      1.3         &lt;2.0
HDL Cholesterol       mmol/L      1.3         &gt;1.5
LDL Chol. (calc)      mmol/L      4.2         &lt;3.0
      </pre>
      
      
      <p>Acme Laboratory, Inc signed: Dr Pete Pathologist</p>
    
    
    </div>"""
    assert inst.text.status == "generated"


def test_DiagnosticReport_7(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example-ultrasound.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_7(inst2)


def impl_DiagnosticReport_7(inst):
    assert inst.category.coding[0].code == "394914008"
    assert inst.category.coding[0].display == "Radiology"
    assert inst.category.coding[0].system == "http://snomed.info/sct"
    assert inst.category.coding[1].code == "RAD"
    assert inst.category.coding[1].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "45036003"
    assert inst.code.coding[0].display == "Ultrasonography of abdomen"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Abdominal Ultrasound"
    assert inst.conclusion == "Unremarkable study"
    assert inst.effectiveDateTime == datetime.fromisoformat("2012-12-01T12:00:00+01:00")
    assert inst.id == "ultrasound"
    assert inst.image[0].comment == "A comment about the image"
    assert inst.image[0].link.display == "WADO example image"
    assert inst.image[0].link.reference == "Media/1.2.840.11361907579238403408700.3.0.14.19970327150033"
    assert inst.issued == datetime.fromisoformat("2012-12-01T12:00:00+01:00")
    assert inst.performer.reference == "Practitioner/example"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: ultrasound</p><p><b>status</b>: final</p><p><b>category</b>: Radiology <span>(Details : {SNOMED CT code '394914008' = '394914008', given as 'Radiology'}; {http://hl7.org/fhir/v2/0074 code 'RAD' = 'Radiology)</span></p><p><b>code</b>: Abdominal Ultrasound <span>(Details : {SNOMED CT code '45036003' = '45036003', given as 'Ultrasonography of abdomen'})</span></p><p><b>subject</b>: <a>Patient/example</a></p><p><b>effective</b>: 01/12/2012 12:00:00 PM</p><p><b>issued</b>: 01/12/2012 12:00:00 PM</p><p><b>performer</b>: <a>Practitioner/example</a></p><h3>Images</h3><table><tr><td>-</td><td><b>Comment</b></td><td><b>Link</b></td></tr><tr><td>*</td><td>A comment about the image</td><td><a>WADO example image</a></td></tr></table><p><b>conclusion</b>: Unremarkable study</p></div>"
    assert inst.text.status == "generated"


def test_DiagnosticReport_8(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-example.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_8(inst2)


def impl_DiagnosticReport_8(inst):
    assert inst.category.coding[0].code == "HM"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "58410-2"
    assert inst.code.coding[0].display == "Complete blood count (hemogram) panel - Blood by Automated count"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.coding[1].code == "CBC"
    assert inst.code.coding[1].display == "MASTER FULL BLOOD COUNT"
    assert inst.code.text == "Complete Blood Count"
    assert inst.contained[0].code.coding[0].code == "718-7"
    assert inst.contained[0].code.coding[0].display == "Hemoglobin [Mass/volume] in Blood"
    assert inst.contained[0].code.coding[0].system == "http://loinc.org"
    assert inst.contained[0].code.text == "Haemoglobin"
    assert inst.contained[0].id == "r1"
    assert inst.contained[0].referenceRange[0].high.code == "g/L"
    assert inst.contained[0].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[0].referenceRange[0].high.unit == "g/L"
    assert inst.contained[0].referenceRange[0].high.value == Decimal("180")
    assert inst.contained[0].referenceRange[0].low.code == "g/L"
    assert inst.contained[0].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[0].referenceRange[0].low.unit == "g/L"
    assert inst.contained[0].referenceRange[0].low.value == Decimal("135")
    assert inst.contained[0].status == "final"
    assert inst.contained[0].valueQuantity.code == "g/L"
    assert inst.contained[0].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[0].valueQuantity.unit == "g/L"
    assert inst.contained[0].valueQuantity.value == Decimal("176")
    assert inst.contained[1].code.coding[0].code == "789-8"
    assert inst.contained[1].code.coding[0].display == "Erythrocytes [#/volume] in Blood by Automated count"
    assert inst.contained[1].code.coding[0].system == "http://loinc.org"
    assert inst.contained[1].code.text == "Red Cell Count"
    assert inst.contained[1].id == "r2"
    assert inst.contained[1].referenceRange[0].high.code == "10*12/L"
    assert inst.contained[1].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[1].referenceRange[0].high.unit == "x10*12/L"
    assert inst.contained[1].referenceRange[0].high.value == Decimal("6.0")
    assert inst.contained[1].referenceRange[0].low.code == "10*12/L"
    assert inst.contained[1].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[1].referenceRange[0].low.unit == "x10*12/L"
    assert inst.contained[1].referenceRange[0].low.value == Decimal("4.2")
    assert inst.contained[1].status == "final"
    assert inst.contained[1].valueQuantity.code == "10*12/L"
    assert inst.contained[1].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[1].valueQuantity.unit == "x10*12/L"
    assert inst.contained[1].valueQuantity.value == Decimal("5.9")
    assert inst.contained[2].code.coding[0].code == "4544-3"
    assert inst.contained[2].code.coding[0].display == "Hematocrit [Volume Fraction] of Blood by Automated count"
    assert inst.contained[2].code.coding[0].system == "http://loinc.org"
    assert inst.contained[2].code.text == "Haematocrit"
    assert inst.contained[2].id == "r3"
    assert inst.contained[2].interpretation.coding[0].code == "H"
    assert inst.contained[2].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[2].referenceRange[0].high.unit == "%"
    assert inst.contained[2].referenceRange[0].high.value == Decimal("52")
    assert inst.contained[2].referenceRange[0].low.unit == "%"
    assert inst.contained[2].referenceRange[0].low.value == Decimal("38")
    assert inst.contained[2].status == "final"
    assert inst.contained[2].valueQuantity.unit == "%"
    assert inst.contained[2].valueQuantity.value == Decimal("55")
    assert inst.contained[3].code.coding[0].code == "787-2"
    assert inst.contained[3].code.coding[0].display == "Erythrocyte mean corpuscular volume [Entitic volume] by Automated count"
    assert inst.contained[3].code.coding[0].system == "http://loinc.org"
    assert inst.contained[3].code.text == "Mean Cell Volume"
    assert inst.contained[3].id == "r4"
    assert inst.contained[3].interpretation.coding[0].code == "H"
    assert inst.contained[3].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[3].referenceRange[0].high.code == "fL"
    assert inst.contained[3].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[3].referenceRange[0].high.unit == "fL"
    assert inst.contained[3].referenceRange[0].high.value == Decimal("98")
    assert inst.contained[3].referenceRange[0].low.code == "fL"
    assert inst.contained[3].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[3].referenceRange[0].low.unit == "fL"
    assert inst.contained[3].referenceRange[0].low.value == Decimal("80")
    assert inst.contained[3].status == "final"
    assert inst.contained[3].valueQuantity.code == "fL"
    assert inst.contained[3].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[3].valueQuantity.unit == "fL"
    assert inst.contained[3].valueQuantity.value == Decimal("99")
    assert inst.contained[4].code.coding[0].code == "785-6"
    assert inst.contained[4].code.coding[0].display == "Erythrocyte mean corpuscular hemoglobin [Entitic mass] by Automated count"
    assert inst.contained[4].code.coding[0].system == "http://loinc.org"
    assert inst.contained[4].code.text == "Mean Cell Haemoglobin"
    assert inst.contained[4].id == "r5"
    assert inst.contained[4].interpretation.coding[0].code == "H"
    assert inst.contained[4].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[4].referenceRange[0].high.code == "pg"
    assert inst.contained[4].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[4].referenceRange[0].high.unit == "pg"
    assert inst.contained[4].referenceRange[0].high.value == Decimal("35")
    assert inst.contained[4].referenceRange[0].low.code == "pg"
    assert inst.contained[4].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[4].referenceRange[0].low.unit == "pg"
    assert inst.contained[4].referenceRange[0].low.value == Decimal("27")
    assert inst.contained[4].status == "final"
    assert inst.contained[4].valueQuantity.code == "pg"
    assert inst.contained[4].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[4].valueQuantity.unit == "pg"
    assert inst.contained[4].valueQuantity.value == Decimal("36")
    assert inst.contained[5].code.coding[0].code == "777-3"
    assert inst.contained[5].code.coding[0].display == "Platelets [#/volume] in Blood by Automated count"
    assert inst.contained[5].code.coding[0].system == "http://loinc.org"
    assert inst.contained[5].code.text == "Platelet Count"
    assert inst.contained[5].id == "r6"
    assert inst.contained[5].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[5].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[5].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[5].referenceRange[0].high.value == Decimal("450")
    assert inst.contained[5].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[5].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[5].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[5].referenceRange[0].low.value == Decimal("150")
    assert inst.contained[5].status == "final"
    assert inst.contained[5].valueQuantity.code == "10*9/L"
    assert inst.contained[5].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[5].valueQuantity.unit == "x10*9/L"
    assert inst.contained[5].valueQuantity.value == Decimal("444")
    assert inst.contained[6].code.coding[0].code == "6690-2"
    assert inst.contained[6].code.coding[0].display == "Leukocytes [#/volume] in Blood by Automated count"
    assert inst.contained[6].code.coding[0].system == "http://loinc.org"
    assert inst.contained[6].code.text == "White Cell Count"
    assert inst.contained[6].id == "r7"
    assert inst.contained[6].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[6].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[6].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[6].referenceRange[0].high.value == Decimal("11.0")
    assert inst.contained[6].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[6].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[6].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[6].referenceRange[0].low.value == Decimal("4.0")
    assert inst.contained[6].status == "final"
    assert inst.contained[6].valueQuantity.code == "10*9/L"
    assert inst.contained[6].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[6].valueQuantity.unit == "x10*9/L"
    assert inst.contained[6].valueQuantity.value == Decimal("4.6")
    assert inst.contained[7].code.coding[0].code == "770-8"
    assert inst.contained[7].code.coding[0].display == "Neutrophils/100 leukocytes in Blood by Automated count"
    assert inst.contained[7].code.coding[0].system == "http://loinc.org"
    assert inst.contained[7].code.text == "Neutrophils"
    assert inst.contained[7].id == "r8"
    assert inst.contained[7].status == "final"
    assert inst.contained[7].valueQuantity.code == "%"
    assert inst.contained[7].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[7].valueQuantity.unit == "%"
    assert inst.contained[7].valueQuantity.value == Decimal("20")
    assert inst.contained[8].code.coding[0].code == "751-8"
    assert inst.contained[8].code.coding[0].display == "Neutrophils [#/volume] in Blood by Automated count"
    assert inst.contained[8].code.coding[0].system == "http://loinc.org"
    assert inst.contained[8].code.text == "Neutrophils"
    assert inst.contained[8].id == "r9"
    assert inst.contained[8].interpretation.coding[0].code == "LL"
    assert inst.contained[8].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[8].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[8].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[8].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[8].referenceRange[0].high.value == Decimal("7.5")
    assert inst.contained[8].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[8].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[8].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[8].referenceRange[0].low.value == Decimal("2.0")
    assert inst.contained[8].status == "final"
    assert inst.contained[8].valueQuantity.code == "10*9/L"
    assert inst.contained[8].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[8].valueQuantity.unit == "x10*9/L"
    assert inst.contained[8].valueQuantity.value == Decimal("0.9")
    assert inst.contained[9].code.coding[0].code == "736-9"
    assert inst.contained[9].code.coding[0].display == "Lymphocytes/100 leukocytes in Blood by Automated count"
    assert inst.contained[9].code.coding[0].system == "http://loinc.org"
    assert inst.contained[9].code.text == "Lymphocytes"
    assert inst.contained[9].id == "r10"
    assert inst.contained[9].status == "final"
    assert inst.contained[9].valueQuantity.code == "%"
    assert inst.contained[9].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[9].valueQuantity.unit == "%"
    assert inst.contained[9].valueQuantity.value == Decimal("20")
    assert inst.contained[10].code.coding[0].code == "731-0"
    assert inst.contained[10].code.coding[0].display == "Lymphocytes [#/volume] in Blood by Automated count"
    assert inst.contained[10].code.coding[0].system == "http://loinc.org"
    assert inst.contained[10].code.text == "Lymphocytes"
    assert inst.contained[10].id == "r11"
    assert inst.contained[10].interpretation.coding[0].code == "L"
    assert inst.contained[10].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[10].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[10].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[10].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[10].referenceRange[0].high.value == Decimal("4.0")
    assert inst.contained[10].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[10].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[10].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[10].referenceRange[0].low.value == Decimal("1.1")
    assert inst.contained[10].status == "final"
    assert inst.contained[10].valueQuantity.code == "10*9/L"
    assert inst.contained[10].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[10].valueQuantity.unit == "x10*9/L"
    assert inst.contained[10].valueQuantity.value == Decimal("0.9")
    assert inst.contained[11].code.coding[0].code == "5905-5"
    assert inst.contained[11].code.coding[0].display == "Monocytes/100 leukocytes in Blood by Automated count"
    assert inst.contained[11].code.coding[0].system == "http://loinc.org"
    assert inst.contained[11].code.text == "Monocytes"
    assert inst.contained[11].id == "r12"
    assert inst.contained[11].status == "final"
    assert inst.contained[11].valueQuantity.code == "%"
    assert inst.contained[11].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[11].valueQuantity.unit == "%"
    assert inst.contained[11].valueQuantity.value == Decimal("20")
    assert inst.contained[12].code.coding[0].code == "742-7"
    assert inst.contained[12].code.coding[0].display == "Monocytes [#/volume] in Blood by Automated count"
    assert inst.contained[12].code.coding[0].system == "http://loinc.org"
    assert inst.contained[12].code.text == "Monocytes"
    assert inst.contained[12].id == "r13"
    assert inst.contained[12].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[12].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[12].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[12].referenceRange[0].high.value == Decimal("1.0")
    assert inst.contained[12].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[12].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[12].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[12].referenceRange[0].low.value == Decimal("0.2")
    assert inst.contained[12].status == "final"
    assert inst.contained[12].valueQuantity.code == "10*9/L"
    assert inst.contained[12].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[12].valueQuantity.unit == "x10*9/L"
    assert inst.contained[12].valueQuantity.value == Decimal("0.9")
    assert inst.contained[13].code.coding[0].code == "713-8"
    assert inst.contained[13].code.coding[0].display == "Eosinophils/100 leukocytes in Blood by Automated count"
    assert inst.contained[13].code.coding[0].system == "http://loinc.org"
    assert inst.contained[13].code.text == "Eosinophils"
    assert inst.contained[13].id == "r14"
    assert inst.contained[13].status == "final"
    assert inst.contained[13].valueQuantity.code == "%"
    assert inst.contained[13].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[13].valueQuantity.unit == "%"
    assert inst.contained[13].valueQuantity.value == Decimal("20")
    assert inst.contained[14].code.coding[0].code == "711-2"
    assert inst.contained[14].code.coding[0].display == "Eosinophils [#/volume] in Blood by Automated count"
    assert inst.contained[14].code.coding[0].system == "http://loinc.org"
    assert inst.contained[14].code.text == "Eosinophils"
    assert inst.contained[14].id == "r15"
    assert inst.contained[14].interpretation.coding[0].code == "HH"
    assert inst.contained[14].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[14].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[14].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[14].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[14].referenceRange[0].high.value == Decimal("0.4")
    assert inst.contained[14].referenceRange[0].low.code == "10*9/L"
    assert inst.contained[14].referenceRange[0].low.system == "http://unitsofmeasure.org"
    assert inst.contained[14].referenceRange[0].low.unit == "x10*9/L"
    assert inst.contained[14].referenceRange[0].low.value == Decimal("0.04")
    assert inst.contained[14].status == "final"
    assert inst.contained[14].valueQuantity.code == "10*9/L"
    assert inst.contained[14].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[14].valueQuantity.unit == "x10*9/L"
    assert inst.contained[14].valueQuantity.value == Decimal("0.92")
    assert inst.contained[15].code.coding[0].code == "706-2"
    assert inst.contained[15].code.coding[0].display == "Basophils/100 leukocytes in Blood by Automated count"
    assert inst.contained[15].code.coding[0].system == "http://loinc.org"
    assert inst.contained[15].code.text == "Basophils"
    assert inst.contained[15].id == "r16"
    assert inst.contained[15].status == "final"
    assert inst.contained[15].valueQuantity.code == "%"
    assert inst.contained[15].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[15].valueQuantity.unit == "%"
    assert inst.contained[15].valueQuantity.value == Decimal("20")
    assert inst.contained[16].code.coding[0].code == "704-7"
    assert inst.contained[16].code.coding[0].display == "Basophils [#/volume] in Blood by Automated count"
    assert inst.contained[16].code.coding[0].system == "http://loinc.org"
    assert inst.contained[16].code.text == "Basophils"
    assert inst.contained[16].id == "r17"
    assert inst.contained[16].referenceRange[0].high.code == "10*9/L"
    assert inst.contained[16].referenceRange[0].high.system == "http://unitsofmeasure.org"
    assert inst.contained[16].referenceRange[0].high.unit == "x10*9/L"
    assert inst.contained[16].referenceRange[0].high.value == Decimal("0.21")
    assert inst.contained[16].status == "final"
    assert inst.contained[16].valueQuantity.code == "10*9/L"
    assert inst.contained[16].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.contained[16].valueQuantity.unit == "x10*9/L"
    assert inst.contained[16].valueQuantity.value == Decimal("0.92")
    assert inst.effectiveDateTime == datetime.fromisoformat("2011-03-04T08:30:00+11:00")
    assert inst.extension[0].url == "http://hl7.org/fhir/StructureDefinition/diagnosticReport-locationPerformed"
    assert inst.extension[0].valueReference.reference == "Location/example"
    assert inst.id == "diagnosticreport-example"
    assert inst.identifier[0].system == "http://acme.com/lab/reports"
    assert inst.identifier[0].value == "5234342"
    assert inst.issued == datetime.fromisoformat("2011-03-04T11:45:33+11:00")
    assert inst.performer.display == "Acme Laboratory, Inc"
    assert inst.performer.reference == "Organization/1832473e-2fe0-452d-abe9-3cdb9879522f"
    assert inst.presentedForm[0].contentType == "application/pdf"
    assert inst.presentedForm[0].data == b"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PSdodHRwOi8vbnMuYWRvYmUuY29tL3BkZi8xLjMvJz48cGRmOlByb2R1Y2VyPkdQTCBHaG9zdHNjcmlwdCA5LjA0PC9wZGY6UHJvZHVjZXI+CjxwZGY6S2V5d29yZHM+KCk8L3BkZjpLZXl3b3Jkcz4KPC9yZGY6RGVzY3JpcHRpb24+CjxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSdlOTA4ODRhMy0zYzlhLTExZTEtMDAwMC02NDI2MDMzYWE1MCYjODsnIHhtbG5zOnhtcD0naHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyc+PHhtcDpNb2RpZnlEYXRlPjIwMTItMDEtMDlUMDg6MjU6NTQrMTE6MDA8L3htcDpNb2RpZnlEYXRlPgo8eG1wOkNyZWF0ZURhdGU+MjAxMi0wMS0wOVQwODoyNTo1NCsxMTowMDwveG1wOkNyZWF0ZURhdGU+Cjx4bXA6Q3JlYXRvclRvb2w+UERGQ3JlYXRvciBWZXJzaW9uIDEuMi4zPC94bXA6Q3JlYXRvclRvb2w+PC9yZGY6RGVzY3JpcHRpb24+CjxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSdlOTA4ODRhMy0zYzlhLTExZTEtMDAwMC02NDI2MDMzYWE1MCYjODsnIHhtbG5zOnhhcE1NPSdodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vJyB4YXBNTTpEb2N1bWVudElEPSd1dWlkOmU5MDg4NGEzLTNjOWEtMTFlMS0wMDAwLTY0MjYwMzNhYTUwJiMxMzg7pyYjMTU3O+7SYyYjMzE7JiMxNjsnLz4KPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9J2U5MDg4NGEzLTNjOWEtMTFlMS0wMDAwLTY0MjYwMzNhYTUwJiM4OycgeG1sbnM6ZGM9J2h0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvJyBkYzpmb3JtYXQ9J2FwcGxpY2F0aW9uL3BkZic+PGRjOnRpdGxlPjxyZGY6QWx0PjxyZGY6bGkgeG1sOmxhbmc9J3gtZGVmYXVsdCc+Q0JDIFJlcG9ydCBmb3IgV2lsZS4gRS4gQ09ZT1RFIChNUk46IDIzNDUzKSBpc3N1ZWQgMy1NYXIgMjAxMSAxMTo0NTwvcmRmOmxpPjwvcmRmOkFsdD48L2RjOnRpdGxlPjxkYzpjcmVhdG9yPjxyZGY6U2VxPjxyZGY6bGk+R3JhaGFtZTwvcmRmOmxpPjwvcmRmOlNlcT48L2RjOmNyZWF0b3I+PGRjOmRlc2NyaXB0aW9uPjxyZGY6U2VxPjxyZGY6bGk+KCk8L3JkZjpsaT48L3JkZjpTZXE+PC9kYzpkZXNjcmlwdGlvbj48L3JkZjpEZXNjcmlwdGlvbj4KPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSd3Jz8+CmVuZHN0cmVhbQplbmRvYmoKMiAwIG9iago8PC9Qcm9kdWNlcihHUEwgR2hvc3RzY3JpcHQgOS4wNCkKL0NyZWF0aW9uRGF0ZShEOjIwMTIwMTA5MDgyNTU0KzExJzAwJykKL01vZERhdGUoRDoyMDEyMDEwOTA4MjU1NCsxMScwMCcpCi9UaXRsZShcMzc2XDM3N1wwMDBDXDAwMEJcMDAwQ1wwMDAgXDAwMFJcMDAwZVwwMDBwXDAwMG9cMDAwclwwMDB0XDAwMCBcMDAwZlwwMDBvXDAwMHJcMDAwIFwwMDBXXDAwMGlcMDAwbFwwMDBlXDAwMC5cMDAwIFwwMDBFXDAwMC5cMDAwIFwwMDBDXDAwME9cMDAwWVwwMDBPXDAwMFRcMDAwRVwwMDAgXDAwMFwoXDAwME1cMDAwUlwwMDBOXDAwMDpcMDAwIFwwMDAyXDAwMDNcMDAwNFwwMDA1XDAwMDNcMDAwXClcMDAwIFwwMDBpXDAwMHNcMDAwc1wwMDB1XDAwMGVcMDAwZFwwMDAgXDAwMDNcMDAwLVwwMDBNXDAwMGFcMDAwclwwMDAgXDAwMDJcMDAwMFwwMDAxXDAwMDFcMDAwIFwwMDAxXDAwMDFcMDAwOlwwMDA0XDAwMDUpCi9DcmVhdG9yKFwzNzZcMzc3XDAwMFBcMDAwRFwwMDBGXDAwMENcMDAwclwwMDBlXDAwMGFcMDAwdFwwMDBvXDAwMHJcMDAwIFwwMDBWXDAwMGVcMDAwclwwMDBzXDAwMGlcMDAwb1wwMDBuXDAwMCBcMDAwMVwwMDAuXDAwMDJcMDAwLlwwMDAzKQovQXV0aG9yKFwzNzZcMzc3XDAwMEdcMDAwclwwMDBhXDAwMGhcMDAwYVwwMDBtXDAwMGUpCi9LZXl3b3JkcygpCi9TdWJqZWN0KCk+PmVuZG9iagp4cmVmCjAgMjEKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAyMTM3IDAwMDAwIG4gCjAwMDAwNjg3OTMgMDAwMDAgbiAKMDAwMDAwMjA3OCAwMDAwMCBuIAowMDAwMDAxOTM2IDAwMDAwIG4gCjAwMDAwMDAwMTUgMDAwMDAgbiAKMDAwMDAwMTkxNiAwMDAwMCBuIAowMDAwMDAyNjU2IDAwMDAwIG4gCjAwMDAwMDQ2ODEgMDAwMDAgbiAKMDAwMDAwMzQ3OSAwMDAwMCBuIAowMDAwMDIxNTc3IDAwMDAwIG4gCjAwMDAwMDQzMjkgMDAwMDAgbiAKMDAwMDA0MTMwNyAwMDAwMCBuIAowMDAwMDAyMjAyIDAwMDAwIG4gCjAwMDAwMDQ5MDUgMDAwMDAgbiAKMDAwMDAyMTc5MyAwMDAwMCBuIAowMDAwMDQxNTI5IDAwMDAwIG4gCjAwMDAwMDIyNTIgMDAwMDAgbiAKMDAwMDAwMjk0OCAwMDAwMCBuIAowMDAwMDAzODMxIDAwMDAwIG4gCjAwMDAwNjcwODggMDAwMDAgbiAKdHJhaWxlcgo8PCAvU2l6ZSAyMSAvUm9vdCAxIDAgUiAvSW5mbyAyIDAgUgovSUQgWzw4RDdGNzc5QTAwQzcwOTc5NTg3MDQyRjA5MkJBQjhDNj48OEQ3Rjc3OUEwMEM3MDk3OTU4NzA0MkYwOTJCQUI4QzY+XQo+PgpzdGFydHhyZWYKNjk0ODUKJSVFT0YK"
    assert inst.presentedForm[0].language == "en-AU"
    assert inst.presentedForm[0].title == "HTML Report"
    assert inst.result[0].reference == "#r1"
    assert inst.result[1].reference == "#r2"
    assert inst.result[2].reference == "#r3"
    assert inst.result[3].reference == "#r4"
    assert inst.result[4].reference == "#r5"
    assert inst.result[5].reference == "#r6"
    assert inst.result[6].reference == "#r7"
    assert inst.result[7].reference == "#r8"
    assert inst.result[8].reference == "#r9"
    assert inst.result[9].reference == "#r10"
    assert inst.result[10].reference == "#r11"
    assert inst.result[11].reference == "#r12"
    assert inst.result[12].reference == "#r13"
    assert inst.result[13].reference == "#r14"
    assert inst.result[14].reference == "#r15"
    assert inst.result[15].reference == "#r16"
    assert inst.result[16].reference == "#r17"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.div == """<div>
      
      
      
      
      <h3>CBC Report for Wile. E. COYOTE (MRN: 23453) issued 3-Mar 2011 11:45</h3>

            
      
      
      
      <pre>
Test                  Units       Value       Reference Range
Haemoglobin           g/L         176         135 - 180
Red Cell Count        x10*12/L    5.9         4.2 - 6.0
Haematocrit                       0.55+       0.38 - 0.52
Mean Cell Volume      fL          99+         80 - 98
Mean Cell Haemoglobin pg          36+         27 - 35
Platelet Count        x10*9/L     444         150 - 450
White Cell Count      x10*9/L     4.6         4.0 - 11.0
Neutrophils           %           20
Neutrophils           x10*9/L     0.9---      2.0 - 7.5
Lymphocytes           %           20
Lymphocytes           x10*9/L     0.9-        1.1 - 4.0
Monocytes             %           20
Monocytes             x10*9/L     0.9         0.2 - 1.0
Eosinophils           %           20
Eosinophils           x10*9/L     0.92++      0.04 - 0.40
Basophils             %           20
Basophils             x10*9/L     0.92+++     &lt;0.21
      </pre>
          
      
      
      
      <p>Acme Laboratory, Inc signed: Dr Pete Pathologist</p>
      
    
    
    
    </div>"""
    assert inst.text.status == "generated"


def test_DiagnosticReport_9(base_settings):
    filename = base_settings["unittest_data_dir"] / "diagnosticreport-micro1.canonical.json"
    inst = diagnosticreport.DiagnosticReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DiagnosticReport" == inst.resource_type
    impl_DiagnosticReport_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DiagnosticReport" == data["resourceType"]

    inst2 = diagnosticreport.DiagnosticReport(**data)
    impl_DiagnosticReport_9(inst2)


def impl_DiagnosticReport_9(inst):
    assert inst.category.coding[0].code == "MB"
    assert inst.category.coding[0].system == "http://hl7.org/fhir/v2/0074"
    assert inst.code.coding[0].code == "632-0"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.code.text == "Culture, MRSA"
    assert inst.contained[0].code.coding[0].code == "ORGANISM"
    assert inst.contained[0].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[0].id == "obx1-4"
    assert inst.contained[0].performer[0].display == "Todd Ashby"
    assert inst.contained[0].status == "final"
    assert inst.contained[0].subject.reference == "Patient/example"
    assert inst.contained[0].valueCodeableConcept.coding[0].code == "Staaur"
    assert inst.contained[0].valueCodeableConcept.coding[0].system == "http://acme.org/lab/codes/organisms"
    assert inst.contained[0].valueCodeableConcept.text == "Staphylococcus aureus"
    assert inst.contained[1].code.coding[0].code == "CULTPOSNEG"
    assert inst.contained[1].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[1].id == "obx1-5"
    assert inst.contained[1].performer[0].display == "Todd Ashby"
    assert inst.contained[1].status == "final"
    assert inst.contained[1].subject.reference == "Patient/example"
    assert inst.contained[1].valueCodeableConcept.coding[0].code == "POS"
    assert inst.contained[1].valueCodeableConcept.coding[0].system == "http://acme.org/lab/codes/flags"
    assert inst.contained[2].code.coding[0].code == "60504"
    assert inst.contained[2].code.coding[0].display == "Ampicillin"
    assert inst.contained[2].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[2].id == "obx2-1"
    assert inst.contained[2].interpretation.coding[0].code == "R"
    assert inst.contained[2].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[2].performer[0].display == "Todd Ashby"
    assert inst.contained[2].status == "final"
    assert inst.contained[2].subject.reference == "Patient/example"
    assert inst.contained[3].code.coding[0].code == "60512"
    assert inst.contained[3].code.coding[0].display == "Cefazolin"
    assert inst.contained[3].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[3].id == "obx2-2"
    assert inst.contained[3].interpretation.coding[0].code == "S"
    assert inst.contained[3].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[3].performer[0].display == "Todd Ashby"
    assert inst.contained[3].status == "final"
    assert inst.contained[3].subject.reference == "Patient/example"
    assert inst.contained[3].valueQuantity.comparator == "<="
    assert inst.contained[3].valueQuantity.value == Decimal("2")
    assert inst.contained[4].code.coding[0].code == "60516"
    assert inst.contained[4].code.coding[0].display == "Cefoxitin"
    assert inst.contained[4].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[4].id == "obx2-4"
    assert inst.contained[4].interpretation.coding[0].code == "S"
    assert inst.contained[4].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[4].performer[0].display == "Todd Ashby"
    assert inst.contained[4].status == "final"
    assert inst.contained[4].subject.reference == "Patient/example"
    assert inst.contained[4].valueQuantity.comparator == "<="
    assert inst.contained[4].valueQuantity.value == Decimal("4")
    assert inst.contained[5].code.coding[0].code == "60527"
    assert inst.contained[5].code.coding[0].display == "Clindamycin"
    assert inst.contained[5].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[5].id == "obx2-6"
    assert inst.contained[5].interpretation.coding[0].code == "S"
    assert inst.contained[5].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[5].performer[0].display == "Todd Ashby"
    assert inst.contained[5].status == "final"
    assert inst.contained[5].subject.reference == "Patient/example"
    assert inst.contained[5].valueQuantity.comparator == ">="
    assert inst.contained[5].valueQuantity.value == Decimal("0.5")
    assert inst.contained[6].code.coding[0].code == "61203"
    assert inst.contained[6].code.coding[0].display == "Daptomycin"
    assert inst.contained[6].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[6].id == "obx2-8"
    assert inst.contained[6].interpretation.coding[0].code == "S"
    assert inst.contained[6].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[6].performer[0].display == "Todd Ashby"
    assert inst.contained[6].status == "final"
    assert inst.contained[6].subject.reference == "Patient/example"
    assert inst.contained[6].valueQuantity.comparator == ">="
    assert inst.contained[6].valueQuantity.value == Decimal("1")
    assert inst.contained[7].code.coding[0].code == "60532"
    assert inst.contained[7].code.coding[0].display == "Doxycycline"
    assert inst.contained[7].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[7].id == "obx2-10"
    assert inst.contained[7].interpretation.coding[0].code == "S"
    assert inst.contained[7].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[7].performer[0].display == "Todd Ashby"
    assert inst.contained[7].status == "final"
    assert inst.contained[7].subject.reference == "Patient/example"
    assert inst.contained[7].valueQuantity.comparator == "<="
    assert inst.contained[7].valueQuantity.value == Decimal("0.5")
    assert inst.contained[8].code.coding[0].code == "60533"
    assert inst.contained[8].code.coding[0].display == "Erythromycin"
    assert inst.contained[8].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[8].id == "obx2-12"
    assert inst.contained[8].interpretation.coding[0].code == "R"
    assert inst.contained[8].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[8].performer[0].display == "Todd Ashby"
    assert inst.contained[8].status == "final"
    assert inst.contained[8].subject.reference == "Patient/example"
    assert inst.contained[8].valueQuantity.comparator == ">="
    assert inst.contained[8].valueQuantity.value == Decimal("8")
    assert inst.contained[9].code.coding[0].code == "60536"
    assert inst.contained[9].code.coding[0].display == "Gentamicin"
    assert inst.contained[9].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[9].id == "obx2-14"
    assert inst.contained[9].interpretation.coding[0].code == "S"
    assert inst.contained[9].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[9].performer[0].display == "Todd Ashby"
    assert inst.contained[9].status == "final"
    assert inst.contained[9].subject.reference == "Patient/example"
    assert inst.contained[9].valueQuantity.comparator == "<="
    assert inst.contained[9].valueQuantity.value == Decimal("2")
    assert inst.contained[10].code.coding[0].code == "61007"
    assert inst.contained[10].code.coding[0].display == "Levofloxacin"
    assert inst.contained[10].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[10].id == "obx2-16"
    assert inst.contained[10].interpretation.coding[0].code == "S"
    assert inst.contained[10].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[10].performer[0].display == "Todd Ashby"
    assert inst.contained[10].status == "final"
    assert inst.contained[10].subject.reference == "Patient/example"
    assert inst.contained[10].valueQuantity.comparator == "<="
    assert inst.contained[10].valueQuantity.value == Decimal("0.5")
    assert inst.contained[11].code.coding[0].code == "60699"
    assert inst.contained[11].code.coding[0].display == "Linezolid"
    assert inst.contained[11].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[11].id == "obx2-18"
    assert inst.contained[11].interpretation.coding[0].code == "S"
    assert inst.contained[11].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[11].performer[0].display == "Todd Ashby"
    assert inst.contained[11].status == "final"
    assert inst.contained[11].subject.reference == "Patient/example"
    assert inst.contained[11].valueQuantity.value == Decimal("4")
    assert inst.contained[12].code.coding[0].code == "61204"
    assert inst.contained[12].code.coding[0].display == "Moxifloxacin"
    assert inst.contained[12].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[12].id == "obx2-20"
    assert inst.contained[12].interpretation.coding[0].code == "S"
    assert inst.contained[12].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[12].performer[0].display == "Todd Ashby"
    assert inst.contained[12].status == "final"
    assert inst.contained[12].subject.reference == "Patient/example"
    assert inst.contained[12].valueQuantity.comparator == "<="
    assert inst.contained[12].valueQuantity.value == Decimal("0.5")
    assert inst.contained[13].code.coding[0].code == "60551"
    assert inst.contained[13].code.coding[0].display == "Oxacillin"
    assert inst.contained[13].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[13].id == "obx2-22"
    assert inst.contained[13].interpretation.coding[0].code == "S"
    assert inst.contained[13].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[13].performer[0].display == "Todd Ashby"
    assert inst.contained[13].status == "final"
    assert inst.contained[13].subject.reference == "Patient/example"
    assert inst.contained[13].valueQuantity.value == Decimal("0.5")
    assert inst.contained[14].code.coding[0].code == "60552"
    assert inst.contained[14].code.coding[0].display == "Penicillin"
    assert inst.contained[14].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[14].id == "obx2-24"
    assert inst.contained[14].interpretation.coding[0].code == "R"
    assert inst.contained[14].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[14].performer[0].display == "Todd Ashby"
    assert inst.contained[14].status == "final"
    assert inst.contained[14].subject.reference == "Patient/example"
    assert inst.contained[14].valueQuantity.comparator == ">="
    assert inst.contained[14].valueQuantity.value == Decimal("2")
    assert inst.contained[15].code.coding[0].code == "60697"
    assert inst.contained[15].code.coding[0].display == "Quinupristin/Dalfopristin"
    assert inst.contained[15].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[15].id == "obx2-26"
    assert inst.contained[15].interpretation.coding[0].code == "S"
    assert inst.contained[15].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[15].performer[0].display == "Todd Ashby"
    assert inst.contained[15].status == "final"
    assert inst.contained[15].subject.reference == "Patient/example"
    assert inst.contained[15].valueQuantity.value == Decimal("0.5")
    assert inst.contained[16].code.coding[0].code == "60555"
    assert inst.contained[16].code.coding[0].display == "Rifampin"
    assert inst.contained[16].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[16].id == "obx2-28"
    assert inst.contained[16].interpretation.coding[0].code == "S"
    assert inst.contained[16].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[16].performer[0].display == "Todd Ashby"
    assert inst.contained[16].status == "final"
    assert inst.contained[16].subject.reference == "Patient/example"
    assert inst.contained[16].valueQuantity.comparator == "<="
    assert inst.contained[16].valueQuantity.value == Decimal("0.5")
    assert inst.contained[17].code.coding[0].code == "60558"
    assert inst.contained[17].code.coding[0].display == "Tetracycline"
    assert inst.contained[17].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[17].id == "obx2-30"
    assert inst.contained[17].interpretation.coding[0].code == "S"
    assert inst.contained[17].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[17].performer[0].display == "Todd Ashby"
    assert inst.contained[17].status == "final"
    assert inst.contained[17].subject.reference == "Patient/example"
    assert inst.contained[17].valueQuantity.comparator == "<="
    assert inst.contained[17].valueQuantity.value == Decimal("0.5")
    assert inst.contained[18].code.coding[0].code == "60561"
    assert inst.contained[18].code.coding[0].display == "Trimethoprim/Sulfamethoxazole"
    assert inst.contained[18].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[18].id == "obx2-32"
    assert inst.contained[18].interpretation.coding[0].code == "S"
    assert inst.contained[18].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[18].performer[0].display == "Todd Ashby"
    assert inst.contained[18].status == "final"
    assert inst.contained[18].subject.reference == "Patient/example"
    assert inst.contained[18].valueQuantity.comparator == "<="
    assert inst.contained[18].valueQuantity.value == Decimal("0.0526")
    assert inst.contained[19].code.coding[0].code == "60563"
    assert inst.contained[19].code.coding[0].display == "Vancomycin"
    assert inst.contained[19].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[19].id == "obx2-34"
    assert inst.contained[19].interpretation.coding[0].code == "S"
    assert inst.contained[19].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[19].performer[0].display == "Todd Ashby"
    assert inst.contained[19].status == "final"
    assert inst.contained[19].subject.reference == "Patient/example"
    assert inst.contained[19].valueQuantity.value == Decimal("1")
    assert inst.contained[20].code.coding[0].code == "2099930"
    assert inst.contained[20].code.coding[0].display == "D-Test"
    assert inst.contained[20].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[20].id == "nte-1"
    assert inst.contained[20].performer[0].display == "Todd Ashby"
    assert inst.contained[20].status == "final"
    assert inst.contained[20].subject.reference == "Patient/example"
    assert inst.contained[20].valueString == "D-Test:  Negative - This isolate does not demonstrate inducible clindamycin resistance in vitro."
    assert inst.contained[21].code.coding[0].code == "60036"
    assert inst.contained[21].code.coding[0].display == "Oxacillin"
    assert inst.contained[21].code.coding[0].system == "http://acme.org/lab/codes/tests"
    assert inst.contained[21].id == "obx3-1"
    assert inst.contained[21].interpretation.coding[0].code == "S"
    assert inst.contained[21].interpretation.coding[0].system == "http://hl7.org/fhir/v2/0078"
    assert inst.contained[21].performer[0].display == "Todd Ashby"
    assert inst.contained[21].status == "final"
    assert inst.contained[21].subject.reference == "Patient/example"
    assert inst.contained[22].code.coding[0].code == "60790"
    assert inst.contained[22].code.coding[0].display == "Susceptibility - Automated broth dilution (Billed)"
    assert inst.contained[22].code.coding[0].system == "http://acme.org/lab/codes/panels"
    assert inst.contained[22].id == "obr-2"
    assert inst.contained[22].performer[0].display == "Todd Ashby"
    assert inst.contained[22].related[0].target.reference == "#obx2-1"
    assert inst.contained[22].related[0].type == "has-member"
    assert inst.contained[22].related[1].target.reference == "#obx2-2"
    assert inst.contained[22].related[1].type == "has-member"
    assert inst.contained[22].related[2].target.reference == "#obx2-4"
    assert inst.contained[22].related[2].type == "has-member"
    assert inst.contained[22].related[3].target.reference == "#obx2-6"
    assert inst.contained[22].related[3].type == "has-member"
    assert inst.contained[22].related[4].target.reference == "#obx2-8"
    assert inst.contained[22].related[4].type == "has-member"
    assert inst.contained[22].related[5].target.reference == "#obx2-10"
    assert inst.contained[22].related[5].type == "has-member"
    assert inst.contained[22].related[6].target.reference == "#obx2-12"
    assert inst.contained[22].related[6].type == "has-member"
    assert inst.contained[22].related[7].target.reference == "#obx2-14"
    assert inst.contained[22].related[7].type == "has-member"
    assert inst.contained[22].related[8].target.reference == "#obx2-16"
    assert inst.contained[22].related[8].type == "has-member"
    assert inst.contained[22].related[9].target.reference == "#obx2-18"
    assert inst.contained[22].related[9].type == "has-member"
    assert inst.contained[22].related[10].target.reference == "#obx2-20"
    assert inst.contained[22].related[10].type == "has-member"
    assert inst.contained[22].related[11].target.reference == "#obx2-22"
    assert inst.contained[22].related[11].type == "has-member"
    assert inst.contained[22].related[12].target.reference == "#obx2-24"
    assert inst.contained[22].related[12].type == "has-member"
    assert inst.contained[22].related[13].target.reference == "#obx2-26"
    assert inst.contained[22].related[13].type == "has-member"
    assert inst.contained[22].related[14].target.reference == "#obx2-28"
    assert inst.contained[22].related[14].type == "has-member"
    assert inst.contained[22].related[15].target.reference == "#obx2-30"
    assert inst.contained[22].related[15].type == "has-member"
    assert inst.contained[22].related[16].target.reference == "#obx2-32"
    assert inst.contained[22].related[16].type == "has-member"
    assert inst.contained[22].related[17].target.reference == "#obx2-34"
    assert inst.contained[22].related[17].type == "has-member"
    assert inst.contained[22].related[18].target.reference == "#nte-1"
    assert inst.contained[22].related[18].type == "has-member"
    assert inst.contained[22].status == "final"
    assert inst.contained[22].subject.reference == "Patient/example"
    assert inst.contained[23].code.coding[0].code == "60418"
    assert inst.contained[23].code.coding[0].display == "Susceptibility - Disk diffusion (Billed)"
    assert inst.contained[23].code.coding[0].system == "http://acme.org/lab/codes/panels"
    assert inst.contained[23].id == "obr-3"
    assert inst.contained[23].related[0].target.reference == "#obx3-1"
    assert inst.contained[23].related[0].type == "has-member"
    assert inst.contained[23].status == "final"
    assert inst.contained[23].subject.reference == "Patient/example"
    assert inst.contained[24].code.coding[0].code == "Staaur"
    assert inst.contained[24].code.coding[0].system == "http://acme.org/lab/codes/organisms"
    assert inst.contained[24].code.text == "Staphylococcus aureus Panel"
    assert inst.contained[24].id == "org1"
    assert inst.contained[24].related[0].target.reference == "#obx1-4"
    assert inst.contained[24].related[0].type == "has-member"
    assert inst.contained[24].related[1].target.reference == "#obx1-5"
    assert inst.contained[24].related[1].type == "has-member"
    assert inst.contained[24].related[2].target.reference == "#obr-2"
    assert inst.contained[24].related[2].type == "has-member"
    assert inst.contained[24].related[3].target.reference == "#obr-3"
    assert inst.contained[24].related[3].type == "has-member"
    assert inst.contained[24].status == "final"
    assert inst.contained[24].subject.reference == "Patient/example"
    assert inst.contained[25].id == "req"
    assert inst.contained[25].identifier[0].value == "255337816"
    assert inst.contained[25].subject.reference == "Patient/example"
    assert inst.effectiveDateTime == datetime.fromisoformat("2009-08-07T19:00:00+10:00")
    assert inst.id == "micro"
    assert inst.identifier[0].system == "http://hnam.org/identifiers/orders"
    assert inst.identifier[0].value == "290741144"
    assert inst.issued == datetime.fromisoformat("2009-08-10T08:25:44+10:00")
    assert inst.performer.display == "Todd Ashby"
    assert inst.request[0].reference == "#req"
    assert inst.result[0].reference == "#org1"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: micro</p><p><b>contained</b>: , , , , , , , , , , , , , , , , , , , , , , , , , </p><p><b>identifier</b>: 290741144</p><p><b>status</b>: final</p><p><b>category</b>: Microbiology <span>(Details : {http://hl7.org/fhir/v2/0074 code 'MB' = 'Microbiology)</span></p><p><b>code</b>: Culture, MRSA <span>(Details : {LOINC code '632-0' = 'Bacteria identified in Wound by Aerobe culture)</span></p><p><b>subject</b>: <a>Patient/example</a></p><p><b>effective</b>: 07/08/2009 7:00:00 PM</p><p><b>issued</b>: 10/08/2009 8:25:44 AM</p><p><b>performer</b>: Todd Ashby</p><p><b>request</b>: id: req; Patient/example; 255337816</p><p><b>result</b>: id: org1; status: final; Staphylococcus aureus Panel <span>(Details : {http://acme.org/lab/codes/organisms code 'Staaur' = '??)</span>; Patient/example</p></div>"
    assert inst.text.status == "generated"
