import pymongo

client = pymongo.MongoClient("mongodb+srv://Naru:Naru2108@cluster0.cjy4ybr.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)

d={"name":"narasimha","email":"abc@gmail.com","surname":"ambati"}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)