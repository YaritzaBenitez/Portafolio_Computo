from elasticsearch import Elasticsearch

# Crear cliente sin seguridad (como está configurado)
es = Elasticsearch("http://127.0.0.1:9200")

try:
    if es.ping():
        print("Conectado correctamente")
    else:
        print("No se pudo conectar")
except Exception as e:
    print("Error de conexión", e)
