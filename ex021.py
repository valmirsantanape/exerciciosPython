palavra = input("Infome uma palavra: ")
if palavra[0] in "a,e,i,o,i,A,E,I,O,U":
    print(f'Palavra iniciada por pela vogal "{palavra[0].upper()}"')
else:
    print('Palavra não iniciada por vogal')