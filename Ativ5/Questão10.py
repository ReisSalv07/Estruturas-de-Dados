from estruturas_dados import Pilha

def eh_palindromo(texto):
    pilha = Pilha()
    texto_processado = "".join(char.lower() for char in texto if char.isalnum())

    for char in texto_processado:
        pilha.empilhar(char)

    texto_invertido = ""
    while not pilha.esta_vazia():
        texto_invertido += pilha.desempilhar()

    return texto_processado == texto_invertido

print("--- Verificador de Palíndromos ---")

palavra1 = "radar"
print(f"A palavra \"{palavra1}\" é um palíndromo? {eh_palindromo(palavra1)}")

palavra2 = "python"
print(f"A palavra \"{palavra2}\" é um palíndromo? {eh_palindromo(palavra2)}")

frase1 = "A man, a plan, a canal: Panama"
print(f"A frase \"{frase1}\" é um palíndromo? {eh_palindromo(frase1)}")

frase2 = "Socorram-me, subi no ônibus em Marrocos"
print(f"A frase \"{frase2}\" é um palíndromo? {eh_palindromo(frase2)}")

frase3 = "O rato roeu a roupa do rei de Roma"
print(f"A frase \"{frase3}\" é um palíndromo? {eh_palindromo(frase3)}")
