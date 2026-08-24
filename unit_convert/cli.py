"""Command-line entrypoint for unit-convert."""

import argparse

from unit_convert.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    kg_to_pounds,
    miles_to_km,
    pounds_to_kg,
)

_CONVERSIONS = {
    "c2f": celsius_to_fahrenheit,
    "f2c": fahrenheit_to_celsius,
    "mi2km": miles_to_km,
    "km2mi": km_to_miles,
    "lb2kg": pounds_to_kg,
    "kg2lb": kg_to_pounds,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert between units.")
    parser.add_argument("conversion", choices=sorted(_CONVERSIONS))
    parser.add_argument("value", type=float)
    args = parser.parse_args()

    result = _CONVERSIONS[args.conversion](args.value)
    print(f"{args.value} -> {result:.2f}")


if __name__ == "__main__":
    main()
