from mcp.server.fastmcp import FastMCP

# 1. Criamos um servidor MCP simples usando FastMCP
mcp = FastMCP("Catalogo_Britanico")

# 2. Definimos a ferramenta (Tool) que o servidor expõe
@mcp.tool()
def consultar_registros(data_consulta: str) -> str:
    """
    Consulta o registro de visitantes da biblioteca em uma data específica.
    Args:
        data_consulta: A data para buscar (ex: '14 de Julho').
    """
    # Lógica simples do Mock (o "Banco de Dados" falso)
    if "14" in data_consulta and "julho" in data_consulta.lower():
        return "REGISTRO ENCONTRADO: Lord Byron e Mary Shelley assinaram o livro de visitas."
    else:
        return "Nenhum registro encontrado para esta data."

# 3. Iniciamos o servidor
if __name__ == "__main__":
    mcp.run()
