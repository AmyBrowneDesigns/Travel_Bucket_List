from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.city_repository as city_repository


def save(city):
    sql = "INSERT INTO city (name, visited, country_id) VALUES ( %s, %s,%s) RETURNING *"
    vakues = [city.name, city.visited, city.country.id]
    results = run_sql(sql, values)
    id - results[0]['id']
    city.id = id
    return city


def select_all():
    city = []

    sql = "SELECT * FROM city"
    results = run_sql(sql)

    for row in results:
        countries = country_repository.select(row['country_id'])
        city = City(row['name'], row["visited"], row['id'])
        cities.append(city)
        return cities

    def select(id):
        city = None
        sql = "SELECT * FROM city WHER id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            country = country_repository.select(result['user_id'])
            city = City(result['name'], result['visited'], result['id'])
        return city




    def delete_all():
        sql = "DELETE FROM city"
        run_sql(sql)


    def delete(id):
        sql = "DELETE from city WHERE id = %s"
        values = [id]
        run_sql(sql, values)

    def update(city):
        sql = "UPDATE city SET(name, visited) = (%s, %s) WHERE id = %s"
        values = [city.name, city.visited, city.id]
        print (values)
        run_sql(sql, values)