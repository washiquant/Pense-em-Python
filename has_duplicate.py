#Exercício
""""Qual é a palavra mais longa que você consegue pensar em que cada letra aparece apenas uma vez? 
Vamos ver se conseguimos encontrar uma mais longa que unpredictably.
Escreva uma função chamada has_duplicates que recebe uma sequência -- como uma lista ou string -- como um parâmetro
e devolve True se houver algum elemento que apareça na sequência mais de uma vez.""""

def has_duplicates(sequencia):
    return len(set(sequencia)) != len(sequencia)

# --- Teste do Exercício ---
# "unpredictably" tem 14 letras e todas são únicas!
palavra = "unpredictably"
print(f"A palavra '{palavra}' tem duplicados? {has_duplicates(palavra)}")

# Testando com duplicados
print(f"A palavra 'banana' tem duplicados? {has_duplicates('banana')}")