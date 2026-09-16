from pydantic import BaseModel

class ClinicalRequest(BaseModel):
    appointment_date: str
    appointment_id: str