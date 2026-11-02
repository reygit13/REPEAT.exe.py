class parrot:
    species = "Spix's Macaw"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blue = parrot("blue", 16)
wood = parrot("wood", 13)

print(blue.name, "is a", blue.species, "and is", blue.age, "years old.")
print(wood.name, "is a", wood.species, "and is", wood.age, "years old.")