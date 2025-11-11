# Comparação de Estabelecimento: PySUS CNES vs API Dados Abertos

## 1. PySUS - CNES

O arquivo de estabelecimentos do [PySUS CNES](https://pysus.readthedocs.io/en/latest/databases/CNES.html) apresenta uma visão detalhada dos dados cadastrais e estruturais dos estabelecimentos de saúde registrados no CNES. Ele possui grande granularidade, especialmente nos campos relacionados à infraestrutura, leitos, serviços de apoio e convênios.

---

## 2. API Dados Abertos

A [API Dados Abertos](https://apidadosabertos.saude.gov.br/v1/#/CNES/get_cnes_estabelecimentos__codigo_cnes_) disponibiliza um modelo de dados mais moderno e enriquecido, com campos de identificação, localização, contato e classificação. Muitos desses campos não estão presentes no PySUS, como nome fantasia, endereço detalhado, latitude/longitude, telefone e e-mail. No entanto, observa-se que alguns campos da API podem vir nulos ou incompletos, e que os indicadores operacionais (como atendimento SUS, ambulatorial, hospitalar) nem sempre refletem a realidade com a mesma precisão do PySUS.

### Estrutura do Objeto ESTABELECIMENTO

| Atributo                                         | Propriedades                  | Tipo      | Tam. | Descrição                                                        | Validação |
|--------------------------------------------------|-------------------------------|-----------|------|------------------------------------------------------------------|-----------|
| codigo_cnes                                      | obrigatório, chave primária   | INT       | 7    | Código Nacional do Estabelecimento de Saúde                      | ✅        |
| numero_cnpj_entidade                             | opcional                      | CHAR      | 14   | CNPJ da entidade mantenedora                                     | ✅        |
| nome_razao_social                                | obrigatório                   | VARCHAR   | 255  | Razão social                                                     | ✅        |
| nome_fantasia                                    | opcional                      | VARCHAR   | 255  | Nome fantasia                                                    | ✅        |
| natureza_organizacao_entidade                    | opcional                      | VARCHAR   | 255  | Natureza da organização mantenedora (pública, privada etc.)      | ⚠️ Nulo   |
| tipo_gestao                                      | obrigatório                   | CHAR      | 1    | Tipo de gestão (M = Municipal, E = Estadual, D = Dupla)          | ✅        |
| descricao_nivel_hierarquia                       | opcional                      | VARCHAR   | 255  | Nível hierárquico do estabelecimento no sistema de saúde         | ⚠️ Nulo   |
| descricao_esfera_administrativa                  | obrigatório                   | VARCHAR   | 50   | Esfera administrativa                                            | ✅        |
| codigo_tipo_unidade                             | obrigatório                  | INT      | 2   | Tipo de unidade (ex.: 70 = Consultório isolado, 22 = Clínica especializada) | ✅ |
| codigo_cep_estabelecimento                       | obrigatório                   | CHAR      | 8    | CEP do estabelecimento                                           | ✅        |
| endereco_estabelecimento                         | obrigatório                   | VARCHAR   | 255  | Logradouro do endereço do estabelecimento                        | ✅        |
| numero_estabelecimento                           | opcional                      | VARCHAR   | 10   | Número do endereço (pode conter “S/N”)                           | ✅        |
| bairro_estabelecimento                           | obrigatório                   | VARCHAR   | 100  | Bairro onde o estabelecimento está localizado                    | ✅        |
| numero_telefone_estabelecimento                  | opcional                      | VARCHAR   | 20   | Telefone de contato do estabelecimento                           | ⚠️ Nulo   |
| latitude_estabelecimento_decimo_grau             | obrigatório                   | DECIMAL   | 15   | Latitude                                                         | ✅        |
| longitude_estabelecimento_decimo_grau            | obrigatório                   | DECIMAL   | 15   | Longitude                                                        | ✅        |
| endereco_email_estabelecimento                   | opcional                      | VARCHAR   | 255  | E-mail de contato do estabelecimento                             | ⚠️ Nulo   |
| numero_cnpj                                     | opcional                      | CHAR      | 14   | CNPJ do próprio estabelecimento (se diferente da entidade mantenedora) | ⚠️ Nulo   |
| codigo_identificador_turno_atendimento           | obrigatório                   | CHAR      | 2    | Código do turno de atendimento (ex.: 03 = manhã e tarde)         | ✅        |
| descricao_turno_atendimento                      | obrigatório                   | VARCHAR   | 100  | Descrição textual do turno de atendimento                        | ✅        |
| estabelecimento_faz_atendimento_ambulatorial_sus | obrigatório                   | CHAR      | 3    | Atende ambulatorial SUS (SIM/NÃO)                                | ✅        |
| codigo_estabelecimento_saude                     | obrigatório, chave composta   | CHAR      | 13   | Código único nacional (UF + município + CNES)                    | ✅        |
| codigo_uf                                        | obrigatório, chave estrangeira| INT       | 2    | Código da Unidade Federativa (IBGE)                              | ✅        |
| codigo_municipio                                 | obrigatório, chave estrangeira| INT       | 6    | Código do município (IBGE)                                       | ✅        |
| descricao_natureza_juridica_estabelecimento      | obrigatório                   | CHAR      | 4    | Código da natureza jurídica (ex.: 1244 = Empresário Individual)  | ✅        |
| codigo_motivo_desabilitacao_estabelecimento      | opcional                      | VARCHAR   | 2    | Motivo da desabilitação do estabelecimento, se houver            | ⚠️ Nulo   |
| estabelecimento_possui_centro_cirurgico          | opcional                      | BOOLEAN   | 1    | Indica se possui centro cirúrgico                                | ✅        |
| estabelecimento_possui_centro_obstetrico         | opcional                      | BOOLEAN   | 1    | Indica se possui centro obstétrico                               | ✅        |
| estabelecimento_possui_centro_neonatal           | opcional                      | BOOLEAN   | 1    | Indica se possui centro neonatal                                 | ✅        |
| estabelecimento_possui_atendimento_hospitalar    | opcional                      | BOOLEAN   | 1    | Indica se possui atendimento hospitalar                          | ✅        |
| estabelecimento_possui_servico_apoio             | opcional                      | BOOLEAN   | 1    | Indica se possui serviço de apoio                                | ✅        |
| estabelecimento_possui_atendimento_ambulatorial  | opcional                      | BOOLEAN   | 1    | Indica se possui atendimento ambulatorial                        | ✅        |
| codigo_atividade_ensino_unidade                  | opcional                      | CHAR      | 2    | Código da atividade de ensino vinculada (ex.: 04 = Ensino)       | ✅        |
| codigo_natureza_organizacao_unidade              | opcional                      | VARCHAR   | 5    | Código da natureza da organização vinculada                      | ⚠️ Nulo   |
| codigo_nivel_hierarquia_unidade                  | opcional                      | VARCHAR   | 5    | Código do nível hierárquico da unidade vinculada                 | ⚠️ Nulo   |
| codigo_esfera_administrativa_unidade             | opcional                      | CHAR      | 2    | Esfera administrativa abreviada (ex.: “M”)                       | ✅        |
| data_atualizacao                                 | obrigatório                   | DATE      | 10   | Data da última atualização                                       | ✅        |



## 3. Comparação de Campos

### 3.1. Equivalência de Campos

Em geral, os campos de identificação e localização são melhor representados na API, enquanto os campos operacionais e de capacidade são mais confiáveis no PySUS.

| PySUS (Origem) | API Dados Abertos (Destino) | Observação / Equivalência |
|----------------|-----------------------------|--------------------------|
| CNES          | codigo_cnes                  | Equivalência Direta. Chave primária. |
| CODUFMUN      | codigo_municipio             | Equivalência Direta. Código IBGE do município (6 dígitos). API também fornece codigo_uf (2 dígitos). |
| COD_CEP       | codigo_cep_estabelecimento   | Equivalência Direta. CEP do estabelecimento. |
| CNPJ_MAN      | numero_cnpj_entidade         | Equivalência Semântica. CNPJ da mantenedora. |
| CPF_CNPJ      | numero_cnpj                  | Equivalência Provável. No PySUS pode ser "0000..."; na API null (mesmo da mantenedora). |
| PF_PJ         | (não existe)                 | PySUS diferencia PF/PJ; API infere pelo campo de natureza jurídica ou tamanho do CNPJ. |
| TPGESTAO      | tipo_gestao                  | Equivalência Direta. Ambos mostram "M" (Municipal). |
| ESFERA_A      | codigo_esfera_administrativa_unidade / descricao_esfera_administrativa | Correspondência. PySUS é código; API fornece código e descrição. |
| TP_UNID       | codigo_tipo_unidade          | Equivalência Direta. Ex: "70" (Consultório isolado). |
| TURNO_AT      | codigo_identificador_turno_atendimento / descricao_turno_atendimento | Correspondência. PySUS é código; API fornece código e descrição. |
| NAT_JUR       | descricao_natureza_juridica_estabelecimento | Equivalência Direta (código). Nome do campo na API é "descricao..." mas contém o código. |
| ATIVIDAD      | codigo_atividade_ensino_unidade | Equivalência Direta. Ex: "04" (Ensino). |
| NIV_HIER      | codigo_nivel_hierarquia_unidade / descricao_nivel_hierarquia | Correspondência. Ambos podem estar vazios/nulos. |
| MOTDESAB      | codigo_motivo_desabilitacao_estabelecimento | Equivalência Semântica. Ambos podem estar vazios/nulos. |
| DT_ATUA       | data_atualizacao             | Equivalência Conceitual. PySUS: AAAAMM, API: AAAA-MM-DD. |
| VINC_SUS      | estabelecimento_faz_atendimento_ambulatorial_sus | **Conflito:** PySUS: "1" (Sim), API: "NAO". |
| ATENDAMB      | estabelecimento_possui_atendimento_ambulatorial | **Conflito:** PySUS: "1" (Sim), API: 0 (Não). |
| CENTRCIR      | estabelecimento_possui_centro_cirurgico | Equivalência Direta. Booleano. |
| CENTROBS      | estabelecimento_possui_centro_obstetrico | Equivalência Direta. Booleano. |
| CENTRNEO      | estabelecimento_possui_centro_neonatal | Equivalência Direta. Booleano. |
| ATENDHOS      | estabelecimento_possui_atendimento_hospitalar | Equivalência Direta. Booleano. |
| SERAPOIO      | estabelecimento_possui_servico_apoio | Equivalência Direta. Booleano. |
| AP02CV01      | (não existe)                 | PySUS detalha convênios; API resume. |

---

### 3.2. Campos Exclusivos e Diferenças Notáveis

#### A) Campos Exclusivos da API (Enriquecimento)

A API traz informações complementares importantes, como nome fantasia, endereço completo, bairro, latitude/longitude, telefone e e-mail. Esses dados enriquecem o modelo e facilitam integrações e visualizações.

#### B) Campos Exclusivos do PySUS (Granularidade)

O PySUS, por sua vez, detalha a infraestrutura, leitos, serviços de apoio, comissões e convênios de forma muito mais granular. Esses campos são essenciais para análises operacionais e de capacidade.

---

### 3.3. Conflitos e Pontos de Atenção

Durante a análise, foram identificados alguns conflitos entre os dados das duas fontes, principalmente nos indicadores de atendimento SUS e ambulatorial. Em situações de divergência, será preferenciado os dados do PySUS, pois refletem melhor a realidade operacional do estabelecimento.

---

## 4. Recomendações para Modelo de Dados (Golden Record)

Estratégia para o modelo de dados:

- Utilizar a API como fonte principal para identificação, localização e enriquecimento dos dados (nome, endereço, contato, coordenadas, etc.).
- Utilizar o PySUS como fonte principal para os campos operacionais e de capacidade (indicadores de atendimento, leitos, infraestrutura, serviços de apoio, etc.).
- Documentar todos os conflitos encontrados e priorizar sempre a granularidade e precisão dos dados.

### Campos Essenciais

**Chaves Primárias e Estrangeiras**
- codigo_cnes
- codigo_municipio (IBGE 6 dígitos)
- codigo_uf

**Identificação**
- nome_razao_social
- nome_fantasia
- numero_cnpj_entidade (mantenedora)
- numero_cnpj (estabelecimento, se houver)

**Localização e Contato**
- endereco_estabelecimento
- numero_estabelecimento
- bairro_estabelecimento
- codigo_cep_estabelecimento
- latitude_estabelecimento_decimo_grau
- longitude_estabelecimento_decimo_grau
- numero_telefone_estabelecimento
- endereco_email_estabelecimento

**Classificação**
- codigo_tipo_unidade (e descrição)
- descricao_esfera_administrativa
- tipo_gestao
- descricao_natureza_juridica_estabelecimento (código e descrição)

**Indicadores Operacionais (PySUS como fonte principal)**
- VINC_SUS (1/0) — Atende SUS?
- ATENDAMB — Possui Atendimento Ambulatorial
- ATENDHOS — Possui Atendimento Hospitalar
- URGEMERG — Possui Urgência/Emergência
- CENTRCIR, CENTROBS, CENTRNEO — Infraestrutura complexa

---

## Exemplos

Pysus

```parquet
{"CNES":"0153281"
"CODUFMUN":"120001"
"COD_CEP":"69945000"
"CPF_CNPJ":"00000000000000"
"PF_PJ":"3"
"NIV_DEP":"3"
"CNPJ_MAN":"84306737000127"
"COD_IR":""
"REGSAUDE":""
"MICR_REG":""
"DISTRSAN":""
"DISTRADM":""
"VINC_SUS":"1"
"TPGESTAO":"M"
"ESFERA_A":"M "
"RETENCAO":""
"ATIVIDAD":"04"
"NATUREZA":""
"CLIENTEL":"01"
"TP_UNID":"70"
"TURNO_AT":"03"
"NIV_HIER":""
"TP_PREST":"99"
"CO_BANCO":""
"CO_AGENC":""
"C_CORREN":""
"CONTRATM":""
"DT_PUBLM":""
"CONTRATE":""
"DT_PUBLE":""
"ALVARA":""
"DT_EXPED":""
"ORGEXPED":""
"AV_ACRED":""
"CLASAVAL":""
"DT_ACRED":""
"AV_PNASS":""
"DT_PNASS":""
"GESPRG1E":"0"
"GESPRG1M":"0"
"GESPRG2E":"0"
"GESPRG2M":"1"
"GESPRG4E":"0"
"GESPRG4M":"0"
"NIVATE_A":"1"
"GESPRG3E":"0"
"GESPRG3M":"0"
"GESPRG5E":"0"
"GESPRG5M":"0"
"GESPRG6E":"0"
"GESPRG6M":"0"
"NIVATE_H":"0"
"QTLEITP1":"   0"
"QTLEITP2":"   0"
"QTLEITP3":"   0"
"LEITHOSP":"0"
"QTINST01":"  0"
"QTINST02":"  0"
"QTINST03":"  0"
"QTINST04":"  0"
"QTINST05":"  0"
"QTINST06":"  0"
"QTINST07":"  0"
"QTINST08":"  0"
"QTINST09":"  0"
"QTINST10":"  0"
"QTINST11":"  0"
"QTINST12":"  0"
"QTINST13":"  0"
"QTINST14":"  0"
"URGEMERG":"0"
"QTINST15":"  1"
"QTINST16":"  0"
"QTINST17":"  0"
"QTINST18":"  0"
"QTINST19":"  0"
"QTINST20":"  0"
"QTINST21":"  0"
"QTINST22":"  0"
"QTINST23":"  0"
"QTINST24":"  0"
"QTINST25":"  1"
"QTINST26":"  0"
"QTINST27":"  0"
"QTINST28":"  0"
"QTINST29":"  0"
"QTINST30":"  0"
"ATENDAMB":"1"
"QTINST31":"  0"
"QTINST32":"  0"
"QTINST33":"  0"
"CENTRCIR":"0"
"QTINST34":"  0"
"QTINST35":"  0"
"QTINST36":"  0"
"QTINST37":"  0"
"CENTROBS":"0"
"QTLEIT05":"  0"
"QTLEIT06":"  0"
"QTLEIT07":"  0"
"QTLEIT08":"  0"
"QTLEIT09":"  0"
"QTLEIT19":"  0"
"QTLEIT20":"  0"
"QTLEIT21":"  0"
"QTLEIT22":"  0"
"QTLEIT23":"  0"
"QTLEIT32":"  0"
"QTLEIT34":"  0"
"QTLEIT38":"  0"
"QTLEIT39":"  0"
"QTLEIT40":"  0"
"CENTRNEO":"0"
"ATENDHOS":"0"
"SERAP01P":"0"
"SERAP01T":"0"
"SERAP02P":"0"
"SERAP02T":"0"
"SERAP03P":"0"
"SERAP03T":"0"
"SERAP04P":"0"
"SERAP04T":"0"
"SERAP05P":"0"
"SERAP05T":"0"
"SERAP06P":"0"
"SERAP06T":"0"
"SERAP07P":"0"
"SERAP07T":"0"
"SERAP08P":"0"
"SERAP08T":"0"
"SERAP09P":"0"
"SERAP09T":"0"
"SERAP10P":"0"
"SERAP10T":"0"
"SERAP11P":"0"
"SERAP11T":"0"
"SERAPOIO":"0"
"RES_BIOL":"1"
"RES_QUIM":"1"
"RES_RADI":"0"
"RES_COMU":"0"
"COLETRES":"1"
"COMISS01":"0"
"COMISS02":"0"
"COMISS03":"0"
"COMISS04":"0"
"COMISS05":"0"
"COMISS06":"0"
"COMISS07":"0"
"COMISS08":"0"
"COMISS09":"0"
"COMISS10":"0"
"COMISS11":"0"
"COMISS12":"0"
"COMISSAO":"0"
"AP01CV01":"0"
"AP01CV02":"0"
"AP01CV03":"0"
"AP01CV04":"0"
"AP01CV05":"0"
"AP01CV06":"0"
"AP01CV07":"0"
"AP02CV01":"1"
"AP02CV02":"0"
"AP02CV03":"0"
"AP02CV04":"0"
"AP02CV05":"0"
"AP02CV06":"0"
"AP02CV07":"0"
"AP03CV01":"0"
"AP03CV02":"0"
"AP03CV03":"0"
"AP03CV04":"0"
"AP03CV05":"0"
"AP03CV06":"0"
"AP03CV07":"0"
"AP04CV01":"0"
"AP04CV02":"0"
"AP04CV03":"0"
"AP04CV04":"0"
"AP04CV05":"0"
"AP04CV06":"0"
"AP04CV07":"0"
"AP05CV01":"0"
"AP05CV02":"0"
"AP05CV03":"0"
"AP05CV04":"0"
"AP05CV05":"0"
"AP05CV06":"0"
"AP05CV07":"0"
"AP06CV01":"0"
"AP06CV02":"0"
"AP06CV03":"0"
"AP06CV04":"0"
"AP06CV05":"0"
"AP06CV06":"0"
"AP06CV07":"0"
"AP07CV01":"0"
"AP07CV02":"0"
"AP07CV03":"0"
"AP07CV04":"0"
"AP07CV05":"0"
"AP07CV06":"0"
"AP07CV07":"0"
"ATEND_PR":"1"
"DT_ATUAL":"202505"
"COMPETEN":"202509"
"NAT_JUR":"1244"}
```
``` parquet
{"CNES":"2304279"
"CODUFMUN":"290020"
"COD_CEP":"48680000"
"CPF_CNPJ":"00000000000000"
"PF_PJ":"3"
"NIV_DEP":"3"
"CNPJ_MAN":"13915657000120"
"COD_IR":""
"REGSAUDE":"010 "
"MICR_REG":""
"DISTRSAN":""
"DISTRADM":""
"VINC_SUS":"1"
"TPGESTAO":"M"
"ESFERA_A":"M "
"RETENCAO":""
"ATIVIDAD":"04"
"NATUREZA":""
"CLIENTEL":"03"
"TP_UNID":"02"
"TURNO_AT":"03"
"NIV_HIER":""
"TP_PREST":"99"
"CO_BANCO":""
"CO_AGENC":""
"C_CORREN":""
"CONTRATM":""
"DT_PUBLM":""
"CONTRATE":""
"DT_PUBLE":""
"ALVARA":""
"DT_EXPED":""
"ORGEXPED":""
"AV_ACRED":""
"CLASAVAL":""
"DT_ACRED":""
"AV_PNASS":""
"DT_PNASS":""
"GESPRG1E":"0"
"GESPRG1M":"1"
"GESPRG2E":"0"
"GESPRG2M":"0"
"GESPRG4E":"0"
"GESPRG4M":"0"
"NIVATE_A":"1"
"GESPRG3E":"0"
"GESPRG3M":"0"
"GESPRG5E":"0"
"GESPRG5M":"0"
"GESPRG6E":"0"
"GESPRG6M":"0"
"NIVATE_H":"0"
"QTLEITP1":"   0"
"QTLEITP2":"   0"
"QTLEITP3":"   0"
"LEITHOSP":"0"
"QTINST01":"  0"
"QTINST02":"  0"
"QTINST03":"  0"
"QTINST04":"  0"
"QTINST05":"  0"
"QTINST06":"  0"
"QTINST07":"  0"
"QTINST08":"  0"
"QTINST09":"  0"
"QTINST10":"  0"
"QTINST11":"  0"
"QTINST12":"  0"
"QTINST13":"  0"
"QTINST14":"  0"
"URGEMERG":"0"
"QTINST15":"  1"
"QTINST16":"  0"
"QTINST17":"  0"
"QTINST18":"  0"
"QTINST19":"  0"
"QTINST20":"  0"
"QTINST21":"  0"
"QTINST22":"  0"
"QTINST23":"  1"
"QTINST24":"  0"
"QTINST25":"  1"
"QTINST26":"  1"
"QTINST27":"  0"
"QTINST28":"  0"
"QTINST29":"  1"
"QTINST30":"  0"
"ATENDAMB":"1"
"QTINST31":"  0"
"QTINST32":"  0"
"QTINST33":"  0"
"CENTRCIR":"0"
"QTINST34":"  0"
"QTINST35":"  0"
"QTINST36":"  0"
"QTINST37":"  0"
"CENTROBS":"0"
"QTLEIT05":"  0"
"QTLEIT06":"  0"
"QTLEIT07":"  0"
"QTLEIT08":"  0"
"QTLEIT09":"  0"
"QTLEIT19":"  0"
"QTLEIT20":"  0"
"QTLEIT21":"  0"
"QTLEIT22":"  0"
"QTLEIT23":"  0"
"QTLEIT32":"  0"
"QTLEIT34":"  0"
"QTLEIT38":"  0"
"QTLEIT39":"  0"
"QTLEIT40":"  0"
"CENTRNEO":"0"
"ATENDHOS":"0"
"SERAP01P":"1"
"SERAP01T":"0"
"SERAP02P":"0"
"SERAP02T":"0"
"SERAP03P":"1"
"SERAP03T":"0"
"SERAP04P":"1"
"SERAP04T":"0"
"SERAP05P":"0"
"SERAP05T":"0"
"SERAP06P":"0"
"SERAP06T":"0"
"SERAP07P":"0"
"SERAP07T":"0"
"SERAP08P":"0"
"SERAP08T":"0"
"SERAP09P":"0"
"SERAP09T":"0"
"SERAP10P":"0"
"SERAP10T":"0"
"SERAP11P":"0"
"SERAP11T":"0"
"SERAPOIO":"1"
"RES_BIOL":"1"
"RES_QUIM":"0"
"RES_RADI":"0"
"RES_COMU":"1"
"COLETRES":"1"
"COMISS01":"0"
"COMISS02":"0"
"COMISS03":"0"
"COMISS04":"0"
"COMISS05":"0"
"COMISS06":"0"
"COMISS07":"0"
"COMISS08":"0"
"COMISS09":"0"
"COMISS10":"1"
"COMISS11":"1"
"COMISS12":"0"
"COMISSAO":"1"
"AP01CV01":"0"
"AP01CV02":"0"
"AP01CV03":"0"
"AP01CV04":"0"
"AP01CV05":"0"
"AP01CV06":"0"
"AP01CV07":"0"
"AP02CV01":"1"
"AP02CV02":"0"
"AP02CV03":"0"
"AP02CV04":"0"
"AP02CV05":"0"
"AP02CV06":"0"
"AP02CV07":"0"
"AP03CV01":"0"
"AP03CV02":"0"
"AP03CV03":"0"
"AP03CV04":"0"
"AP03CV05":"0"
"AP03CV06":"0"
"AP03CV07":"0"
"AP04CV01":"0"
"AP04CV02":"0"
"AP04CV03":"0"
"AP04CV04":"0"
"AP04CV05":"0"
"AP04CV06":"0"
"AP04CV07":"0"
"AP05CV01":"0"
"AP05CV02":"0"
"AP05CV03":"0"
"AP05CV04":"0"
"AP05CV05":"0"
"AP05CV06":"0"
"AP05CV07":"0"
"AP06CV01":"0"
"AP06CV02":"0"
"AP06CV03":"0"
"AP06CV04":"0"
"AP06CV05":"0"
"AP06CV06":"0"
"AP06CV07":"0"
"AP07CV01":"0"
"AP07CV02":"0"
"AP07CV03":"0"
"AP07CV04":"0"
"AP07CV05":"0"
"AP07CV06":"0"
"AP07CV07":"0"
"ATEND_PR":"1"
"DT_ATUAL":"202510"
"COMPETEN":"202509"
"NAT_JUR":"1244"}
```

---

```json
{
  "codigo_cnes": 153281,
  "numero_cnpj_entidade": "84306737000127",
  "nome_razao_social": "CENTRO DE ATENCAO PSICOSSOCIAL",
  "nome_fantasia": "CENTRO DE ATENCAO PSICOSSOCIAL SALVADOR DIAS DA SILVA",
  "natureza_organizacao_entidade": null,
  "tipo_gestao": "M",
  "descricao_nivel_hierarquia": null,
  "descricao_esfera_administrativa": "MUNICIPAL",
  "codigo_tipo_unidade": 70,
  "codigo_cep_estabelecimento": "69945000",
  "endereco_estabelecimento": "AVENIDA BRASIL",
  "numero_estabelecimento": "S/N",
  "bairro_estabelecimento": "CENTRO",
  "numero_telefone_estabelecimento": null,
  "latitude_estabelecimento_decimo_grau": -10.078471911109563,
  "longitude_estabelecimento_decimo_grau": -67.05347145624873,
  "endereco_email_estabelecimento": null,
  "numero_cnpj": null,
  "codigo_identificador_turno_atendimento": "03",
  "descricao_turno_atendimento": "ATENDIMENTOS NOS TURNOS DA MANHA E A TARDE",
  "estabelecimento_faz_atendimento_ambulatorial_sus": "NAO",
  "codigo_estabelecimento_saude": "1200010153281",
  "codigo_uf": 12,
  "codigo_municipio": 120001,
  "descricao_natureza_juridica_estabelecimento": "1244",
  "codigo_motivo_desabilitacao_estabelecimento": null,
  "estabelecimento_possui_centro_cirurgico": 0,
  "estabelecimento_possui_centro_obstetrico": 0,
  "estabelecimento_possui_centro_neonatal": 0,
  "estabelecimento_possui_atendimento_hospitalar": 0,
  "estabelecimento_possui_servico_apoio": 0,
  "estabelecimento_possui_atendimento_ambulatorial": 0,
  "codigo_atividade_ensino_unidade": "04",
  "codigo_natureza_organizacao_unidade": null,
  "codigo_nivel_hierarquia_unidade": null,
  "codigo_esfera_administrativa_unidade": "M ",
  "data_atualizacao": "2025-09-03"
}
```

```json
{
  "codigo_cnes": 2304279,
  "numero_cnpj_entidade": "13915657000120",
  "nome_razao_social": "MUNICIPIO DE ABARE",
  "nome_fantasia": "UNIDADE DE SAUDE DA FAMILIA JOSINO SOARES DA SILVA",
  "natureza_organizacao_entidade": null,
  "tipo_gestao": "M",
  "descricao_nivel_hierarquia": null,
  "descricao_esfera_administrativa": "MUNICIPAL",
  "codigo_tipo_unidade": 2,
  "codigo_cep_estabelecimento": "48680000",
  "endereco_estabelecimento": "POV ICOZEIRA",
  "numero_estabelecimento": "100",
  "bairro_estabelecimento": "ZONA RURAL",
  "numero_telefone_estabelecimento": "(75)32872387",
  "latitude_estabelecimento_decimo_grau": -8.94104646322875,
  "longitude_estabelecimento_decimo_grau": -39.32887673377991,
  "endereco_email_estabelecimento": "smsabare@gmail.com",
  "numero_cnpj": null,
  "codigo_identificador_turno_atendimento": "03",
  "descricao_turno_atendimento": "ATENDIMENTOS NOS TURNOS DA MANHA E A TARDE",
  "estabelecimento_faz_atendimento_ambulatorial_sus": "SIM",
  "codigo_estabelecimento_saude": "2900202304279",
  "codigo_uf": 29,
  "codigo_municipio": 290020,
  "descricao_natureza_juridica_estabelecimento": "1244",
  "codigo_motivo_desabilitacao_estabelecimento": null,
  "estabelecimento_possui_centro_cirurgico": 0,
  "estabelecimento_possui_centro_obstetrico": 0,
  "estabelecimento_possui_centro_neonatal": 0,
  "estabelecimento_possui_atendimento_hospitalar": 0,
  "estabelecimento_possui_servico_apoio": 1,
  "estabelecimento_possui_atendimento_ambulatorial": 0,
  "codigo_atividade_ensino_unidade": "04",
  "codigo_natureza_organizacao_unidade": null,
  "codigo_nivel_hierarquia_unidade": null,
  "codigo_esfera_administrativa_unidade": "M ",
  "data_atualizacao": "2025-09-03"
}
```