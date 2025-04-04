

import particula as part
import espaco_virtual as ev
import resultado_simulacao as res




# Este programa simula a reacao entre particulas P e Q, que se transformam em particulas R.
# As particulas R reagem entre si, formando duas particulas P e duas particulas Q.
# As particulas P , Q e R se movem aleatoriamente pelo recipiente

# declaracao de variaveis globais
ladoGrelha = 8
numAtomosP = 120
limiteMinimoP = numAtomosP / 2
numAtomosQ=90
limiteMinimoQ = numAtomosQ /2
limiarR=50
tempoSimulacao=2
limiteDeslocamento=2
intervaloTempo=0.001
indexParticula=0



# Inicializacao do recipiente
recipiente = ev.Recipiente(ladoGrelha)
# recipiente.desenhar_grelha()

    
def addParticulas(recipiente,tipo, numero,indexParticula, dimensao,limiteDeslocamento):
    # Adiciona um numero de particulas do tipo ao recipiente 
    for i in range(int(float(numero))):
        particula = part.Atomo(tipo,indexParticula,dimensao,limiteDeslocamento)
        indexParticula+=1
        recipiente.adicionar_particula(particula)
    return indexParticula

def removeParticulasR(recipiente):
    # Remove um numero de particulas do tipo ao recipiente 
    recipiente.remover_particulas(ladoGrelha/2)
    

#adicionar particulas P ao recipiente
indexParticula=addParticulas(recipiente,"P",numAtomosP,indexParticula,ladoGrelha,limiteDeslocamento)


#adicionar particulas Q ao recipiente
indexParticula=addParticulas(recipiente,"Q",numAtomosQ,indexParticula,ladoGrelha,limiteDeslocamento)


# Calculo do numero de iteracoes que serao feitas
# O tempo de simulacao e dividido pelo intervalo de tempo
tempo=int(float(tempoSimulacao/intervaloTempo))
# Simulacao que ira mover as particulas e verificar as reacoes
for i in range(tempo):
    recipiente.recolher_estatisticas()
    recipiente.mover_particulas()
    indexParticula=recipiente.verifica_reacoes(indexParticula+1)
    # Se o numero de particulas P e Q diminui até ao limite minimo
    # adiciona um numero igual ao limite minimo de particulas P
    if(recipiente.particulasP[i]<=limiteMinimoP):
        indexParticula=addParticulas(recipiente,"P",limiteMinimoP,indexParticula,ladoGrelha,limiteDeslocamento)
    if(recipiente.particulasQ[i]<=limiteMinimoQ):
        indexParticula=addParticulas(recipiente,"Q",limiteMinimoQ,indexParticula,ladoGrelha,limiteDeslocamento)
    # Se o numero de particulas R aumentar até ao limiar R
    # remove as particulas R que se encontram no quandre inferior esquerdo
    # do recipiente
    if(recipiente.particulasR[i]>=limiarR):
        removeParticulasR(recipiente)

    
    

# Inicializacao do resultado da simulacao
resultado = res.ResultadoSimulacao()
resultado.desenhar_resultado(tempo,recipiente)


    
