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
        print("Adicionando particula ao recipiente")

    def desenhar_grelha(self):
        self.grelhaInterna = gr.Grelha(self.dimensao)
        self.grelhaInterna.desenhar_grelha()
        

    
    def mover_particulas(self):
        for particula in self.particulas:
            particula.mover(self.grelhaInterna.grid)

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
            for i in range(0,len(reacao.objectArray),2):
                if i+1>=len(reacao.objectArray):
                    break
                id1=reacao.objectArray[i]
                id2=reacao.objectArray[i+1]
                particula1=None
                particula2=None
                for particula in self.particulas:
                    if particula.id == id1:
                        particula1=particula
                        break
                for particula in self.particulas:
                    if particula.id == id2:
                        particula2=particula
                        break   
                if (particula1.tipo=='P' and particula2.tipo=='Q') or (particula1.tipo=='Q' and particula2.tipo=='P'):
                    particula1.tipo='R'
                    self.particulas.remove(particula2)
                    self.consumidosP+=1
                    self.consumidosQ+=1
                    self.criadosR+=1
                
                if particula1.tipo=='R' and particula2.tipo=='R':

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


                    