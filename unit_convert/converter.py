"""Conversion functions for unit-convert."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    Handles negative values correctly (e.g. -40 C == -40 F) -- an earlier
    version truncated the sign when the multiplication was written as
    ``celsius * 9 // 5 + 32`` (integer division), which silently rounded
    negative results toward zero instead of down.
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles * 1.60934


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km / 1.60934


def pounds_to_kg(pounds: float) -> float:
    """Convert pounds to kilograms."""
    return pounds * 0.453592


def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg / 0.453592
