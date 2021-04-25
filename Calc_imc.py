import mysql.connector
from os import system
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='calc_imc')
cursor = conn.cursor()
system("clear")
print("\nSelecione uma das opções:\n\n1 = Listar usuarios \n2 = Adicionar usuarios \n3 = Calculadora de IMC\n")
opcao = int(input("> "))
if opcao == 1:
	cursor.execute("SELECT * FROM pessoas;")
	printar = cursor.fetchall()
	print("\nID - NOME - PESO - ALTURA")
	for comando in printar:
		print(comando[0],comando[1],comando[2],comando[3])
elif opcao == 2:
	print("\nInsira seu nome")
	nome = str(input("> "))
	print("\nInsira seu peso")
	peso = float(input("> "))
	print("\nInsira sua altura")
	altura = float(input("> "))
	cursor.execute("INSERT INTO pessoas (nome, peso, altura) VALUES (%s, %s, %s);", (str(nome), float(peso), float(altura)))
	conn.commit()
elif opcao == 3:
	print("Selecione o usuario pelo id!")
	ID = input("> ")
	cursor.execute(f"SELECT altura, peso FROM pessoas WHERE id={str(ID,)}")
	printar = cursor.fetchmany()
	for comando in printar:
		altura = (comando[0])
		peso = (comando[1])
		imc = round((peso / (altura * altura)), 2)
		system("clear")
		if imc < 17:
			print("Muito abaixo do peso")
			print(f"{imc}\n")
		elif imc >= 17 and imc <= 18.49:
			print("Abaixo do peso")
			print(f"{imc}\n")
		elif imc >= 18.50 and imc <= 24.99:
			print("Peso Normal")
			print(f"{imc}\n")
		elif imc >= 25 and imc <= 29.99:
			print("Acima do Peso")			
			print(f"{imc}\n")
		elif imc >= 30 and imc <= 34.99:
			print("Obesidade 1")
			print(f"{imc}\n")
		elif imc >= 35 and imc <= 39.99:
			print("Obesidade 2 (Severa)")
			print(f"{imc}\n")
		else:
			print("Obesidade III (Mórbida)")
			print(f"{imc}\n")
conn.close()
