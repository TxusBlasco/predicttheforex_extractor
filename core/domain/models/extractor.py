from pydantic import BaseModel


class ExtractionModel(BaseModel):
    instruments: list
