import os

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-8UFTKYbB81NBEvEKjuQh15BJcnMvFztzgkx33gqxceiMzY6K"

from llama_parse import LlamaParse

documentos = LlamaParse(result_type="markdown", parsing_instruction="this file contains text and tables, I'd like to get only the tables from the text").load_data("resultado.pdf")

print(len(documentos))

for i, pagina in enumerate(documentos):
    with open(f"meu_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)
