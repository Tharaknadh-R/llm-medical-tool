from app.services.cosmos_service import get_appointments_by_date, get_appointment_mapping
from app.services.clinical_service import generate_clinical_response
from app.prompts.prompts import QUESTION_MAP

def main():

    # Appointment Date
    date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()

    if not get_appointments_by_date(date):
        print("No appointment's found on given date")
        exit()

    # Appointment ID
    appointment_id = input("Enter Appointment ID: ").strip()
    if not get_appointment_mapping(date, appointment_id):
        print("No appointment found for the given appointment id")
        exit()

    # Question selection
    print("\nChoose Question: ")

    print("1. Summary")
    print("2. SOAP_Notes")
    print("3. VBC_Notes")
    print("4. Recommended_Tests")
    print("5. Recommended_Medicines")

    choice = input("\nEnter Choice: ").strip()

    if choice not in QUESTION_MAP:
        print("Invalid Choice")
        exit()

    # get selected Prompt
    question_type = QUESTION_MAP[choice]

    # Generate llm response
    print("\n Generating Response...")

    try:
        response = generate_clinical_response(
            appointment_date=date,
            appointment_id=appointment_id,
            question_type=question_type
        )
    except ValueError as error:
        print(f"\nError: {error}")
        return
    except Exception as error:
        print("\nAn unexpected error occured.")
        print(f"Error: {error}")
        return

    # Display response
    print("\n")
    print("=" * 50)
    print(question_type.upper())
    print("=" * 50)
    print(response)

if __name__ == "__main__":
    main()