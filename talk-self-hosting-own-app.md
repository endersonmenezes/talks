---
title: Hospedando um Portal em casa? Experiência, desafios e aprendizados!
type: talk
status: active
area: personal
tags:
  - kind/talk
  - area/personal
  - status/active
created: 2026-05-25
updated: 2026-05-26
source:
---

## Resumo

Esta palestra narra a jornada de construir e hospedar [api.codaqui.dev](https://api.codaqui.dev) em uma Raspberry Pi 4 dentro de casa — sem IPv4 público, sem VPS pago e com custo mensal próximo de zero. Partimos da motivação econômica e filosófica do self-hosting, passamos pela stack técnica completa (NestJS + PostgreSQL + Podman Compose), pelo processo de build para ARM64, pela exposição segura via Cloudflare Tunnel e pela gestão de deployments com Coolify. Uma jornada de quem aprendeu na prática que a nuvem nem sempre é a melhor resposta.

> [!NOTE] Sobre este documento
> Este arquivo nasceu de **experiências práticas do projeto Codaqui** combinadas com pesquisa técnica e teórica, com o auxílio de IA como parceira na organização e estruturação do conteúdo. Todo o código mencionado está disponível em [github.com/codaqui/institucional](https://github.com/codaqui/institucional) — **me faz um PR se encontrar algo errado** 😄

Blog complementar: [Cloudflare Tunnel: economizando IPv4 ao expor serviços em VMs](https://codaqui.dev/blog/2025/08/22/cloudflare-tunnel-economizando-ipv4-ao-expor-servicos-em-vms)

## Público-alvo

Desenvolvedores iniciantes e intermediários, entusiastas de infraestrutura e homelab, estudantes de computação interessados em DevOps e arquitetura de sistemas reais. Conhecimento básico de terminal e containers é útil, mas não obrigatório.

## Objetivo

O ouvinte deve sair entendendo **por que** self-hosting faz sentido econômica e filosoficamente, **o que** compõe a stack da Codaqui do ambiente local até a Raspberry Pi, e **como** os principais desafios — ARM64, exposição sem IPv4, gestão de secrets, migrations — foram resolvidos, com comandos reais e código que funciona.

---

## Roteiro Detalhado

### Bloco 1 — Abertura

> *Slide: título + foto de uma Raspberry Pi com Post-it "api.codaqui.dev"*

**Pergunta para o público:** "Quem aqui já teve um projeto pessoal ou de uma comunidade que morreu porque ficou caro demais na nuvem?"

A Codaqui é uma ONG. Zero fins lucrativos. Cada real conta. E em algum momento do crescimento da associação, precisamos de uma API: autenticação de membros com GitHub OAuth, integração com Stripe para doações, módulo financeiro de dupla partida, controle de despesas, transparência de gastos. Tudo isso vai muito além de um site estático.

A primeira pergunta foi inevitável: *onde hospedar?*

Uma VPS básica em 2025 custa entre R$ 50 e R$ 200 por mês. Um plano managed com banco de dados no Railway, Render ou Fly.io custa parecido ou mais. Em doze meses, isso é de R$ 600 a R$ 2.400 — dinheiro que poderia financiar eventos, brindes ou equipamentos para membros.

A alternativa: **uma Raspberry Pi 4B (hardware ~R$ 700, compra única) + internet residencial já existente + Cloudflare Tunnel (gratuito)** = custo mensal de aproximadamente R$ 0 (fora a energia elétrica, cerca de R$ 3–5/mês para um Pi em idle/baixo processamento).

Essa palestra conta como chegamos lá, o que aprendemos — e o que quebramos no caminho.

---

### Bloco 2 — O que é Self-Hosting? História e Filosofia

> *Slides: linha do tempo da computação + frase "The cloud is just someone else's computer"*

**Definição:**

Self-hosting é o ato de executar software e serviços em hardware que você controla, ao invés de delegar a um provedor terceiro. O controle pode ser um servidor físico em casa (homelab), uma VPS gerenciada por você, ou qualquer infraestrutura onde você é o responsável pelo sistema operacional acima.

**Uma breve história:**

| Época | Modelo predominante |
|---|---|
| **1960–1970s** | Mainframes centralizados. Computação era cara e rara. |
| **1980–1990s** | PCs pessoais. Compute voltou para casa. Servidores locais nas empresas. |
| **2000–2010s** | Internet + AWS (lançado em 2006) → o início da "nuvem pública". |
| **2010–2020s** | Cloud-first. *"Por que manter servidor se você pode só pagar?"* |
| **2020s→** | **Self-hosting renaissance**: custos de nuvem sobem, privacidade em pauta, LGPD/GDPR, hardware ARM barato e acessível. |

A narrativa dominante na última década foi: *"suba tudo na nuvem, não se preocupe com infraestrutura"*. Mas nos últimos anos uma reversão silenciosa aconteceu — especialmente para organizações pequenas ou grandes, projetos pessoais e comunidades sem fins lucrativos.

**Por que a reversão? Três fatores convergentes:**

1. **Custo**: os preços de cloud subiram consistentemente. A Amazon aumentou preços de instâncias EC2 em 2023. Serviços managed (RDS, ElastiCache, Lambda) têm custos que escalam depressa com o uso. [[#^ref-2-1|[2.1]]]
2. **Privacidade e soberania de dados**: a LGPD (Brasil, Lei 13.709/2018) e o GDPR (UE, Regulamento 2016/679) tornaram a localização e o controle dos dados uma questão legal, não apenas filosófica. [[#^ref-2-2|[2.2]]]
3. **Hardware ARM acessível**: Raspberry Pi 4/5, Orange Pi e similares transformaram um SBC de US$ 35–70 em um servidor doméstico viável para cargas modestas.

**A questão filosófica:**

> *"The cloud is just someone else's computer"*

Virou meme, mas contém uma verdade fundamental: toda infraestrutura "sem servidor" tem servidores — você simplesmente não os vê nem os controla. O preço da conveniência é a dependência e a perda de soberania sobre seus dados e processos.

**O que é computação em nuvem, afinal?** O NIST (National Institute of Standards and Technology) define formalmente: *"a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources"* [[#^ref-2-3|[2.3]]]. Cinco características essenciais: *on-demand self-service*, *broad network access*, *resource pooling*, *rapid elasticity*, *measured service*. É uma definição de conveniência — não de inevitabilidade.

Para uma ONG como a Codaqui, que publica transparência financeira de membros e processa doações via Stripe, a questão de quem controla esses dados não é abstrata.

---

### Bloco 3 — A Economia do Self-Hosting: Quando Faz Sentido?

> *Slides: gráfico de custo cloud vs. hardware próprio ao longo do tempo*

**O caso DHH e 37signals (2022–2023)**

Em outubro de 2022, David Heinemeier Hansson (criador do Ruby on Rails, co-fundador do Basecamp e do serviço de e-mail HEY) publicou um artigo direto ao ponto: *"Why we're leaving the cloud"*. A empresa, que processava dezenas de milhões de e-mails por dia no AWS e Google Cloud, calculou que gastaria **US$ 3,2 milhões em nuvem em 2023** — valor que, investido em servidores próprios, seria amortizado em menos de dois anos. Em março de 2023, a empresa anunciou a conclusão da migração. [[#^ref-3-1|[3.1]]]

O movimento atraiu atenção de todo o mercado, e a Andreessen Horowitz (a16z) publicou um estudo complementar: *"The Cost of Cloud, a Trillion Dollar Paradox"* (2021). A conclusão: empresas de software maduras gastam entre **50% e 80%** de suas receitas brutas em infraestrutura de nuvem. [[#^ref-3-2|[3.2]]]

**Mas isso vale para a Codaqui?**

Não exatamente — o racional de DHH se aplica a empresas com escala e carga previsível. Para nós, o cálculo é diferente:

| Item | VPS (12 meses) | Raspberry Pi 4B |
|---|---|---|
| Custo inicial | R$ 0 | ~R$ 700 (hardware) |
| Custo mensal | R$ 80–150 (VPS + RDS gerenciado) | ~R$ 5 (energia elétrica) |
| Custo em 12 meses | R$ 960–1.800 | ~R$ 760 (hardware + energia) |
| Custo em 24 meses | R$ 1.920–3.600 | ~R$ 820 |
| Controle operacional | Parcial | Total |
| Aprendizado técnico | Baixo | Alto |

Para projetos comunitários, educacionais ou de aprendizado, o Pi é especialmente interessante porque o hardware vira laboratório permanente mesmo quando a aplicação não está em uso.

**Quando self-hosting *não* faz sentido:**

- SLA crítico (uptime 99,99%) — energia e internet doméstica não garantem isso
- Equipes sem capacidade de manutenção técnica
- Escalabilidade imprevisível e rápida (Black Friday, viralização)
- Dados altamente sensíveis sem política de segurança física robusta

A decisão da Codaqui foi consciente: a API é importante, mas uma intermitência de algumas horas não é catastrófica. O custo educacional e financeiro favorece fortemente o Pi.

---

### Bloco 4 — A Stack da Codaqui: Cada Peça e Por Quê

> *Slides: diagrama de arquitetura em dois ambientes — local e produção (Pi)*

```
┌──────────────────────────────────────────────────────────────┐
│                      PRODUÇÃO (Raspberry Pi)                 │
│                                                              │
│  Internet ──► Cloudflare Edge ──► Tunnel ──► Raspberry Pi   │
│                    (DNS)                          │          │
│                                       ┌───────────▼──────┐  │
│                                       │ compose.prod.yaml │  │
│  api.codaqui.dev ────────────────────►│ backend : 3002   │  │
│                                       │ postgres : 5432  │  │
│                                       └──────────────────┘  │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                   DESENVOLVIMENTO LOCAL                      │
│                                                              │
│  localhost:3001 ── backend (NestJS) + Swagger /docs          │
│  localhost:3000 ── frontend (Docusaurus)                     │
│  localhost:5432 ── PostgreSQL 18                             │
│  stripe-cli    ── forward de webhooks do Stripe              │
└──────────────────────────────────────────────────────────────┘
```

**NestJS (Backend)**

NestJS é um framework Node.js para APIs server-side escaláveis, inspirado fortemente na arquitetura do Angular. Usa TypeScript por padrão, injeção de dependência nativa e decorators para definir módulos, controllers e services. [[#^ref-4-1|[4.1]]]

Por que NestJS e não Express puro, Fastify ou Go?

- **Estrutura opinada** → menos decisões de arquitetura para uma equipe pequena e voluntária
- **Integração nativa** com TypeORM, Passport, Swagger (OpenAPI)
- **Geração automática** de documentação da API — crucial para onboarding
- **Validação global** via `class-validator` + `ValidationPipe` (whitelist + transform)

A API da Codaqui expõe os seguintes módulos:

| Módulo | Descrição |
|---|---|
| **Auth** | GitHub OAuth 2.0 + JWT em httpOnly cookie |
| **Members** | Perfis e dados dos membros da associação |
| **Ledger** | Contabilidade de dupla partida (débito/crédito) |
| **Expenses** | Gestão de despesas organizacionais |
| **Stripe** | Checkout Sessions + Webhooks com validação de assinatura |
| **Club** | Programa de benefícios para membros |

**PostgreSQL 18**

Banco relacional open source, com suporte nativo a JSON, full-text search, particionamento e extensões. Escolha natural para dados financeiros que exigem consistência ACID. Rodamos a imagem `postgres:18-alpine` — mínima, cerca de 65 MB comprimida. Sem gerenciamento de schema dinâmico: todas as mudanças passam por migrations versionadas com TypeORM.

**Podman (e não Docker)**

Podman é um runtime de containers compatível com Docker, mas com uma diferença arquitetural importante: **sem daemon root**. Cada container roda como processo filho do usuário que o iniciou — sem o `dockerd` privilegiado em background. Isso melhora a postura de segurança e é o padrão recomendado em ambientes Linux modernos, inclusive em distribuições Red Hat e derivados. [[#^ref-4-2|[4.2]]]

Para o desenvolvedor, a experiência é idêntica:

```bash
# Docker
docker compose up

# Podman (mesma sintaxe)
podman compose up
```

O Makefile do projeto abstrai tudo via `podman compose -f compose.yaml [...]`.

**Cloudflare Tunnel**

Componente de rede responsável por expor o backend sem necessidade de IPv4 público. Veremos em detalhe no Bloco 7.

---

### Bloco 5 — Rodando Tudo Localmente: Do Clone ao Primeiro Request

> *Slides: fluxo de setup com código + saída do terminal*

**Pré-requisitos:**

- Node.js 24+
- Podman + podman-compose (ou Docker + docker-compose)
- Um OAuth App do GitHub configurado (gratuito)
- Opcional: conta Stripe em modo teste

**1. Clone e setup inicial**

```bash
git clone https://github.com/codaqui/institucional.git
cd institucional
make setup
```

O `make setup` faz três coisas em sequência:
1. Copia `.env.example` para `.env` se o arquivo ainda não existir
2. Roda `npm install` para as dependências do frontend (Docusaurus)
3. Roda `cd backend && npm install` para as dependências do backend (NestJS)

**2. Configurar o `.env`**

O `.env.example` é completamente documentado com comentários explicativos. As variáveis principais:

```bash
# Banco de dados
DB_PASSWORD=sua_senha_local   # openssl rand -hex 16

# GitHub OAuth — crie em: github.com/settings/developers → OAuth Apps
# Callback DEV: http://localhost:3001/auth/github/callback
GITHUB_CLIENT_ID=seu_client_id
GITHUB_CLIENT_SECRET=seu_client_secret

# JWT (gere com: openssl rand -hex 64)
JWT_SECRET=seu_secret_longo_aqui

# URLs (dev)
BACKEND_URL=http://localhost:3001
FRONTEND_URL=http://localhost:3000

# Stripe (opcional — modo teste)
STRIPE_SECRET_KEY=sk_test_...
```

**3. Subir a stack completa**

```bash
make up
```

O `make up` tem um comportamento inteligente: antes de subir todos os serviços, ele inicia o `stripe-cli`, aguarda 6 segundos para que o CLI gere o `STRIPE_WEBHOOK_SECRET`, captura esse secret dos logs e atualiza automaticamente o `.env`. Depois sobe todos os serviços.

Resultado — quatro containers ativos:

| Container | Porta | Descrição |
|---|---|---|
| `codaqui_postgres` | 5432 | PostgreSQL 18 |
| `codaqui_backend` | 3001 | API NestJS (mapeada de 3000→3001) |
| `codaqui_docusaurus` | 3000 | Site/Frontend Docusaurus |
| `codaqui_stripe_cli` | — | Forward de webhooks Stripe |

**4. Rodar as migrations do banco**

```bash
make migration-run
```

TypeORM gerencia o schema via migrations versionadas em `backend/src/migrations/`. O projeto usa `synchronize: false` em todos os ambientes — cada mudança de schema é uma migration explícita, revisável via PR.

Para gerar uma nova migration quando o modelo de dados muda:

```bash
make migration-generate
# Gera: backend/src/migrations/MigrationNNN_YYYYMMDD.ts
```

O nome é gerado automaticamente com sequência + data, facilitando a ordenação e revisão.

**5. Testar a API**

```bash
# Health check
curl http://localhost:3001/
# → {"message":"Codaqui API","version":"0.3.0",...}

# Documentação interativa (Swagger UI)
open http://localhost:3001/docs
```

O Swagger UI está disponível em `/docs` no ambiente de desenvolvimento. Ele lista todos os endpoints, DTOs, schemas de autenticação e permite fazer chamadas diretamente do browser — essencial para onboarding de novos membros.

**Comandos úteis do dia a dia:**

```bash
make logs SERVICE=backend     # acompanha logs do backend em tempo real
make restart SERVICE=backend  # reinicia apenas o backend
make db-shell                 # abre psql direto no container
make backend-lint             # roda o linter e auto-corrije
make backend-test             # executa os testes unitários
```

---

### Bloco 6 — Do x86 para ARM64: Construindo para a Raspberry Pi

> *Slides: diagrama de build multi-arch + o problema do QEMU + fluxo CI→GHCR→Pi*

Este é provavelmente o bloco mais técnico da palestra — e o que mais causou dores de cabeça na Codaqui.

**O problema:**

Seu notebook de desenvolvimento provavelmente roda **x86_64** (Intel ou AMD 64-bit). A Raspberry Pi 4 roda **ARM64** (aarch64). Uma imagem Docker compilada para x86 **não executa nativamente em ARM64**.

Solução ingênua: compilar direto no Pi. Funciona, mas compilar TypeScript + NestJS num Pi de 4 GB leva vários minutos, aquece o hardware e bloqueia o servidor durante o processo.

**A solução: builds multi-arch com Docker buildx e QEMU**

O `buildx` é uma [extensão do Docker](https://github.com/docker/buildx)  que usa o emulador QEMU para simular outras arquiteturas durante o build. [[#^ref-6-1|[6.1]]] Você compila uma imagem ARM64 no seu x86, envia para um registry, e o Pi apenas faz o pull da imagem pronta — sem compilar nada.

```bash
# Habilitar buildx com suporte multi-arch
docker buildx create --use --platform linux/arm64,linux/amd64

# Build e push direto para o GHCR (GitHub Container Registry)
docker buildx build \
  --platform linux/arm64/v8 \
  --file backend/Dockerfile \
  --tag ghcr.io/codaqui/institucional-backend:latest-arm64-v8 \
  --push \
  ./backend
```

**O Dockerfile já é otimizado para produção:**

```dockerfile
# ── Estágio 1: compilar o TypeScript ────────────────────────
FROM node:24-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build          # tsc → dist/

# ── Estágio 2: imagem de produção (mínima e segura) ─────────
FROM node:24-alpine AS runner
RUN apk add --no-cache curl && apk upgrade --no-cache
WORKDIR /app
ENV NODE_ENV=production

# Segurança: arquivos root-owned, read-only (S6504)
COPY --from=builder --chown=root:root --chmod=444 /app/package.json ./
COPY --from=builder --chown=root:root --chmod=444 /app/package-lock.json ./
RUN npm ci --omit=dev      # apenas dependências de produção

COPY --from=builder --chown=root:root --chmod=555 /app/dist ./dist

# Roda como usuário não-root (uid 1000)
USER node
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

Dois benefícios do multi-stage build:
- **Imagem menor**: o compilador TypeScript, as devDependencies e os arquivos `.ts` não vão para produção. Imagem final: ~300 MB vs. ~437 MB com tudo (stage builder com devDeps + fonte TypeScript).
- **Segurança**: `USER node` garante que o processo não tem privilégios de root dentro do container, e os arquivos são somente leitura.

> 📦 **Verificação pública** — versão `0.3.0` no GHCR:
> - `amd64`: 97,8 MB comprimido · `sha256:2f15f5c3f9ce1434666adc626c2f76024ec6565791041b204e552a527ae2433c`
> - `arm64`: 99,0 MB comprimido · `sha256:cd701ac519c1cb36721c8d29139464fbd6486c77145bdf76f32e10ffb0b3f9d7`
> - No disco (Podman / `podman images`): ~300 MB descomprimido

**GitHub Container Registry (GHCR)**

O GHCR é o registry de containers integrado ao GitHub — gratuito para repositórios públicos. A Codaqui usa-o para armazenar as imagens ARM64 geradas no CI:

```
ghcr.io/codaqui/institucional-backend:latest-arm64-v8
```

No `compose.prod.yaml` (que roda no Pi), o backend simplesmente faz pull dessa imagem:

```yaml
services:
  backend-codaqui:
    image: ghcr.io/codaqui/institucional-backend:latest-arm64-v8
    restart: always
    ports:
      - "3002:3000"   # Cloudflare Tunnel aponta para esta porta
    environment:
      - DB_HOST=postgres-codaqui
      - NODE_ENV=production
      - BACKEND_URL=https://api.codaqui.dev
      - FRONTEND_URL=https://codaqui.dev
      # ... demais variáveis do .env de produção
    depends_on:
      postgres-codaqui:
        condition: service_healthy
```

**O fluxo completo (dev → Pi):**

```
Desenvolvedor (x86_64)
    │
    ├── git push → GitHub
    │
    └── buildx build → GHCR (imagem ARM64/v8)
                           │
                           └── Pi faz `podman compose pull` + `up`
```

Esse fluxo pode ser totalmente automatizado com GitHub Actions — um `push` na branch `main` dispara o build, faz push para o GHCR, e o Pi pode ser notificado via webhook para atualizar automaticamente.

---

### Bloco 7 — Expondo a API sem IP Público: Cloudflare Tunnel

> *Slides: diagrama do tunnel — conexão de saída, não de entrada*

> Esta seção é baseada no artigo publicado no blog da Codaqui: [Cloudflare Tunnel: economizando IPv4 ao expor serviços em VMs](https://codaqui.dev/blog/2025/08/22/cloudflare-tunnel-economizando-ipv4-ao-expor-servicos-em-vms) [[#^ref-7-2|[7.2]]]

**O problema:**

Internet residencial tipicamente não oferece IPv4 fixo. Mesmo que ofereça, abrir portas no roteador doméstico cria superfície de ataque. Como expor `api.codaqui.dev` de dentro de casa sem IPv4 público, sem firewall aberto e sem risco desnecessário?

**A inspiração teórica: o modelo Zero Trust**

O Zero Trust é um modelo de segurança cunhado por John Kindervag na Forrester Research em 2010 e popularizado pelo paper *BeyondCorp* do Google (2014). A premissa central: **nenhuma rede deve ser considerada confiável por padrão** — nem a rede interna da organização. Cada acesso deve ser verificado, independentemente de onde o request se originou. [[#^ref-7-3|[7.3]]]

O Cloudflare Tunnel aplica essa filosofia de forma prática: ao invés de abrir portas para o mundo e confiar em quem entra, o Pi *se conecta* à Cloudflare — e apenas tráfego autorizado pela Cloudflare chega até ele.

**Como o Cloudflare Tunnel funciona:**

O túnel inverte completamente o modelo tradicional. Em vez de esperar conexões de entrada (o que exige IP público e porta aberta), o `cloudflared` estabelece **conexões de saída** persistentes para a rede Cloudflare:

```
Internet
    │
    ▼
Cloudflare Edge (POP global)
    │  [conexão TLS de saída — iniciada pelo Pi]
    ▼
cloudflared (daemon no Pi)
    │
    ▼
backend-codaqui:3002
```

Ninguém acessa o Pi diretamente. Todo tráfego passa pelo edge da Cloudflare, que é responsável por TLS, proteção DDoS, rate limiting e roteamento. [[#^ref-7-1|[7.1]]]

Do ponto de vista da rede doméstica: nenhuma porta aberta, nenhum IP público necessário. O Pi é completamente invisível na internet — exceto pelo que você configura explicitamente no ingress do tunnel.

**Instalação na Raspberry Pi (Ubuntu/Debian ARM64):**

```bash
# 1. Baixar o binário ARM64
curl -L -o cloudflared \
  https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/

# 2. Login — abre URL para autenticação no Cloudflare Dashboard
cloudflared tunnel login

# 3. Criar o túnel (gera um UUID único)
cloudflared tunnel create codaqui-api

# 4. Vincular o hostname DNS ao túnel (Cloudflare cria o registro CNAME)
cloudflared tunnel route dns codaqui-api api.codaqui.dev

# 5. Criar arquivo de configuração
sudo mkdir -p /etc/cloudflared
sudo tee /etc/cloudflared/config.yml > /dev/null <<'YAML'
tunnel: <TUNNEL-UUID>
credentials-file: /etc/cloudflared/<TUNNEL-UUID>.json
ingress:
  - hostname: api.codaqui.dev
    service: http://localhost:3002
  - service: http_status:404
YAML

# 6. Instalar como serviço systemd
sudo tee /etc/systemd/system/cloudflared.service > /dev/null <<'UNIT'
[Unit]
Description=Cloudflare Tunnel — api.codaqui.dev
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/cloudflared --config /etc/cloudflared/config.yml run
Restart=on-failure

[Install]
WantedBy=multi-user.target
UNIT

sudo systemctl daemon-reload
sudo systemctl enable --now cloudflared
```

> ⚠️ **Nota sobre `User=root`:** o serviço está configurado com root para simplificar o acesso ao credentials file durante o setup inicial. Para hardening em produção, crie um usuário dedicado (`cloudflared`), ajuste as permissões dos arquivos em `/etc/cloudflared/` e altere `User=cloudflared` no unit file. O `cloudflared` não precisa de acesso ao Docker, ao Podman ou ao socket do Coolify — ele apenas faz conexão TCP para `localhost:3002` (acessível por qualquer usuário local) e conexões de saída para a Cloudflare. Consulte a documentação oficial para o passo a passo de least-privilege.

**Validação:**

```bash
# Status no Pi
sudo systemctl status cloudflared

# De qualquer lugar do mundo
curl -I https://api.codaqui.dev/
# HTTP/2 200 ← sucesso
```

**Cloudflare Access (Zero Trust — bonus gratuito):**

O Cloudflare Access permite adicionar autenticação antes do request chegar ao backend. Para endpoints administrativos (ex: `/admin/*`), você pode exigir login via GitHub ou Google. Gratuito para até 50 usuários no plano básico.

---

### Bloco 8 — Coolify: Uma PaaS Open Source no seu Próprio Hardware

> *Slides: print da interface do Coolify + diagrama "Git push → Coolify → Pi"*

**O problema que o Coolify resolve:**

Rodamos `podman compose` na linha de comando, SSH no Pi, `podman logs`, mais SSH para verificar variáveis... Funciona — mas escala mal conforme o projeto cresce. Cada deploy é uma sequência manual de comandos. Cada debug exige abrir terminal. O Coolify resolve isso sem abrir mão do self-hosting.

**O que é o Coolify:**

Coolify é uma plataforma open-source e auto-hospedável que funciona como alternativa ao Heroku, Netlify e Vercel — mas rodando no seu próprio hardware. A proposta central: **a ergonomia da nuvem com o controle do self-hosting**. [[#^ref-8-1|[8.1]]]

> "Imagine having the ease of a cloud but with your own servers. That is Coolify." — documentação oficial

Suporta qualquer máquina acessível via SSH: VPS, bare metal, Raspberry Pi, notebook velho. A Codaqui usa-o para gerenciar o que roda na Pi sem precisar lembrar cada flag do podman.

> ℹ️ **Coolify e Podman:** o Coolify roda internamente com Docker. Para o desenvolvimento local, a Codaqui incentiva o uso do Podman — compatível sintaticamente com Docker, mas sem daemon root. No Pi (produção), o Coolify gerencia os containers via Docker. Ao clonar o repositório e trabalhar localmente, use `podman compose` conforme documentado no Makefile.

**Instalação (60 segundos):**

```bash
# No servidor/Pi — um único comando
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```

> ⚠️ **Verifique o comando atualizado:** a URL e os flags do script de instalação podem mudar entre versões. Consulte sempre o site oficial antes de executar: [coolify.io/docs/installation](https://coolify.io/docs/installation)

Isso instala o Coolify, cria os containers necessários e expõe uma UI na porta 8000. Depois: adicione o servidor via SSH, conecte o repositório GitHub, e o Coolify assume o ciclo de deploy.

**O que o Coolify gerencia:**

| Funcionalidade | Sem Coolify | Com Coolify |
|---|---|---|
| Deploy de nova versão | SSH + podman pull + compose up | Automático via push no GitHub |
| Variáveis de ambiente | Arquivo `.env` no servidor | Interface web, com histórico |
| Logs em tempo real | `podman logs -f <container>` | Interface web, por serviço |
| Health checks | Cron manual ou ausente | Monitoramento nativo com alertas |
| Rollback | Recriar container manualmente | Um clique na interface |
| SSL/TLS | Configuração manual (nginx/caddy) | Automático via Let's Encrypt |

**Como a Codaqui usa:**

```
GitHub push (main)
    │
    └─→ GitHub Actions: build ARM64 → push ghcr.io
              │
              └─→ Coolify detecta nova imagem
                        │
                        └─→ `podman compose pull` + `up` no Pi
                                  │
                                  └─→ Cloudflare Tunnel expõe api.codaqui.dev
```

O Coolify não substitui o `compose.prod.yaml` — ele *orquestra* a execução dele, adicionando UI, logs e automatização. Os arquivos de configuração continuam no repositório (sem vendor lock-in).

**Filosofia: PaaS open source como categoria**

O Coolify representa uma tendência mais ampla: a repatriação das ferramentas de plataforma para o domínio do software livre. Alternativas proprietárias (Heroku, Render, Railway) cobram pela abstração. O Coolify oferece a mesma abstração sem o custo de lock-in, alinhado ao princípio de que infraestrutura de plataforma também pode ser um bem comum. [[#^ref-8-1|[8.1]]]

---

### Bloco 9 — Segurança, Secrets e Manutenção

> *Slides: checklist de segurança + diagrama de backup*

**1. Containers não-root**

Tanto o frontend quanto o backend rodam como `USER node` (uid 1000). Um eventual escape do container não carrega privilégios de root no host.

**2. Arquivos read-only no container**

O Dockerfile usa `--chmod=444` para configuração e `--chmod=555` para código executável. O processo da aplicação não pode modificar seus próprios arquivos em disco — mitigando uma classe de ataques de persistência.

**3. Secrets: nunca no código, nunca no repositório**

```bash
# Gerar senha do banco
openssl rand -hex 16

# Gerar JWT secret robusto
openssl rand -hex 64
```

O `.env` está no `.gitignore`. O `.env.example` documentado está no repositório. Em CI/CD, os secrets são armazenados como GitHub Secrets e injetados via environment.

**4. Um OAuth App por ambiente — sem exceções**

```
DEV:  callback → http://localhost:3001/auth/github/callback
PROD: callback → https://api.codaqui.dev/auth/github/callback
```

Dois apps separados impedem que credenciais de desenvolvimento funcionem em produção. Cada ambiente tem seu próprio `GITHUB_CLIENT_ID` e `GITHUB_CLIENT_SECRET`.

**5. Fail-fast em produção**

O `main.ts` do NestJS tem uma checagem explícita de variáveis obrigatórias ao iniciar:

```typescript
if (isProd) {
  const required = ['JWT_SECRET', 'GITHUB_CLIENT_ID',
                    'GITHUB_CLIENT_SECRET', 'STRIPE_SECRET_KEY',
                    'STRIPE_WEBHOOK_SECRET'];
  const missing = required.filter((k) => !process.env[k]);
  if (missing.length > 0) {
    logger.error(`Variáveis ausentes: ${missing.join(', ')}`);
    process.exit(1);
  }
}
```

Se subir sem secrets, o processo encerra imediatamente com log claro — ao invés de falhar silenciosamente em runtime.

**6. Backup do PostgreSQL**

O volume de dados (`pgdata-codaqui`) é persistente. Em produção, o **Coolify cuida dos backups automaticamente** — a cada 4 horas, faz um dump do PostgreSQL e envia para um bucket **Amazon S3**.

A configuração é trivial: no painel do Coolify, basta informar as credenciais S3, o bucket de destino e a frequência. Sem cron job manual, sem scripts extras.

> 💡 Usamos o free tier da AWS: 5 GB de S3 gratuito por mês. Nossa base cabe inteira nesse espaço — e sobra. Backups que nunca precisamos usar, mas que dormem tranquilos no S3 esperando o dia em que alguém vai agradecer por eles existirem.

O projeto também inclui `scripts/db-restore-prod.sh` para restaurar dumps de produção localmente.

**7. Atualizações e Dependabot**

- **Dependabot** (GitHub) monitora dependências npm e abre PRs automaticamente
- Imagem base `node:24-alpine` pode ser fixada em digest para builds reproduzíveis
- `cloudflared` deve ser atualizado periodicamente (Cloudflare recomenda versão recente)

---

### Bloco 10 — O Que Aprendemos: Erros, Acertos e Decisões

> *Slide: "lessons learned" com ícones ✅ e ❌*

**Acertos:**

✅ **Makefile como interface única** — qualquer pessoa nova chega, roda `make help` e tem todos os comandos documentados. Zero "mas como eu faço X?".

✅ **Multi-stage Dockerfile** — imagem final de ~300 MB vs. ~437 MB com devDeps e código-fonte TypeScript (verificado: `ghcr.io/codaqui/institucional-backend:0.3.0`, amd64 `sha256:2f15f5c3f9ce1434...`, arm64 `sha256:cd701ac519c1cb36...`).

✅ **Podman sem daemon root** — melhora a postura de segurança sem mudar a experiência do desenvolvedor.

✅ **Cloudflare Tunnel** — elimina completamente a necessidade de IPv4 público, firewall aberto ou VPN.

✅ **Migrations TypeORM versionadas** — cada mudança de schema é um arquivo `.ts` revisável, revertível e com nome automático com sequência + data.

✅ **Swagger automático** — o NestJS gera documentação OpenAPI a partir dos decorators. Novo membro não precisa pedir "me explica os endpoints".

✅ **`.env.example` documentado** — cada variável tem um comentário explicando de onde obter o valor. Reduz drasticamente o tempo de onboarding.

**Erros (e como corrigimos):**

❌ **Não tínhamos `.env.example` no início** → novos contribuidores ficavam perdidos tentando descobrir o que configurar.
→ Criamos `.env.example` com comentários detalhados para cada variável.

❌ **Build ARM64 direto no Pi levava 15+ minutos** → atrasava deploys e aquecia o hardware.
→ Migramos para `docker buildx` no CI; o Pi só faz `pull`.

❌ **`synchronize: true` no TypeORM em dev destruiu dados** durante uma migration mal planejada.
→ `synchronize: false` em todos os ambientes, para sempre. Migrations explícitas apenas.

❌ **JWT secret fraco em um teste público** → descoberto numa revisão de segurança antes de causar dano real.
→ Rotina de geração obrigatória com `openssl rand -hex 64` e checklist de deploy documentado.

---

### Bloco 11 — Conclusão e Chamada para Ação

> *Slide: Raspberry Pi + api.codaqui.dev uptime dashboard*

**Síntese:**

- Self-hosting não é para todo mundo — mas para projetos educacionais e comunitários, o custo-benefício e o aprendizado são extraordinários
- A stack (NestJS + PostgreSQL + Podman + Cloudflare Tunnel) é reproduzível, documentada e inteiramente open source
- O maior desafio não foi técnico — foi cultural: disciplina com secrets, migrations e backups
- Uma Raspberry Pi 4 é perfeitamente capaz de rodar uma API REST com banco de dados para centenas de usuários simultâneos — confira as métricas reais de uso em [codaqui.dev/sobre/insights](https://codaqui.dev/sobre/insights) e os dados abertos em [github.com/codaqui/dados](https://github.com/codaqui/dados)

**Chamada para ação:**

> *"Pegue um Raspberry Pi — ou uma VM num notebook velho — clone o repositório da Codaqui, rode `make setup && make up`, e acesse `localhost:3001/docs`. Em 10 minutos você tem uma API REST completa rodando localmente. Daí para uma Raspberry Pi com Cloudflare Tunnel são mais uns 30 minutos seguindo o passo a passo do blog."*

Todo o código está em: **[github.com/codaqui/institucional](https://github.com/codaqui/institucional)**

Se você hospedar algo usando essa stack — ou encontrar algo para melhorar — **abre uma issue ou faz um PR** 😄

---

## Apresentações

| Data | Evento | Cidade | Link | Slides |
|---|---|---|---|---|
| *(em breve)* | — | — | — | — |

---

## Referências e Bibliografia

> Organizadas por Bloco. O número entre colchetes `[N.M]` identifica cada referência no texto.

### Bloco 2 — O que é Self-Hosting? História e Filosofia

**[2.1]** Amazon Web Services. (2025). *Amazon EC2 On-Demand Pricing*. https://aws.amazon.com/ec2/pricing/on-demand/ — Para histórico de mudanças de preço: https://cloudprice.net/ ^ref-2-1

**[2.2]** Brasil. Lei nº 13.709, de 14 de agosto de 2018. *Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm — European Parliament & Council. (2016). *Regulation (EU) 2016/679 — General Data Protection Regulation (GDPR)*. Official Journal of the EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679 ^ref-2-2

**[2.3]** Mell, P., & Grance, T. (2011). *The NIST Definition of Cloud Computing (SP 800-145)*. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145 ^ref-2-3

### Bloco 3 — A Economia do Self-Hosting

**[3.1]** Hansson, D. H. (2022). *Why we're leaving the cloud*. HEY World. https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0 ^ref-3-1

**[3.2]** Wang, S., Casado, M. (2021). *The Cost of Cloud, a Trillion Dollar Paradox*. Andreessen Horowitz (a16z). https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/ ^ref-3-2

### Bloco 4 — A Stack da Codaqui

**[4.1]** Myśliwiec, K. (2017). *NestJS — A progressive Node.js framework*. https://nestjs.com/ | GitHub: https://github.com/nestjs/nest ^ref-4-1

**[4.2]** Heon, D., & contributors. (2018–2025). *Podman: A daemonless container engine for OCI containers*. Red Hat / containers community. https://podman.io/ | GitHub: https://github.com/containers/podman ^ref-4-2

### Bloco 6 — Do x86 para ARM64

**[6.1]** Docker Inc. (2025). *Docker Buildx — Build multi-platform images*. Docker Documentation. https://docs.docker.com/build/building/multi-platform/ — QEMU Project. (2025). *QEMU — Open source processor emulator and virtualizer*. https://www.qemu.org/ ^ref-6-1

### Bloco 7 — Cloudflare Tunnel

**[7.1]** Cloudflare. (2025). *What is Cloudflare Tunnel?* Cloudflare Developers. https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/ | cloudflare/cloudflared (GitHub): https://github.com/cloudflare/cloudflared ^ref-7-1

**[7.2]** Menezes, E. (2025). *Cloudflare Tunnel: economizando IPv4 ao expor serviços em VMs*. Blog Codaqui. https://codaqui.dev/blog/2025/08/22/cloudflare-tunnel-economizando-ipv4-ao-expor-servicos-em-vms ^ref-7-2

**[7.3]** Ward, B. S., Beyer, B., Lahanas, Y., & Zangrandi, A. (2014). *BeyondCorp: A New Approach to Enterprise Security*. USENIX ;login:. https://research.google/pubs/beyondcorp-a-new-approach-to-enterprise-security/ — Kindervag, J. (2010). *Build Security Into Your Network's DNA: The Zero Trust Network Architecture*. Forrester Research. ^ref-7-3

### Bloco 8 — Coolify

**[8.1]** Bacsai, A. (2023–2025). *Coolify: An open-source & self-hostable Heroku / Netlify / Vercel alternative*. Coollabs.io. https://coolify.io/ | GitHub: https://github.com/coollabsio/coolify ^ref-8-1

### Referências complementares

- Turnbull, J. (2014). *The Docker Book: Containerization is the new virtualization*. → https://dockerbook.com/
- Merkel, D. (2014). Docker: Lightweight Linux Containers for Consistent Development and Deployment. *Linux Journal*, 239. https://www.linuxjournal.com/content/docker-lightweight-linux-containers-consistent-development-and-deployment
- Raspberry Pi Ltd. (2025). *Raspberry Pi 4 Model B specifications*. https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/
- OWASP. *Docker Security Cheat Sheet*. https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html
- Codaqui. *Repositório institucional (open source)*. https://github.com/codaqui/institucional
- NestJS Docs. *Database (TypeORM)*. https://docs.nestjs.com/techniques/database
- TypeORM. *Migrations*. https://typeorm.io/migrations

---

## Leituras Recomendadas

### Para começar (acessíveis, práticos)

- DHH. (2022). *Why we're leaving the cloud* — https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0
- Cloudflare Docs. *Cloudflare Tunnel Quick Start* — https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/
- Coolify Docs. *Installation* — https://coolify.io/docs/installation
- NestJS Docs. *First steps* — https://docs.nestjs.com/first-steps
- Podman Docs. *Basic setup and use of Podman* — https://podman.io/docs

### Para se aprofundar tecnicamente

- Docker Documentation. *Multi-stage builds* — https://docs.docker.com/build/building/multi-stage/
- OWASP. *Docker Security Cheat Sheet* — https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html
- PostgreSQL 18 Release Notes — https://www.postgresql.org/docs/18/release-18.html
- NIST SP 800-145. *The NIST Definition of Cloud Computing* — https://doi.org/10.6028/NIST.SP.800-145

### Para entender o contexto mais amplo

- a16z. *The Cost of Cloud, a Trillion Dollar Paradox* — https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/
- Google BeyondCorp papers — https://research.google/pubs/?category=security-privacy-and-abuse-prevention

### Comunidades e recursos práticos

- https://reddit.com/r/homelab (Reddit) — comunidade de self-hosting e home servers
- https://selfhosted.show — podcast sobre self-hosting
- https://awesome-selfhosted.net — lista curada de software auto-hospedável
- https://codaqui.dev — Associação Codaqui (contribua!)
- https://github.com/codaqui/institucional — código desta stack

---

## Créditos e Reconhecimentos

- **Coolify / Andras Bacsai** — pela plataforma open-source que elimina a complexidade operacional sem abrir mão do controle
- **Equipe Codaqui** — pelo projeto institucional open source que tornou esta palestra possível
- **Cloudflare** — pelo Tunnel gratuito e pela documentação exemplar
- **NestJS Team** — pelo framework e pela documentação de qualidade
- **Raspberry Pi Foundation** — por tornar hardware acessível para educação e projetos comunitários
- **Comunidade open source** — por cada biblioteca, ferramenta e resposta no Stack Overflow que compõe esta stack

