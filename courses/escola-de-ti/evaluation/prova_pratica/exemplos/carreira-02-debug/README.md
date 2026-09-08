# Exemplo — Carreira 02 (Debugging em camadas)

Arquivos:

| Arquivo | O que é |
| --- | --- |
| `ExemploDebug.java` | 1 arquivo Java com **5 erros propositais** — a camada "compilação" em miniatura |
| `gabarito.md` | Tabela erro→correção + **jornada de debug em 4 rodadas, verificada com `javac` real** (sintaxe → semântica → fluxo → execução) |
| `Dockerfile.exemplo` + `compose-exemplo.yaml` | O mesmo exemplo dentro do ciclo de vida do container — `compose build` falha como a camada 1 falha na prova real |
| `container-exemplo.md` | Como o container é a **interface de inserção de erros** na prova real: camada do erro → comando → sintoma |

O que a prova real adiciona: app Spring Boot + React distribuída em Compose, com erros
nas 3 camadas (compilação, configuração, startup) — ver a Base de Notas em
`../../avaliacao_04_prova_pratica.md`.

> ⚠️ Exemplo de formato: o projeto, os erros e os valores da prova real são diferentes.
