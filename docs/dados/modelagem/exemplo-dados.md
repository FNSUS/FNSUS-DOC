# Documentação dos Dados e Pipelines

## Histórico de Versões
| Versão | Data       | Descrição                                 |
|--------|------------|-------------------------------------------|
| 1.0    | 03/11/2025 | Criação inicial do documento.             |

Esta documentação detalha os pipelines de dados do IBGE e CNES (atuais), desde a extração (Bronze) até as camadas de dados transformados (Silver) e prontos para consumo (Gold). O objetivo é fornecer uma visão clara da origem, transformação e estrutura dos dados utilizados.

[🔗 Acessar Repositório de Pipeline (Github)](https://github.com/FNSUS/api)


## 1. Glossário de Termos

- **IBGE**: Instituto Brasileiro de Geografia e Estatística.
- **CNES**: Cadastro Nacional de Estabelecimentos de Saúde.
- **API**: Application Programming Interface - interface de programação de aplicações.
- **Pipeline de Dados**: Conjunto de processos automatizados para mover e transformar dados de uma origem para um destino.
- **Camada Bronze**: Dados brutos, extraídos diretamente da fonte, sem transformações ou limpezas. Preserva o formato original.
- **Camada Silver**: Dados limpos, padronizados e enriquecidos, prontos para análises mais aprofundadas.
- **Camada Gold**: Dados agregados e prontos para consumo por aplicações, dashboards ou relatórios.
- **JSON**: JavaScript Object Notation - formato de intercâmbio de dados leve e de fácil leitura.
- **Parquet**: Formato de armazenamento de dados em coluna otimizado para análises.
- **pysus**: Biblioteca Python para acesso e manipulação de dados do SUS.
- **FTP**: File Transfer Protocol - protocolo para transferência de arquivos.
- **CBO**: Classificação Brasileira de Ocupações.

## 2. Estrutura dos Pipelines

### 2.1. IBGE (Instituto Brasileiro de Geografia e Estatística)

Caminho: `pipeline/ibge/`

Este pipeline é responsável por coletar e processar dados geográficos e demográficos dos municípios brasileiros, utilizando as APIs do IBGE.

#### 2.1.1. bronze_localidade.py

- **Descrição**: Extrai informações detalhadas sobre os municípios brasileiros, como nome, microrregião, mesorregião, UF e região, diretamente da API de Localidades do IBGE.
- **Fonte**: https://servicodados.ibge.gov.br/api/v1/localidades/municipio
- **Formato de Saída (Exemplo)**: JSON

```json
[
    {
        "id": 1100015,
        "nome": "Alta Floresta D'Oeste",
        "microrregiao": {
        "id": 11006,
        "nome": "Cacoal",
        "mesorregiao": {
            "id": 1102,
            "nome": "Leste Rondoniense",
            "UF": {
            "id": 11,
            "sigla": "RO",
            "nome": "Rondônia",
            "regiao": {
                "id": 1,
                "sigla": "N",
                "nome": "Norte"
            }
            }
        }
        },
        "regiao-imediata": {
        "id": 110005,
        "nome": "Cacoal",
        "regiao-intermediaria": {
            "id": 1102,
            "nome": "Ji-Paraná",
            "UF": {
            "id": 11,
            "sigla": "RO",
            "nome": "Rondônia",
            "regiao": {
                "id": 1,
                "sigla": "N",
                "nome": "Norte"
            }
            }
        }
        }
    }
    // ...continua
]
```

#### 2.1.2. bronze_demografia.py

- **Descrição**: Coleta dados demográficos dos municípios, especificamente a área territorial em km² e a densidade demográfica (habitantes/km²), utilizando a API de Agregados do IBGE.
- **Fonte**: https://servicodados.ibge.gov.br/api/v3/agregados/4714/periodos/{ano}/variaveis/6318|614?localidades=N6[all]
  - ID Agregado: 4714 - "População Residente, Área territorial e Densidade demográfica".
  - Ano: Último ano do Censo (período).
  - Variáveis: 6318 (Área Territorial) e 614 (Densidade Demográfica).
- **Observação**: A extração na camada Bronze deve ser pura, sem filtros, para manter a fidelidade aos dados da fonte. O filtro de variáveis (6318|614) já está sendo aplicado na URL, o que é aceitável, pois são as variáveis desejadas daquele agregado específico. A população será obtida de outra fonte mais atualizada.
- **Formato de Saída (Exemplo)**: JSON

```json
{
    "id": "614",
    "variavel": "Densidade demográfica",
    "unidade": "Habitante por quilômetro quadrado",
    "resultados": [
    {
        "classificacoes": [],
        "series": [
        {
            "localidade": {
            "id": "1100015",
            "nivel": {
                "id": "N6",
                "nome": "Município"
            },
            "nome": "Alta Floresta D'Oeste - RO"
            },
            "serie": {
            "2022": "3.04"
            }
        },
        {
            "localidade": {
            "id": "1100023",
            "nivel": {
                "id": "N6",
                "nome": "Município"
            },
            "nome": "Ariquemes - RO"
            },
            "serie": {
            "2022": "21.88"
            }
        },

        ...

        {
"id": "614",
"variavel": "Densidade demográfica",
"unidade": "Habitante por quilômetro quadrado",
"resultados": [
  {
    "classificacoes": [],
    "series": [
      {
        "localidade": {
          "id": "1100015",
          "nivel": {
            "id": "N6",
            "nome": "Município"
          },
          "nome": "Alta Floresta D'Oeste - RO"
        },
        "serie": {
          "2022": "3.04"
        }
      },
      {
        "localidade": {
          "id": "1100023",
          "nivel": {
            "id": "N6",
            "nome": "Município"
          },
          "nome": "Ariquemes - RO"
        },
        "serie": {
          "2022": "21.88"
        }
      },
      ...

      (era para extrair puro e viria o de populacao, mas acaba filtrando --> como vou extrair a populacao por outro meio que é mais atualizado, faz sentido extrair a requisicao pura sem filtrar, COMMAND:"ANALISE SE NAO PODE FILTRAR MESMO, TEM QUE SER PURO O BRONZE")
```

#### 2.1.3. bronze_distribuicao.py

- **Descrição**: Extrai a população residente por situação de domicílio (urbana/rural) dos municípios, utilizando a API de Agregados do IBGE.
- **Fonte**: https://servicodados.ibge.gov.br/api/v3/agregados/9923/periodos/{ano}/variaveis/93?localidades=N6[all]&classificacao=1[1,2]
  - ID Agregado: 9923 - "População residente, por situação do domicílio".
  - Ano: Último ano do Censo (período).
  - Variável: 93 - População residente.
  - Classificação: 1[1,2] - Situação do domicílio (1: Urbana, 2: Rural).
- **Formato de Saída (Exemplo)**: JSON

```json
{
"id": "93",
"variavel": "População residente",
"unidade": "Pessoas",
"resultados": [
  {
    "classificacoes": [
      {
        "id": "1",
        "nome": "Situação do domicílio",
        "categoria": {
          "1": "Urbana"
        }
      }
    ],
    "series": [
      {
        "localidade": {
          "id": "1100015",
          "nivel": {
            "id": "N6",
            "nome": "Município"
          },
          "nome": "Alta Floresta D'Oeste - RO"
        },
        "serie": {
          "2022": "12971"
        }
      }
      // ...continua
    ]
  }
]
}
```

#### 2.1.4. silver_dados_municipais.py

- **Descrição**: Responsável por limpar, padronizar e enriquecer os dados brutos do IBGE. Esta camada pode incluir:
  - Unificação de dados de localidade, demografia e distribuição populacional.
  - Cálculo de percentuais de população urbana/rural.
  - Renomeação de colunas para maior clareza.
  - Tratamento de valores nulos ou inconsistentes.
- **Entradas**: Dados brutos das APIs de Localidades, Demografia e Distribuição Populacional do IBGE.
- **Saída Esperada**: Um conjunto de dados limpo e estruturado com informações municipais.
  
### 2.2. CNES (Cadastro Nacional de Estabelecimentos de Saúde)

Caminho: `pipeline/cnes/`

Este pipeline processa dados relacionados a estabelecimentos de saúde, profissionais e serviços, obtidos do CNES.

#### 2.2.1. bronze_dados_auxiliares.py

- **Descrição**: Inicialmente, extraía arquivos CSV de dimensões (tabelas auxiliares). Atualmente, esses arquivos são salvos manualmente em data/bronze.
- **Melhoria**: Mudar para extração automatizada via FTP para garantir que os dados estejam sempre atualizados e a solução seja mais robusta.
- **Conteúdo Esperado**: Tabelas de mapeamento para códigos (ex: tipo de unidade, CBO, conselhos).
  
#### 2.2.2. bronze_estabelecimentos.py

- **Descrição**: Extrai dados dos estabelecimentos de saúde, utilizando o pysus para obter os arquivos mais recentes e complementa com informações da API do CNES para detalhes adicionais (ex: coordenadas geográficas, nome fantasia).
- **Fonte (Pysus)**: Arquivos de estabelecimentos do CNES (via pysus).
- **Fonte (API Complementar)**: https://apidadosabertos.saude.gov.br/cnes/estabelecimentos/{cnes}
- **Observações**: A API complementar pode gerar grandes volumes de dados, exigindo processamento em chunks para evitar problemas de memória/travamento.
- **Melhoria**: Avaliar a substituição do pysus por extração via FTP para maior controle e flexibilidade.
- **Formato de Saída (Exemplo Pysus - Parquet)**:

```parquet
{"CNES":"0153281","CODUFMUN":"120001","COD_CEP":"69945000","CPF_CNPJ":"00000000000000","PF_PJ":"3","NIV_DEP":"3","CNPJ_MAN":"84306737000127","COD_IR":"","REGSAUDE":"","MICR_REG":"","DISTRSAN":"","DISTRADM":"","VINC_SUS":"1","TPGESTAO":"M","ESFERA_A":"","RETENCAO":"","ATIVIDAD":"04","NATUREZA":"","CLIENTEL":"01","TP_UNID":"70","TURNO_AT":"03","NIV_HIER":"","TP_PREST":"99"}
```

- **Formato de Saída (Exemplo API Complementar - JSON)**:

```json
{"codigo_cnes":153281,"numero_cnpj_entidade":"84306737000127","nome_razao_social":"CENTRO DE ATENCAO PSICOSSOCIAL","nome_fantasia":"CENTRO DE ATENCAO PSICOSSOCIAL SALVADOR DIAS DA SILVA","natureza_organizacao_entidade":null,"tipo_gestao":"M","descricao_nivel_hierarquia":null,"descricao_esfera_administrativa":"MUNICIPAL","codigo_tipo_unidade":70,"codigo_cep_estabelecimento":"69945000","endereco_estabelecimento":"AVENIDA BRASIL","numero_estabelecimento":"S/N","bairro_estabelecimento":"CENTRO","numero_telefone_estabelecimento":null,"latitude_estabelecimento_decimo_grau":-10.0784719111096,"longitude_estabelecimento_decimo_grau":-67.0534714562487,"endereco_email_estabelecimento":null,"numero_cnpj":null,"codigo_identificador_turno_atendimento":"03","descricao_turno_atendimento":"ATENDIMENTOS NOS TURNOS DA MANHA E A TARDE","estabelecimento_faz_atendimento_ambulatorial_sus":"NAO","codigo_estabelecimento_saude":"1200010153281","codigo_uf":12,"codigo_municipio":120001,"descricao_natureza_juridica_estabelecimento":"1244","codigo_motivo_desabilitacao_estabelecimento":null,"estabelecimento_possui_centro_cirurgico":0,"estabelecimento_possui_centro_obstetrico":0,"estabelecimento_possui_centro_neonatal":0,"estabelecimento_possui_atendimento_hospitalar":0,"estabelecimento_possui_servico_apoio":0,"estabelecimento_possui_atendimento_ambulatorial":0,"codigo_atividade_ensino_unidade":"04","codigo_natureza_organizacao_unidade":null,"codigo_nivel_hierarquia_unidade":null,"codigo_esfera_administrativa_unidade":"M ","data_atualizacao":"2025-09-03"}
```

#### 2.2.3. bronze_profissionais.py

- **Descrição**: Extrai dados dos profissionais de saúde cadastrados, utilizando o pysus para obter os arquivos mais recentes.
- **Fonte**: Arquivos de profissionais do CNES (via pysus).
- **Observações**:
  - Devido ao grande volume de dados, o script utiliza processamento em chunks para evitar travamentos.
  - **Melhoria Sugerida**: Avaliar a substituição do pysus por extração via FTP.
- **Colunas do Parquet (Exemplo)**: CNES, CODUFMUN, REGSAUDE, ..., NAT_JUR

#### 2.2.4. bronze_servicos.py

- **Descrição**: Extrai dados sobre os serviços oferecidos pelos estabelecimentos de saúde, utilizando o pysus para obter os arquivos mais recentes.
- **Fonte**: Arquivos de serviços do CNES (via pysus).
- **Melhoria Sugerida**: Avaliar a substituição do pysus por extração via FTP.
- **Formato de Saída (Exemplo - Parquet)**:

```parquet
{"CNES":"0271438","CODUFMUN":"120001","SERV_ESP":"141","CLASS_SR":"001","SRVUNICO":"141","TP_UNID":"50","TURNO_AT":"03","AMB_NSUS":0,"AMB_SUS":1,"HOSP_NSUS":0,"HOSP_SUS":1}
```

#### 2.2.5. bronze_leitos.py

- **Descrição**: Extrai dados sobre a quantidade e tipo de leitos disponíveis nos estabelecimentos de saúde, utilizando o pysus para obter os arquivos mais recentes.
- **Fonte**: Arquivos de leitos do CNES (via pysus).
- **Melhoria Sugerida**: Avaliar a substituição do pysus por extração via FTP.
- **Formato de Saída (Exemplo - Parquet)**:

```parquet
{"CNES":"5701929","CODUFMUN":"120001","REGSAUDE":"001 ","MICR_REG":"","DISTRSAN":"","DISTRADM":"","TPGESTAO":"E","PF_PJ":"3","CPF_CNPJ":"00000000000000","NIV_DEP":"3","CNPJ_MAN":"04034526000143","ESFERA_A":"","ATIVIDAD":"04","RETENCAO":"","NATUREZA":"","CLIENTEL":"03","TP_UNID":"15","TURNO_AT":"06","NIV_HIER":"","TERCEIRO":"","TP_LEITO":"2 ","CODLEITO":"33","QT_EXIST":"   3","QT_CONTR":"   0","QT_SUS":"   3","QT_NSUS":"   0","COMPETEN":"202507","NAT_JUR":"1023"}
```

#### 2.2.6. bronze_tipo_unidade.py

- **Descrição**: Extrai os tipos de unidades de saúde cadastrados no CNES.
- **Fonte**: https://apidadosabertos.saude.gov.br/cnes/tipounidades
- **Melhoria Sugerida**: Pode ser substituído por extração via FTP, caso um arquivo correspondente esteja disponível.
- **Formato de Saída (Exemplo - JSON)**:

```json
{"tipos_unidade": [{"codigo_tipo_unidade": 80, "descricao_tipo_unidade": "LABORATORIO DE SAUDE PUBLICA"}, {"codigo_tipo_unidade": 81, "descricao_tipo_unidade": "CENTRAL DE REGULACAO DO ACESSO"}, {"codigo_tipo_unidade": 79, "descricao_tipo_unidade": "OFICINA ORTOPEDICA"}, {"codigo_tipo_unidade": 82, "descricao_tipo_unidade": "CENTRAL DE NOTIFICACAO,CAPTACAO E DISTRIB DE ORGAOS ESTADUAL"}, {"codigo_tipo_unidade": 78, "descricao_tipo_unidade": "UNIDADE DE ATENCAO EM REGIME RESIDENCIAL"}, {"codigo_tipo_unidade": 74, "descricao_tipo_unidade": "POLO ACADEMIA DA SAUDE"}, {"codigo_tipo_unidade": 75, "descricao_tipo_unidade": "TELESSAUDE"}, {"codigo_tipo_unidade": 77, "descricao_tipo_unidade": "SERVICO DE ATENCAO DOMICILIAR ISOLADO(HOME CARE)"}, {"codigo_tipo_unidade": 76, "descricao_tipo_unidade": "CENTRAL DE REGULACAO MEDICA DAS URGENCIAS"}, {"codigo_tipo_unidade": 69, "descricao_tipo_unidade": "CENTRO DE ATENCAO HEMOTERAPIA E OU HEMATOLOGICA"}]}
```

#### 2.2.7. silver_estabelecimento.py

- **Descrição**: Limpa e padroniza os dados dos estabelecimentos. Inclui:
  - Seleção de colunas relevantes.
  - Unificação de dados de estabelecimentos (pysus) com informações complementares da API do CNES.
  - Tratamento de valores nulos e padronização de formatos.
  - Filtragem por tipos de unidades de saúde de interesse.
- **Entradas**: bronze_estabelecimentos.py e bronze_tipo_unidade.py (para mapeamento).
- **Saída (Exemplo)**:

```json
{"CNES":"0153281","CODUFMUN":"120001","COD_CEP":"69945000","TP_UNID":"70","nome_razao_social":"CENTRO DE ATENCAO PSICOSSOCIAL","nome_fantasia":"CENTRO DE ATENCAO PSICOSSOCIAL SALVADOR DIAS DA SILVA","endereco_estabelecimento":"AVENIDA BRASIL","numero_estabelecimento":"S/N","bairro_estabelecimento":"CENTRO","latitude_estabelecimento_decimo_grau":-10.078471911109563,"longitude_estabelecimento_decimo_grau":-67.05347145624873,"numero_telefone_estabelecimento":null,"endereco_email_estabelecimento":null}
```

#### 2.2.8. silver_dados_auxiliares.py

- **Descrição**: Filtra e prepara dados auxiliares.
- **Revisão**: A observação de que "é desnecessário, pois existe uma tabela de conselho que poderia filtrar pelo conselho desejado" é um ponto crucial. Se o objetivo final é contar profissionais por conselho, a filtragem deve ser baseada nos dados de conselho, e não na CBO. Esta etapa deve focar na criação de dimensões limpas e prontas para junção.
- **Entradas**: Dados brutos de dimensões (ex: CBO, Conselhos, etc.).
- **Saída (Exemplo - CBOs de Interesse)**:

```json
{
    "225154": "MEDICO ANTROPOSOFICO",
    "225355": "MEDICO RADIOLOGISTA INTERVENCIONISTA",
    "225103": "MEDICO INFECTOLOGISTA",
    "225105": "MEDICO ACUPUNTURISTA",
    "225106": "MEDICO LEGISTA",
    "225109": "MEDICO NEFROLOGISTA",
    "225110": "MEDICO ALERGISTA E IMUNOLOGISTA",
    "225112": "MEDICO NEUROLOGISTA"
}
```

#### 2.2.9. silver_servico.py

- **Descrição**: Limpa os dados de serviços, removendo colunas desnecessárias e ajustando formatos.
- **Entradas**: bronze_servicos.py.
- **Saída (Exemplo)**:

```json
{"CNES":"0153281","CODUFMUN":"120001","SERV_ESP":"115","CLASS_SR":"002","SRVUNICO":"115","TP_UNID":"70","TURNO_AT":"03","AMB_NSUS":1,"AMB_SUS":0,"HOSP_NSUS":1,"HOSP_SUS":0}
```

#### 2.2.10. silver_leitos.py

- **Descrição**: Limpa os dados de leitos, removendo colunas desnecessárias e ajustando formatos.
- **Entradas**: bronze_leitos.py.
- **Saída (Exemplo)**:

```json
{"CNES":"5701929","CODUFMUN":"120001","TURNO_AT":"06","TP_LEITO":"2 ","CODLEITO":"33","QT_SUS":3,"QT_NSUS":0}
```

#### 2.2.11. silver_profissionais.py

- **Descrição**: Limpa os dados de profissionais, removendo colunas desnecessárias, ajustando formatos e filtrando pelos profissionais de saúde de interesse.
- **Entradas**: bronze_profissionais.py e silver_dados_auxiliares.py (para filtros de CBO/Conselho).
- **Observação**: A filtragem deve ser cuidadosamente definida para reduzir o volume, possivelmente usando a tabela de conselhos em vez de CBOs individuais para uma abordagem mais escalável.
- **Saída (Exemplo)**:

```json
{"CNES":"0153281","CODUFMUN":"120001","CBO":"251510","CNS_PROF":"702009369235087"}
```

### 2.3. Camada Gold (Consumo)

Esta camada integra e agrega os dados Silver do IBGE e CNES, criando conjuntos de dados otimizados para consumo final.

#### 2.3.1. gold_infraestrutura.py

- **Descrição**: Une informações de estabelecimentos, serviços e leitos do CNES para calcular indicadores de infraestrutura de saúde por município.
- **Entradas**: silver_estabelecimento.py, silver_servico.py, silver_leitos.py.
- **Saída (Exemplo - por município)**:

```json
{
    "codigo_ibge":1100015,
    "qtde_ubs":4,
    "qtde_hospitais":2,
    "qtde_upas":0,
    "qtde_caps":1,
    "samu":false,
    "qtde_leitos_uti":0,
    "equipe_saude_familia":"Nao informado",
    "perc_cobertura_atencao_basica":"Nao informado"
}
```

#### 2.3.2. gold_profissionais.py

- **Descrição**: Une as informações, faz cálculo de profissionais. Será usado para consumo.
- **Saída (Exemplo)**:

```json
{
    "codigo_ibge":1100015,
    "municipio":"Alta Floresta D'Oeste",
    "uf":"RO",
    "qtde_medicos":62,
    "qtde_enfermeiros":39,
    "qtde_tecnicos_enfermagem":97,
    "qtde_psicologos":3
}
```

### 2.4. Integração CNES + IBGE

#### 2.4.1. gold_dados_gerais.py

- **Descrição**: Une as informações, faz cálculo das informações do IBGE. Será usado para consumo.
- **Saída (Exemplo)**:

```json
{
    "codigo_ibge":1100015,
    "municipio":"Alta Floresta D'Oeste",
    "uf":"RO",
    "estado":"Rondônia",
    "regiao":"Norte",
    "area_territorial_km2":7067.127,
    "densidade_demografica":3.04,
    "populacao_total":21494,
    "perc_populacao_urbana":60.35,
    "perc_populacao_rural":39.65
}
```

## 3. Consumo

Atualmente o consumo será realizado por uma API que pelo código IBGE do município irá retornar um relatório geral e a partir dele poderá acessar os estabelecimentos ligados ao município.