from cosmos_db import (
    get_appointments_by_date,
    get_appointment_mapping,
    get_patient,
    get_transcript
)

from azure_open_ai import ask_llm

from prompts import QUESTION_MAP


date = input(
    "Enter Appointment Date (YYYY-MM-DD): "
).strip()
if not get_appointments_by_date(date):
    print("No Appointment's found on given date")
    exit()    

appointment_id = input(
    "Enter Appointment ID: "
).strip()
if not get_appointment_mapping(date, appointment_id):
    print("No appointment found for the given appointment id")
    exit()


print("\nChoose Question:")

print("1. Summary")
print("2. SOAP_Notes")
print("3. VBC_Notes")
print("4. Recommended_Tests")
print("5. Recommended_Medicines")

choice = input(
    "\nEnter Choice: "
).strip()

if choice not in QUESTION_MAP:
    print("Invalid Choice")
    exit()


# Appointment Mapping

appointment_mapping = get_appointment_mapping(
    date=date,
    appointment_id=appointment_id
)

if not appointment_mapping:
    print("Appointment not found")
    exit()


patient_id = appointment_mapping["patient_id"]

doctor_email = appointment_mapping["doctor_email"]

firstname = appointment_mapping[ "firstname"]
lastname = appointment_mapping[ "lastname"]
email = appointment_mapping[ "email"]

# Fetch Patient Data

patient = get_patient(
    patient_id, firstname, lastname, email
    )

if not patient:
    print("Patient not found")
    exit()



# Fetch Transcript Data

transcript = get_transcript(
    doctor_email,
    appointment_id
)

if not transcript:
    print("Transcript not found")
    exit()


question_type = QUESTION_MAP[
    choice
]

print("\nGenerating Response...")


response = ask_llm(
    question_type=question_type,
    patient_data=patient,
    transcript_data=transcript
)


print("\n")
print("=" * 50)
print(question_type.upper())
print("=" * 50)

print(response)