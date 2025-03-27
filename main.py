
import particula as part
import espaco_virtual as ev
import resultado as res
import ecra as ecra


# declaracao de variaveis globais
ladoGrelha = 8
numAtomosP=120
numAtomosQ=90
limiarR=50
tempoSimulacao=2
limiteDeslocamento=2
intervaloTempo=0.001
indexParticula=0

# Inicializacao do ecra
meuEcra = ecra.EcraTotal()

# Inicializacao do recipiente
recipiente = ev.Recipiente(ladoGrelha)
recipiente.desenhar_grelha()

#adicionar particulas P ao recipiente
for i in range(numAtomosP):
    atomP = part.Atomo("P",indexParticula, ladoGrelha,limiteDeslocamento)
    indexParticula+=1
    recipiente.adicionar_particula(atomP)

#adicionar particulas Q ao recipiente
for i in range(numAtomosQ):
    atomQ = part.Atomo("Q",indexParticula,ladoGrelha,limiteDeslocamento)
    indexParticula+=1
    recipiente.adicionar_particula(atomQ)

# Inicializacao do resultado da simulacao
resultado = res.ResultadoSimulacao()

# Calculo do numero de iteracoes que serao feitas
# O tempo de simulacao e dividido pelo intervalo de tempo
tempo=int(float(tempoSimulacao/intervaloTempo))
# Simulacao que ira mover as particulas e verificar as reacoes
for i in range(tempo):
    recipiente.recolher_estatisticas()
    resultado.desenhar_resultado(i,recipiente.particulasP,recipiente.particulasQ,recipiente.particulasR)
    recipiente.mover_particulas()
    indexParticula=recipiente.verifica_reacoes(indexParticula+1)
    
    


