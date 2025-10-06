from collections import deque

# Definição dos processos (id, tempo de execução)
processos = deque([
    ["P1", 5],
    ["P2", 7],
    ["P3", 3]
])

quantum = 2

print("Simulação Round Robin:\n")

while processos:
    processo = processos.popleft()
    id_proc, tempo_restante = processo

    if tempo_restante > quantum:
        tempo_restante -= quantum
        print(f"{id_proc} executou {quantum} unidades (restam {tempo_restante})")
        processos.append([id_proc, tempo_restante])
    else:
        print(f"{id_proc} executou {tempo_restante} unidades (restam 0)")

print("\nTodos os processos foram concluídos!")
