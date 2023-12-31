class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = f'{self.name} {other_country.name}'
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

# Example usage:
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)  # Output: 15,000,000
print(bosnia_herzegovina.name)  # Output: 'Bosnia Herzegovina'



class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        if isinstance(other_country, Country):
            combined_name = f'{self.name} {other_country.name}'
            combined_population = self.population + other_country.population
            return Country(combined_name, combined_population)
        else:
            raise ValueError("Unsupported operand types for +: 'Country' and non-Country")

# Example usage:
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)  # Output: 15,000,000
print(bosnia_herzegovina.name)  # Output: 'Bosnia Herzegovina'



class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        return self.speed

# Example usage:
my_car = Car('Toyota', 'Camry', 2022)

my_car.accelerate()  # Increase speed by 5
print(my_car.display_speed())  # Output: 5

my_car.brake()  # Decrease speed by 5
print(my_car.display_speed())  # Output: 0

my_car.accelerate()  # Increase speed by 5
print(my_car.display_speed())  # Output: 5
