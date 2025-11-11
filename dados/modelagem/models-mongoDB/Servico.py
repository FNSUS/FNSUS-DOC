from beanie import Document, Link, PydanticObjectId
from pydantic import Field
from typing import Optional
from .Estabelecimento import Estabelecimento

class Servico(Document):
    id: Optional[PydanticObjectId] = None
    estabelecimento: Optional[Link[Estabelecimento]] = None
    cnes: str = Field(..., alias="CNES")
    cod_mun: str = Field(alias="CODUFMUN")
    serv_esp: Optional[str] = Field(None, alias="SERV_ESP")
    class_sr: Optional[str] = Field(None, alias="CLASS_SR")
    srv_unico: Optional[str] = Field(None, alias="SRVUNICO")
    tp_unid: Optional[str] = Field(None, alias="TP_UNID")
    turno_at: Optional[str] = Field(None, alias="TURNO_AT")
    amb_nsus: int = Field(default=0, alias="AMB_NSUS")
    amb_sus: int = Field(default=0, alias="AMB_SUS")
    hosp_nsus: int = Field(default=0, alias="HOSP_NSUS")
    hosp_sus: int = Field(default=0, alias="HOSP_SUS")

    class Settings:
        name = "servicos"
        indexes = ["cnes", "serv_esp", "class_sr"]
