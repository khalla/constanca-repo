import random
import turtle as t
class Atomo:
    posicaoX = 0.0
    posicaoY = 0.0
    vectorX = 0.0
    vectorY = 0.0
    deltaZoom =10.0
    #isto será um objeto do tipo turtle para desenho grafico
    grafico=None    
    tipo = None
    id=None
    #construtor
    def __init__(self, tipo,id,size=8, limiteDeslocamento=2):
        self.tipo = tipo
        self.id=id
        self.posicaoX = random.randint(1, size)
        self.posicaoY = random.randint(1, size)
        self.vectorX = random.randint(1, limiteDeslocamento *10)/10
        self.vectorY = random.randint(1, limiteDeslocamento *10)/10
        #criar um objeto do tipo turtle para desenho grafico
        self.grafico = t.Turtle()
        self.grafico.shape('square')
        self.grafico.resizemode("user")
        self.grafico.shapesize(0.1, 0.1, 0.1) # width, len, outline
        
        self.__verificarCor()
            
        print("Inicializando átomo com tipo %s , na posição (x,y) -> (%f,%f) e com vector (x,y) -> (%f,%f) " %(
              self.tipo, self.posicaoX, self.posicaoY,self.vectorX, self.vectorY))
        
    def __verificarCor(self):    
        if self.tipo == 'P':  
            self.grafico.color('red')
            
        if self.tipo == 'Q':  
            self.grafico.color('blue')
            
        if self.tipo == 'R':  
            self.grafico.color('green')



    def mover(self, grid,min=0, max=8):
        self.__verificarCor()
        # verificar se a particula esta dentro dos limites da grelha X > 8
        if  (self.posicaoX+ self.vectorX) > max:
            sinalX= None
            if self.vectorX>0 : 
                sinalX=1
            else:
                sinalX=-1
            
            self.vectorX= -sinalX *  + self.vectorX

        # verificar se a particula esta dentro dos limites da grelha X < 0
        if (self.posicaoX+ self.vectorX) < min  :
            sinalX= None
            if self.vectorX>0 : 
                sinalX=1
            else:
                sinalX=-1
            
            self.vectorX= sinalX *  self.vectorX
          
        self.posicaoX = self.posicaoX + self.vectorX    

        # verificar se a particula esta dentro dos limites da grelha Y > 8
        if  (self.posicaoY+ self.vectorY) > max:
            sinalY= None
            if self.vectorY>0 : 
                sinalY=1
            else:
                sinalY=-1
            
            self.vectorY= -sinalY *  + self.vectorY

        # verificar se a particula esta dentro dos limites da grelha Y < 0
        if (self.posicaoY+ self.vectorY) < min  :
            sinalY= None
            if self.vectorY>0 : 
                sinalY=1
            else:
                sinalY=-1
            
            self.vectorY= sinalY *  self.vectorY
          
        self.posicaoY = self.posicaoY + self.vectorY    

        #mover o objecto grafico
        self.grafico.penup()
        self.grafico.goto(grid['left']+ self.posicaoX*self.deltaZoom *1.8,-grid['bottom']+self.posicaoY*self.deltaZoom*1.8)    
        self.grafico.pendown()
        t.update()
        print("Movendo átomo com tipo %s , na posição (x,y) -> (%f,%f) e com vector (x,y) -> (%f,%f) " %(
              self.tipo, self.posicaoX, self.posicaoY,self.vectorX, self.vectorY))

