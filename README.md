# Solar System Generator

This is a Python-package which generates a 2D solar (or rather stelar) system consisting of one sun and a user-defined number of planets orbiting around the sun in circular orbits. See the full project description [here](https://sites.google.com/view/python3-umk/projects#h.6plj5vogra3y).

![Solar system](solar_system.png)

The feature is not implemented yet, but eventually, the Python package will be able to determine the period of rotation of the planets around the star using Kepler's third law:

```math
T^2  = \big( \frac{4\pi^2}{GM} \big) r^3
```

In other words, $T^2 \propto r^3$. Here, $T$ is the orbital period, $G$ is the gravitational constant, $M$ is the mass of the star and $r$ is distance between the planet and the star (considering circular orbits).

## Installation instructions
Clone the repository:

```bash
git clone https://github.com/iubr/solar-system-generator.git
cd solar-system-generator
pip install .
```

## How to run
See an example Jupyter notebook in [examples](https://github.com/iubr/solar-system-generator/tree/main/examples).

## Other useful information
This project is part of the [Python3 - 7404-FIZ-KKP](https://sites.google.com/view/python3-umk/home) course at UMK.
