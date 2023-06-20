import random

def roleta_um_terco_dobra(aposta):
    if random.randint(1,3) == 1:
        return(aposta * 2)
    else:
        return (-1 * aposta)
    
def roleta_um_terco_triplica(aposta):
    if random.randint(1,3) == 1:
        return(aposta * 3)
    else:
        return (-1 * aposta)
    
def roleta_um_terco_quadruplica(aposta):
    if random.randint(1,3) == 1:
        return(aposta * 4)
    else:
        return (-1 * aposta)

gasto = 0
recebido = 0

aposta = 1

for i in range(1000000):

    resultado = roleta_um_terco_quadruplica(aposta)
    gasto = gasto + aposta
    if resultado > 1:
        recebido = recebido + resultado

print("Gastei: " + str(gasto))
print("Recebi: " + str(recebido))
print("O RTP foi de: " + str(recebido/gasto))
    