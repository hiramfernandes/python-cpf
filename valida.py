from itertools import *

def valida_cpf():
    print('Execution from valida_cpf function')

    cpf = 96451963020
    cpfChars = str(cpf)
    if (len(cpfChars) == 11):
        # Iterate through first 9 digits
        print("Iterate through first 9 digits")
        for index, value in enumerate(islice(cpfChars, 0, 9)):
            print(f"{index} - {value}")

        print("Iterate through first 10 digits")
        # Iterate through first 10 digits (with the validation before added)
        for index, value in enumerate(islice(cpfChars, 0, 10)):
            print(f"{index} - {value}")
    
if __name__ == "__main__":
    valida_cpf()


def main():
    print('Execution from main method')
    # TODO: Get info from user input
    valida_cpf()