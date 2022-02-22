from coin_code import get_coin_code
from coin_converter import get_converted_amount

def menu():
	print("Bem vindo ao conversor de moedas")
	print("Escolha pelo numero da lista o pais a consultar pelo codigo da moeda.")

	countries_code = get_coin_code()

	try:
		source_coin = int(input("Insira pelo numero a moeda de origem: "))
		countries_code[source_coin]
	except:
		print("Por favor insira um numero valido: ")
		menu()

	source_code = countries_code[source_coin]['code']

	try:
		destination_coin = int(input("Insira pelo numero a moeda de destino: "))
		countries_code[destination_coin]
	except:
		print("Por favor insira um numero valido: ")
		menu()
		
	destination_code = countries_code[destination_coin]['code']

	amount = int(input("Insira a quantidade de dinheiro a converter: "))

	converted_amount = get_converted_amount(source_code, destination_code, amount)

	print(f"{amount} {source_code} são {converted_amount} {destination_code}") #podem usar o babel

menu()