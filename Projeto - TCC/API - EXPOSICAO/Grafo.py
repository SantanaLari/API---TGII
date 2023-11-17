import networkx as nx 
import matplotlib.pyplot as plt 

class Grafo:
    def __init__(self):        
        pass

    def gera_grafo(self, lista_dados_coletados, lista_dados_ajustados):
        grafo = nx.DiGraph()

        dados_ajustados = lista_dados_ajustados
        dados_coletados = lista_dados_coletados

        conexoes = [(dados_ajustados[2], dados_ajustados[8]), (dados_ajustados[2], dados_ajustados[4]), (dados_ajustados[3], dados_ajustados[2]), 
        (dados_ajustados[4], dados_ajustados[8]), (dados_ajustados[4], dados_ajustados[5]), 
        (dados_ajustados[5], dados_ajustados[8]), (dados_ajustados[5], dados_ajustados[6]), 
        (dados_ajustados[6], dados_ajustados[8]), (dados_ajustados[6], dados_ajustados[7]), 
        (dados_ajustados[8], dados_ajustados[6]), (dados_ajustados[8], dados_ajustados[5]), (dados_ajustados[8], dados_ajustados[4]), (dados_ajustados[8], dados_ajustados[2]), 
        (dados_ajustados[9], dados_ajustados[8]), (dados_ajustados[9], dados_ajustados[13]), (dados_ajustados[9], dados_ajustados[12]), (dados_ajustados[9], dados_ajustados[11]), (dados_ajustados[9], dados_ajustados[10]), (dados_ajustados[9], dados_ajustados[1]), (dados_ajustados[9], dados_ajustados[0]), 
        (dados_ajustados[10], dados_ajustados[0]), (dados_ajustados[10], dados_ajustados[1]), (dados_ajustados[10], dados_ajustados[11]),
        (dados_ajustados[10], dados_ajustados[9]), (dados_ajustados[10], dados_ajustados[8]), 
        (dados_ajustados[11], dados_ajustados[0]), (dados_ajustados[11], dados_ajustados[1]), 
        (dados_ajustados[12], dados_ajustados[9]), (dados_ajustados[12], dados_ajustados[8]),
        (dados_ajustados[13], dados_ajustados[9]), (dados_ajustados[13], dados_ajustados[0]), (dados_ajustados[13], dados_ajustados[8]),
        (dados_ajustados[14], dados_ajustados[12]), (dados_ajustados[14], dados_ajustados[0]), (dados_ajustados[14], dados_ajustados[1]), (dados_ajustados[14], dados_ajustados[8])

        ]

        for dado in dados_coletados:
            grafo.add_node(dado)
            for ponto_origem, ponto_destino in conexoes:
                if dado == ponto_origem:
                    grafo.add_node(ponto_destino)
                    grafo.add_edge(ponto_origem, ponto_destino)
                    

        nivel_exposicao = (nx.number_of_edges(grafo) / 36) * 100
        
        nx.draw(grafo, with_labels=True, font_size=8, node_size=800, node_color='skyblue', font_color='black', font_weight='bold', arrowsize=20)
        plt.show()

        return f'O nivel de exposição é {nivel_exposicao:.1f}%.'
