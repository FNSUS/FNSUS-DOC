from enum import Enum
from beanie import Document, Link, PydanticObjectId
from pydantic import BaseModel, Field
from typing import Optional

class TipoUnidade(Document):
    # Mantém ObjectId para TipoUnidade, pois o Link precisa de um _id estável
    id: Optional[PydanticObjectId] = None
    tp_unid: str = Field(..., unique=True) # Garante que tp_unid seja único
    descricao: str

    class Settings:
        name = "tipos_unidade"

class Estabelecimento(Document):
    id: str = Field(..., alias="_id") # _id é o CNES string
    cod_mun: str = Field(alias="CODUFMUN")
    tipo_unidade: Optional[Link[TipoUnidade]] = None
    tp_unid: str = Field(alias="TP_UNID")
    nome_razao_social: Optional[str] = None
    nome_fantasia: Optional[str] = None
    cod_cep: Optional[str] = Field(None, alias="COD_CEP")
    endereco_estabelecimento: Optional[str] = None
    numero_estabelecimento: Optional[str] = None
    bairro_estabelecimento: Optional[str] = None
    latitude_estabelecimento_decimo_grau: Optional[float] = None
    longitude_estabelecimento_decimo_grau: Optional[float] = None
    numero_telefone_estabelecimento: Optional[str] = None
    endereco_email_estabelecimento: Optional[str] = None
    turno_atendimento: Optional[str] = None
    # Corrigido typo no nome do campo original
    atendimento_pronto_socorro: Optional[bool] = Field(None, alias="atendiemento_pronto_socorro")
    vinculo_sus: Optional[bool] = None
    tipo_gestao: Optional[str] = None
    cpf_cnpf: Optional[str] = None

    class Settings:
        name = "estabelecimentos"

# --- EstabelecimentoSimples EXPANDIDO ---
class EstabelecimentoSimples(BaseModel):
    # Campo ID (CNES)
    id: str = Field(..., alias='_id')

    # Campos que você pediu para adicionar, com aliases para mapear
    razao_social: Optional[str] = Field(None, alias='nome_razao_social')
    nome_fantasia: Optional[str] = None # Nome já é igual no DB
    cep: Optional[str] = Field(None, alias='COD_CEP')
    numero_endereco: Optional[str] = Field(None, alias='numero_estabelecimento')
    endereco: Optional[str] = Field(None, alias='endereco_estabelecimento')
    bairro: Optional[str] = Field(None, alias='bairro_estabelecimento')
    latitude: Optional[float] = Field(None, alias='latitude_estabelecimento_decimo_grau')
    longitude: Optional[float] = Field(None, alias='longitude_estabelecimento_decimo_grau')
    telefone: Optional[str] = Field(None, alias='numero_telefone_estabelecimento')
    email: Optional[str] = Field(None, alias='endereco_email_estabelecimento')
    turno_atendimento: Optional[str] = None # Nome já é igual no DB
    # Corrigido typo no nome do campo original ao definir o alias
    pronto_socorro: Optional[bool] = Field(None, alias='atendimento_pronto_socorro')

    class Config:
        from_attributes = True # Permite mapear atributos do objeto Beanie
        populate_by_name = True # Essencial para que os aliases funcionem na leitura
# --- FIM DA EXPANSÃO ---

class TipoGestao(Enum):
    M = "Municipal"
    E = "Estadual"
    D = "Dupla"
    S = "Sem Gestão"

