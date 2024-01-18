from fastapi import APIRouter, status, Body
from core.application.services.extractor import ExtractorAppService
from core.domain.models.extractor import InstrumentList

extraction = APIRouter()


@extraction.post("/v1/instruments/fetch",
                 status_code=status.HTTP_201_CREATED,
                 tags=["instrument_extraction"])
async def start_extraction(instruments: InstrumentList = Body(...)):
    """
    Endpoint to start the stream of price extractions. Needs a body with a list of candles to fetch
    :return: None
    """
    ExtractorAppService(insts=instruments.instruments).fetch_stream()
