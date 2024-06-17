import pandas as pd

# Carregar a planilha
file_path = '/mnt/data/RELAÇÃO GERAL DE COMUNIDADES ATENDIDAS_GERAL_PAINEL SH -I (2).xlsx'
sheet_name = 'Sheet1'  # Substitua pelo nome correto da aba, se necessário
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Converter para JSON
json_data = df.to_json(orient='records', force_ascii=False)

# Salvar o JSON em um arquivo
output_json_path = '/mnt/data/comunidades.json'
with open(output_json_path, 'w', encoding='utf-8') as f:
    f.write(json_data)

output_json_path