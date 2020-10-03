from db.run_sql import run_sql

from models.country import Country
from models.city import City


def save(country):
    sql = "INSERT INTO country(name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    country = []

    sql = "SELECT * FROM country"
    results = run_sql(sql)

    for rown in results:
        country = Country(row ['name'], row ['id'])
        country.append(country)
    return country