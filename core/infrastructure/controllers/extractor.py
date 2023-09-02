from fastapi import APIRouter, status
from core.application.services.extractor import ExtractorAppService
from core.domain.models.extractor import ExtractionModel

extraction = APIRouter()


@extraction.post("v1/instruments",
                 status_code=status.HTTP_201_CREATED,
                 response_model=ExtractionModel,
                 tags=["instrument_extraction"])
async def start_extraction():
    ExtractorAppService(insts=ExtractionModel.instruments).fetch_stream()
