from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        car = self.__create_car(car_type, model, speed_limit)

        if car:
            if self._is_car_model_in_cars_data(model):
                raise Exception(f"Car {model} is already created!")
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if self._is_driver_in_driver_data(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if self._is_race_name_in_race_data(race_name):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self._get_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        found_car = self._get_free_car_by_type(car_type)
        if not found_car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_car = driver.car
            new_car = found_car
            found_car.is_taken = True
            old_car.is_taken = False
            driver.car = new_car
            return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."
        else:
            driver.car = found_car
            found_car.is_taken = True
            return f"Driver {driver_name} chose the car {found_car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self._get_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self._get_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self._get_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted([d for d in self.drivers], key=lambda d: -d.car.speed_limit)[0:3]

        result = ""
        for winner in winners:
            winner.number_of_wins += 1
            result += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n"

        return result.strip()

    @staticmethod
    def __create_car(car_type, model, speed_limit):
        if car_type == "MuscleCar":
            return MuscleCar(model, speed_limit)
        if car_type == "SportsCar":
            return SportsCar(model, speed_limit)
        return None




    def _get_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def _get_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return None



    def _get_free_car_by_type(self, car_type):
        cars = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        if cars:
            return cars[-1]
        return None

    def _is_car_model_in_cars_data(self, model):
        return model in [c.model for c in self.cars]

    def _is_driver_in_driver_data(self, driver_name):
        return driver_name in [d.name for d in self.drivers]

    def _is_race_name_in_race_data(self, race_name):
        return race_name in [r.name for r in self.races]
