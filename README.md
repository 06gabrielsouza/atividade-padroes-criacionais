# Atividade: Padrões de Projeto Criacionais

Este repositório contém a implementação prática de dois padrões de projeto criacionais como parte da atividade de pesquisa autoral.

## Padrões Implementados

1. **Singleton**: Garante que a classe `ConexaoBanco` tenha apenas uma instância em todo o ciclo de vida da aplicação.
2. **Factory Method**: Define uma interface para criar objetos de transporte, permitindo que as subclasses (`LogisticaTerrestre` e `LogisticaMaritima`) decidam qual tipo de transporte instanciar.

## Como executar

Certifique-se de ter o Python instalado.

```bash
# Para testar o Singleton
python singleton.py

# Para testar o Factory Method
python factory_method.py

---
