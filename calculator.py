# declaration des differentens operations possibles
op= int(input("quel calcule souhaitez-vous faire ? 1=addition, 2=soustraction, 3=multiplication, 4=division"))
print (op)

# choix de l'operation
# si l'operation choisie est l'addition
if op == 1:
    print("vous avez choisie l'addition")
    w=x+y
    print("le resultat de ton addition est :",w)


# si l'operation choisie est la soustraction
elif op == 2:
    print("vous avez choisie la soustraction")
    w=x-y
    print("le resultat de ta soustracton est:",w)


# si l'operation choisie est la multiplication
elif op == 3:
    print("vouz avez choisie la multiplication")
    w=x*y
    print("le resultat de ta multiplication est:",w)


# si l'operation choisie est la division
elif op == 4:
    print("vous avez choisie la division")
    while y==0:
        print("veillez definir y>=0")
        x= float(input(nombre1))
        y= float(input(nombre2))
        print("le resultat de ta division est:",w)
    w=x/y
else:
        print("operation non definie")
