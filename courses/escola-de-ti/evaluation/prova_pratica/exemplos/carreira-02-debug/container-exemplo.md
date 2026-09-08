# Container + Compose na Carreira 02 — como a dinâmica funciona

Na prova real, a app quebrada (Spring Boot + React) é distribuída como um projeto
Compose. O container é a **interface de inserção de erros**: cada erro proposital
ocupa um ponto do ciclo de vida do container, e o aluno descobre a camada do erro
pelo **comando que falha**.

## Mapeamento: camada do erro → onde ele aparece

| Camada do erro | Comando do aluno | Sintoma |
| --- | --- | --- |
| **Compilação** | `docker compose build` | Build da imagem falha (saída do `javac`/`mvn` no build) |
| **Configuração** | `docker compose up` | Container sai imediatamente com exit code ≠ 0 |
| **Startup/lógica** | `docker compose up` + app | Sobe e cai; causa nos `docker compose logs` |

## Exemplo mínimo (este diretório)

O `Dockerfile.exemplo` compila e roda o `ExemploDebug.java` — o mesmo arquivo com
os 5 erros do exemplo. Como ele **não compila**, o build falha: é a demonstração
da camada 1 (compilação).

```bash
# Docker
docker compose -f compose-exemplo.yaml build
# Podman
podman-compose -f compose-exemplo.yaml build
```

Saída: o erro de compilação aparece no log do build — exatamente como na jornada
do `gabarito.md`, só que dentro do ciclo de build da imagem.

## O ciclo do aluno na prova real

```bash
docker compose up --build      # ou podman-compose
# leu o erro? corrigiu o menor ponto possível? repete:
docker compose up --build
docker compose logs -f app     # para erros de startup/lógica
```

> 💡 Por que container ajuda o professor: a correção roda `docker compose up` no
> repositório do aluno — se subir de ponta a ponta, o ambiente está íntegro.
> Sem "na minha máquina funcionou" nem diferença de JDK/Node entre alunos.

## Na prova real (Spring + React), o compose tem 2 serviços

```yaml
# modelo conceitual — não é o arquivo do exemplo
services:
  backend:   # build falha = erros de compilação; logs = erros de startup
    build: ./backend
    ports: ["8080:8080"]
    environment:
      - SPRING_DATASOURCE_URL=jdbc:postgresql://db:5432/app  # config errada = camada 2
  frontend:  # build ok, tela branca = rota/CORS = camada 3
    build: ./frontend
    ports: ["3000:3000"]
    depends_on: [backend]
```
