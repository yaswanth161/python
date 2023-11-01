def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets

limit = int(input("Enter the limit: "))
triplets = generate_pythagorean_triplets(limit)
print("Pythagorean Triplets:")
for triplet in triplets:
    print(triplet)
