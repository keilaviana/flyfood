from time import time

possiveis_rotas = []
coordenadas = []

comeco = time()

def ler_arquivo():
    file = open('teste_5.txt', 'r')
    r, c = [int(i) for i in file.readline().split(' ') ]

    for linha in range(r):
        linha_atual = file.readline().split(' ')

        for i, coluna in enumerate(linha_atual):
            if coluna == '0' or coluna == '0\n':
                continue
            else:
                coordenadas.append((coluna.replace("\n", ""), (linha, i)))
    return coordenadas

def permutar(coordenadas):
    if len(coordenadas) <= 1:
        return [coordenadas]
    
    lista_auxiliar = []
    for i, atual in enumerate(coordenadas):
        elementos_restantes = coordenadas[:i] + coordenadas[i+1:]
        
        if(atual[0] == 'R'):
            continue
        else:
            for p in permutar(elementos_restantes):
                lista_auxiliar.append([atual] + p)
    
    return lista_auxiliar

def rota_otimizada(rotas):    
    menor_valor = 100000
    menor_rota = ()
    for r in rotas:
        distancia = 0
        rota_em_analise = []
        for p, _ in enumerate(r):
            if p < len(r) - 1:
                distancia += abs(r[p][1][0] - r[p+1][1][0]) + abs(r[p][1][1] - r[p+1][1][1])
                rota_em_analise.append(r[p][0])
        if(distancia < menor_valor):
            menor_valor = distancia
            menor_rota = (rota_em_analise, menor_valor)

    return menor_rota[0]

ler_arquivo()
menor_rota = rota_otimizada(permutar(coordenadas))
print ('R ', end="")
for i in menor_rota:
    print(i, end=" ")

termino = time()
print(termino - comeco)