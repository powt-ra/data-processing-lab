import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]

def aggregate(aggregation_key, aggregation_function, dict_list):
    return aggregation_function([item[aggregation_key] for item in dict_list])


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
avg_temp = aggregate("temperature", lambda temps: sum(float(t) for t in temps) / len(temps), cities)
print(avg_temp)
print()

# Print all cities in Germany
print("All cities in Germany:")
germany_cities = filter_items(lambda city: city['country'] == "Germany", cities)
for city in germany_cities:
    print(city["city"])
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
spain_hot_cities = filter_items(lambda city: city['country'] == "Spain" and float(city["temperature"]) > 12, cities)
for city in spain_hot_cities:
    print(f"{city['city']} with {city['temperature']}°C")
print()

# Count the number of unique countries
print("Number of unique countries:")
unique_countries_count = aggregate("country", lambda countries: len(set(countries)), cities)
print(unique_countries_count)
print()

# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany:")
germany_avg_temp = aggregate("temperature", lambda temps: sum(float(t) for t in temps) / len(temps), germany_cities)
print(germany_avg_temp)
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy:")
italy_cities = filter_items(lambda city: city['country'] == "Italy", cities)
italy_max_temp = aggregate("temperature", lambda temps: max(float(t) for t in temps), italy_cities)
print(italy_max_temp)