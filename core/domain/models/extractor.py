from pydantic import BaseModel


class InstrumentList(BaseModel):
    instruments: list[str]
