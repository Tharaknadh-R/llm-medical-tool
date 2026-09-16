from azure.cosmos import CosmosClient

from app.core.config import (
    COSMOS_ENDPOINT,
    COSMOS_KEY,
    PATIENT_DB_NAME,
    PATIENT_CONTAINER,
    TRANSCRIPT_DB_NAME,
    TRANSCRIPT_CONTAINER,
    APPOINTMENT_DB_NAME,
    APPOINTMENT_CONTAINER
)

client = CosmosClient(        #Database Connection
    COSMOS_ENDPOINT,
    credential=COSMOS_KEY
)


# Patients Container

patient_db = client.get_database_client(
    PATIENT_DB_NAME
)

patient_container = patient_db.get_container_client(
    PATIENT_CONTAINER
)


# Transcript Container

transcript_db = client.get_database_client(
    TRANSCRIPT_DB_NAME
)

transcript_container = transcript_db.get_container_client(
    TRANSCRIPT_CONTAINER
)


# Appointment Container

appointment_db = client.get_database_client(
    APPOINTMENT_DB_NAME
)

appointment_container = appointment_db.get_container_client(
    APPOINTMENT_CONTAINER
)


def get_appointments_by_date(date):
    query = """
    SELECT *
    FROM c
    WHERE c.id = @date
    """

    return list(
        appointment_container.query_items(
            query=query,
            parameters=[
                {
                    "name": "@date",
                    "value": date
                }
            ],
            enable_cross_partition_query=True
        )
    )


def get_appointment_mapping(date, appointment_id):
    appointments = get_appointments_by_date(date)
    if not appointments:
        return None

    for appointment in appointments[0]["data"]:

        if appointment["id"] == appointment_id:

            return {
                "appointment_id": appointment["id"],
                "patient_id": appointment["patient_id"],
                "doctor_email": appointment["doctor_email"],
                "firstname": appointment["first_name"],
                "lastname": appointment["last_name"],
                "email": appointment["email"]
            }

    return None


def get_patient(patient_id, firstname, lastname, email):
    query = """
    SELECT *
    FROM c
    WHERE c.patientID = @patient_id 
    AND c.original_json.original_json.details.firstname = @firstname 
    AND c.original_json.original_json.details.lastname = @lastname 
    AND c.original_json.original_json.details.email = @email
    """

    return list(
        patient_container.query_items(
            query=query,
            parameters=[
                {
                    "name": "@patient_id",
                    "value": patient_id
                },
                {
                    "name": "@firstname",
                    "value": firstname
                },
                {
                    "name": "@lastname",
                    "value": lastname
                },
                {
                    "name": "@email",
                    "value": email
                }
            ],
            enable_cross_partition_query=True
        )
    )


def get_transcript(doctor_email, appointment_id):

    transcript_id = (
        f"{doctor_email}_{appointment_id}_transcription"
    )

    query = """
    SELECT *
    FROM c
    WHERE c.id = @transcript_id
    """

    return list(
        transcript_container.query_items(
            query=query,
            parameters=[
                {
                    "name": "@transcript_id",
                    "value": transcript_id
                }
            ],
            enable_cross_partition_query=True
        )
    )