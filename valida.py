from itertools import islice
import sys

def valida_cpf(cpf):
    # cpf = 96451963020
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
    

def main():
    cpf_input = sys.argv[1]
    print(f'Execution from main method: Received arg1 {cpf_input}')
    print(f'Arg0 {sys.argv[0]}')
    valida_cpf(cpf_input)


if __name__ == "__main__":
    main()
