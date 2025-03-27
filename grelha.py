# Description: This file contains the class Grelha that is responsible for creating the grid where the particles will be "placed".
import turtle as t
class Grelha:
    size = 8
    zoomGrid=10

    grid={
        'left':0.0,
        'right':0.0,
        'top':0.0,
        'bottom':0.0,
        'interval':0
        }
    def __init__(self, size=4):
        self.size = size
        print("Start grid with size", self.size)

    def desenhar_grelha(self):
       t.clear()
       t.tracer(0, 0)
       t.speed(0)

       t.penup()
       t.setpos(0,0)
       t.pendown()

       
       a=t.position()
       print(a)   
       
       # We need this offsetVertical because the grid is displaced after we draw the grid Resultado
       offsetVertical=0
       self.grid={
            'left':-(self.size*self.zoomGrid),
            'right':self.size*self.zoomGrid,
            'top':-(self.size*self.zoomGrid)+ offsetVertical,
            'bottom':self.size*self.zoomGrid + offsetVertical,
            'interval':self.size*2
            }

       # Draw the grid
          
       x_positions=range(self.grid['left'],self.grid['right'],self.grid['interval'])
       y_positions=range(self.grid['top'],self.grid['bottom'],self.grid['interval'])
       print("Desenhar grelha com esquerda %s, direita %s, topo %s, baixo %s" %(
              self.grid['left'], self.grid['right'],self.grid['top'], self.grid['bottom']))

       for x in x_positions:
            t.penup()
            t.setpos(x,self.grid['top'])
            t.pendown()
            t.setpos(x,self.grid['bottom'])

       for y in y_positions:
            t.penup()
            t.setpos(self.grid['left'],y)
            t.pendown()
            t.setpos(self.grid['right'],y)


       t.update()
       


       


   


