import java.util.List;

public class ExemploDebug {
    public static void main(String[] args) {
        Carrinho carrinho = new Carrinho();
        carrinho.adicionar("Teclado", 120.0);
        carrinho.adicionar("Mouse", 60.0);
        carrinho.adicionar("Monitor");
        System.out.println("Total: " + carrinho.total());
        System.out.println("Qtd Teclado: " + carrinho.quantidade("Teclado"));
    }
}

class Carrinho {
    private List<String> itens = new ArrayList<>();

    public void adicionar(String nome, double preco) {
        itens.add(nome + " - R$" + preco);
    }

    public double total() {
        double soma = 0;
        for (String item : itens) {
            String[] partes = item.split("R\\$")
            soma += Double.parseDouble(partes[1]);
        }
        return soma
    }

    public int quantidade(String nome) {
        int qtd;
        for (String item : itens) {
            if (item.startsWith(nome)) {
                qtd = qtd + 1;
            }
        }
        return qtd;
    }
}
