
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class ResultadoSimulacao:
    def __init__(self):
        pass

    def desenhar_resultado(self, tempo, recipiente):
        fig, ax = plt.subplots()

        fig.set_figheight(6)
        fig.set_figwidth(12)


        #Determinar o tamanho do eixo y
        alturaMaxima = max(max(recipiente.particulasP), max(recipiente.particulasQ), max(recipiente.particulasR))

        tempoArray = np.arange(0, tempo, 1)
        line1 = ax.plot(tempoArray, recipiente.particulasP, label=f'Nº de particulas P',color="red")[0]
        line2 = ax.plot(tempoArray, recipiente.particulasQ, label=f'Nº de particulas Q',color="blue")[0]
        line3 = ax.plot(tempoArray, recipiente.particulasR, label=f'Nº de particulas R',color="green")[0]
        ax.set(xlim=[0, tempo], ylim=[0, alturaMaxima], xlabel='Time [ms]', ylabel='Z [m]')
        ax.legend()

        deltaX=100
        ax.text(tempo+deltaX, alturaMaxima, 'Estatisticas', weight='bold', fontsize=15)
        ax.text(tempo+deltaX, alturaMaxima-10, f"Criados P: {recipiente.criadosP}", weight='normal', fontsize=12)
        ax.text(tempo+deltaX, alturaMaxima-20, f"Criados Q: {recipiente.criadosQ}", weight='normal', fontsize=12)
        ax.text(tempo+deltaX, alturaMaxima-30, f"Criados R: {recipiente.criadosR}", weight='normal', fontsize=12)
        ax.text(tempo+deltaX, alturaMaxima-50, f"Consumidos P: {recipiente.consumidosP}", weight='normal', fontsize=12)
        ax.text(tempo+deltaX, alturaMaxima-60, f"Consumidos Q: {recipiente.consumidosQ}", weight='normal', fontsize=12)
        ax.text(tempo+deltaX, alturaMaxima-70, f"Consumidos R: {recipiente.consumidosR}", weight='normal', fontsize=12)

        plt.title('Simulacao de Reacoes')
        plt.tight_layout()
        plt.show()