# Gabarito — DebugExample.java

Exemplo **mínimo** só para mostrar a dinâmica da Carreira 02. Na prova real, os erros
estão espalhados num projeto Spring Boot + React, em 3 camadas (compilação, configuração, startup).

Os 5 erros propositais deste arquivo:

| # | Linha | Erro | Correção |
| --- | --- | --- | --- |
| 1 | `private List<String> itens = new ArrayList<>();` | `ArrayList` usado sem import (`java.util.ArrayList`) | Adicionar `import java.util.ArrayList;` |
| 2 | `String[] partes = item.split("R\\$")` | Falta ponto e vírgula no fim da instrução | `...split("R\\$");` |
| 3 | `return soma` | Falta ponto e vírgula | `return soma;` |
| 4 | `int qtd;` + `qtd = qtd + 1;` + `return qtd;` | Variável usada sem inicialização (em **dois** pontos) | `int qtd = 0;` |
| 5 | `carrinho.adicionar("Monitor");` | Chamada com número errado de argumentos (método exige nome + preço) | `carrinho.adicionar("Monitor", 350.0);` |

## O que se observa na correção do aluno

- Ele **compila primeiro** e lê as mensagens do compilador — os 5 erros aparecem na compilação, mas em **rodadas separadas** (sintaxe → semântica → fluxo).
- O erro 4 ("variable might not have been initialized") só surge na última rodada de compilação — nem todo erro aparece de imediato.
- Método sistemático: compilar → ler mensagem → localizar → corrigir → recompilar.

## 🛤️ Jornada de debug (verificada executando `javac` de verdade)

A sequência abaixo foi **confirmada rodando o `javac`** neste arquivo, passada a passada.
Na prova real (Spring + React em Container/Compose), o ciclo é o mesmo, só muda a ferramenta:
`docker compose build` (compilação) → `docker compose up` + `docker compose logs` (configuração e startup)
— ou `podman-compose` no lugar de `docker compose`. Ver [[container-exemplo]].

> 💡 Por que a jornada tem 4 rodadas e não 1: o compilador **revela os erros em camadas** —
> cada rodada só mostra o que a fase atual consegue analisar. Quem tenta corrigir
> "de olho" os 5 erros de uma vez perde exatamente o feedback de cada camada.

### Rodada 1 — primeira compilação

```bash
javac DebugExample.java
```

Na primeira passada **só aparecem os erros de sintaxe** (2 e 3) — erros de parsing
impedem as fases seguintes da compilação:

```
DebugExample.java:24: error: ';' expected
            String[] partes = item.split("R\\$")
                                                ^
DebugExample.java:27: error: ';' expected
        return soma
                   ^
2 errors
```

- **Erros 2 e 3**: mensagem `';' expected` aponta exatamente o caractere onde falta o `;`.
  Correção direta em ambas as linhas.

### Rodada 2 — recompilar e revelar erros de semântica

```bash
javac DebugExample.java
```

Com a sintaxe válida, o compilador avança e revela os erros **1 e 5**:

```
DebugExample.java:8: error: method adicionar in class Carrinho cannot be applied to given types;
        carrinho.adicionar("Monitor");
                ^
  required: String,double
  found:    String
  reason: actual and formal argument lists differ in length
DebugExample.java:15: error: cannot find symbol
    private List<String> itens = new ArrayList<>();
                                     ^
  symbol:   class ArrayList
  location: class Carrinho
2 errors
```

- **Erro 5**: a mensagem diz exatamente o que falta (`required: String, double`) —
  basta olhar a assinatura do método `adicionar(String nome, double preco)`.
- **Erro 1**: o símbolo `ArrayList` não existe no escopo → falta o import.
  Correção no topo do arquivo: `import java.util.ArrayList;`

### Rodada 3 — mais uma camada: análise de fluxo

```bash
javac DebugExample.java
```

Só agora o erro **4** aparece — e em **duas ocorrências** (o uso e o `return`):

```
DebugExample.java:35: error: variable qtd might not have been initialized
                qtd = qtd + 1;
                ^
DebugExample.java:38: error: variable qtd might not have been initialized
        return qtd;
               ^
2 errors
```

- **Erro 4**: "might not have been initialized" → a variável precisa nascer com valor:
  `int qtd = 0;` (uma correção resolve as duas ocorrências).

> 💡 Ensinamento: o compilador **não reporta tudo na primeira vez** — erros de análise
> de fluxo ficam escondidos atrás de erros semânticos, que ficam escondidos atrás de
> erros de sintaxe. O ciclo *compilar → corrigir → recompilar* se repete até zerar.

### Rodada 4 — compila limpo, validar em execução

```bash
javac DebugExample.java && java DebugExample
```

Saída esperada (verificada):

```
Total: 530.0
Qtd Teclado: 1
```

- Se a saída viesse diferente (ex.: `Total: 0.0` ou exceção em `parseDouble`),
  o aluno investigaria a **lógica**, não a sintaxe — é aqui que entram hipótese,
  isolamento e verificação.

### O ciclo completo (válido para as 3 carreiras da prova)

```
executar → ler mensagem de erro → localizar origem → formar hipótese
→ corrigir a menor coisa possível → executar de novo
```
