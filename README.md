# unit-convert

A tiny command-line unit converter. Supports temperature, length, and weight
conversions.

## Install

```bash
pip install -e .
```

## Usage

```bash
unit-convert c2f 100      # 100.0 -> 212.00
unit-convert f2c 32       # 32.0 -> 0.00
unit-convert mi2km 26.2   # 26.2 -> 42.16
unit-convert kg2lb 70     # 70.0 -> 154.32
```

Run `unit-convert --help` for the full list of supported conversions.
