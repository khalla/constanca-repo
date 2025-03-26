import turtle as t

class ResultadoSimulacao:


    grid={
        'left':0.0,
        'right':0.0,
        'top':0.0,
        'bottom':0.0,
        'interval':0
        }
    
    # Constructor
    def __init__(self):
        
        self.__desenhar_grelha()
        print("Start grid for result")

    # Draw the grid
    def __desenhar_grelha(self):
       t.clear()
       t.tracer(0, 0)
       t.speed(0)
       
       t.penup()
       t.setpos(0,0)
       t.pendown()


       self.grid={
            'left':-(80),
            'right':80,
            'top':200,
            'bottom':280,
            'interval':1
            }

       x_positions=range(self.grid['left'],self.grid['right'],self.grid['interval'])
       y_positions=range(self.grid['top'],self.grid['bottom'],self.grid['interval'])

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