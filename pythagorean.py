def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit+1):
        for b in range(a, limit+1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets

upper_limit = int(input("Enter upper limit: "))

triplets = generate_pythagorean_triplets(upper_limit)
for triplet in triplets:
    print(" ".join(map(str, triplet)))
