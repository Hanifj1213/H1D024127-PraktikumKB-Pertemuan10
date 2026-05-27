import random

def two_point_crossover(parent1, parent2):
    titik1 = random.randint(1, len(parent1)-2)
    titik2 = random.randint(titik1+1, len(parent1)-1)
    anak1 = parent1[:titik1] + parent2[titik1:titik2] + parent1[titik2:]
    anak2 = parent2[:titik1] + parent1[titik1:titik2] + parent2[titik2:]
    return anak1, anak2

if __name__ == "__main__":
    parent1 = [1, 0, 1, 1, 0]
    parent2 = [0, 1, 0, 0, 1]

    anak1, anak2 = two_point_crossover(parent1, parent2)
    print("\nAnak Hasil Two-Point Crossover:")
    print(f"Anak 1: {anak1}")
    print(f"Anak 2: {anak2}")
