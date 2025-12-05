from enumerate import seperator

cities = ["Graz", "Belgrade", "Warsaw", "Berlin"]
for index, city in enumerate(cities[:-1]):
    print(f"{city} -> {cities[index + 1]}")

seperator()

from itertools import pairwise

for city, next_city in pairwise(cities):
    print(f"{city} -> {next_city}")