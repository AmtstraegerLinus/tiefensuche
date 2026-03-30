matrix = [
#   A  B  C  D  E  F
    [0, 1, 1, 0, 0, 0],  # A (0)
    [0, 0, 0, 1, 1, 0],  # B (1)
    [0, 0, 0, 0, 0, 1],  # C (2)
    [0, 0, 0, 0, 0, 0],  # D (3)
    [0, 0, 0, 0, 0, 0],  # E (4)
    [0, 0, 0, 0, 0, 0],  # F (5)
]

namen = ["A", "B", "C", "D", "E", "F"]
knoten = []

def dfs(matrix, start_knoten, gesuchter_knoten, besucht=None):
    if besucht is None:
        besucht = set()

    besucht.add(start_knoten)
    knoten.append(namen[start_knoten])

    #print(start_knoten, gesuchter_knoten)
    if start_knoten == gesuchter_knoten:
        print("Knoten", namen[start_knoten], "wurde im Baum gefunden")
        return

    for nachbar in range(len(matrix[start_knoten])):
        if matrix[start_knoten][nachbar] == 1 and nachbar not in besucht:
            dfs(matrix, nachbar, gesuchter_knoten, besucht)


dfs(matrix, 0, 3)
# Ausgabe: A B D E C F

print(knoten)
