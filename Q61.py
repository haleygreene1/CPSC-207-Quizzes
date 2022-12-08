import dbm

db1 = dbm.open ("photo_category", "c")

#descriptions on paper
#db1["animals.png"] = "A dog and a cat"
#db1["flowers.png"] = "a purple flower surrounded by white ones"
#db1["ring.png"] = "A saint mary's class ring"

#new descriptions
db1["animals.png"] = "A horse and a cow"
db1["flowers.png"] = "Many yellow flower"
db1["ring.png"] = "Several girls with Saint Mary's class rings"

for item in db1.keys():
    print(item, db1[item])
