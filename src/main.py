from elasticsearch import Elasticsearch

print("hello")
es = Elasticsearch(["http://es:9200/"], verify_certs=True)

if not es.ping():
    raise ValueError("Connection failed")
else:
    print("Succeeded!")
