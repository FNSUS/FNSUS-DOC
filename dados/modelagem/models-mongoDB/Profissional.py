from beanie import Document, Link, PydanticObjectId
from pydantic import Field
from typing import Optional
from .Estabelecimento import Estabelecimento

class CBO(Document):
    """
    Representa um Código Brasileiro de Ocupação.
    O 'id' (ou _id) é o próprio código CBO.
    """
    id: str = Field(..., description="Código CBO", alias='_id')
    descricao: str = Field(..., description="Descrição da Ocupação (e.g., 'Médico Clínico')")

    class Settings:
        name = "cbos"

class Profissional(Document):
    id: Optional[PydanticObjectId] = None

    cns_prof: str = Field(..., alias="CNS_PROF", description="CNS do Profissional (pode repetir)")

    estabelecimento: Optional[Link[Estabelecimento]] = None
    cnes: str = Field(..., alias="CNES")
    cod_mun: str = Field(..., alias="CODUFMUN")
    cbo: Optional[str] = Field(None, alias="CBO")

    class Settings:
        name = "profissionais"
        indexes = ["cns_prof", "cnes", "cbo"]