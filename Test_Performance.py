import time

def performance_test():
    num_tests = 10
    success_count = 0
    total_time = 0
    for i in range(num_tests):
        start_time = time.time()
        eight_queens = EightQueens()
        solution, attacks = eight_queens.hill_climbing()
        end_time = time.time()

        duration = end_time - start_time
        total_time += duration

        if attacks == 0:
            success_count += 1
            print(f"Teste {i + 1}: Solução encontrada em {duration:.4f} segundos")
        else:
            print(f"Teste {i + 1}: Ótimo local encontrado em {duration:.4f} segundos com {attacks} ataques restantes")

    print("\nResumo:")
    print(f"Soluções bem-sucedidas: {success_count}/{num_tests}")
    print(f"Tempo médio de execução: {total_time / num_tests:.4f} segundos")

# Executar o teste de performance
performance_test()
