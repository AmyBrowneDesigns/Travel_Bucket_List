import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

#seeding connect repo and database


# city_repository.delete_all()
# country_repository.delete_all()

country1 = Country("Singapore")
country_repository.save(country1)
country2 = Country("UAE")
country_repository.save(country2)
country3 = Country("Argentina")
country_repository.save(country3)
country4 = Country("China")
country_repository.save(country4)

# country_repository.select_all()

city1 = City("Singapore", country1, False)
city_repository.save(city1)
city2 = City(" Abu Dhabi", country2, False)
city_repository.save(city2)
city3 = City("Buenos Aires", country3,False)
city_repository.save(city3)
city4 = City("Shangai", country4, False)
city_repository.save(city4)
city5 = City("Dubai", country2, False)
city_repository.save(city5)
city6 = City("Beijing", country4, False)
city_repository.save(city6)
city7 = City("Sharjah", country2, False)
city_repository.save(city7)

# city_repository.select_all()

pdb.set_trace()