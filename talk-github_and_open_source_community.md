---
title: "GitHub e Comunidade Open Source"
type: talk
status: active
area: personal
tags:
  - kind/talk
  - area/personal
  - status/active
created: 2026-03-23
updated: 2026-03-25
source:
---
## Resumo

Open Source não é apenas uma licença de software — é um modelo de produção coletiva, estudado por economistas, sociólogos e cientistas da computação, que está redefinindo como o mundo cria, compartilha e sustenta tecnologia. Esta palestra conecta a base acadêmica do movimento a práticas concretas de contribuição no GitHub. Este arquivo está otimizado para sua leitura via Obsidian. Se você deseja conhecer um pouco mais do Obsidean, acesse [obsidian.md](https://obsidian.md/).

> [!NOTE] Sobre este documento
> Este arquivo nasceu de **notas pessoais e pesquisas acumuladas ao longo de muito tempo**, com o auxílio de IA como parceira na organização, estruturação e expansão do conteúdo. Tentei revisar tudo com atenção — mas se algo passou batido, **me faz um PR** 😄

Apresentação de Slides: [Google Slides](https://docs.google.com/presentation/d/1fWq87ske2XvC9e4X6el5weC81XxcqRmj/edit?usp=sharing&ouid=105231768257065375837&rtpof=true&sd=true) - Está disponível para comentários também.

## Público-alvo

Desenvolvedores iniciantes e intermediários, estudantes de computação e tecnologia, profissionais curiosos sobre comunidades de software. Nenhum pré-requisito técnico avançado necessário.

## Objetivo

O ouvinte deve sair entendendo **por que** o Open Source funciona (teoria), **o que** o GitHub representa nesse ecossistema (dados), e **como** dar os primeiros passos concretos na contribuição (prática).

## Duração estimada

60 min (45 min de conteúdo + 10–15 min de Q&A) 

---
## Roteiro Detalhado

### Bloco 1 — Abertura (5 min)

> *Slide: título + pergunta provocadora*

**Pergunta para o público:** "Quantos de vocês usaram software open source hoje?"

Resposta: todos. Android, Linux, Python, Node.js, VSCode, Firefox, o kernel que roda nos servidores que entregam o conteúdo de vocês — tudo open source.

> *Citação de abertura:*
> "Vale a pena, no entanto, dedicar algumas páginas a explicar por que, e sob quais condições, a produção colaborativa baseada em bens comuns, e a produção social de forma mais geral, não são apenas sustentáveis, mas também formas eficientes de organizar a produção de informação." — **Yochai Benkler**, *The Wealth of Networks* (2006) [[#^ref-1-1|[1.1]]]

---
### Bloco 2 — O que é Open Source? História e Filosofia (8 min)

> *Slides: linha do tempo + definições*

**1983/1985 — GNU Project e Manifesto (Richard Stallman)**

Em **27 de setembro de 1983**, Stallman anuncia o GNU Project via Usenet. Em **março de 1985**, publica o *GNU Manifesto* na *Dr. Dobb's Journal*. Por meio do GNU Project e da Free Software Foundation (FSF, fundada em 1985), Stallman formaliza as quatro liberdades fundamentais do software livre — numeradas de 0 a 3: [[#^ref-2-1|[2.1]]]

0. Liberdade de executar o programa para qualquer propósito
1. Liberdade de estudar e modificar o código-fonte
2. Liberdade de redistribuir cópias
3. Liberdade de distribuir versões modificadas

**1991 — Linux**

Linus Torvalds anuncia o Linux em uma lista de e-mail com a famosa frase: *"I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu)"*.

![Imagem do E-mail](https://preview.redd.it/linux-has-a-interested-history-this-is-one-of-early-emails-v0-e79xc1ewkwr61.png?auto=webp&s=034e3acd6302f758e393c637030fde3e8e4ddc68)

> *Imagem via:* https://www.reddit.com/r/linux/comments/mmmlh3/linux_has_a_interested_history_this_is_one_of/

**1998 — O termo "Open Source"**

Christine Peterson cunha o termo *Open Source* em fevereiro de 1998 em Palo Alto, Califórnia, logo após o anúncio da liberação do código-fonte do Netscape. A sessão estratégica surgiu da percepção de que a atenção em torno do anúncio do Netscape havia criado uma oportunidade para educar e defender a superioridade de um processo de desenvolvimento aberto.

Os participantes da conferência acreditavam que os fundamentos pragmáticos e de negócios que motivaram a Netscape a liberar seu código ilustravam uma maneira valiosa de interagir com potenciais usuários e desenvolvedores de software, e convencê-los a criar e aprimorar o código-fonte participando de uma comunidade engajada. Os participantes também acreditavam que seria útil ter um rótulo único que identificasse essa abordagem e a diferenciasse do rótulo filosófico e politicamente focado "software livre". O brainstorming para esse novo rótulo finalmente convergiu para o termo "código aberto", originalmente sugerido por Christine Peterson.

Dois dos presentes na reunião de Palo Alto (Eric Raymond e Michael Tiemann) mais tarde se tornariam presidentes da OSI, e outros participantes (incluindo Todd Andersen, Jon "maddog" Hall, Larry Augustin e Sam Ockman) se tornaram importantes apoiadores iniciais da organização.

A Open Source Initiative (OSI) é co-fundada dias depois por **Eric S. Raymond e Bruce Perens**. A troca terminológica visava eliminar a ambiguidade de "free" (gratuito × livre) e tornar o conceito mais acessível a novos públicos, inclusive o mundo corporativo.

A adoção do termo foi rápida, com apoio inicial de figuras da comunidade, como Linus Torvalds, e da Cúpula de Software Livre de abril de 1998, que contou com a presença de muitas personalidades importantes, incluindo os fundadores do sendmail, Perl, Python, Apache e representantes da IETF e do Consórcio de Software da Internet.

Em 7 de abril de 1998, Tim O'Reilly realizou uma reunião com os principais líderes da área. Anunciada previamente como a primeira "Freeware Summit", em 14 de abril já era conhecida como a primeira "Open Source Summit". [[#^ref-2-2|[2.2]]]

> *Fonte:* Peterson, C. (2018). "How I coined the term 'open source'". *Opensource.com*. [[#^ref-2-2|[2.2]]]

**Definição formal (OSI):**
Software é Open Source quando sua licença garante acesso ao código-fonte, permite modificação e redistribuição. Hoje, a OSI aprova mais de 100 licenças (MIT, Apache 2.0, GPL, LGPL, Mozilla, etc.).

> *Dado:* 96% dos codebases comerciais auditados contêm componentes open source (Synopsys OSSRA Report, 2024). O relatório analisa codebases durante processos de fusões e aquisições — um recorte representativo do software empresarial em produção. [[#^ref-2-3|[2.3]]]

---

### Bloco 3 — A Catedral e o Bazar: dois modelos de desenvolvimento (7 min)

> *Slides: analogia visual catedral vs. mercado*

**Eric S. Raymond, "The Cathedral and the Bazaar" (1997/1999)**

Imaginem uma catedral gótica: construída por um pequeno grupo de mestres artesãos, a portas fechadas, revelada ao mundo somente quando considerada "pronta". Agora imaginem um bazar persa — barulhento, aparentemente caótico, com dezenas de pessoas contribuindo, testando e corrigindo em público o tempo todo.

Raymond usou essa metáfora para descrever dois modelos completamente distintos de desenvolvimento de software — e argumentou que o segundo, contra toda intuição, produz software *melhor*. O ensaio, apresentado originalmente em 1997 na Linux Kongress, se tornou o manifesto cultural do movimento Open Source:

| **A Catedral** | **O Bazar** |
|---|---|
| Código liberado apenas em releases | Código disponível o tempo todo |
| Desenvolvimento fechado, controlado | Desenvolvimento aberto, caótico |
| Ex.: primeiros softwares proprietários | Ex.: Linux, Mozilla |

A tese central de Raymond: *"Given enough eyeballs, all bugs are shallow"* — batizada de **Lei de Linus**. [[#^ref-3-1|[3.1]]]

**Implicação:** o modelo distribuído não é apenas mais democrático, é mais eficiente para certos tipos de problemas (software com muitos contribuidores potenciais).

> *Referência acadêmica:* Raymond, E. S. (1999). *The Cathedral and the Bazaar*. O'Reilly Media. ISBN 978-0596001087. [[#^ref-3-1|[3.1]]]

---
### Bloco 4 — A Ciência da Contribuição: Por que as pessoas contribuem? (8 min)

> *Slides: gráfico de motivações + tipos de contribuidores*

Aqui chegamos no coração acadêmico desta palestra — e, pra mim, a parte mais fascinante. Pesquisadores se perguntaram: por que alguém cederia seu tempo e expertise gratuitamente? A resposta vai surpreender vocês.

**Lakhani & Wolf (2005) — O estudo mais citado sobre motivação em OSS**
Pesquisa com 684 desenvolvedores open source em 287 projetos. Resultado: [[#^ref-4-1|[4.1]]]

| Motivação | % dos contribuidores |
|---|---|
| Prazer intelectual / desafio criativo | **41,8%** (motivação mais citada) |
| Melhora de habilidades próprias | 33,8% |
| Necessidade de usar o software | 31,8% |
| Senso de obrigação com a comunidade | 28,6% |
| Reputação profissional | 17,3% |
| Remuneração direta | 14,5% |

> *"The most important motivation factor for open source developers is intellectual stimulation."*
> — Lakhani & Wolf, 2005, p. 12 [[#^ref-4-1|[4.1]]]

**Conclusão:** A maioria dos contribuidores é movida por motivações **intrínsecas** (prazer, aprendizado, identidade) mais do que extrínsecas (dinheiro, emprego). Isso tem implicações profundas para como projetos devem tratar sua comunidade.

**von Krogh, Spaeth & Lakhani (2003)**
Estudo sobre como novos contribuidores entram em projetos OSS. Identificaram o processo de *"joining script"* — uma sequência de tarefas menores e progressivamente complexas que integra novos membros. Projetos saudáveis têm onboarding estruturado, mesmo que informal. [[#^ref-4-2|[4.2]]]

---
### Bloco 5 — Peer Production e Bens Comuns Digitais (8 min)

> *Slides: triângulo de formas de produção + Ostrom*

**Yochai Benkler e a "Commons-based Peer Production" (2002)**

O professor de Direito de Harvard propôs que o open source representa uma **terceira forma de produção**, distinta do mercado (preços) e da hierarquia (ordens):

> *"In this paper I explain why we are beginning to see the emergence of a new, third mode of production, in the digitally networked environment, a mode I call commons-based peer production."*
> — Benkler, Y. (2002). Coase's Penguin, or, Linux and The Nature of the Firm. [[#^ref-5-1|[5.1]]]

O nome vem de Ronald Coase (Prêmio Nobel de Economia, 1991): Coase explicou por que firmas existem (reduzem custos de transação). Benkler inverte a pergunta — por que o Linux, feito fora de firmas, é tão bem-sucedido?

**Resposta:** para tarefas modulares e granulares (partes pequenas e independentes), coordenação descentralizada é mais eficiente do que hierarquia ou mercado.

**Elinor Ostrom e os Comuns (1990)**

Mas antes de falar de Ostrom, precisamos entender o que ela veio derrubar.

**A "Tragédia dos Comuns" de Garrett Hardin (1968)**
Em um artigo célebre na revista *Science*, Hardin descreveu um dilema clássico: imagine um pasto compartilhado por vários fazendeiros. Cada um, agindo racionalmente em interesse próprio, tem incentivo para adicionar mais um boi — porque o ganho é individual, mas o custo (a degradação do pasto) é distribuído entre todos. Repetido por todos os fazendeiros, o resultado é a destruição inevitável do recurso. Conclusão de Hardin: bens comuns estão *condenados ao fracasso* — a saída seria privatização ou controle estatal.

**Por que isso importa pra gente?**
Se Hardin estivesse certo, o Linux deveria ter implodido em anos. Por que alguém contribuiria com código que qualquer empresa pode usar de graça, sem retribuição?

Ostrom (Nobel de Ciências Econômicas, 2009 — compartilhado com Oliver Williamson) foi quem **derrubou empiricamente** essa tese. Ela estudou centenas de casos reais de comunidades que gerenciam bens comuns com sucesso — sem privatização, sem Estado. Demonstrou que a tragédia não é inevitável: comunidades são capazes de se auto-governar de forma sustentável — uma terceira via completamente ignorada por Hardin.

Seus **8 princípios de governança de comuns** se aplicam perfeitamente a projetos OSS: [[#^ref-5-2|[5.2]]]
1. Limites claros (quem é membro da comunidade)
2. Regras adaptadas ao contexto local
3. Participação nas decisões coletivas
4. Monitoramento
5. Sanções graduadas
6. Mecanismos de resolução de conflitos
7. Reconhecimento do direito de auto-organização
8. Organizações aninhadas (para projetos grandes)

---
### Bloco 6 — A Economia do Open Source (8 min)

> *Slides: gráficos de valor econômico + modelo de negócios*

**Lerner & Tirole (2002) — O paper econômico seminal**
Dois economistas de peso — Josh Lerner (Harvard) e Jean Tirole (Nobel 2014) — resolveram analisar o Open Source com as ferramentas da teoria dos jogos e da economia da informação. A pergunta deles era basicamente: *isso faz algum sentido econômico?*

Conclusão principal: desenvolvedores investem em OSS porque sinalizam qualidade ao mercado de trabalho. Contribuir é um **mecanismo de reputação** — código público funciona como portfólio verificável. [[#^ref-6-1|[6.1]]]

> *"The open source movement has been a puzzle for economists. How is it possible for programmers to voluntarily provide a public good?"*
> — Lerner & Tirole, 2002 [[#^ref-6-1|[6.1]]]

**Hoffmann, Nagle & Zhou (2024) — O valor do Open Source**
Pesquisa de Harvard quantificou o valor do open source pela primeira vez em escala: [[#^ref-6-2|[6.2]]]
- O custo para recriar apenas as dependências de código aberto usadas em produção seria de **$8,8 trilhões de dólares**
- O custo de criação pelo lado da oferta (o que custaria pagar para produzir esse código) é de apenas **~$4,15 bilhões** — uma alavancagem superior a **2.000× em relação ao valor gerado**
- Aproximadamente 5% dos desenvolvedores geram ~96% do valor do lado da demanda (concentração extrema, consistente com distribuição de Pareto)

**Modelos de negócio em OSS (Fitzgerald, 2006 — OSS 2.0)**
Brian Fitzgerald documentou a transição do OSS "puramente voluntário" para o "OSS comercial" (OSS 2.0): [[#^ref-6-3|[6.3]]]

| Modelo | Exemplos |
|---|---|
| Dual licensing | MySQL, Qt |
| SaaS sobre OSS | Red Hat, Elastic |
| Open core | GitLab, HashiCorp |
| Serviços e suporte | Canonical, IBM |
| Financiamento de fundações | Apache, Linux Foundation |

---

### Bloco 7 — GitHub como Plataforma Social de Desenvolvimento (7 min)

> *Slides: dados do Octoverse + modelo pull request*

**Dabbish et al. (2012) — Social Coding in GitHub**
Pesquisadores de Carnegie Mellon foram os primeiros a estudar GitHub como fenômeno social. Descobriram que a transparência radical do GitHub (histórico público, forks visíveis, stars, follows) cria sinais sociais que influenciam decisões técnicas: [[#^ref-7-1|[7.1]]]

- Desenvolvedores **seguem** outros para descobrir projetos interessantes
- **Stars** funcionam como curadoria coletiva de qualidade
- **Forks** revelam o gráfico de interesse e especialização da comunidade

> *"GitHub creates a transparent record of developer activity that serves both as a portfolio and a social network."*
> — Dabbish et al., CSCW 2012 [[#^ref-7-1|[7.1]]]

**O modelo Pull Request (Gousios et al., 2014)**
Pesquisa analisando dados de **291 projetos no GitHub** sobre o modelo pull-based de desenvolvimento. Achados: [[#^ref-7-2|[7.2]]]
- PRs pequenos têm maior taxa de aceitação
- Histórico de contribuições anteriores aumenta significativamente a confiança dos maintainers
- Comunicação no PR é parte do trabalho — não overhead

**GitHub em Números (Octoverse 2025):** [[#^ref-7-3|[7.3]]]
- **180 milhões+** de desenvolvedores na plataforma
- **630 milhões** de repositórios totais
- **43,2 milhões** de pull requests mergeados por mês (+23% YoY)
- **~986 milhões** de commits em 2025 (+25,1% YoY — "nearly 1 billion")
- **63%** dos repositórios são públicos ou open source
- **+1 novo desenvolvedor** a cada segundo (em média)
- LATAM: ~6 novos desenvolvedores por minuto

---

### Bloco 8 — Open Source na Indústria Hoje (5 min)

> *Slides: logos de empresas + modelo InnerSource*

**Open Source como estratégia corporativa:**
- **Linux Foundation** hospeda projetos cujos contribuidores recebem salário de Google, Intel, Microsoft, IBM, Meta...
- **OpenSSF (Open Source Security Foundation)** — financiamento coletivo de segurança em OSS
- **CNCF (Cloud Native Computing Foundation)** — Kubernetes, Prometheus, Helm, Argo, e mais de 170 projetos. A CNCF não é só infraestrutura — é uma das comunidades open source mais ativas do mundo, com **CNCF Community Groups** locais espalhados pelo planeta. E tem novidade aqui do Paraná: o **CNCF Community Group de Maringá** está sendo criado agora, e a gente está organizando o evento de lançamento! → [acompanhe o processo](https://github.com/cncf/communitygroups/issues/599)
- Microsoft comprou o GitHub em 2018 por $7,5 bilhões — sinal do valor estratégico

**InnerSource (Stol & Fitzgerald, 2015)**
Aplicação dos princípios do Open Source dentro de organizações privadas: [[#^ref-8-1|[8.1]]]
- Transparência interna de código
- Pull requests entre equipes
- Documentação como cidadã de primeira classe
- Reconhecimento de contribuição

**Desafio atual — Sustentabilidade:**

Em dezembro de 2021, o mundo da tecnologia levou um susto. Uma vulnerabilidade crítica foi descoberta no **Apache Log4j** — uma biblioteca Java de logging usada em literalmente bilhões de dispositivos: servidores da Apple, Amazon, Cloudflare, sistemas industriais, até servidores de Minecraft. A falha, batizada de **Log4Shell** (CVE-2021-44228), permitia execução remota de código — o pior tipo de vulnerabilidade possível. [[#^ref-8-2|[8.2]]]

A pergunta que o mundo fez foi: *quem mantinha essa biblioteca crítica?* A resposta foi constrangedora — um punhado de voluntários, sem remuneração, em seu tempo livre.

Mas não foi só isso. Em março de 2025, um ataque de cadeia de suprimentos comprometeu a **GitHub Action `tj-actions/changed-files`** — usada em dezenas de milhares de repositórios. O atacante modificou a action para vazar segredos de CI (tokens, credenciais de produção) de qualquer repositório que a executasse. Mais uma vez: uma peça de infraestrutura crítica mantida por voluntários, sem modelo de financiamento sustentável. [[#^ref-8-3|[8.3]]]

Esses casos expõem a mesma vulnerabilidade sistêmica: **infraestrutura crítica global sendo mantida por voluntários sobrecarregados**. A comunidade debate como resolver isso com iniciativas como **Open Collective**, **GitHub Sponsors**, **Tidelift** e o **Sovereign Tech Fund** (governo alemão) — mas ainda estamos longe de uma solução estrutural.

---

### Bloco 9 — GitHub para Não-Programadores (15 min)

> *Slides: mosaico de perfis não-técnicos no GitHub + título provocador: "Você não precisa saber programar para contribuir"*

Este bloco expande a ideia central do Bloco 9 anterior: contribuição não é sinônimo de código. O GitHub se tornou uma plataforma de colaboração que transcende o desenvolvimento de software. Aqui, mostramos exemplos concretos de como pessoas de diversas áreas usam o GitHub e participam do ecossistema open source.

---

#### 9.1 — Quem mais está no GitHub? (5 min)

> *Slides: uma categoria por slide, com screenshot do repositório e dados*

**Escritores e documentação técnica**

O livro *Pro Git*, referência mundial sobre Git, é escrito e mantido inteiramente no GitHub por Scott Chacon e Ben Straub. O repositório [`progit/progit2`](https://github.com/progit/progit2) aceita contribuições de qualquer pessoa — correções, traduções, melhorias de texto. A segunda edição foi traduzida para mais de 50 idiomas, quase inteiramente por voluntários.

Outros exemplos notáveis:
- [`github/opensource.guide`](https://github.com/github/opensource.guide) — o guia oficial do GitHub sobre como participar de open source, escrito colaborativamente em Markdown
- [`EbookFoundation/free-programming-books`](https://github.com/EbookFoundation/free-programming-books) — um dos repositórios mais estrelados do GitHub (aproximadamente 350 mil stars em 2025), é essencialmente uma **lista curada de livros gratuitos** mantida por centenas de contribuidores não-programadores

**Cientistas e pesquisadores**

O GitHub se tornou infraestrutura de pesquisa. [[#^ref-9-1|[9.1]]] Exemplos:
- **Jupyter Notebooks públicos** — milhões de notebooks `.ipynb` estão hospedados no GitHub, tornando pesquisas reproduzíveis. O GitHub renderiza notebooks Jupyter diretamente no navegador desde 2015
- **Papers With Code** ([paperswithcode.com](https://paperswithcode.com)) — plataforma que vincula artigos acadêmicos aos seus repositórios de código no GitHub, promovendo reprodutibilidade
- **COVID-19**: durante a pandemia, repositórios como [`CSSEGISandData/COVID-19`](https://github.com/CSSEGISandData/COVID-19) (Johns Hopkins University) se tornaram fontes primárias de dados globais, com contribuições de pesquisadores de dezenas de países
- **CERN** mantém repositórios públicos no GitHub para análise de dados de física de partículas

**Designers**

Projetos de design open source prosperam no GitHub:
- [`feathericons/feather`](https://github.com/feathericons/feather) — coleção de ícones open source com mais de 25 mil stars, onde contribuições são majoritariamente visuais (SVGs)
- [`FortAwesome/Font-Awesome`](https://github.com/FortAwesome/Font-Awesome) — a biblioteca de ícones mais popular da web (~74 mil stars), com contribuições da comunidade incluindo sugestões de novos ícones e ajustes visuais
- [`google/material-design-icons`](https://github.com/google/material-design-icons) — ícones do Material Design do Google, open source
- [`simple-icons/simple-icons`](https://github.com/simple-icons/simple-icons) — ícones de marcas em SVG, mantidos quase inteiramente por contribuidores voluntários que criam e refinam os ícones

**Educadores**

O GitHub é amplamente usado como plataforma de ensino:
- [`freeCodeCamp/freeCodeCamp`](https://github.com/freeCodeCamp/freeCodeCamp) — plataforma gratuita de ensino de programação e um dos repositórios mais estrelados do GitHub (aproximadamente 410 mil stars). A organização se descreve como *"a friendly community where you can learn to code for free"*
- [`TheOdinProject/curriculum`](https://github.com/TheOdinProject/curriculum) — currículo completo de desenvolvimento web mantido pela comunidade
- [`ossu/computer-science`](https://github.com/ossu/computer-science) — currículo de Ciência da Computação autodidata baseado em cursos abertos, com mais de 170 mil stars
- **GitHub Classroom** — ferramenta oficial do GitHub para educadores distribuírem e corrigirem exercícios via repositórios

**Jornalistas e Data Journalism**

O jornalismo de dados adotou o GitHub como ferramenta de transparência e reprodutibilidade:
- [`fivethirtyeight/data`](https://github.com/fivethirtyeight/data) — a equipe do FiveThirtyEight (famosa pelas projeções eleitorais de Nate Silver) publicou os dados e código por trás de suas matérias
- **The Pudding** ([pudding.cool](https://pudding.cool)) — publicação de jornalismo visual que disponibiliza seus dados e código no GitHub
- **ProPublica** ([github.com/propublica](https://github.com/propublica)) — organização de jornalismo investigativo sem fins lucrativos com dezenas de repositórios públicos contendo dados e ferramentas
- **The Guardian** e **The New York Times** também mantêm repositórios públicos com ferramentas e dados de suas apurações

**Governo e políticas públicas**

Governos de vários países usam o GitHub como ferramenta de transparência e colaboração:
- 🇬🇧 **Reino Unido**: o Government Digital Service (GDS) mantém a organização [`alphagov`](https://github.com/alphagov) no GitHub com mais de 1.000 repositórios, incluindo o código do portal GOV.UK. O Reino Unido é referência mundial em governo digital aberto
- 🇺🇸 **Estados Unidos**: a agência 18F ([`github.com/18F`](https://github.com/18F)) publica código e padrões de design do governo americano. O portal [code.gov](https://code.gov) cataloga software open source do governo federal
- 🇫🇷 **França**: o governo francês mantém a organização [`etalab`](https://github.com/etalab) com projetos de dados abertos e serviços públicos digitais
- 🇧🇷 **Brasil**: diversas iniciativas — detalhadas na seção 9.4 deste bloco
- A **Open Government Partnership** (OGP), fundada em 2011, conta com mais de 75 países comprometidos com transparência, incluindo o Brasil como membro fundador

> *Dado:* Segundo o GitHub Octoverse (2023), repositórios de organizações governamentais cresceram significativamente, refletindo uma tendência global de "governo como plataforma" (*government as a platform*). [ver 9.5]

**Comunidades de tradução**

A tradução de documentação técnica é uma das formas mais acessíveis de contribuição:
- **Documentação do Python** — o projeto de tradução para português brasileiro é mantido no GitHub ([`python/python-docs-pt-br`](https://github.com/python/python-docs-pt-br)), coordenado por voluntários da comunidade Python Brasil.
- **Mozilla L10n** (Localization) — a Mozilla mantém um dos maiores projetos de localização do mundo, com comunidades ativas em dezenas de idiomas. O portal [Pontoon](https://pontoon.mozilla.org/) é a ferramenta principal para tradutores contribuírem
- **Kubernetes**, **React**, **Vue.js** e dezenas de outros projetos mantêm repositórios específicos para tradução de documentação

---

#### 9.2 — Hacktoberfest para Não-Programadores (3 min)

> *Slides: logo Hacktoberfest + timeline + tipos de contribuição*

**O que é o Hacktoberfest?**

O Hacktoberfest é o maior evento anual de incentivo à contribuição open source do mundo. Criado pela **DigitalOcean em 2013**, em parceria com o GitHub, o evento acontece todo mês de **outubro** e convida pessoas a fazerem pull requests em repositórios open source em troca de reconhecimento e brindes. [[#^ref-9-2|[9.2]]]

**Breve histórico:**

| Ano | Marco |
|-----|-------|
| **2013** | Primeira edição, organizada pela DigitalOcean. Participação modesta |
| **2014–2019** | Crescimento exponencial. Camiseta exclusiva anual como incentivo. Em 2019, o evento relatou centenas de milhares de pull requests abertos |
| **2020** | **Crise do spam**: a facilidade de ganhar a camiseta gerou uma onda de PRs triviais e spam em repositórios (ex: adicionar espaços em branco). A DigitalOcean introduziu o modelo **opt-in** — apenas repositórios com o tópico `hacktoberfest` aceitam contribuições válidas. Foi um ponto de inflexão importante |
| **2021–2022** | Regras mais rígidas. Introdução da opção de **plantar uma árvore** como alternativa à camiseta |
| **2023–2025** | Transição para **recompensas digitais** como padrão. Foco crescente em **contribuições não-técnicas**: documentação, design, tradução, triagem de issues |

**Tipos de contribuições aceitas (atualmente):**
- ✏️ Documentação e tutoriais
- 🎨 Design e ícones
- 🌐 Tradução e localização
- 🧪 Testes e reprodução de bugs
- 🏷️ Triagem e organização de issues
- 📋 Revisão de pull requests

**Mecânica básica:**
1. Registre-se em [hacktoberfest.com](https://hacktoberfest.com) durante outubro
2. Faça 4 pull requests em repositórios participantes (marcados com o tópico `hacktoberfest`)
3. PRs devem ser aceitos/mergeados ou marcados como `hacktoberfest-accepted`
4. Receba a recompensa digital (ou plante uma árvore)

**Comunidade brasileira no Hacktoberfest:**
- A comunidade brasileira é uma das mais ativas da América Latina no Hacktoberfest
- Grupos como **DevParaná**, **PHP com Rapadura**, **He4rt Developers** e **Training Center** historicamente organizam eventos satélite e listas de projetos brasileiros que aceitam contribuições

---

#### 9.3 — Comunidades Open Source Internacionais que Incluem Não-Programadores (3 min)

> *Slides: logo de cada comunidade + uma frase sobre como participar sem programar*

O ecossistema open source vai muito além de código. Estas comunidades internacionais são referência em inclusão de contribuidores não-técnicos:

**Mozilla**
Mais do que o Firefox, a Mozilla é uma das comunidades open source mais diversas do mundo:
- **Tradução** — via [Pontoon](https://pontoon.mozilla.org/), voluntários traduzem Firefox, Thunderbird e outros produtos para mais de 100 idiomas
- **Advocacy** — campanhas de privacidade e internet aberta (ex: *Internet Health Report*)
- **Documentação** — o [MDN Web Docs](https://developer.mozilla.org/) é mantido com contribuições da comunidade e é a referência global para documentação web
- A Mozilla Foundation é uma organização sem fins lucrativos fundada em 2003

**Wikipedia e Wikimedia**
- A **Wikipedia** é o maior projeto de escrita colaborativa da história — com mais de 60 milhões de artigos em 300+ idiomas (Wikimedia Foundation, 2024)
- O **Wikidata** ([wikidata.org](https://www.wikidata.org/)) é um banco de dados estruturado e aberto que alimenta Wikipedia, Google Knowledge Graph e outros serviços. Qualquer pessoa pode editar
- A comunidade Wikimedia é um exemplo canônico de *peer production* como descrito por Benkler [ver 5.1]

**OpenStreetMap (OSM)**
- O "Wikipedia dos mapas" — projeto de mapeamento colaborativo global com mais de 10 milhões de usuários registrados
- Contribuidores mapeiam estradas, prédios, pontos de interesse — **nenhum conhecimento de programação necessário**
- Usado extensivamente em resposta a desastres naturais via a **Humanitarian OpenStreetMap Team (HOT)**
- No Brasil, comunidades ativas mapeiam cidades que o Google Maps não cobre adequadamente

> *Site:* https://www.openstreetmap.org

**Creative Commons**
- Fundada em 2001 por Lawrence Lessig, a Creative Commons criou o sistema de licenças mais usado para conteúdo aberto (textos, imagens, música, vídeos)
- As licenças CC são usadas por Wikipedia, Flickr, MIT OpenCourseWare, e milhões de criadores
- Contribuir com a CC envolve advocacy, tradução de licenças para contextos legais locais e educação sobre direitos autorais

**The Turing Way**
- Projeto do [Alan Turing Institute](https://www.turing.ac.uk/) (Reino Unido) — um guia aberto e colaborativo sobre ciência de dados reproduzível, ética e colaboração [[#^ref-9-3|[9.3]]]
- Repositório: [`the-turing-way/the-turing-way`](https://github.com/the-turing-way/the-turing-way)
- Destacado pela comunidade **extremamente inclusiva**: contribuições incluem escrita, ilustrações, tradução, e até revisão de linguagem inclusiva
- Realiza *Book Dashes* — sprints presenciais e remotos onde pessoas de qualquer background contribuem
- É frequentemente citado como modelo de governança comunitária saudável em projetos open source

**CHAOSS (Community Health Analytics in Open Source Software)**
- Projeto da Linux Foundation que desenvolve **métricas para avaliar a saúde de comunidades open source** [[#^ref-9-4|[9.4]]]
- Site: [chaoss.community](https://chaoss.community/)
- Contribuições incluem definir métricas, escrever documentação, participar de grupos de trabalho — trabalho essencialmente não-técnico
- As métricas CHAOSS são usadas por projetos como Kubernetes, GNOME e Mozilla para avaliar diversidade, inclusão e sustentabilidade de suas comunidades

---

#### 9.4 — Comunidades Open Source no Brasil (4 min)

> *Slides: mapa do Brasil com pins das comunidades + dados do Octoverse*

**Brasil no GitHub — Panorama**

O Brasil é consistentemente uma das maiores comunidades de desenvolvedores no GitHub. Segundo o **GitHub Octoverse 2025**, o Brasil ocupava a **3ª posição** no ranking de países com mais desenvolvedores na plataforma, atrás apenas de Estados Unidos, Índia e China. No Octoverse 2024 o Brasil aparece entre a 4ª e 5ª posição. [[#^ref-9-5|[9.5]]]

![Imagem com Projeção para 2030](https://github.blog/wp-content/uploads/2025/10/octoverse-2025-projecting-the-top-developer-populations-2030.png?w=768)

**Comunidades de diversidade e inclusão:**

- **PyLadies Brasil** ([pyladies.com.br](http://brasil.pyladies.com/)) — comunidade internacional com capítulos ativos em dezenas de cidades brasileiras, focada em incluir mulheres e pessoas não-binárias na comunidade Python. Organizam workshops, meetups e contribuem para tradução da documentação Python
- **Django Girls Brasil** — workshops gratuitos de introdução à programação com Django para mulheres, baseados no tutorial aberto do [djangogirls.org](https://djangogirls.org/). O material do tutorial é mantido no GitHub e traduzido por voluntárias
- **Reprograma** ([reprograma.com.br](https://reprograma.com.br/)) — programa de formação em tecnologia exclusivo para mulheres em situação de vulnerabilidade social. Fundada em 2016, é uma das iniciativas mais reconhecidas de inclusão em tech no Brasil

**Comunidades de software livre:**

- **GNOME Brasil** e **KDE Brasil** — comunidades brasileiras dos dois maiores ambientes desktop Linux. Contribuem com tradução, documentação, testes e divulgação. A comunidade GNOME Brasil é ativa na tradução do GNOME para português brasileiro há mais de duas décadas

**Dados abertos e transparência:**

- **Open Knowledge Brasil (OKBR)** ([ok.org.br](https://ok.org.br/)) — capítulo brasileiro da Open Knowledge Foundation. Promove dados abertos, transparência e participação cidadã. Mantém o **Índice de Dados Abertos** e diversas ferramentas para monitoramento de políticas públicas

- **Operação Serenata de Amor** — um dos projetos de tecnologia cívica mais emblemáticos do Brasil. Criado em 2016 e financiado via crowdfunding (Catarse), o projeto usou inteligência artificial para auditar gastos de parlamentares brasileiros, especificamente a **CEAP** (Cota para o Exercício da Atividade Parlamentar)
  - O sistema **Rosie** é um robô que analisa reembolsos de deputados e identifica gastos suspeitos
  - O **Jarbas** ([jarbas.serenata.ai](https://jarbas.serenata.ai/)) é a interface web que permite qualquer cidadão consultar os gastos analisados [PENDENTE: verificar disponibilidade em 2026]
  - Repositório: [`okfn-brasil/serenata-de-amor`](https://github.com/okfn-brasil/serenata-de-amor)
  - O projeto é um exemplo poderoso de como **open source + dados abertos + comunidade = accountability**

> *Citação do projeto:*
> "A Operação Serenata de Amor é um projeto aberto que usa ciência de dados para fiscalizar gastos públicos e compartilha tudo: código, dados e metodologia."
> — Descrição do projeto no GitHub

**Governo aberto e dados públicos:**

- **dados.gov.br** — portal central de dados abertos do governo federal brasileiro, parte do compromisso do Brasil com a Open Government Partnership (OGP). Disponibiliza milhares de datasets de órgãos federais
- **Portal da Transparência** ([portaldatransparencia.gov.br](https://portaldatransparencia.gov.br/)) — mantido pela CGU (Controladoria-Geral da União), permite consulta a gastos, receitas, convênios e servidores públicos federais
- **Brasil.io** ([brasil.io](https://brasil.io/)) — projeto independente mantido por Álvaro Justen (Turicas) e colaboradores que disponibiliza dados públicos brasileiros em formatos acessíveis. Ganhou grande visibilidade durante a pandemia de COVID-19 ao compilar dados de casos e óbitos por município quando o governo federal tentou alterar a metodologia de divulgação

---

#### 9.5 — Codaqui & DevParaná: Open Source que Transforma Vidas (5 min)

> *Slides: logo da Codaqui + timeline visual + lista de projetos*

Você está aqui hoje por causa do **DevParaná** — uma comunidade que conecta desenvolvedores por todo o estado. Mas talvez você ainda não saiba que o DevParaná é uma das comunidades sob o guarda-chuva de algo maior: a **Codaqui**. [[#^ref-9-6|[9.6]]] Em outras palavras, ao participar deste evento, você já faz parte dessa história. E a história merece ser contada.

**O que é a Codaqui**

A **Codaqui.dev** é uma escola de programação **sem fins lucrativos** que apoia jovens que desejam aprender tecnologia mas não têm acesso por outros meios. Seus pilares são **inclusão, diversidade e aprendizado contínuo** — valores que ressoam diretamente com os princípios de *commons-based peer production* que vimos ao longo desta palestra.

A Codaqui é uma associação formalizada como ONG (CNPJ: **44.593.429/0001-05**), com suporte jurídico e pedagógico desde sua fundação. A organização pratica **transparência radical**: suas finanças estão no [Open Collective](https://opencollective.com/codaqui) e as atas de reuniões no [Google Drive público](https://drive.google.com/drive/folders/1-5VqXGS_UaRTdrRJLbawT8FUSpKxaKSU). Esse modelo de governança transparente é exatamente o que Ostrom descreveu como essencial para a sustentabilidade de bens comuns [ver 5.2] — regras claras, monitoramento pela própria comunidade e prestação de contas acessível a todos.

O [Código de Conduta](https://www.codaqui.dev/conduta/) da Codaqui reforça um ambiente livre de assédio para todos, independente de gênero, idade, orientação sexual, deficiência, aparência, etnia, religião ou experiência técnica. É um modelo do que uma comunidade saudável precisa para crescer — **cidadania aberta, inclusão e respeito**.

**De Kids Academy à ONG: uma linha do tempo**

| Ano | Marco |
|------|-------|
| 2020 | Hackathon em Campo Mourão — o fundador atua como mentor e conhece a "Kids Academy" |
| 2021 | Primeiro encontro no Discord (19/02); renomeada para **Codaqui**; formalização como ONG (CNPJ); primeiros voluntários; 12 alunos, 8 bolsas, 3 computadores doados, 1 trilha completa (Python) |
| 2022 | Parcerias com **Google Education** e **GitHub Education**; novos voluntários; 32 membros no Discord |
| 2023 | Doação de computadores para escola no RJ; lançamento do Projeto Mentoria; financiamento coletivo e transparência mensal |
| 2024 | Modalidade **híbrida** (presencial no CPM): 25 encontros no 1º sem., 16 no 2º; 31 mentorias; **501 membros no Discord**, +14 mil visualizações/mês |
| 2025 | **95 mentorias**, 66h, 45 alunos; **692 Discord**, 463 WhatsApp, +7 mil visualizações/mês |

**Projetos abertos para você contribuir agora**

| Projeto | Descrição | GitHub |
|---------|-----------|--------|
| Boletim Diário de Segurança | Bot que publica notícias de segurança todo dia às 10h | [codaqui/boletim-diario-seguranca](https://github.com/codaqui/boletim-diario-seguranca) |
| Laboratório de Data Analytics | Aprenda Data Analytics com Python | [codaqui/dados](https://github.com/codaqui/dados) |
| Secret Sharing | Gerador/compartilhador de senhas via PiPing Server | [codaqui/secret-sharing](https://github.com/codaqui/secret-sharing) |
| GitHub Action FreeDiskSpace | Limpa espaço em disco de Runners SaaS do GitHub | [endersonmenezes/free-disk-space](https://github.com/endersonmenezes/free-disk-space) |
| GitHub Action CODEOWNERS Super Power | Aumenta o poder do CODEOWNERS no GitHub | [endersonmenezes/codeowners-superpowers](https://github.com/endersonmenezes/codeowners-superpowers) |
| Laboratório de Terraform | Estude Terraform dentro da Codaqui | [codaqui/terraform-organization](https://github.com/codaqui/terraform-organization) |
| Tutor | App para explorar Python e conceitos de Dev | [codaqui/tutor](https://github.com/codaqui/tutor) |
| Copilot Dashboard | Painel de analytics de uso do GitHub Copilot | [codaqui/copilot-dashboard](https://github.com/codaqui/copilot-dashboard) |
| Backstage Lab | Explore o Backstage (plataforma OSS do Spotify) | [codaqui/backstage](https://github.com/codaqui/backstage) |

O processo para contribuir é simples:

1. **Escolha** um projeto da tabela acima
2. **Abra uma issue** no repositório descrevendo o que você quer fazer
3. **Aguarde aprovação** da equipe — e comece a contribuir!

**Como entrar na comunidade**

Junte-se à Codaqui pelo **Discord** ou **WhatsApp** através de [codaqui.dev/bio](https://codaqui.dev/bio). Para parcerias institucionais, o contato é **contato@codaqui.dev**. E para conhecer tudo sobre a ONG, acesse [codaqui.dev](https://www.codaqui.dev/).

---

> **Nota sobre duração:** Este bloco (9.1–9.5) tem aproximadamente ~20 minutos de conteúdo. Para encaixá-lo na palestra de 45 minutos, considere reduzir os Blocos 3 e 5 (que são mais acadêmicos) para 4–5 minutos cada, ou selecionar apenas 2 das 4 sub-seções para apresentação ao vivo, mantendo as demais como material de apoio.

---

### Bloco 10 — Como Começar a Contribuir (5 min)

> *Slides: fluxo visual de contribuição*

**Desmistificando a barreira de entrada:**
Contribuição ≠ apenas código. Segundo a pesquisa de contribuidores da GitHub (2023), as contribuições mais necessárias são frequentemente:
- Documentação e tradução
- Triagem de issues
- Revisão de código
- Testes e reprodução de bugs
- Design e UX
- Respostas no fórum/discussões

**Guia prático em 5 passos:**

1. **Use o software** — contribuições surgem de necessidades reais
2. **Leia CONTRIBUTING.md** — cada projeto tem suas regras
3. **Comece pequeno** — busque labels `good first issue` ou `help wanted`
4. **Comunique antes de codar** — abra uma issue antes de mandar PR
5. **Seja consistente** — confiança se constrói com histórico

**Dicas extras para baixar a barreira:**

- **Use o editor web do GitHub** — para correções pequenas (typos, links quebrados, melhorias de texto), você pode editar qualquer arquivo diretamente no navegador clicando no ícone de lápis ✏️. O GitHub cria o fork e o PR automaticamente — zero configuração local necessária
- **Participe das Discussions** — muitos projetos usam a aba *Discussions* do GitHub como fórum. Responder perguntas de outros usuários, relatar sua experiência ou sugerir melhorias já é contribuição valiosa — e te torna conhecido pelos maintainers antes do primeiro PR
- **Exemplo concreto:** encontrou um erro de digitação na documentação do React, do Python ou de qualquer projeto que você usa? Abra o arquivo no GitHub, clique em "Edit this file", corrija o typo, e submeta o PR. Sua primeira contribuição open source pode levar menos de 5 minutos

**Recursos:**
- https://firstcontributions.github.io
- https://goodfirstissue.dev
- https://up-for-grabs.net

---

### Bloco 11 — Conclusão e Chamada para Ação (3 min)

> *Slide: resumo + chamada*

**Síntese:**
- Open Source não é caridade — é um modelo economicamente racional estudado por múltiplos Prêmios Nobel (Coase, Tirole, Ostrom)
- A motivação principal dos contribuidores é **intrínseca**: prazer intelectual e aprendizado
- GitHub transformou OSS em uma plataforma social com efeitos de rede poderosos
- Contribuir é uma habilidade — e começa com passos pequenos

**Chamada para ação:**
> *"Escolha um projeto que você usa. Abra o repositório no GitHub. Leia o CONTRIBUTING.md. Encontre uma issue com 'good first issue'. Você não precisa saber tudo — você só precisa começar."*

> E se vocês encontrarem algo errado nesta palestra — me façam um PR 😄

---

## Apresentações

| Data | Evento | Cidade | Link | Slides |
|------|--------|--------|------|--------|
| 2026-03-25 | DevParaná na Estrada 2026 | Umuarama / PR | [[2026-03-25_devparana_na_estrada_umuarama]] | — |
| 2026-03-26 | DevParaná na Estrada 2026 | Cianorte / PR | [[2026-03-26_devparana_na_estrada_cianorte]] | — |

---

## Referências e Bibliografia

> Organizadas por Bloco (seção da palestra). O número entre colchetes `[N.M]` identifica cada referência no texto.

### Bloco 1 — Abertura

**[1.1]** Benkler, Y. (2006). *The Wealth of Networks: How Social Production Transforms Markets and Freedom*. Yale University Press. → [Versão online gratuita](http://www.benkler.org/Benkler_Wealth_Of_Networks.pdf) | [Site oficial](https://www.benkler.org/) ^ref-1-1

### Bloco 2 — O que é Open Source? História e Filosofia

**[2.1]** Stallman, R. (1983). *Anúncio do GNU Project* (via Usenet, 27 set. 1983). https://www.gnu.org/gnu/initial-announcement.html — Stallman, R. (1985). *The GNU Manifesto*. *Dr. Dobb's Journal*. https://www.gnu.org/gnu/manifesto.html — Free Software Foundation. *The Free Software Definition*. https://www.gnu.org/philosophy/free-sw.pt-br.html | [GNU History](https://www.gnu.org/gnu/gnu-history.pt-br.html) ^ref-2-1

**[2.2]** Peterson, C. (2018). How I coined the term "open source". *Opensource.com*. https://opensource.com/article/18/2/coining-term-open-source-software — O'Reilly, T. (1998). Freeware Summit / Open Source Summit announcement. https://www.oreilly.com/pub/pr/796 ^ref-2-2

**[2.3]** Synopsys. (2024). *Open Source Security and Risk Analysis (OSSRA) Report*. https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html ^ref-2-3

### Bloco 3 — A Catedral e o Bazar

**[3.1]** Raymond, E. S. (1999). *The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary*. O'Reilly Media. ISBN 978-0596001087. → [Versão online gratuita](http://www.catb.org/~esr/writings/cathedral-bazaar/) ^ref-3-1

### Bloco 4 — A Ciência da Contribuição

**[4.1]** Lakhani, K. R., & Wolf, R. G. (2005). Why Hackers Do What They Do: Understanding Motivation and Effort in Free/Open Source Software Projects. In J. Feller, B. Fitzgerald, S. Hissam, & K. R. Lakhani (Eds.), *Perspectives on Free and Open Source Software* (pp. 3–22). MIT Press. → ISBN: 9780262562270 | [MIT Press](https://mitpress.mit.edu/9780262562270/perspectives-on-free-and-open-source-software/) ^ref-4-1

**[4.2]** von Krogh, G., Spaeth, S., & Lakhani, K. R. (2003). Community, joining, and specialization in open source software innovation. *Research Policy*, 32(7), 1217–1241. https://doi.org/10.1016/S0048-7333(03)00050-7 ^ref-4-2

### Bloco 5 — Peer Production e Bens Comuns Digitais

**[5.1]** Benkler, Y. (2002). Coase's Penguin, or, Linux and The Nature of the Firm. *Yale Law Journal*, 112(3), 369–446. https://doi.org/10.2307/1562247 → [PDF](https://www.benkler.org/CoasesPenguin.PDF) ^ref-5-1

**[5.2]** Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press. [Prêmio Nobel de Economia, 2009] → [Internet Archive](https://archive.org/details/governingcommons0000ostr) | [Nobel Lecture (PDF)](https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf) ^ref-5-2

### Bloco 6 — A Economia do Open Source

**[6.1]** Lerner, J., & Tirole, J. (2002). Some Simple Economics of Open Source. *Journal of Industrial Economics*, 50(2), 197–234. https://doi.org/10.1111/1467-6451.00174 → [NBER Working Paper](https://www.nber.org/papers/w7600) ^ref-6-1

**[6.2]** Hoffmann, M., Nagle, F., & Zhou, Y. (2024). The Value of Open Source Software. *Harvard Business School Working Paper* 24-038. https://www.hbs.edu/faculty/Pages/item.aspx?num=65230 ^ref-6-2

**[6.3]** Fitzgerald, B. (2006). The Transformation of Open Source Software. *MIS Quarterly*, 30(3), 587–598. https://doi.org/10.2307/25148740 → [PDF livre (autor)](https://www.brian-fitzgerald.com/wp-content/uploads/2013/10/BF-MISQ-OSS-paper.pdf) ^ref-6-3

### Bloco 7 — GitHub como Plataforma Social de Desenvolvimento

**[7.1]** Dabbish, L., Stuart, C., Tsay, J., & Herbsleb, J. (2012). Social coding in GitHub: Transparency and collaboration in an open software repository. *Proceedings of CSCW 2012*, 1277–1286. https://doi.org/10.1145/2145204.2145396 ^ref-7-1

**[7.2]** Gousios, G., Pinzger, M., & van Deursen, A. (2014). An exploratory study of the pull-based software development model. *Proceedings of ICSE 2014*, 345–355. https://doi.org/10.1145/2568225.2568260 → [PDF livre (autor)](https://gousios.org/pub/exploration-pullreqs.pdf) ^ref-7-2

**[7.3]** GitHub. (2025). *Octoverse 2025: A new developer joins GitHub every second*. https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1 ^ref-7-3

### Bloco 8 — Open Source na Indústria Hoje

**[8.1]** Stol, K. J., & Fitzgerald, B. (2015). Inner Source—Adopting Open Source Development Practices in Organizations: A Tutorial. *IEEE Software*, 32(4), 60–67. https://ieeexplore.ieee.org/document/6809709 | [InnerSource Commons](https://innersourcecommons.org/) ^ref-8-1

**[8.2]** Apache Software Foundation. (2021). *Apache Log4j Security Vulnerabilities — CVE-2021-44228 (Log4Shell)*. https://logging.apache.org/log4j/2.x/security.html — CISA. (2021). *Alert AA21-356A: Mitigating Log4Shell and Other Log4j-Related Vulnerabilities*. https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-356a ^ref-8-2

**[8.3]** Wiz Research. (2025). *tj-actions/changed-files GitHub Action supply chain attack*. https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack — StepSecurity. (2025). *Harden Runner Detection: tj-actions/changed-files Action Is Compromised*. https://www.stepsecurity.io/blog/harden-runner-detection-tj-actions-changed-files-action-is-compromised ^ref-8-3

### Bloco 9 — GitHub para Não-Programadores

**[9.1]** Perkel, J. M. (2016). Democratic databases: science on GitHub. *Nature*, 538, 127–128. https://doi.org/10.1038/538127a ^ref-9-1

**[9.2]** DigitalOcean. Hacktoberfest. https://hacktoberfest.com ^ref-9-2

**[9.3]** The Turing Way Community. (2022). *The Turing Way: A handbook for reproducible, ethical and collaborative research*. Zenodo. https://doi.org/10.5281/zenodo.3233853 ^ref-9-3

**[9.4]** CHAOSS Project. Community Health Analytics in Open Source Software. Linux Foundation. https://chaoss.community/ ^ref-9-4

**[9.5]** GitHub. (2023). *Octoverse 2023*. https://github.blog/news-insights/octoverse/ ^ref-9-5

**[9.6]** Codaqui. *Associação Codaqui* (CNPJ: 44.593.429/0001-05). https://www.codaqui.dev/ → [ONG](https://www.codaqui.dev/ong/) | [Projetos](https://www.codaqui.dev/projetos/) | [Timeline](https://www.codaqui.dev/timeline/) | [Código de Conduta](https://www.codaqui.dev/conduta/) | [Transparência](https://opencollective.com/codaqui) ^ref-9-6

### Referências Complementares

> Obras citadas na versão anterior da bibliografia que complementam os temas abordados, mas não são referenciadas diretamente no corpo da palestra.

- Lakhani, K. R., & von Hippel, E. (2003). How open source software works: "free" user-to-user assistance. *Research Policy*, 32(6), 923–943. https://doi.org/10.1016/S0048-7333(02)00095-1
- von Hippel, E., & von Krogh, G. (2003). Open Source Software and the "Private-Collective" Innovation Model: Issues for Organization Science. *Organization Science*, 14(2), 209–223. https://doi.org/10.1287/orsc.14.2.209.14992
- Chesbrough, H. (2003). *Open Innovation: The New Imperative for Creating and Profiting from Technology*. Harvard Business School Press. → [Internet Archive](https://archive.org/details/openinnovationne0000ches)
- Weber, S. (2004). *The Success of Open Source*. Harvard University Press. → [Internet Archive](https://archive.org/details/successofopensou0000webe)
- West, J., & Gallagher, S. (2006). Challenges of open innovation: the paradox of firm investment in open source software. *R&D Management*, 36(3), 319–331. https://doi.org/10.1111/j.1467-9310.2006.00436.x
- Tsay, J., Dabbish, L., & Herbsleb, J. (2014). Influence of social and technical factors for evaluating contribution in GitHub. *Proceedings of ICSE 2014*, 356–366. https://dl.acm.org/doi/10.1145/2568225.2568315
- Coelho, J., & Valente, M. T. (2017). Why modern open source projects fail. *Proceedings of FSE 2017*, 186–196. https://doi.org/10.1145/3106237.3106246 → [PDF livre (autor)](https://homepages.dcc.ufmg.br/~mtov/pub/2017-fse.pdf)
- Open Knowledge Brasil. https://ok.org.br/
- Operação Serenata de Amor. https://github.com/okfn-brasil/serenata-de-amor
- Linux Foundation. *The State of Open Source Report*. https://www.linuxfoundation.org/research

---

## Leituras Recomendadas

> Para quem quer se aprofundar após a palestra.

### Para começar (acessíveis, não acadêmicos)
- Raymond, E. S. (1999). *The Cathedral and the Bazaar* — [leitura gratuita online](http://www.catb.org/~esr/writings/cathedral-bazaar/)
- Benkler, Y. (2006). *The Wealth of Networks* — [leitura gratuita online](http://www.benkler.org/Benkler_Wealth_Of_Networks.pdf)

### Para se aprofundar academicamente
- Feller, J., Fitzgerald, B., Hissam, S., & Lakhani, K. R. (Eds.). (2005). *Perspectives on Free and Open Source Software*. MIT Press. - [leitura gratuita online acervo da https://www.math.unipd.it/](https://www.math.unipd.it/~bellio/Perspectives%20on%20Free%20and%20Open%20Source%20Software.pdf)
- Weber, S. (2004). *The Success of Open Source*. Harvard University Press. - [acesso registro a universidade ou compra](https://www.jstor.org/stable/j.ctv26071g2)
- Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press. - [leitura gratuita online](https://www.actu-environnement.com/media/pdf/ostrom_1990.pdf)

### Comunidades e recursos práticos
- https://firstcontributions.github.io — guia interativo para primeiro PR
- https://goodfirstissue.dev — agregador de issues para iniciantes
- https://up-for-grabs.net — projetos que buscam contribuidores
- https://opensource.guide — guia oficial do GitHub para OSS
- https://hacktoberfest.com — evento anual de contribuição open source (outubro)
- https://chaoss.community — métricas de saúde de comunidades OSS
- https://the-turing-way.netlify.app — guia de ciência reproduzível e colaboração aberta
- https://ok.org.br — Open Knowledge Brasil (dados abertos e transparência)

---

## Créditos e Reconhecimentos

- **Eric S. Raymond** — pela sistematização do modelo Bazar
- **Yochai Benkler** — pela teoria da peer production que enquadra o movimento
- **Elinor Ostrom** — pelos princípios de governança de comuns que explicam a resiliência das comunidades OSS
- **Karim Lakhani** — pela pesquisa empírica sobre motivação de contribuidores
- **DevParaná** — pelo espaço e pela comunidade que torna essas conversas possíveis
- **Codaqui** — por ser um exemplo vivo de como o open source pode transformar vidas e comunidades
