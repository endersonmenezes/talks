---
title: "Engenharia de Dados para Engenharia de Plataformas: Um Modelo de Dados de Referência para Portais Internos de Desenvolvedores"
type: talk
status: active
area: personal
tags:
  - kind/talk
  - area/personal
  - status/active
created: 2026-05-20
updated: 2026-05-26
source:
---

## Resumo

Um modelo de dados de referência para a construção de Portais Internos de Desenvolvedores, organizado em Estrelas de Capacidade, onde cada estrela representa um domínio de capacidade da plataforma. O *Átomo Tecnológico* é o hub central que conecta todas as estrelas.

O modelo se baseia em duas referências principais: [Backstage](https://backstage.io) para a arquitetura de entidades central (Componente, API, Sistema, Domínio, Recurso, Grupo, Usuário, Modelo) e o modelo Blueprint do [Port.io](https://port.io) para o conceito de Blueprints como entidades de dados configuráveis. No entanto, este modelo de dados é independente de ferramentas — ele pode ser implementado no Backstage, Port.io, Cortex, OpsLevel ou qualquer IdP que suporte um modelo de dados configurável.

---
## Bora lá!

### Ato 1 — A Engenharia de Dados e sua história

> *"Como chegamos aqui?"*

A Engenharia de Dados não nasceu com esse nome. Ela surgiu da necessidade de mover dados de um lugar para outro — os primeiros profissionais eram DBA (administradores de banco de dados) e engenheiros de ETL (Extract, Transform, Load). Viviam no mundo dos Data Warehouses relacionais: dados estruturados, schemas rígidos, pipelines frágeis.

Com o Big Data nos anos 2010 (Hadoop, Spark, Kafka), o papel se transformou. Agora o engenheiro de dados precisava lidar com escala, latência, formatos diversos. O Data Lake surgiu como solução — e trouxe novos problemas.

O conceito prometia centralizar dados de qualquer formato (estruturado, semi-estruturado, não-estruturado) em um repositório barato e escalável. Na prática, sem governança, esses lagos viraram **pântanos de dados** (*data swamps*):

- **Sem catálogo**: ninguém documentava o que estava armazenado, qual a origem ou o significado de cada dataset.
- **Sem qualidade**: dados eram ingeridos brutos, sem validação — lixo entrava, lixo saía (*garbage in, garbage out*).
- **Sem rastreabilidade**: não havia como saber de onde o dado veio, quais transformações sofreu ou em quem confiar.
- **Sem dono**: datasets duplicados em múltiplos formatos, sem responsável claro nem política de acesso.
- **Sem ciclo de vida**: dados acumulavam indefinidamente; nada era descontinuado ou arquivado.

O resultado era cruel: analistas gastavam mais tempo procurando e validando dados do que analisando. A confiança caiu. Times voltaram a criar planilhas locais — exatamente o problema que o Data Lake deveria resolver.

> *"A Data Lake is a store that holds raw data as a source for data scientists to explore ways to gain information. It should not be accessed by end-users or used for system integration."*
> — Martin Fowler, [DataLake](https://martinfowler.com/bliki/DataLake.html) *(fev. 2015)*
>
> *Tradução livre: "Um Data Lake é um repositório que armazena dados brutos como fonte para que cientistas de dados explorem formas de extrair informação. Ele não deve ser acessado por usuários finais nem usado para integração entre sistemas."*

> *"Many organizations approach building a data lake as a purely infrastructural effort, assuming 'if we build it, use cases will come.' This often leads to data lakes filled with disparate, undocumented data with unclear ownership — eventually deteriorating into a data swamp."*
> — ThoughtWorks, [The Curse of the Data Lake Monster](https://www.thoughtworks.com/en-gb/insights/blog/data-engineering/curse-data-lake-monster) *(fev. 2019)*
>
> *Tradução livre: "Muitas organizações encaram a construção de um data lake como um esforço puramente infraestrutural, apostando em 'se construirmos, os casos de uso vão aparecer'. Isso frequentemente resulta em lagos cheios de dados díspares, sem documentação e com responsabilidade indefinida — que inevitavelmente se deterioram em um data swamp."*

A evolução continuou com o conceito de **Modern Data Stack**: orquestração com Airflow/dbt, armazenamento em cloud (S3, GCS), processamento com Spark/Flink, catálogos de dados (DataHub, OpenMetadata). O profissional passou de "operador de pipelines" para **arquiteto de fluxos de dados**.

A resposta estrutural ao problema dos data swamps viria depois, com o **Data Mesh** — uma abordagem que distribui a propriedade dos dados por domínio de negócio, tratando dados como produto. *(Zhamak Dehghani, [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html) — Martin Fowler Blog, mai. 2019)*

**Mensagem central:** A Engenharia de Dados é a disciplina de tornar dados confiáveis, acessíveis e úteis — independente de onde estão.

---

### Ato 2 — A Engenharia de Plataformas e sua história

> *"O mesmo problema, em outro domínio."*

A Engenharia de Plataformas tem uma história paralela. Começou com a adoção de DevOps nos anos 2010 — a ideia de que desenvolvimento e operação não deveriam viver em silos. SRE (Site Reliability Engineering) do Google formalizou o conceito de tratar infraestrutura como software.

Mas DevOps gerou um novo problema: cada time criava sua própria infraestrutura, seus próprios pipelines, suas próprias ferramentas. **Duplicação de esforço em escala**.

Um caso concreto: uma grande empresa de serviços financeiros australiana (*"BigCo"*) havia investido pesadamente em cloud e automação — mas mantinha times separados por competência técnica: middleware, midrange, DBA, redes, load balancer, segurança. Resultado: pequenas mudanças de infraestrutura levavam de semanas a meses. *(Martin Fowler, [Building an Infrastructure Platform](https://martinfowler.com/articles/building-infrastructure-platform.html), 9 fev. 2022)*

A resposta da indústria foi Platform Engineering: criar times dedicados que entregam capacidades reutilizáveis como produto interno.

> *"Platform engineering aims to solve many of the challenges that DevOps teams can introduce, such as siloed operations and process bottlenecks."*
> — ThoughtWorks, [Platform Engineering: Help Developers Deliver More Value](https://www.thoughtworks.com/en-br/insights/articles/platform-engineering-help-developers-deliver-more-value-at-a-lower-cost) *(2 ago. 2023)*
>
> *Tradução livre: "A engenharia de plataformas visa resolver muitos dos desafios que os times de DevOps podem introduzir, como operações em silos e gargalos de processo."*

O artefato central dessa disciplina é o **Internal Developer Portal (IDP)**, definido por Martin Fowler como:

> *"A foundation of self-service APIs, tools, services, knowledge and support which are arranged as a compelling internal product. Autonomous delivery teams can make use of the platform to deliver product features at a higher pace, with reduced co-ordination."*
> — Martin Fowler, [Talking About Platforms](https://martinfowler.com/articles/talk-about-platforms.html) *(5 mar. 2018)*
>
> *Tradução livre: "Uma base de APIs, ferramentas, serviços, conhecimento e suporte de autoatendimento, organizados como um produto interno atraente. Times de entrega autônomos podem usar a plataforma para entregar funcionalidades em ritmo mais acelerado, com menos necessidade de coordenação."*

Um alerta importante, porém:

> *"Organizations often conflate 'the platform' with 'the portal.' Tools like Backstage, Port or Cortex are valuable, but without real delivery capabilities behind them, they become empty shells. A platform must be defined by its capabilities, not by its UI."*
> — ThoughtWorks, [The Evolution of Platform Engineering](https://www.thoughtworks.com/en-br/insights/blog/platforms/the-evolution-of-platform-engineering--lessons-from-the-trenches) *(15 set. 2025)*
>
> *Tradução livre: "Organizações frequentemente confundem 'a plataforma' com 'o portal'. Ferramentas como Backstage, Port ou Cortex são valiosas, mas sem capacidades de entrega reais por trás, tornam-se cascas vazias. Uma plataforma deve ser definida por suas capacidades, não por sua interface."*

**Mensagem central:** Platform Engineering é a disciplina de reduzir a carga cognitiva dos times de desenvolvimento, entregando capacidades como produto — não como ferramenta.

---

### Ato 3 — O Modelo Estrela: uma ponte conceitual

> *"Um padrão que você já conhece."*

O Modelo Estrela (Star Schema) vem da Engenharia de Dados — especificamente do mundo de Data Warehousing. Introduzido por **Ralph Kimball na década de 90**, ele foi criado para organizar dados de forma otimizada para consulta e análise:

> *"Os esquemas em estrela armazenam dados, gerenciam o histórico e atualizam os dados com eficiência, reduzindo a duplicação de definições de negócios repetitivas e agregando e filtrando dados em data warehouses em alta velocidade."*
> — Databricks, [O que é um Esquema em Estrela?](https://www.databricks.com/br/blog/what-is-star-schema) *(c. 2024)*

A ideia é simples e poderosa:

> *"No centro do esquema em estrela, está uma única tabela de fatos que contém os fatos do seu negócio (como valores e quantidades de transações). A tabela de fatos se conecta a várias outras tabelas de dimensões como tempo ou produto."*
> — Databricks *(c. 2024)*

- **Tabela Fato** (hub central): contém os eventos, as métricas, o que aconteceu.
- **Tabelas Dimensão** (raios da estrela): enriquecem o fato com contexto — quem, quando, onde, como.

A grande vantagem: **desnormalização orientada a consulta** — menos joins, maior velocidade, mais clareza para o analista. Os dados das dimensões são redundantes por design, porque o objetivo não é normalização perfeita — é velocidade de resposta.

Esse padrão resolve um problema fundamental: **como modelar dados de forma que seja fácil consultar, sem criar dependências rígidas entre domínios**.

A pergunta que fazemos aqui é: **e se aplicarmos esse padrão à Engenharia de Plataformas?**

Mas a resposta mais precisa não é o Modelo Estrela simples — é o **Esquema Galáxia**.
#### Do Modelo Estrela ao Esquema Galáxia

O Modelo Estrela funciona bem para **um único domínio** de capacidade. Mas a Engenharia de Plataformas não tem um domínio — ela tem vários: CI/CD, Segurança, Observabilidade, Controle de Versão, Infraestrutura...

Na Engenharia de Dados, quando múltiplas estrelas compartilham dimensões comuns, o resultado é chamado de **Esquema Galáxia** (também conhecido como *Fact Constellation Schema*):

> *"A Galaxy Schema, also known as a Fact Constellation Schema, uses two or more fact tables that share common dimension tables. This setup allows multiple business processes to be modeled together using shared dimensions such as Time, Product, and Location. This schema is ideal for large, enterprise-scale analytics."*
> — GeeksForGeeks, [Galaxy Schema in Data Warehouse Modeling](https://www.geeksforgeeks.org/gate/galaxy-schema-in-data-warehouse-modeling/) *(20 nov. 2025)*
>
> *Tradução livre: "O Esquema Galáxia utiliza duas ou mais tabelas de fatos que compartilham tabelas de dimensões comuns. Isso permite que múltiplos processos de negócio sejam modelados juntos por meio de dimensões compartilhadas. Esse esquema é ideal para ambientes de analytics em escala empresarial."*

A referência canônica vem de Kimball & Ross:

> *"A fact constellation [...] shares dimension tables between fact tables."*
> — Ralph Kimball & Margy Ross, *The Data Warehouse Toolkit*, 3ª ed. *(2013)*
>
> *Tradução livre: "Uma constelação de fatos [...] compartilha tabelas de dimensões entre as tabelas de fatos."*

Em termos de Engenharia de Plataformas, a analogia é direta:

| Conceito (Data Engineering) | Equivalente (Platform Engineering) |
|---|---|
| Tabela de fato | Uma capacidade do landscape (CI/CD, Security, Observability...) |
| Tabelas de dimensão compartilhadas | Átomo Tecnológico (hub central partilhado por todas as estrelas) |
| Esquema Galáxia | Internal Developer Portal (IDP) |

Cada capacidade do landscape é uma **estrela independente** que orbita o mesmo sol:

- ⭐ **Estrela CI/CD** — fatos: builds, deploys, golden paths
- ⭐ **Estrela Security** — fatos: vulnerabilidades, CVEs, políticas
- ⭐ **Estrela Observability** — fatos: alertas, SLOs, métricas de serviço
- ⭐ **Estrela Version Control** — fatos: commits, PRs, branches, releases
- ⭐ **Estrela Infrastructure** — fatos: recursos de cloud, clusters, custos

Todas orbitam o mesmo **Sol**: o **Átomo Tecnológico**.

```
            ⭐ CI/CD
                |
⭐ Security ────☀ ÁTOMO TECNOLÓGICO ────⭐ Observability
                |
      ⭐ Version Control    ⭐ Infrastructure
```

O Átomo Tecnológico é o **Sol da Galáxia de Plataformas** — a dimensão compartilhada que conecta todas as estrelas de capacidade. É equivalente ao **Software Catalog** do IDP: a entidade central que dá sentido a todas as outras.

Um IDP construído sobre esse modelo não é uma ferramenta — é o **centro gravitacional do landscape tecnológico**.

Em vez de dados de negócio, temos entidades tecnológicas. O hub não é uma "Venda" ou um "Pedido" — é um **Átomo Tecnológico**. As dimensões não são "Cliente" ou "Produto" — são "Repositório GitHub", "Pipeline de CI", "Serviço em Produção", "Vulnerabilidade de Segurança".

---
### Ato 4 — Por que a Engenharia de Dados é fundamental para a Engenharia de Plataformas?

> *"Não fazer de tudo. Consultar a tudo."*

Um dos maiores mal-entendidos sobre Platform Engineering é pensar que a plataforma deve *executar* tudo. Que o time de plataforma deve *possuir* o CI/CD, o monitoramento, o catálogo de serviços, a segurança.

Esse modelo não escala. E não é o modelo correto.

O que a Engenharia de Dados nos ensina é que **a centralização não precisa ser de execução — pode ser de observabilidade**. Um Data Warehouse não executa as transações do dia a dia; ele *consolida e disponibiliza* os dados para consulta.

O IDP deveria funcionar da mesma forma. A Port.io descreve bem o objetivo:

> *"The internal developer portal gives developers a connected map of everything they need to care about — every devops asset, cloud resource, devtool, infrastructure, Kubernetes cluster and the software that runs on it all. A good data model should provide everything that developers need to know so that they can understand the SDLC in context."*
> — Port.io, [What You Need to Know About the Data Model in an Internal Developer Portal](https://www.port.io/blog/what-you-need-to-know-about-the-data-model-in-an-internal-developer-portal) *(18 jun. 2025)*
>
> *Tradução livre: "O portal interno de desenvolvedores oferece um mapa conectado de tudo o que precisam acompanhar — cada ativo de DevOps, recurso de nuvem, ferramenta, infraestrutura, cluster Kubernetes e o software que roda sobre tudo isso. Um bom modelo de dados deve fornecer tudo o que os desenvolvedores precisam saber para entender o SDLC em contexto."*

A ThoughtWorks descreve como a Engineering Platform organiza essas capacidades em "hubs":

> *"The Delivery Infrastructure (DI) hub provides product teams with self-service and automated 'golden paths' that go from development to production with quality and security checks baked in."*
> — ThoughtWorks, [Engineering Platform: Key to Maximizing Software Development Effectiveness](https://www.thoughtworks.com/en-br/insights/blog/platforms/engineering-platform-key-to-maximizing-software-development-effectiveness) *(23 fev. 2023)*
>
> *Tradução livre: "O hub de Delivery Infrastructure (DI) oferece aos times de produto 'caminhos dourados' automatizados e de autoatendimento que vão do desenvolvimento à produção com verificações de qualidade e segurança embutidas."*

| Serviço | Onde executa | Quem consulta |
|---|---|---|
| CI/CD | GitHub Actions / Jenkins | IDP (consulta status) |
| Version Control | GitHub / GitLab | IDP (consulta repositórios) |
| Security | Snyk / Dependabot | IDP (consulta vulnerabilidades) |
| Observability | Datadog / Grafana | IDP (consulta métricas de serviços) |
| Software Catalog | Backstage / Port | IDP (hub central) |

A plataforma não substitui nenhuma dessas ferramentas. Ela **conecta**, **consolida** e **apresenta** — exatamente como um modelo estrela conecta dimensões ao redor de um fato central.

**Mensagem central:** A grande contribuição da Engenharia de Dados para a Engenharia de Plataformas é o paradigma: centralizar a visibilidade, não a execução.

---

### Ato 5 — Platform Engineering: Serviço e Operação

> *"Duas lentes para o mesmo problema."*

Platform Engineering pode ser enxergada por duas dimensões complementares:
#### Dimensão 1 — Serviço (o que você entrega)

O time de plataforma entrega **capacidades** para os times de desenvolvimento. A ThoughtWorks organiza essas capacidades em cinco hubs *(ThoughtWorks, [Engineering Platform: Key to Maximizing Software Development Effectiveness](https://www.thoughtworks.com/en-br/insights/blog/platforms/engineering-platform-key-to-maximizing-software-development-effectiveness), 23 fev. 2023)*:

1. **Delivery Infrastructure Hub** — CI/CD, golden paths, automação de deploy (GitHub Actions, Tekton, Jenkins)
2. **Services Hub** — publicação e descoberta de APIs, SDKs, eventos (Software Catalog: Backstage, Port.io, Cortex)
3. **Knowledge Hub** — documentação, onboarding, guias, padrões de segurança
4. **Automated Governance** — dashboards de DORA metrics, compliance, cloud cost, observability (Datadog, Grafana, OpenTelemetry)
5. **Developer Experience Portal** — ponto único de self-service para os times (IDP)

Cada um desses hubs conecta e agrega ferramentas do landscape:

- **Version Control** → GitHub, GitLab
- **CI/CD** → GitHub Actions, Tekton, Jenkins
- **Security** → Snyk, Dependabot, Trivy
- **Infrastructure** → Terraform, Crossplane, Pulumi
- **Secrets Management** → Vault, AWS Secrets Manager

O IDP é o ponto de convergência — não substitui nenhum deles, mas os conecta.

#### Dimensão 2 — Operação (como você organiza os times)

**Team Topologies** (Matthew Skelton & Manuel Pais) oferece o modelo operacional. A grande sacada central, na visão de Martin Fowler:

> *"The primary benefit of a platform is to reduce the cognitive load on stream-aligned teams."*
> — Martin Fowler, [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) *(set. 2019)*
>
> *Tradução livre: "O principal benefício de uma plataforma é reduzir a carga cognitiva dos times orientados ao fluxo de valor."*

Os quatro tipos de times:

- **Stream-aligned Teams**: times orientados ao fluxo de valor (produto, feature) — *"full-stack e full-lifecycle: responsáveis por front-end, back-end, banco de dados, UX, testes, deploy, monitoramento"*
- **Platform Teams**: times que entregam capacidades reutilizáveis — interagem com os stream-aligned em modo **X-as-a-Service**
- **Enabling Teams**: times que transferem conhecimento e capacidades para outros times — atuam em **Facilitating mode** (coaching, não execução)
- **Complicated Subsystem Teams**: times especializados em domínios complexos que reduzem carga cognitiva dos stream-aligned

> *"Team Topologies is designed explicitly recognizing the influence of Conway's Law. The team organization it encourages takes into account the interplay between human and software organization."*
> — Martin Fowler, [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) *(set. 2019)*
>
> *Tradução livre: "Team Topologies foi concebido reconhecendo explicitamente a influência da Lei de Conway. A organização de times que ele propõe leva em conta a interação entre a organização humana e a organização do software."*

Complementando com o modelo de maturidade da CNCF, a Platform Engineering evolui em 4 níveis *(CNCF, [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/), out. 2023)*:

| Nível | Nome | Característica |
|---|---|---|
| 1 | Provisional | Capacidades construídas por necessidade, sem financiamento central |
| 2 | Operationalized | Time dedicado, tratado como centro de custo |
| 3 | Scalable (as product) | Investimento similar a produto externo, com product management e UX |
| 4 | Optimizing | Ecossistema habilitado, eficiência organizacional amplificada |

O time de Platform Engineering é, por definição, um **Platform Team** no modelo de Team Topologies. Sua missão é reduzir a carga cognitiva dos stream-aligned teams — e o objetivo de maturidade é operar no **Nível 3 (as product)**.

---
### Ato 6 — O Átomo Tecnológico: a grande ideia

> *"Mudando a unidade de propriedade."*

Aqui está a virada de chave central deste talk.

Em qualquer landscape de Platform Engineering, existe uma quantidade enorme de entidades: repositórios, pipelines, serviços, deployments, certificados, policies de segurança, times, usuários...

A Port.io descreve bem o desafio de modelar isso:

> *"A data model is a representation of the layout and architecture of the different components that make up an organization's environment and infrastructure. Its goal is to make it easy to understand the interdependencies in the infrastructure and how the SDLC tech stack comes together."*
> — Port.io, [What You Need to Know About the Data Model in an Internal Developer Portal](https://www.port.io/blog/what-you-need-to-know-about-the-data-model-in-an-internal-developer-portal) *(18 jun. 2025)*
>
> *Tradução livre: "Um modelo de dados é uma representação da estrutura e arquitetura dos diferentes componentes que formam o ambiente e a infraestrutura de uma organização. Seu objetivo é facilitar a compreensão das interdependências na infraestrutura e de como a stack tecnológica do SDLC se une."*

Adora Nwodo vai além e nos dá o alerta central:

> *"Your data model is basically a contract between your teams. When that agreement is crystal clear and well-kept, teams can sprint ahead on their own. But when it gets fuzzy or quietly contradictory, everyone ends up paying a massive coordination tax just to ship the simplest things."*
> — Adora Nwodo, [Your Data Model is Actually a Product](https://www.linkedin.com/pulse/your-data-model-actually-product-adora-nwodo-peedc/) *(s.d.)*
>
> *Tradução livre: "Seu modelo de dados é essencialmente um contrato entre os seus times. Quando esse acordo é cristalino e bem mantido, os times conseguem avançar de forma autônoma. Mas quando ele fica nebuloso ou silenciosamente contraditório, todos acabam pagando um enorme imposto de coordenação só para entregar as coisas mais simples."*

E o risco acumulado ao longo do tempo é real:

> *"A naming convention that felt clever when you had ten engineers completely falls apart when you hit two hundred. A relationship model that worked perfectly for your first big launch becomes an absolute nightmare when your data volume explodes."*
> — Adora Nwodo *(s.d.)*
>
> *Tradução livre: "Uma convenção de nomes que parecia inteligente com dez engenheiros desmorona completamente quando você chega a duzentos. Um modelo de relacionamentos que funcionava perfeitamente no seu primeiro grande lançamento se torna um pesadelo absoluto quando o volume de dados explode."*

A pergunta é: **qual é a unidade mínima que conecta tudo isso?**

Apresentamos o conceito de **Átomo Tecnológico** (*Atomic Tech*):

> O Átomo Tecnológico é a menor unidade identificável de tecnologia que pode ser possuída, rastreada e gerenciada dentro de um landscape de Platform Engineering.

**Exemplo concreto:**

Um `GitHub Repository` existe como objeto no GitHub. Mas no modelo tradicional, o time "possui o repositório". Isso cria um acoplamento entre o time e a *ferramenta*.

No modelo do Átomo Tecnológico:
- O time não é dono do **repositório GitHub** — é dono do **Átomo Tecnológico** que representa aquele software.
- O repositório GitHub é uma **dimensão** do Átomo.
- O pipeline de CI é outra **dimensão** do mesmo Átomo.
- O serviço em produção é outra **dimensão**.
- A vulnerabilidade de segurança encontrada é outra **dimensão**.

```
                    ┌─────────────────────────┐
    GitHub Repo ────┤                         ├──── CI/CD Pipeline
                    │    ÁTOMO TECNOLÓGICO     │
  Security Scan ────┤  (hub do modelo estrela) ├──── Deploy em Produção
                    │                         │
  Team Ownership ───┤                         ├──── Observability
                    └─────────────────────────┘
```

O Backstage, ao modelar o Software Catalog, chama esse conceito de **Component**:

> *"A component is a piece of software, for example a mobile feature, web site, backend service or data pipeline. A component can be tracked in source control, or use some existing open source or commercial software."*
> — Backstage, [System Model](https://backstage.io/docs/features/software-catalog/system-model) *(s.d., documentação viva)*
>
> *Tradução livre: "Um componente é uma peça de software, como uma funcionalidade mobile, um site, um serviço de backend ou um pipeline de dados. Um componente pode ser rastreado em controle de versão, ou usar algum software open source ou comercial existente."*

E organiza o landscape ao redor dele com três entidades core — **Component**, **API**, **Resource** — agrupadas em **Systems** e **Domains**.

A Port.io modela isso como blueprints configuráveis *(Port.io, [Default Components](https://docs.port.io/getting-started/default-components))*:

| Blueprint | O que representa | Equivale a |
|---|---|---|
| **Service** | Código estático — repositório + metadados | Átomo Tecnológico |
| **Environment** | Onde o serviço é implantado (prod, staging, dev) | Dimensão de Contexto |
| **Workload** | Service + Environment (a instância viva) | Dimensão de Execução |
| **Deployment** | Evento de deploy — PR merged to default branch | Dimensão de Rastreabilidade |
| **Team** | Time dono do service | Dimensão de Propriedade |

O conceito do Átomo é mais abstrato do que qualquer implementação de ferramenta — ele é o **modelo conceitual** que transcende Backstage, Port, Cortex ou OpsLevel.

**Por que o Átomo Tecnológico importa?**

1. **Portabilidade**: se o time migrar de GitHub para GitLab, o Átomo continua existindo. Apenas a dimensão "Version Control" muda.
2. **Visibilidade consolidada**: o IDP pode responder "tudo sobre esse software" sem importar em quantas ferramentas ele existe.
3. **Governança clara**: propriedade é sobre o Átomo, não sobre instâncias em ferramentas específicas.
4. **Modelo escalável**: o mesmo padrão funciona para um monolito, 10 microsserviços ou 500.

**O Átomo Tecnológico é o hub do modelo estrela aplicado à Engenharia de Plataformas.**

---
### Conclusão — O modelo que conecta tudo

> *"Engenharia de Dados nos deu o padrão. Engenharia de Plataformas nos deu o contexto. O Átomo Tecnológico é a síntese."*

| Conceito | Origem | Aplicação em Platform Engineering |
|---|---|---|
| Modelo Estrela | Data Warehousing | Átomo Tecnológico como hub central |
| Centralização de visibilidade | Modern Data Stack | IDP como camada de consulta |
| Propriedade de dados | Data Governance | Times possuem Átomos, não ferramentas |
| Pipeline de integração | Data Engineering | Conectores do IDP com o landscape |
| Team Topologies | Platform Engineering | Operação dos times ao redor da plataforma |

O resultado é uma plataforma que **não compete** com as ferramentas existentes — ela as **conecta**. Um IDP construído sobre o Átomo Tecnológico é agnóstico de ferramentas, escalável por design e naturalmente alinhado com os princípios que a Engenharia de Dados já provou no contexto de dados.

### E o futuro? IA precisa de Platform Engineering.

> *"AI amplifies the strengths of high-performing organisations and the dysfunctions of struggling ones. Without a solid foundation, localised productivity gains from AI are quickly lost to downstream chaos."*
> — PlatformEngineering.org, [AI Needs Platform Engineering](https://platformengineering.org/blog/ai-needs-platform-engineering-just-ask-thoughtworks-and-google) *(8 out. 2025)*
>
> *Tradução livre: "A IA amplifica os pontos fortes das organizações de alto desempenho e as disfunções das que enfrentam dificuldades. Sem uma base sólida, os ganhos localizados de produtividade com IA se perdem rapidamente em caos mais adiante."*

> *"When the magic of AI comes in place, it just exposes a lot of those technical debt issues. If your documentation is trapped in PDFs or your security policies are inconsistent, an AI agent won't fix it and it will simply fail more efficiently."*
> — Rickey Zachary, Global Engineering Platforms Lead at Thoughtworks *(in: PlatformEngineering.org, 8 out. 2025)*
>
> *Tradução livre: "Quando a magia da IA entra em cena, ela simplesmente expõe uma quantidade enorme de dívida técnica. Se a sua documentação está presa em PDFs ou suas políticas de segurança são inconsistentes, um agente de IA não vai resolver — ele apenas vai falhar de forma mais eficiente."*

**86% das organizações acreditam que Platform Engineering é essencial para realizar o valor total da IA no negócio.** *(State of AI in Platform Engineering, 2025)*

O Átomo Tecnológico — como Sol do esquema galáxia — é exatamente a estrutura que dá à IA o que ela precisa: **APIs documentadas, dados de contexto centralizados e relações explícitas entre entidades tecnológicas**.

---
## Referências

### ThoughtWorks
- [The Curse of the Data Lake Monster](https://www.thoughtworks.com/en-gb/insights/blog/data-engineering/curse-data-lake-monster) *(fev. 2019)*
- [Engineering Platform: Key to Maximizing Software Development Effectiveness](https://www.thoughtworks.com/en-br/insights/blog/platforms/engineering-platform-key-to-maximizing-software-development-effectiveness) *(23 fev. 2023)*
- [Platform Engineering: Help Developers Deliver More Value at a Lower Cost](https://www.thoughtworks.com/en-br/insights/articles/platform-engineering-help-developers-deliver-more-value-at-a-lower-cost) *(2 ago. 2023)*
- [The Evolution of Platform Engineering: Lessons from the Trenches](https://www.thoughtworks.com/en-br/insights/blog/platforms/the-evolution-of-platform-engineering--lessons-from-the-trenches) *(15 set. 2025)*
- [Enterprise Guide to Platform Thinking (PDF)](https://www.thoughtworks.com/content/dam/thoughtworks/documents/guide/tw_guide_enterprise_guide_to_platform_thinking.pdf) *(PDF binário — não extraível por ferramentas)*
- [How ThoughtWorks Bridges the Platform Engineering Gap — TheNewStack](https://thenewstack.io/how-thoughtworks-bridges-the-platform-engineering-gap/)
### Martin Fowler
- [DataLake](https://martinfowler.com/bliki/DataLake.html) *(fev. 2015)*
- [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html) *(20 mai. 2019)* - [Zhamak Dehghani](https://twitter.com/zhamakd)
- [What I Talk About When I Talk About Platforms](https://martinfowler.com/articles/talk-about-platforms.html) *(5 mar. 2018)* - [Evan Bottcher](https://twitter.com/evanbottcher)
- [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) *(set. 2019)*
- [Building an Infrastructure Platform](https://martinfowler.com/articles/building-infrastructure-platform.html) *(9 fev. 2022)* - [Poppy Rowse](https://poppy-rowse.medium.com/) & [Chris Shepherd](https://thesheps.medium.com/)
### Backstage (Spotify)
- [Software Catalog System Model](https://backstage.io/docs/features/software-catalog/system-model) *(s.d., documentação viva)*
- [Software Templates](https://backstage.io/docs/features/software-templates/)
- [Backend System](https://backstage.io/docs/backend-system/)
- [Frontend System Architecture](https://backstage.io/docs/frontend-system/architecture/generated-index)
### Port.io
- [What You Need to Know About the Data Model in an IDP](https://www.port.io/blog/what-you-need-to-know-about-the-data-model-in-an-internal-developer-portal) *(18 jun. 2025)*
- [Scorecards: Concepts and Structure](https://docs.port.io/scorecards/concepts-and-structure)
- [Default Components](https://docs.port.io/getting-started/default-components)
### Data Engineering & Data Warehousing
- [O que é um Esquema em Estrela? — Databricks](https://www.databricks.com/br/blog/what-is-star-schema) *(c. 2024)*
- [Galaxy Schema in Data Warehouse Modeling — GeeksForGeeks](https://www.geeksforgeeks.org/gate/galaxy-schema-in-data-warehouse-modeling/) *(20 nov. 2025)*
- 📚 Kimball, R. & Ross, M. *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling*, 3ª ed. Wiley, 2013.

### CNCF
- [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) *(out. 2023)*
- [CNCF Landscape](https://landscape.cncf.io/)
### Outros
- [AI Needs Platform Engineering — PlatformEngineering.org](https://platformengineering.org/blog/ai-needs-platform-engineering-just-ask-thoughtworks-and-google) *(8 out. 2025)*
- [Your Data Model is Actually a Product — Adora Nwodo (LinkedIn)](https://www.linkedin.com/pulse/your-data-model-actually-product-adora-nwodo-peedc/) *(s.d.)*