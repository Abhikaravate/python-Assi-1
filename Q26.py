# Define facts
class KnowledgeBase:
    def __init__(self):
        self.food = {"apple", "mango"}  # Apple and Mango are Food
        self.likes = {"Ravi": "Food"}  # Ravi likes all kinds of Food
        self.eats = {}
        self.alive = {}

    # Add food logic: Anything anyone eats and is not killed is Food
    def add_food_if_eaten_and_not_killed(self, person, item, killed=False):
        if not killed:
            self.food.add(item)
            self.eats[person] = item
            self.alive[person] = True

    # Add eating logic
    def add_eating(self, person, item):
        self.eats[person] = item
        if person not in self.alive:
            self.alive[person] = True

    # Logic for Soham eats anything Vijay eats
    def add_soham_logic(self, vijay_eat):
        self.eats["Soham"] = vijay_eat

# Initialize knowledge base
kb = KnowledgeBase()

# i) Ravi likes all kinds of Food (already defined in 'likes')
# ii) Apple and Mango are Food (already defined in 'food')

# iii) Anything anyone eats and is not killed is a Food
kb.add_food_if_eaten_and_not_killed("Vijay", "peanuts", killed=False)

# iv) Vijay eats peanuts and is still alive
kb.add_eating("Vijay", "peanuts")

# v) Soham eats anything that Vijay eats
kb.add_soham_logic(kb.eats["Vijay"])

# Output the knowledge base
print("Food items:", kb.food)
print("Who eats what:", kb.eats)
print("Is Alive:", kb.alive)
