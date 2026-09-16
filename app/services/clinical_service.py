from app.services.cosmos_service import get_appointment_mapping, get_patient, get_transcript

from app.services.llm_service import ask_llm

def generate_clinical_response(appointment_date, appointment_id, question_type):
    appointment_mapping = get_appointment_mapping(date= appointment_date, appointment_id=appointment_id)
    if not appointment_mapping:
        raise ValueError("Appointment not found")

    patient_id = appointment_mapping["patient_id"]
    doctor_email = appointment_mapping["doctor_email"]
    firstname = appointment_mapping["firstname"]
    lastname = appointment_mapping["lastname"]
    email = appointment_mapping["email"]

    patient = get_patient(patient_id, firstname, lastname, email)
    if not patient:
        raise ValueError("Patient not found")

    transcipt = get_transcript(doctor_email, appointment_id)
    if not transcipt:
        raise ValueError("Transcript not found")

    response = ask_llm(
        question_type=question_type, 
        patient_data=patient,
        transcript_data=transcipt
    )

    return response