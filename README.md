# Atividade: Padrões de Projeto Criacionais

Este repositório contém a parte prática da atividade de pesquisa sobre Design Patterns Criacionais. 

## 🚀 Padrões Implementados

Para demonstrar a aplicação real dos conceitos estudados, implementei dois padrões clássicos em Python:

1. **Singleton (`singleton.py`)**: 
   - **Objetivo:** Garantir que a classe `ConexaoBanco` tenha uma única instância global.
   - **Funcionamento:** O código impede a criação de múltiplos objetos de conexão, economizando recursos e mantendo a consistência.

2. **Factory Method (`factory_method.py`)**: 
   - **Objetivo:** Desacoplar a lógica de negócio do tipo específico de objeto criado.
   - **Funcionamento:** Simula um sistema de logística que fabrica transportes (Caminhão ou Navio) de forma dinâmica, facilitando a expansão do sistema no futuro.

## 🛠️ Como executar os códigos

Certifique-se de ter o Python instalado em sua máquina.

```bash
# Para testar o padrão Singleton
python singleton.py

# Para testar o padrão Factory Method
python factory_method.py
