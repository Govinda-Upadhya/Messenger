import random
import string

class UniqueNameGenerator:
    def __init__(self):
        self.existing_names = set()

    def generate_random_name(self, length=20):
        characters = string.ascii_letters + string.digits
        name = ''.join(random.choice(characters) for _ in range(length))
        return name

    def generate_unique_random_name(self, length=20):
        while True:
            name = self.generate_random_name(length)
            if name not in self.existing_names:
                self.existing_names.add(name)
                return name

# Example usage:
if __name__ == "__main__":
    name_generator = UniqueNameGenerator()
    for _ in range(10):
        print(name_generator.generate_unique_random_name())
