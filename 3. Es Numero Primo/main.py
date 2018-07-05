from tasks import add, es_primo

while True:
    numero = int(input("Inserta un numero: (0) salir: >> "))
    if numero==0:
        break
    if numero > 0:
        primo = es_primo.delay(numero)
        if primo.get():
            print("\n El numero %s es primo" % numero)
        else:
            print("\n El numero %s NO es primo" % numero)