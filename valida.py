from itertools import islice
import sys

"""
Usage

REPL:           main(96451963020)
Command Line:   python valida.py 96451963020
"""

def valida_cpf(cpf):
    # cpf = 96451963020
    cpfChars = str(cpf)
    if (len(cpfChars) == 11):
        print(cpf)

        digito1 = calcula_digito(cpf, 1)
        digito2 = calcula_digito(cpf, 2)
        
        print(f"Digito 1: {digito1}")
        print(f"Digito 2: {digito2}")


def calcula_digito(cpf, digito):
    numberOfIterations = 9 if digito == 1 else 10
    indexMultiplier = 10 if digito == 1 else 11

    cpfChars = str(cpf)
    currentSum = 0
    for index, value in enumerate(islice(cpfChars, 0, numberOfIterations)):
        currentSum += int(value) * (indexMultiplier - index)

    result = currentSum % 11

    if (result > 2):
        return 11- result
    
    return 0


def main(cpf_input):
    print(f'Execution from main method: Received {cpf_input}')
    valida_cpf(cpf_input)


if __name__ == "__main__":
    try:
        cpf_input = sys.argv[1]
    except IndexError:
        cpf_input = '96451963030'

    main(cpf_input)
