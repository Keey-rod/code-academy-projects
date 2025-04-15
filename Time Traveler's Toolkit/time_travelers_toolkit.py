import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

#current date and time
current_date = dt.date.today()
current_time = dt.datetime.now().time()
print(f"Current Date: {current_date}, Current Time: {current_time}")

#generate random year for time travel
try:
    year = randint(0, 3500)
except ValueError as e:
    print("Error generating year:", e)

#function to calculate time travel cost
def calculate_cost(base_cost, annual_rate, current_year, target_year):
    year_difference = abs(target_year - current_year)
    cost_multiplier = Decimal(annual_rate * year_difference)
    return (base_cost * cost_multiplier).quantize(Decimal('0.00'))

cost = calculate_cost(Decimal('150.00'), 0.02, dt.datetime.now().year, year)

possible_destination = ['Swiss Alps', 'Bora, Bora', 'Rome', 'Macchu Pichu', 'Tokyo', 'Maui', 'Maldives', 'Tanzania', 'Petra', 'Glacier National Park', 'South Island, New Zealand', 'Paris', 'Costa Rica', 'Yellowstone National Park', 'London, England', 'Grand Canyon National Park', 'Banff', 'Amsterdam', 'Turks & Caicos', 'Jamaica', 'Victoria Falls', 'Mauritius', 'Zanzibar', 'Palawan', 'Mount Fuji', 'Bhutan']
destination = choice(possible_destination)

print(custom_module.generate_time_travel_message(year, destination, cost))