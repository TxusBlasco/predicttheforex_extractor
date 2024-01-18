from fastapi import APIRouter, status, Body, BackgroundTasks
from core.application.services.extractor import ExtractorAppService
from core.domain.models.extractor import InstrumentList
from fastapi.responses import JSONResponse

extraction = APIRouter()


@extraction.post("/v1/instruments/fetch",
                 status_code=status.HTTP_201_CREATED,
                 tags=["Start a stream of candles, being sent to kafka"])
async def start_candle_extraction(background_tasks: BackgroundTasks, instruments: InstrumentList = Body(...)):
    """
    Endpoint to start the stream of price extractions. Needs a body with a list of candles to fetch
    :return: None
    """
    start = ExtractorAppService(insts=instruments.instruments)
    background_tasks.add_task(start.fetch_stream)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Candle extraction stream successfully started"})
