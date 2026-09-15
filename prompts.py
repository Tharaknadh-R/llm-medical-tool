Summary = """
Review the Patient Record and Encounter Transcript provided above.

Instructions:

* Use only information explicitly available in the provided data.
* Do not infer, assume, estimate, predict, or hallucinate information.
* If information is unavailable, state "Not Available".
* Use professional clinical terminology.
* Prioritize information from the encounter transcript for today's visit.
* Use the patient record as supporting clinical history.
* Focus on clinical accuracy and completeness.
* Return only the report below.

====================================================
CLINICAL SUMMARY REPORT
=======================

## CLINICAL SUMMARY

Provide a concise summary of the encounter covering:

* Reason for visit
* Relevant medical history discussed
* Symptoms and concerns
* Significant findings
* Diagnoses addressed
* Treatment decisions
* Follow-up recommendations

## MINUTES OF CONVERSATION

List the 10 most important discussion points from the encounter.

## CLINICAL ASSESSMENT

Primary Diagnosis:
Secondary Conditions:
Important Clinical Findings:
Current Symptoms:
Relevant Medical History:

## RECOMMENDED NEXT STEPS

Provide documented follow-up recommendations, monitoring plans, referrals, lifestyle guidance, and next actions discussed during the encounter.

## CONCLUSION

Provide a brief clinical conclusion summarizing the patient's current status and care plan.

## AI CONFIDENCE SCORE

Confidence Score: XX/100

Reason:
Explain confidence based only on the completeness and quality of the provided information.

Rules:

* Use only documented information.
* Never create diagnoses or findings.
* Never leave sections blank.
* Write "Not Available" if information is unavailable.
  """



SOAP_Notes = """
Review the Patient Record and Encounter Transcript.

Instructions:

* Use only documented information.
* Do not infer, estimate, or hallucinate information.
* If information is unavailable, write "Not Available".
* Follow standard clinical SOAP documentation practices.

====================================================
SOAP NOTES
==========

## SUBJECTIVE

Document:

* Chief complaint
* Symptoms
* History discussed
* Patient concerns
* Relevant statements from the patient

## OBJECTIVE

Document available:

* Clinical findings
* Medications
* Laboratory results
* Diagnostic findings
* Observations
* Vital signs

## ASSESSMENT

Summarize the clinician's assessment using only documented information.

## PLAN

Document:

* Treatment plan
* Medication discussions
* Follow-up recommendations
* Referrals
* Additional testing
* Lifestyle recommendations
* Next steps

## MISSING INFORMATION

List any clinically relevant information that was not available.

Rules:

* Never invent information.
* Never leave sections blank.
* Use "Not Available" when necessary.
  """


VBC_Notes = """
You are a clinical documentation and Value Based Care (VBC) assistant.

Review BOTH the Patient Record and Encounter Transcript.

Your task has TWO outputs:

1. Generate a complete Value Based Care (VBC) report.
2. After the report, output a structured JSON with selected patient info and the full transcript.

====================================================
PATIENT RECORD
====================================================
{patient_data}

====================================================
ENCOUNTER TRANSCRIPT
====================================================
{transcript_data}

====================================================
VALUE BASED CARE (VBC) REPORT
====================================================

## ACTIVE CONDITIONS
List all documented symptoms, complaints, diagnoses, and medical problems.

## CHRONIC CONDITIONS
List all chronic or long-term conditions.

## RISK-ADJUSTING DIAGNOSES
List all explicitly documented diagnoses relevant to risk adjustment.

## RELEVANT COMORBIDITIES
List all comorbid conditions affecting health status.

## PREVENTIVE CARE OPPORTUNITIES
List all documented preventive care, screenings, tests, vaccinations, or wellness activities.

## CARE GAPS
List all unresolved issues, treatment concerns, lifestyle concerns, or gaps in care.

## MEDICATION ADHERENCE CONCERNS
List all documented concerns about medication adherence, compliance, or effectiveness.

## FOLLOW-UP AND CARE COORDINATION
List all documented follow-up actions, referrals, tests, medication changes, or care coordination.

## HEALTH RISKS REQUIRING MONITORING
List all documented risks, abnormal findings, or conditions requiring monitoring.

## VBC SUMMARY
Concise summary of patient’s health status, conditions, care opportunities, gaps, medication concerns, risks, and follow-up.

====================================================
STRUCTURED JSON RESPONSE
====================================================

After the VBC report, output this JSON:

{
  "patients_data": [
    {
      "id": "value",
      "firstname": "value",
      "lastname": "value",
      "city": "value",
      "email": "value"
    }
  ],
  "transcripts_data": [
    {
      "user_id": "value",
      "session_id": "value",
      "status": "value"
    }
  ]
}

====================================================
RULES
====================================================
1. Use info from BOTH Patient Record and Transcript.
2. Do not infer or invent diagnoses.
3. If no info for a section, write "Not Available".
4. Preserve distinction between confirmed conditions, symptoms, possible conditions, and recommendations.
5. Include specific documented medications, tests, referrals, and actions.
6. JSON must be valid, contain only specified fields, and use original values.
7. If a field is missing, use "Not Available".
8. Do not add explanations after JSON.
9. Final output order: First the VBC Report, then the JSON.
"""


