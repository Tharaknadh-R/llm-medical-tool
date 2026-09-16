from fastapi import APIRouter

from app.data.requirements import REQUIREMENTS

router = APIRouter()

@router.get("/requirements")
def get_requirements():
    return {
        "requirements": REQUIREMENTS
    }