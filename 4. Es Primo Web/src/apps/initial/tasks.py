from celery import task, shared_task

@shared_task
def add(x, y):
    print("Res: %s" % str(x+y))
    return x + y

@shared_task
def es_primo(numero):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    cont = 0
    verificar= False
    for i in range(1,numero+1):
        if (numero%i)==0:
            cont = cont+1            
        if cont >= 3:
            verificar=True
            break
    if cont==2 or verificar==False:
        return True
    else:
        return False