from unit_convert.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    kg_to_pounds,
    miles_to_km,
    pounds_to_kg,
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(-40) == -40


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0


def test_miles_km_round_trip():
    assert round(km_to_miles(miles_to_km(10)), 4) == 10


def test_pounds_kg_round_trip():
    assert round(kg_to_pounds(pounds_to_kg(10)), 4) == 10
