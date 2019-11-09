import json
import hashlib 
import requests

alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
          "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

with open("answer.json", "r") as arquivoJson:
    dados = json.load(arquivoJson)

#pegando os dados do json
numCasas = dados["numero_casas"]
cifrado = dados["cifrado"]
resumo = dados["resumo_criptografico"]
token = dados["token"]

URL = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token="

#usamos uma lista pois python nao permite a modificacao de strings
decifrado=[]

for letra in cifrado.lower():
  aux = ord(letra)

  if letra in alfabeto:
    aux = aux - numCasas
    if(aux < 97):
      aux = aux + 26
      decifrado.append(chr(aux))
    else:
      decifrado.append(chr(aux))
  else:
    decifrado.append(letra)

#transformando a lista em uma string
listToString = ''.join(decifrado)

print(listToString)

#sha1
resumo = hashlib.sha1(listToString.encode("utf-8")).hexdigest()

#modificando json
dados["decifrado"] = listToString 
dados["resumo_criptografico"] = resumo

#salvando json
with open("answer2.json", "w") as arquivoJson2:
  json.dump(dados, arquivoJson2)
  
#mandar pro site
answer = {"answer": open("answer2.json","r")}
print(requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=589b7ddf5b5c80f97fd9bdc7f7809b44611a430a", files=answer))
