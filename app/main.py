from fastapi import FastAPI

from app.routes.summary import router as summary_router
from app.routes.soap import router as soap_router
from app.routes.vbc import router as vbc_router
from app.routes.recommended_tests import router as tests_router
from app.routes.recommended_medicines import router as medicines_router
from app.routes.requirements import router as requirements_router

app = FastAPI(
    title="Medical Tool API",
    version="1.0.0"
)

app.include_router(summary_router, prefix="/v1")
app.include_router(soap_router, prefix="/v1")
app.include_router(vbc_router, prefix="/v1")
app.include_router(tests_router, prefix="/v1")
app.include_router(medicines_router, prefix="/v1")
app.include_router(requirements_router, prefix="/v1")

@app.get("/health")
def health():
    return {"status":"OK"}