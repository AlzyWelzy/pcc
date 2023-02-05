class Restaurant:
    def __init__(
        self,
        name,
        cuisine,
    ):
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"The Restaurant name is {self.name} and it's famous for its {self.cuisine} cuisine."
        )

    def increment_number_served(self, number):
        self.number_served += number

    def set_number_served(self, number):
        self.number_served = number


restaurant = Restaurant("Jannaks", "North Indian")
restaurant.describe_restaurant()

print(restaurant.number_served)

restaurant.number_served = 10

print(restaurant.number_served)


restaurant.increment_number_served(10)

print(restaurant.number_served)
