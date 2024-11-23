import random

class EightQueens:
    def __init__(self, size=8):
        self.size = size
        # Inicializa uma solução aleatória com uma rainha em cada coluna
        self.state = [random.randint(0, self.size - 1) for _ in range(self.size)]

    def get_attacks(self, state):
        """Calcula o número de ataques no tabuleiro."""
        attacks = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def get_neighbors(self, state):
        """Gera todos os vizinhos ao mover uma rainha em cada coluna."""
        neighbors = []
        for col in range(self.size):
            for row in range(self.size):
                if row != state[col]:  # Evita repetir o estado atual
                    new_state = state[:]
                    new_state[col] = row
                    neighbors.append(new_state)
        return neighbors

    def hill_climbing(self):
        """Implementa o método de Hill Climbing."""
        current_state = self.state
        current_attacks = self.get_attacks(current_state)

        while True:
            neighbors = self.get_neighbors(current_state)
            next_state = min(neighbors, key=self.get_attacks)
            next_attacks = self.get_attacks(next_state)

            # Verifica se o vizinho é melhor que o estado atual
            if next_attacks >= current_attacks:
                break  # Se não há melhora, sai do loop
            current_state, current_attacks = next_state, next_attacks

        return current_state, current_attacks

    def print_board(self, state):
        """Imprime o tabuleiro de forma legível."""
        for row in range(self.size):
            line = ""
            for col in range(self.size):
                if state[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

# Execução
eight_queens = EightQueens()
solution, attacks = eight_queens.hill_climbing()

print("Solução encontrada:")
eight_queens.print_board(solution)
print(f"Número de ataques na solução: {attacks}")
