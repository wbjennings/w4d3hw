from requests import get
from node import Node
from LinkedList import LinkedList

class Pokemon():
    
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.types = []
        self.weight = None
        self.image = None
        self.species_url = None
        self.evolve_chain = LinkedList()
        self.call_poke_api()
        self.pokes = []
        
    def call_poke_api(self):
        if isinstance(self.name, str) and self.name.isalpha():
            self.name = self.name.lower()
        response = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response.status_code == 200:
            print('Success')
            data = response.json()
            self.name = data['name']
            self.abilities = [ability_object['ability']['name'] for ability_object in data['abilities']]
            self.types = [type_object['type']['name'] for type_object in data['types']]
            self.weight = data['weight']
#             self.image = data['sprites']['front_defualt']
            self.image = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
            if not self.image:
                self.image = data['sprites']['front_default']
            self.species_url = data['species']['url']
        else:
            print(f'Error status code {response.status_code}')
            
    def get_evolution_chain(self):
        response = get(self.species_url)
        if response.status_code == 200:
            data = response.json()
        evolution_chain_url = data['evolution_chain']['url']
        evolution_chain = get(evolution_chain_url)
        if evolution_chain.status_code == 200:
            return evolution_chain.json()['chain']
    
    def add_evolve_chain(self):
        self.evolve_chain.add_node(self.name)
        if not self.species_url:
            return
        evolution_chain = self.get_evolution_chain()
        if not evolution_chain:
            return
        while True:
            if not evolution_chain['evolves_to']:
                break
            next_pokemon = evolution_chain['evolves_to'][0]['species']['name']
            self.evolve_chain.add_node(next_pokemon)
            evolution_chain = evolution_chain['evolves_to'][0]
            
    def evolve_pokemon(self, evolution_chain):
        if not evolution_chain['evolves_to']:
            print(f'This is the final from')
            return
        current_pokemon_in_chain = evolution_chain['species']['name']
        next_pokemon_in_chain = evolution_chain['evolves_to'][0]['species']['name']
        if current_pokemon_in_chain == self.name:
            self.name = next_pokemon_in_chain
            self.call_poke_api()
            return
        else:
            return self.evolve_pokemon(evolution_chain['evolves_to'][0])

pikachu = Pokemon('Pikachu')
pikachu.add_evolve_chain()
for node in pikachu.evolve_chain:
    print(node.value)