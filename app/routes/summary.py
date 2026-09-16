from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool

from app.schemas.requests import ClinicalRequest
from app.services.clinical_service import generate_clinical_response
from app.prompts.prompts import Summary
from app.data.requirements import REQUIREMENTS

router = APIRouter()

@router.post("/summary")
async def generate_summary(request: ClinicalRequest):
    response = await run_in_threadpool(
        generate_clinical_response,
        appointment_date=request.appointment_date,
        appointment_id=request.appointment_id,
        question_type=Summary
    )

    REQUIREMENTS["summary"].append({
        "appointment_date": request.appointment_date,
        "appointment_id": request.appointment_id,
        "response": response
    })

    return {
        "response": response
    }
