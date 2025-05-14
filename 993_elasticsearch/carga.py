from elasticsearch import Elasticsearch
import pandas as pd

# CSV
df = pd.read_csv('Math-Students.csv')

# Conexión 
es = Elasticsearch("http://127.0.0.1:9200")

if not es.ping():
    raise ValueError("No se pudo conectar a Elasticsearch")

# indice
index_name = "students"

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

for _, row in df.iterrows():
    es.index(index=index_name, document=row.to_dict())

print("Datos cargados exitosamente")
