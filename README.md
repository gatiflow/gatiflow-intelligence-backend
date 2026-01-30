# GatiFlow Intelligence Backend

GatiFlow é um backend de inteligência B2B focado em detectar tendências reais de tecnologia,
skills e mercado a partir de dados públicos do StackOverflow.

O objetivo é transformar sinais técnicos (perguntas, tags, volume e engajamento)
em relatórios acionáveis para consultorias, startups e áreas de decisão técnica.

Este repositório contém o backend responsável por:
- Coletar dados do StackOverflow
- Normalizar e enriquecer esses dados
- Gerar insumos para relatórios estratégicos
## 🎯 Público-alvo & Proposta de Valor

### 🎯 Público-alvo inicial (ICP)

O **GatiFlow Intelligence** é projetado para atender principalmente **consultorias B2B de tecnologia e dados** que precisam identificar talentos técnicos reais a partir de sinais públicos confiáveis.

Clientes ideais incluem:
- Consultorias de dados, IA e engenharia de software
- Boutiques de recrutamento técnico
- Startups em crescimento (Series A–B)
- Empresas médias estruturando times de tecnologia
- Founders técnicos validando talentos e parcerias

---

### 💡 Problema que resolvemos

A maioria das empresas depende de fontes tradicionais como LinkedIn, que frequentemente apresentam:
- perfis inflados ou desatualizados
- pouca evidência técnica real
- alto ruído e baixa confiabilidade

Por outro lado, o GitHub contém **sinais técnicos reais**, porém:
- os dados são dispersos
- difíceis de interpretar manualmente
- inviáveis de analisar em escala sem automação

O GatiFlow resolve esse problema ao transformar atividade técnica pública em **inteligência acionável**.

---

### 🧠 O que o GatiFlow entrega

O backend do GatiFlow:
- coleta dados públicos do GitHub de forma ética
- cruza múltiplos sinais técnicos
- calcula scores interpretáveis de senioridade e influência
- classifica perfis por especialização técnica

O resultado são **insights claros**, prontos para apoiar decisões estratégicas.

---

### 📊 Produto inicial: Relatório de Inteligência Técnica

O primeiro produto vendável do GatiFlow é o:

**Relatório de Inteligência de Talentos Técnicos (baseado em GitHub)**

Esse relatório responde perguntas como:
- Quem são os desenvolvedores mais relevantes em determinado nicho?
- Quem possui senioridade técnica real versus presença social?
- Onde estão talentos fora do radar tradicional?
- Qual o nível técnico médio de uma região, stack ou comunidade?

---

### 🧩 Diferencial competitivo

O GatiFlow **não é**:
- uma plataforma de recrutamento
- um scraper agressivo
- um banco de currículos

O GatiFlow **é**:
- uma camada de inteligência técnica
- baseada em sinais reais e públicos
- com metodologia transparente
- pensada para decisões B2B
## 📄 Estrutura do Relatório Vendável (MVP)

O primeiro produto do GatiFlow é um **Relatório de Inteligência Técnica**,
gerado sob demanda, com base em dados públicos do GitHub.

O relatório é estruturado para apoiar **decisões reais de negócio**,
não apenas curiosidade técnica.

---

### 1️⃣ Visão Geral do Mercado Técnico

**Objetivo:**  
Oferecer uma visão macro do cenário técnico analisado.

**Conteúdo:**
- Volume total de perfis analisados
- Principais stacks tecnológicas identificadas
- Distribuição geográfica dos talentos
- Nível médio de senioridade técnica

**Dados utilizados (backend):**
- `search_users()` — volume e filtros
- Linguagens inferidas via query
- Localização dos perfis
- Score médio (`calculate_score`)

---

### 2️⃣ Ranking de Talentos Técnicos

**Objetivo:**  
Identificar os profissionais tecnicamente mais relevantes no recorte analisado.

**Conteúdo:**
- Lista ordenada por score técnico
- Nome / username
- Role inferido
- Score GatiFlow (65–99)
- Link para o perfil público

**Dados utilizados (backend):**
- `fetch_talents()`
- `calculate_score()`
- `_infer_role()`

---

### 3️⃣ Distribuição de Senioridade

**Objetivo:**  
Entender a maturidade técnica do mercado.

**Faixas sugeridas:**
- 90–99 → Lideranças técnicas / referência
- 80–89 → Sênior
- 70–79 → Pleno
- 65–69 → Júnior / emergente

**Dados utilizados (backend):**
- Score final por perfil

---

### 4️⃣ Análise de Especialização Técnica

**Objetivo:**  
Mapear quais perfis dominam quais áreas técnicas.

**Conteúdo:**
- Agrupamento por role inferido
- Frequência de cada especialização
- Perfis destaque por área

**Dados utilizados (backend):**
- `_infer_role()`
- Bio + métricas de perfil

---

### 5️⃣ Insights Estratégicos (Parte Mais Valiosa)

**Objetivo:**  
Transformar dados técnicos em recomendações de negócio.

**Exemplos de insights:**
- Onde estão talentos subexplorados
- Regiões com alta densidade técnica e baixo custo
- Comunidades técnicas emergentes
- Riscos de escassez em determinadas stacks

**Dados utilizados (backend):**
- Agregações sobre scores
- Distribuição geográfica
- Roles + senioridade

---

### 6️⃣ Metodologia & Transparência

**Objetivo:**  
Gerar confiança no cliente.

**Conteúdo:**
- Fonte dos dados (GitHub público)
- Critérios de pontuação
- Limitações do modelo
- Uso ético dos dados

**Dados utilizados (backend):**
- Documentação do algoritmo
- `calculate_score()` explicado
