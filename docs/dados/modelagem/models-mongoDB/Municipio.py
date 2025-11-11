from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional

class DadosGerais(BaseModel):
    municipio: str
    uf: str
    estado: str
    regiao: str
    area_territorial_km2: Optional[float] = None
    populacao_total: Optional[int] = None
    densidade_demografica: Optional[float] = None
    perc_populacao_urbana: Optional[float] = None
    perc_populacao_rural: Optional[float] = None

class Infraestrutura(BaseModel):
    qtde_ubs: int = 0
    qtde_hospitais: int = 0
    qtde_upas: int = 0
    qtde_caps: int = 0
    samu: bool = False
    qtde_leitos_uti: int = 0
    equipe_saude_familia: Optional[str] = "Não informado"
    perc_cobertura_atencao_basica: Optional[str] = "Não informado"

class ProfissionaisSaude(BaseModel):
    qtde_medicos: int = 0
    qtde_enfermeiros: int = 0
    qtde_tecnicos_enfermagem: int = 0
    qtde_psicologos: int = 0

class Municipio(Document):
    id: int = Field(alias="_id")
    dados_gerais: DadosGerais
    infraestrutura: Infraestrutura
    profissionais: ProfissionaisSaude

    class Settings:
        name = "municipios"

class MunicipioBase(BaseModel):
    codigo_ibge: int
    municipio: str
    uf: str

class ListaMunicipio(MunicipioBase):
    pass