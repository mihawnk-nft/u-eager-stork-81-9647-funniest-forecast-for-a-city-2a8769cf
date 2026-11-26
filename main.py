#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes one original, funny weather-forecast line for the invented city
of Wobbleton to /output/entry.txt. Pure Python standard library, no
network, no external files, deterministic output.
"""

import os

FORECAST = (
    "Tomorrow in Wobbleton: heavy rain of left socks, 18\xb0C, "
    "winds 40 km/h - umbrellas useless, laundry baffled."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
