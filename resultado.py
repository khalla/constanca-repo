import turtle as t

class ResultadoSimulacao:

    grid=   {
            'left':-(80),
            'right':120,
            'top':220,
            'bottom':100,
            'interval':10
            }
    
    linhaP= None
    linhaQ= None
    linhaR= None


    # Constructor
    def __init__(self):
        self.__desenhar_grelha()
        self.__inicializar_linhas()
        print("Start grid for result")


    def desenhar_resultado(self,tempo,particulasP,particulasQ,particulasR):
        # Desenha os resultados no ecra

        self.linhaP.penup()
        self.linhaQ.penup() 
        self.linhaR.penup()
        if tempo > 0:
            self.linhaP.setpos(self.grid['left']+tempo,self.grid['bottom']+particulasP[tempo-1])
            self.linhaQ.setpos(self.grid['left']+tempo,self.grid['bottom']+particulasQ[tempo-1])
            self.linhaR.setpos(self.grid['left']+tempo*2,self.grid['bottom']+particulasR[tempo-1])
        else:
           self.linhaP.pendown()
           self.linhaQ.pendown()   
           self.linhaR.pendown()
           return

        self.linhaP.pendown()
        self.linhaQ.pendown()   
        self.linhaR.pendown()

        self.linhaP.setpos(self.grid['left']+tempo,self.grid['bottom']+particulasP[tempo])
        self.linhaQ.setpos(self.grid['left']+tempo,self.grid['bottom']+particulasQ[tempo])
        self.linhaR.setpos(self.grid['left']+tempo*2,self.grid['bottom']+particulasR[tempo])

        self.linhaP.penup()
        self.linhaQ.penup() 
        self.linhaR.penup()
        t.update()

    # Inicializa as linhas de resultado para contagem de particulas
    # e as cores de cada linha
    def __inicializar_linhas(self):  
     self.linhaP= t.Turtle()
     self.linhaP.color('red') 
     self.linhaP.penup()
     
     
     self.linhaQ= t.Turtle()
     self.linhaQ.color('blue')
     self.linhaQ.penup()

     self.linhaR= t.Turtle()
     self.linhaR.color('green')
     self.linhaR.penup()
     
    # Draw the grid
    def __desenhar_grelha(self):  
     self.__desenhar_rectangulo()
     self.__desenhar_legenda()


    def __desenhar_rectangulo(self):
       #  lado esquerdo
       t.penup()
       t.setpos(self.grid['left'],self.grid['top'])
       t.pendown()
       t.setpos(self.grid['left'],self.grid['bottom'])


       # lado direito
       t.penup()
       t.setpos(self.grid['right'],self.grid['top'])
       t.pendown()
       t.setpos(self.grid['right'],self.grid['bottom'])
       
       # baixo
       t.penup()
       t.setpos(self.grid['right'],self.grid['bottom'])
       t.pendown()
       t.setpos(self.grid['left'],self.grid['bottom'])

       # topo
       t.penup()
       t.setpos(self.grid['right'],self.grid['top'])
       t.pendown()
       t.setpos(self.grid['left'],self.grid['top'])

       t.update()
     
    def __desenhar_legenda(self):
     t.color("gray")

     for i in range(0,120,10):
         t.penup()
         t.setpos(self.grid['left'] -20,-10 +self.grid['top']-(i))
         t.pendown()
         t.write(str(120-i),font=("Arial", 7, "normal"))
         t.penup()
         t.setpos(self.grid['left']-5 ,self.grid['top']-(i))
         t.pendown()
         t.setpos(self.grid['left'] ,self.grid['top']-(i))
         t.update()
     for i in range(0,210,25):
         t.penup()
         t.setpos(-5+self.grid['left'] +i,self.grid['bottom']-20)
         t.pendown()
         t.write(str(i),font=("Arial", 7, "normal"))
         t.penup()
         t.setpos(self.grid['left']+i ,self.grid['bottom']-5)
         t.pendown()
         t.setpos(self.grid['left']+i ,self.grid['bottom'])
         t.update()
