from pysolsys import Sun, SolarSystem

class TestSolarSystem:

    def test_solar_system(self):
        rigil = Sun(mass=1.0788, radius=1.21, luminosity=1.5, name="Rigil Kentaurus")
        stelar_system = SolarSystem(sun=rigil, number_of_planets=3)

        assert len(stelar_system.planets) == 3