Recommended_Tests = """
Review the Patient Record and Encounter Transcript.

Instructions:

* Use only documented information.
* Do not infer undocumented diagnoses.
* Do not recommend tests without documented clinical justification.
* If insufficient information exists, clearly state so.
* Return only the completed report.

====================================================
DIAGNOSTIC TEST RECOMMENDATIONS
===============================

For each recommendation provide:

TEST NAME
Clinical Justification:
Priority Level: High / Medium / Low

## DOCUMENTED CLINICAL INDICATIONS

Summarize the symptoms, conditions, findings, or concerns supporting the recommendations.

## RECOMMENDED TESTS

Test Name:
Clinical Justification:
Priority Level:

Test Name:
Clinical Justification:
Priority Level:

(Repeat as needed)

## MONITORING RECOMMENDATIONS

List any documented laboratory monitoring, follow-up testing, imaging surveillance, or ongoing assessments.

## NO ADDITIONAL TESTING

If the available information does not support additional testing recommendations, explicitly state:

"No additional testing recommendations can be made based on the provided information."

## CLINICAL SUMMARY

Provide a brief explanation of how the recommendations relate to the documented clinical findings.

Rules:

* Use only documented information.
* Do not invent symptoms, diagnoses, or risk factors.
* Every recommendation must have a documented rationale.
* Use "Not Available" when necessary.
  """



Recommended_Medicines = """
Review the Patient Record and Encounter Transcript.

Instructions:

* Use only documented information.
* Do not recommend medications for undocumented conditions.
* Do not create diagnoses.
* Recommendations are for clinical consideration only and must not be presented as prescriptions.
* Return only the completed report.

====================================================
MEDICATION REVIEW AND CLINICAL CONSIDERATION REPORT
===================================================

## DOCUMENTED CONDITIONS

List documented diagnoses, symptoms, and conditions relevant to medication management.

## CURRENT MEDICATION CONSIDERATIONS

Summarize any medications discussed, reviewed, continued, adjusted, or monitored during the encounter.

## MEDICATION OPTIONS FOR CLINICAL CONSIDERATION

Medication:
Clinical Purpose:
Reason for Recommendation:
Potential Precautions:
Monitoring Considerations:

Medication:
Clinical Purpose:
Reason for Recommendation:
Potential Precautions:
Monitoring Considerations:

(Repeat as needed)

## POTENTIAL MEDICATION RISKS

Document any potential interactions, precautions, contraindications, adherence concerns, or monitoring needs discussed in the provided information.

## NO MEDICATION RECOMMENDATIONS

If there is insufficient documented information to support medication recommendations, explicitly state:

"Insufficient clinical information available to support medication recommendations."

## CLINICAL SUMMARY

Provide a concise explanation of how the medication considerations relate to the documented clinical findings.

Rules:

* Use only documented information.
* Never prescribe medications.
* Never recommend treatment for undocumented conditions.
* Never leave sections blank.
* Use "Not Available" when necessary.
  """



QUESTION_MAP = {
    "1": Summary,
    "2": SOAP_Notes,
    "3": VBC_Notes,
    "4": Recommended_Tests,
    "5": Recommended_Medicines
}