from beanie import Document, Link, PydanticObjectId
from pydantic import Field
from typing import Optional
from .Estabelecimento import Estabelecimento

class Leito(Document):
    id: Optional[PydanticObjectId] = None
    estabelecimento: Optional[Link[Estabelecimento]] = None
    cnes: str = Field(..., alias="CNES")
    cod_mun: str = Field(alias="CODUFMUN")
    turno_at: Optional[str] = Field(None, alias="TURNO_AT")
    tp_leito: Optional[str] = Field(None, alias="TP_LEITO")
    cod_leito: Optional[str] = Field(None, alias="CODLEITO")
    qt_sus: int = Field(default=0, alias="QT_SUS")
    qt_nsus: int = Field(default=0, alias="QT_NSUS")

    class Settings:
        name = "leitos"
        indexes = ["cnes"]
