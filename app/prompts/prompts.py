Summary = """
Review Patient Record and Encounter Transcript.

Rules:
1. Use only documented info; no inference.
2. If missing, write "Not Available".
3. Prioritize transcript for today’s visit.
4. Use professional clinical terminology.
5. Never leave sections blank.

====================================================
CLINICAL SUMMARY REPORT
=======================

## CLINICAL SUMMARY
- Reason for visit
- Medical history
- Symptoms/concerns
- Findings
- Diagnoses
- Treatment decisions
- Follow-up

## MINUTES OF CONVERSATION
List top 10 discussion points.

## CLINICAL ASSESSMENT
Primary Diagnosis:
Secondary Conditions:
Findings:
Symptoms:
History:

## RECOMMENDED NEXT STEPS
Follow-up, monitoring, referrals, lifestyle guidance.

## CONCLUSION
Brief summary of patient status and care plan.

## AI CONFIDENCE SCORE
Confidence: XX/100  
Reason: Based on completeness of provided info.
"""



SOAP_Notes = """
Review Patient Record and Encounter Transcript.

Rules:
1. Use only documented info.
2. No inference or hallucination.
3. If missing, write "Not Available".
4. Follow SOAP format.

====================================================
SOAP NOTES
==========

## SUBJECTIVE
Chief complaint, symptoms, history, patient concerns.

## OBJECTIVE
Findings, medications, labs, diagnostics, vitals.

## ASSESSMENT
Clinician’s assessment (documented only).

## PLAN
Treatment plan, meds, follow-up, referrals, tests, lifestyle.

## MISSING INFORMATION
List unavailable but clinically relevant info.
"""


VBC_Notes = """
You are a Value Based Care (VBC) assistant.

Review Patient Record and Encounter Transcript.

====================================================
PATIENT RECORD
====================================================
{patient_data}

====================================================
ENCOUNTER TRANSCRIPT
====================================================
{transcript_data}

Task:
1. Generate VBC Report.
2. Then output JSON with patient info + transcript.

====================================================
VALUE BASED CARE REPORT
=======================

## ACTIVE CONDITIONS
## CHRONIC CONDITIONS
## RISK-ADJUSTING DIAGNOSES
## COMORBIDITIES
## PREVENTIVE CARE
## CARE GAPS
## MEDICATION ADHERENCE
## FOLLOW-UP & COORDINATION
## HEALTH RISKS
## VBC SUMMARY

====================================================
STRUCTURED JSON
================
{
  "patients_data":[
    {
    "id":"value",
    "firstname":"value",
    "lastname":"value",
    "city":"value",
    "email":"value"
    }
  ],
  "transcripts_data":[
    {
    "user_id":"value",
    "session_id":"value",
    "status":"value"
    }
  ]
}

Rules:
1. Use both record + transcript.
2. No inference; if missing → "Not Available".
3. JSON must be valid, only specified fields.
4. Output order: Report first, JSON second.
"""

Recommended_Tests = """
Review Patient Record and Encounter Transcript.

Rules:
1. Use only documented info.
2. No invented diagnoses/tests.
3. Every test must have justification.
4. If none, state "No additional testing recommendations".

====================================================
DIAGNOSTIC TEST RECOMMENDATIONS
===============================

## DOCUMENTED INDICATIONS
Symptoms, conditions, findings.

## RECOMMENDED TESTS
Test Name:
Justification:
Priority: High/Medium/Low

(Repeat as needed)

## MONITORING
Documented follow-up or surveillance.

## NO ADDITIONAL TESTING
If insufficient info, state explicitly.

## CLINICAL SUMMARY
Brief explanation linking recommendations to findings.
"""



Recommended_Medicines = """
Review Patient Record and Encounter Transcript.

Rules:
1. Use only documented info.
2. Do not prescribe; only clinical considerations.
3. No recommendations for undocumented conditions.
4. If insufficient info, state explicitly.

====================================================
MEDICATION REVIEW
=================

## DOCUMENTED CONDITIONS
Relevant diagnoses/symptoms.

## CURRENT MEDICATIONS
Discussed, continued, adjusted, or monitored.

## OPTIONS FOR CONSIDERATION
Medication:
Purpose:
Reason:
Precautions:
Monitoring:

(Repeat as needed)

## RISKS
Interactions, contraindications, adherence concerns.

## NO MEDICATION RECOMMENDATIONS
If insufficient info, state explicitly.

## CLINICAL SUMMARY
Concise explanation linking meds to findings.
"""



QUESTION_MAP = {
    "1": Summary,
    "2": SOAP_Notes,
    "3": VBC_Notes,
    "4": Recommended_Tests,
    "5": Recommended_Medicines
}