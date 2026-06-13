from pymongo import MongoClient

cleint = MongoClient("mongodb://localhost:27017/")
patients = cleint["clinique"]["patients"]
# for pat in patients.find() :
#     if (pat['nom'] == "idrissi"):
#         print(pat)

# patients.update_one({"nom":"kamili"},{"$set":{"nom":"rifai"}})

# for patient in patients.aggregate([{"$match":{"prenom":"sara"}},{"$project":{"_id":0,"nom":1,"prenom":1}}]):
#     print(patient)

# print(len(list(patients.find())))
nom = input("saisir un nom pour chercher dans collection: ")
listPat = list(patients.find({"nom":nom}))
if listPat:
    for pat in listPat:
        print(pat)
else:
    print("no resultat")

