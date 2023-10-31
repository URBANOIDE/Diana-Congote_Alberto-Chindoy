#astar: algoritmo de busqueda utilizando la funcion heuristica de distancia en el estado actual y estado objetivo

from simpleai.search import astar, SearchProblem

#estado objetivo y estado inicial

GOAL = '''e-1-2
3-4-5
6-7-8'''

INITIAL = '''7-2-4
5-3-6
8-e-1'''

#convierte una lista de listas en una cadena de texto con salto de linea
def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

#convierte una cadena de texto con salto de linea en una lista de listas
def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]

#devuelve la posicion de un elemento en forma de tupla (0,0)
def find_location(rows, element_to_find):
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


#almacena la posicion final de cada elemento
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in 'e12345678':
    goal_positions[number] = find_location(rows_goal, number)


class EigthPuzzleProblem(SearchProblem):
    #identificar las acciones posibles del problema
    def actions(self, state):
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')

        actions = []
        if row_e > 0:
            actions.append(rows[row_e - 1][col_e])
        if row_e < 2:
            actions.append(rows[row_e + 1][col_e])
        if col_e > 0:
            actions.append(rows[row_e][col_e - 1])
        if col_e < 2:
            actions.append(rows[row_e][col_e + 1])

        return actions

    def result(self, state, action):
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')
        row_n, col_n = find_location(rows, action)

        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]

        return list_to_string(rows)

    def is_goal(self, state):
        return state == GOAL
     
    def heuristic(self, state):
        rows = string_to_list(state)

        distance = 0

        for number in 'e12345678':
            row_n, col_n = find_location(rows, number)
            row_n_goal, col_n_goal = goal_positions[number]

            distance += abs(row_n - row_n_goal) + abs(col_n - col_n_goal)
        return distance
        


result = astar(EigthPuzzleProblem(INITIAL))


for action, state in result.path():
    print('Mover el numero ', action)
    print(state)