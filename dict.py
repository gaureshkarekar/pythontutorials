print("Diction example !!!")

datas = [
    {
        "fname" :"Gauresh",
        "lname" :"Karekar",
        "company":"TCS"
    },
    {
        "fname" :"Ashwini",
        "lname" :"Kamat",
        "company":"TCS"    
    },
    {
        "fname" :"Urmila",
        "lname" :"Shinde",
        "company":"V21Group",
        "address":{
            "pin":411033,
            "street":{
                "streetname":"Punawale Road",
                "landmark" : "zudio"
            },
            "Apartment":"Sai Paradise"
        }
    }
]
# print(datas[2]["address"]["street"]["landmark"])

d = [1,2,3]

if(type(d) == dict):
    print("It is a dictionary")
else:
    print("not a dictionary")

# for data in datas:
#     fname = data["fname"]
#     lname = data["lname"]
#     company = data["company"]
#     print(f"First Name : {fname} Last Name : {lname}  Company : {company}")

# newDic = {
#     "name" : "Gauresh",
#     "lname" : {
#         "asd":"asdasd"
#     },
#     "company" : "TCS"
# }

# for k,v in newDic.items():
#     print(f"{k} : {v}")