import requests

while 1:
	op = raw_input("Digite:\n1 - Fazer requisicoes customizadas\n2 - Fazer requisicoes pre-programadas\n3 - Sair\n")

	if op == '1':
		while op != 0:
			if op == '0':
				break
			op = raw_input("Digite a requisicaoo conforme o formato padrao ( http://localhost:5000/...requisicao... ), ou digite 0 para sair\n")
			res = requests.get("http://localhost:5000/"+ op)
			print(res.text)


	elif op == '2':
		while op != '0':
			op = raw_input("Digite o numero da requisicao (1 a 10, 0 para sair)\n")

			if(op == '1'):
				print("Numero de publicacoes em uma determinada conferencia de uma area\n")

				print("Request: GET http://localhost:5000/api/ai/GECCO/papers/total\n")
				res = requests.get('http://localhost:5000/api/ai/GECCO/papers/total')
				print(res.text)

				print("Request: GET http://localhost:5000/api/chi/INTERACT/papers/total\n")
				res = requests.get('http://localhost:5000/api/chi/INTERACT/papers/total')
				print(res.text)

			elif(op == '2'):

				print("Numero de publicacoes no conjunto de conferencias de uma area\n")

				print("Request: GET http://localhost:5000/api/ai/papers/total\n")
				res = requests.get('http://localhost:5000/api/ai/papers/total')
				print(res.text)

				print("Request: GET http://localhost:5000/api/data/papers/total\n")
				res = requests.get('http://localhost:5000/api/data/papers/total')
				print(res.text)

			elif(op=='3'):


				print("Scores de todos os departamentos em uma area\n")

				print("Request: GET http://localhost:5000/api/data/scores\n")
				res = requests.get('http://localhost:5000/api/data/scores')
				print(res.text)

				print("Request: GET http://localhost:5000/api/net/scores\n")
				res = requests.get('http://localhost:5000/api/net/scores')
				print(res.text)

			elif (op=='4'):

				print("Score de um determinado departamento em uma area.\n")

				print("Request: GET http://localhost:5000/api/data/UFMG/scores\n")
				res = requests.get('http://localhost:5000/api/data/UFMG/scores')
				print(res.text)

				print("Request: GET http://localhost:5000/api/net/UFMG/scores\n")
				res = requests.get('http://localhost:5000/api/net/UFMG/scores')
				print(res.text)

			elif (op=='5'):


				print("Numero de professores que publicam em uma determinada area (organizados por departamentos)\n")

				print("Request: GET http://localhost:5000/api/professors/vision/total")
				res = requests.get('http://localhost:5000/api/professors/vision/total')
				print(res.text)

				print("Request: GET http://localhost:5000/api/professors/security/total")
				res = requests.get('http://localhost:5000/api/professors/security/total')
				print(res.text)

			elif (op=='6'):
				
				print("Numero de professores de um determinado departamento que publicam em uma area\n")

				print("Request: GET http://localhost:5000/api/professors/vision/USP/total")
				res = requests.get('http://localhost:5000/api/professors/vision/USP/total')
				print(res.text)

				print("Request: GET http://localhost:5000/api/professors/security/UFMG/total")
				res = requests.get('http://localhost:5000/api/professors/security/UFMG/total')
				print(res.text)

			elif (op=='7'):

				print("Todos os papers de uma area (ano, titulo, deptos e autores)\n")

				print("Request: GET http://localhost:5000/api/ai/papers")
				res = requests.get('http://localhost:5000/api/ai/papers')
				print(res.text)

				print("Request: GET http://localhost:5000/api/data/papers")
				res = requests.get('http://localhost:5000/api/data/papers')
				print(res.text)

			elif (op=='8'):

				print("Todos os papers de uma area em determinado ano\n")

				print("Request: GET http://localhost:5000/api/db/papers/2015")
				res = requests.get('http://localhost:5000/api/db/papers/2015')
				print(res.text)

				print("Request: GET http://localhost:5000/api/theory/papers/2016")
				res = requests.get('http://localhost:5000/api/theory/papers/2016')
				print(res.text)

			elif (op=='9'):

				print("Todos os papers de um departamento em uma area\n")

				print("Request: GET http://localhost:5000/api/db/UFMG/papers")
				res = requests.get('http://localhost:5000/api/db/UFMG/papers')
				print(res.text)

				print("Request: GET http://localhost:5000/api/theory/UFMG/papers")
				res = requests.get('http://localhost:5000/api/theory/UFMG/papers')
				print(res.text)


			elif (op=='10'):

				print("Todos os papers de um professor (dado o seu nome)\n")

				print("Request: GET http://localhost:5000/api/professors/Wagner-Meira/papers")
				res = requests.get('http://localhost:5000/api/professors/Wagner-Meira/papers')
				print(res.text)

				print("Request: GET http://localhost:5000/api/professors/Marco-Tulio-Valente/papers")
				res = requests.get('http://localhost:5000/api/professors/Marco-Tulio-Valente/papers')
				print(res.text)

			elif op=='0':
				break
	elif op == '3':
		break