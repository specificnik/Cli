grades = [90, 85, 74]
prices = [12.99, 9.99, 5.49, 7.50]
print(sum(grades) / len(grades))
print(sum(prices) / len(prices))


def average(numbers):
    return sum(numbers) / len(numbers)


print(average(grades))
print(average(prices))

address = "3022 Broadway, New York, NY 10027, USA"
city = address.split(", ")[1]
print(city)


def get_city(address):
    return address.split(", ")[1]


print(get_city(address))
