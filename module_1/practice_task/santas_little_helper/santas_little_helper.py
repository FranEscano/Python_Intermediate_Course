def toy_maker(num):
    while True:
        yield f"Toy {num} made"
        num +=1

santas_toys = toy_maker(1)

print(next(santas_toys))
print(next(santas_toys))
print(next(santas_toys))
print(next(santas_toys))
print(next(santas_toys))