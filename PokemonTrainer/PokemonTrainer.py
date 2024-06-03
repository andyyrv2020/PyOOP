class Pokemon:
    def __init__(self, name, element, health):
        self.name = name
        self.element = element
        self.health = health

class Trainer:
    def __init__(self, name):
        self.name = name
        self.badges = 0
        self.pokemons = []

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def check_element(self, element):
        return any(pokemon.element == element for pokemon in self.pokemons)

    def apply_damage(self):
        self.pokemons = [pokemon for pokemon in self.pokemons if pokemon.health > 0]

    def __str__(self):
        return f"{self.name} {self.badges} {len(self.pokemons)}"

def main():
    trainers = {}

    while True:
        command = input()
        if command == "Tournament":
            break
        name, pokemon_name, element, health = command.split()
        if name not in trainers:
            trainers[name] = Trainer(name)
        trainers[name].add_pokemon(Pokemon(pokemon_name, element, int(health)))

    while True:
        element = input()
        if element == "End":
            break
        for trainer in trainers.values():
            if trainer.check_element(element):
                trainer.badges += 1
            else:
                for pokemon in trainer.pokemons:
                    pokemon.health -= 10
                trainer.apply_damage()

    for trainer in sorted(trainers.values(), key=lambda x: (-x.badges, x.name)):
        print(trainer)

if __name__ == "__main__":
    main()

