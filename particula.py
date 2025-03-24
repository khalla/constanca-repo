import random
class Atomo:
    posicao =  { 
        'x': random.randint(1, 8)/10,
        'y': random.randint(1, 8)/10
        }
    vector =  { 
        'dx': random.randint(1, 8)/10,
        'dy': random.randint(1, 8)/10
        }
    
    
    tipo = None
    
    def __init__(self, tipo):
        self.tipo = tipo
        print("Inicializando átomo com tipo %s , na posição (x,y) -> (%f,%f) e com vector (x,y) -> (%f,%f) " %(
              self.tipo, self.posicao["x"], self.posicao["y"],self.vector["dx"], self.vector["dy"]))
        
    

    def mover(self, min=0, max=8):

        if  (self.posicao["x"]+ self.vector["dx"]) > max:
            sinalX= None
            if self.vector["dx"]>0 : 
                sinalX=1
            else:
                sinalX=-1
            
            self.vector["dx"]= -sinalX *  + self.vector["dx"]

        if (self.posicao["x"]+ self.vector["dx"]) < min  :
            sinalX= None
            if self.vector["dx"]>0 : 
                sinalX=1
            else:
                sinalX=-1
            
            self.vector["dx"]= sinalX *  self.vector["dx"]
          
        self.posicao["x"] = self.posicao["x"] + self.vector["dx"]    


        if  (self.posicao["y"]+ self.vector["dy"]) > max:
            sinalY= None
            if self.vector["dy"]>0 : 
                sinalY=1
            else:
                sinalY=-1
            
            self.vector["dy"]= -sinalY *  + self.vector["dy"]

        if (self.posicao["y"]+ self.vector["dy"]) < min  :
            sinalY= None
            if self.vector["dy"]>0 : 
                sinalY=1
            else:
                sinalY=-1
            
            self.vector["dy"]= sinalY *  self.vector["dy"]
          
        self.posicao["y"] = self.posicao["y"] + self.vector["dy"]    


        print("Movendo átomo com tipo %s , na posição (x,y) -> (%f,%f) e com vector (x,y) -> (%f,%f) " %(
              self.tipo, self.posicao["x"], self.posicao["y"],self.vector["dx"], self.vector["dy"]))
