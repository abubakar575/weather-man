"""
This module is used in parser class when we get the raw_file data then this
module helps to map the readings data structure with correct data types
"""


class WeatherData:
    """
    A class to represent a WeatherData.
    ...
    Attributes
    ----------
    date : str
        date of the weather
    highest_temp : int
        highest temperature of the weather
    lowest_temp : int
        lowest temperature of the weather
    humidity : int
        humidity of the weather

    """

    def __init__(self, date, highest_temp, lowest_temp, humidity):
        """
        Constructs all the necessary attributes for the weather object.
        """
        self.date = date
        self.highest_temp = highest_temp
        self.lowest_temp = lowest_temp
        self.humidity = humidity
