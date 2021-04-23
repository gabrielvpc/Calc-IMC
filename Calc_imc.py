#Conexão com o banco mysql
import mysql.connector
from os import system
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='calc_imc')
cursor = conn.cursor()
#Conexão com o banco mysql

#i = 1
#while i == 1:

print("\nSelecione uma das opções:\n\n1 = Listar usuarios \n2 = Procurar usuarios \n3 = Calculadora de IMC\n")
opcao = int(input("> "))
if opcao == 1:
	cursor.execute("SELECT * FROM pessoas;")
	printar = cursor.fetchall()
	print("\nNOME - PESO - ALTURA")
	for comando in printar:
		print(comando[1],comando[2],comando[3])
#elif opcao == 2:





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
		if imc >= 18:
			print("susexo")
			print(f"{imc}\n")
			

		


conn.close()
