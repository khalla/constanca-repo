import grelha as gr
import reacoes as reac
import particula as part

class Recipiente:
    dimensao=8
    particulas=[]
    grelhaInterna= None

    consumidosP=0
    consumidosQ=0
    consumidosR=0

    criadosP=0
    criadosQ=0
    criadosR=0

    #Variaveis para guardar as particulas de cada tipo em cada instante de tempo
    particulasP=[]
    particulasQ=[]
    particulasR=[]
    def __init__(self, dimensao=8):
        self.dimensao = dimensao
        print("Inicializando o recepiente com tamanho de  %s  " %(self.dimensao))
        
    def adicionar_particula(self, particula):
        self.particulas.append(particula)
        # print("Adicionando particula ao recipiente")

    def remover_particula(self,size):
        for i in range(len(self.particulas)):
            if self.particulas[i].tipo == "R" and self.particulas[i].posicaoX < size and self.particulas[i].posicaoY < size:
                self.particulas.remove(self.particulas[i])
                break
        # print("Removendo particula do recipiente")

    # def desenhar_grelha(self):
    #     self.grelhaInterna = gr.Grelha(self.dimensao)
    #     self.grelhaInterna.desenhar_grelha()
        

    
    def mover_particulas(self):
        for particula in self.particulas:
            particula.mover()

    def recolher_estatisticas(self):
        contagemP=0
        contagemQ=0
        contagemR=0
        for particula in self.particulas:
            if particula.tipo == 'P':
                contagemP+=1
            if particula.tipo == 'Q':
                contagemQ+=1
            if particula.tipo == 'R':
                contagemR+=1
        self.particulasP.append(contagemP)
        self.particulasQ.append(contagemQ)
        self.particulasR.append(contagemR)

    def verifica_reacoes(self,currentIndex):
        gridReacoes=[]
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                reacao = reac.ReacaoHolder(i,j)
                for particula in self.particulas:
                    if particula.posicaoX > i and particula.posicaoX<i+1 and particula.posicaoY > j and particula.posicaoY<j+1:
                        reacao.objectArray.append(particula.id)
                gridReacoes.append(reacao)
        
        for reacao in gridReacoes:
            particulasEncontradasNaCelula=[]
            for j in range(0,len(reacao.objectArray)):
                for particula in self.particulas:
                    if particula.id == reacao.objectArray[j]:
                        particulasEncontradasNaCelula.append(particula)
            if len(particulasEncontradasNaCelula) == 0:
                continue
            if len(particulasEncontradasNaCelula) == 1:
                continue

            particulasEncontradasNaCelulaTipoP=list(filter(lambda x: x.tipo == 'P', particulasEncontradasNaCelula))
            particulasEncontradasNaCelulaTipoQ=list(filter(lambda x: x.tipo == 'Q', particulasEncontradasNaCelula))
            particulasEncontradasNaCelulaTipoR=list(filter(lambda x: x.tipo == 'R', particulasEncontradasNaCelula))

            lenP= len(particulasEncontradasNaCelulaTipoP) 
            lenQ= len(particulasEncontradasNaCelulaTipoQ)
            lenR= len(particulasEncontradasNaCelulaTipoR)

            for i in range(0,lenP,1):
                if(len(particulasEncontradasNaCelulaTipoQ)<= i):
                    continue
                
                particulaP=particulasEncontradasNaCelulaTipoP[i]
                particulaQ=particulasEncontradasNaCelulaTipoQ[i]


                #criar uma nova particula R
                particulaR=part.Atomo("R",currentIndex,self.dimensao,2)
                particulaR.posicaoX=particulaP.posicaoX
                particulaR.posicaoY=particulaP.posicaoY
                self.particulas.append(particulaR)
                currentIndex+=1

                #remover as duas particulas P e Q
                self.particulas.remove(particulaP)
                self.particulas.remove(particulaQ)

                self.consumidosP+=1
                self.consumidosQ+=1
                self.criadosR+=1                

            for i in range(0,len(particulasEncontradasNaCelulaTipoR),2):
                if i+1>=len(particulasEncontradasNaCelulaTipoR):
                    break
                id1=particulasEncontradasNaCelulaTipoR[i]
                id2=particulasEncontradasNaCelulaTipoR[i+1]
                particula1=particulasEncontradasNaCelulaTipoR[i]
                particula2=particulasEncontradasNaCelulaTipoR[i+1]

                #criar 2 particulas P
                particulaP1=part.Atomo("P",currentIndex,self.dimensao,2)
                particulaP1.posicaoX=particula1.posicaoX
                particulaP1.posicaoY=particula1.posicaoY
                self.particulas.append(particulaP1)
                currentIndex+=1

                particulaP2=part.Atomo("P",currentIndex,self.dimensao,2)
                particulaP2.posicaoX=particula1.posicaoX
                particulaP2.posicaoY=particula1.posicaoY
                self.particulas.append(particulaP2)
                currentIndex+=1
                #remover a primeira particula R
                self.particulas.remove(particula1)

                #criar 2 particulas Q
                particulaQ1=part.Atomo("Q",currentIndex,self.dimensao,2)
                particulaQ1.posicaoX=particula2.posicaoX
                particulaQ1.posicaoY=particula2.posicaoY
                self.particulas.append(particulaQ1)
                currentIndex+=1

                particulaQ2=part.Atomo("Q",currentIndex,self.dimensao,2)
                particulaQ2.posicaoX=particula2.posicaoX
                particulaQ2.posicaoY=particula2.posicaoY
                self.particulas.append(particulaQ2)
                currentIndex+=1
                
                #remover a segunda particula R
                self.particulas.remove(particula2)

                self.consumidosR+=2
                self.criadosP+=2
                self.criadosQ+=2
        return currentIndex


                    