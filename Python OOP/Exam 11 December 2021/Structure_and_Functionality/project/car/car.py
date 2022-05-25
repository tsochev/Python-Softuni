from abc import ABC, abstractmethod


class Car(ABC):
    _MIN_SPEED_LIMIT = 0
    _MAX_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False


    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        #if self.min_speed_limit > value > self.max_speed_limit:
        if value not in range(self._MIN_SPEED_LIMIT, self._MAX_SPEED_LIMIT + 1):
            raise ValueError(f"Invalid speed limit! Must be between {self._MIN_SPEED_LIMIT} and {self._MAX_SPEED_LIMIT}!")
        self.__speed_limit = value
