class ConexaoBanco:
    _instancia = None

    def __new__(cls):
        # Se a instância ainda não existe, cria uma
        if cls._instancia is None:
            print("Iniciando conexão com o Banco de Dados...")
            cls._instancia = super(ConexaoBanco, cls).__new__(cls)
        return cls._instancia

# Teste para validar o padrão
if __name__ == "__main__":
    db1 = ConexaoBanco()
    db2 = ConexaoBanco()

    print(f"ID objeto 1: {id(db1)}")
    print(f"ID objeto 2: {id(db2)}")

    if db1 is db2:
        print("Sucesso: Ambas as variáveis apontam para a mesma instância única.")
