import requests

print("Numero de publicacoes em uma determinada conferencia de uma area\n")


res = requests.get('http://localhost:5000/api/ai/papers/total')



print(res.text)