import matplotlib.pyplot as plt
import time


def calculate_time(name, func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    process_time = end_time - start_time
    print(f"Tempo de processamento para {name}: {process_time:.6f} segundos")
    return process_time, result


def crivo_eratostenes(n: int) -> list[int]:
    # Initialize a boolean list assuming all numbers are prime
    # Indices 0 and 1 are not prime
    is_prime = [False, False] + [True] * (n - 1)

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark all multiples of p, starting from p*p, as not prime
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    # Return only the numbers marked as prime
    return [i for i, prime in enumerate(is_prime) if prime]


def plot_comparer_process_time(case1, case2, case3, case4):
    tempos = [case1[0], case2[0], case3[0], case4[0]]
    casos = ["10^5", "10^6", "10^7", "10^8"]

    plt.plot(casos, tempos, marker="o")
    plt.title("Comparação de Tempo de Processamento")
    plt.xlabel("Casos")
    plt.ylabel("Tempo (segundos)")
    plt.grid(True)
    plt.show()


# Exemplo de uso
CASE_1 = calculate_time("CASE 1", crivo_eratostenes, 10**5)
CASE_2 = calculate_time("CASE 2", crivo_eratostenes, 10**6)
CASE_3 = calculate_time("CASE 3", crivo_eratostenes, 10**7)
CASE_4 = calculate_time("CASE 3", crivo_eratostenes, 10**8)

plot_comparer_process_time(CASE_1, CASE_2, CASE_3, CASE_4)
