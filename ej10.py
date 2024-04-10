from generate_stats import *
from top_scorer import *
from most_influential import *

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]


stats = generate_stats(names, goals, goals_avoided, assists)
print(stats)

top_scorer = top_scorer(stats)
print(f'El/la goleador/a de la temporada fue {top_scorer[0]} con {top_scorer[1]} goles.')

most_influential = most_influential(stats)
print(f'El/la jugador/a más influyente fue {most_influential}.')

goals_average = lambda: sum(goals) / 25
print(f'El promedio de goles por partido en la temporada fue de {goals_average()}.')

average_topscorer = lambda: top_scorer[1] / 25
print(f'El promedio de goles por partido por parte de {top_scorer[0]} fue de {average_topscorer()}.')