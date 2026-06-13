from pymongo import MongoClient
client = MongoClient(host = 'localhost',port=27017)
# print(client)
db = client['clinique']
patients = db['patients']
# print(patients)
# res = patients.insert_one({'nom':'idrissi','prenom':'kamal'})
# print(res.inserted_id)
# res = patients.insert_many([
#     {'nom':'drai','prenom':'nadia','age':20},
#     {'nom':'hour','prenom':'hicham','age':30},
#     {'nom':'kamili','prenom':'sara','age':16}
# ])
# print(res.inserted_ids)

# for document in patients.find({'age':{'$gt':10}}):
#     print(document['nom'] + ' ' + document['prenom'])
# print(len(list(patients.find())))

# critere = {'age':{'$gt':18,'$lt':60}}
# projection = {'_id':0,'nom':1,'prenom':1,'age':1}
# triDage = {'age':-1}
# liste = list(patients.find())
# # for doc in patients.find(critere,projection).sort(triDage):
# #     print(f"nom complet est :{doc['nom']} {doc['prenom']},age: {doc['age']}")

# for doc in liste:
#     print(f"nom complet est :{doc['nom']} {doc['prenom']},age: {doc['age']}")


op1 = {"$match":{'age':{'$gt':18}}}
op2 = {"$group":{'_id':"$sexe",'effectif':{'$sum':1}}}
op3 = {'$sort':{'effectif':-1}}
op3 = {'$project':{'sexe':'$_id','effectif':1}}
operation = [op1,op2,op3]
maliste = list(patients.aggregate(operation))
for doc in maliste:
     print(doc)

# patients.update_many({"actif":False},{'$set':{"actif":True}})
# patients.update_many({"nom":"drai"},{'$set':{"actif":False}})
patients.delete_many({"actif":False})
for doc in patients.find():
    print(doc)