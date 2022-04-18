lista = "zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quize","dezesseis","dezessete","dezoito","dezenove","vinte"
resp = int(input("Digite um numero de 0 á 20: "))
while resp < 0 or resp > 20:
	resp = int(input("tente novamente um numero de 0 a 20: "))
print(f"voce digitou o numero {lista[resp]}")