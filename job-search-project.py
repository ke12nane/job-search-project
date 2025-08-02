import requests


#ici nous concervons notre endpoint(point de determinaison)


enpoint = "https://jsearch.p.rapidapi.com/search"


#here is my api key


api_key = "0e0506fd6amsh5db42442dfe9666p102ecdjsn851649d7ccb3"


method = "Get"


headers = {
    "x-rapidapi-key" : api_key ,
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}


#ici nous avons nos parametres


parameters = {
    "query":"developer jobs" , 
    "country":"us"
}


#differents pays


pays = {
    "1" : "US" ,
    "2" : "Ca" ,
    "3" : "ae"
}


print("1.Etat Unis")
print("2.Canada")
print("3.ae")


#Entrer le choix du pays


choisir = input("choisir un pays  : ")


if choisir != pays :
    print("error")
    input("choisir un autre pays :")


#Entrer le poste


poste = input("Entrer le poste que vous recherchez : ")


response = requests.request(method , enpoint , params=parameters , headers=headers)


if response.status_code == 200 :
    data = response.json()
    for emploi in data.get("data" , [])[ : 5] :
        print(f"\n Titre : {emploi.get("job_title" , "Genie logiciel")}")
        print(f" Entreprise : {emploi.get("employer_name" , "Ange")}")
        print(f" Localisation : {emploi.get("job_country" , "Douala")}")
        print(f" Type de contrat : {emploi.get("contrat_type" , "Ecrit")}")
        print(f" Description : {emploi.get("job_description" , "Educatif")}")
else :
    print("Error : " , response.status_code)