import random

def swap_mutation(kromosom):
    kromosom = list(kromosom)
    posisi1, posisi2 = random.sample(range(len(kromosom)), 2)
    kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]
    return kromosom

if __name__ == "__main__":
    anak1 = [0, 1, 1, 0, 1]

    mutasi_anak1 = swap_mutation(anak1.copy())
    print("\nAnak Setelah Swap Mutation:")
    print(f"Anak 1 (Swap Mutation): {mutasi_anak1}")
