travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above 
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
def add_new_country(country_visited, times_visited, city_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = city_visited
    travel_log.append(new_country)

#🚨 Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)