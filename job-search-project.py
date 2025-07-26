
import requests

pays = {
    "1" : "US" ,
    "2" : "Ca" ,
    "3" : "ae"
}

choisir = input("choisir un pays  (1 : US , 2 : Ca , 3 : ae) : ")

poste = input("Entrer le poste que vous recherchez : ")


enpoint = "https://jsearch.p.rapidapi.com/search"
api_key = "0e0506fd6amsh5db42442dfe9666p102ecdjsn851649d7ccb3"

method = "Get"

headers = {
    "x-rapidapi-key" : api_key ,
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

parameters = {
    "query":"developer jobs" , 
    "country":"us"
}

response = requests.request(method , enpoint , params=parameters , headers=headers)

if response.status_code == 200 :
    donnes = response.json()
    for emploi in donnes.get("data" , [])[ : 5] :
        print(f"\n Titre : {emploi.get("job_title" , "Genie logiciel")}")
        print(f" Entreprise : {emploi.get("employer_name" , "Ange")}")
        print(f" Localisation : {emploi.get("job_country" , "Douala")}")
        print(f" Type de contrat : {emploi.get("contrat_type" , "Ecrit")}")
        print(f" Description : {emploi.get("job_description" , "Educatif")}")
else :
    print("Error : " , response.status_code)