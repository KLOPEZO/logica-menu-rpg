import random 

def vivos(personajes):
    contador = 0
    for p in personajes:
        if p.vida > 0:
            contador += 1
    
    return contador

def batalla(personajes):
    while vivos(personajes) > 1:

        for atacante in personajes:

            if atacante.vida <= 0:
                continue

            objetivos = [
                    p for p in personajes 
                    if p != atacante and p.vida > 0
                    ]
        
            if objetivos:
                objetivo = random.choice(objetivos)
                atacante.atacar(objetivo)