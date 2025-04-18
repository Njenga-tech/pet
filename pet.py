import time
import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 3  # 0 = full, 10 = very hungry
        self.happiness = 3
        self.energy = 3  # 0 = tired, 10 = full rested
        self.age = 0
        self.alive = True

    def feed(self, amount):
        if self.alive:
            self.hunger -= amount
            self.happiness += 1
            if self.hunger < 0:
                self.hunger = 0

    def sleep(self, seconds):
        if self.alive:
            print(f"{self.name} is sleeping...")
            time.sleep(1)
            self.energy += 5
            self.happiness += 2
            self.hunger += 2
            if self.energy > 10:
                self.energy = 10

    def play(self, seconds):
        if self.alive:
            print(f"{self.name} is playing...")
            time.sleep(1)
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1

    def status(self):
        if self.alive:
            print("\n.......Pet Status.......")
            print(f"Name: {self.name}")
            print(f"Hunger: {self.hunger}/10")
            print(f"Happiness: {self.happiness}/10")
            print(f"Energy: {self.energy}/10")

def main():
    name = input("Name your pet: ")
    pet1 = Pet(name)

    while pet1.alive:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Check status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            food = int(input("How much food do you want to give? "))
            pet1.feed(food)

        elif choice == "2":
            seconds = int(input("How long do you want to sleep (seconds)? "))
            pet1.sleep(seconds)

        elif choice == "3":
            seconds = int(input("How long do you want to play (seconds)? "))
            pet1.play(seconds)

        elif choice == "4":
            pet1.status()

        elif choice == "5":
            print("Thanks for playing! Goodbye.")
            break  

        else:
            print("Invalid choice, try again.")

    print(f"{pet1.name} is no longer alive. Game over 😢")

if __name__ == "__main__":
    main()
