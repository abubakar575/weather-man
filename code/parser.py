"""
This module is used to create the parsed data from the raw data filed.
"""

from datetime import datetime

from weather_data import WeatherData


class Parser:
    """
        A class to represent a Parser.
    """

    @staticmethod
    def parse_data(files_data: list) -> list:
        """
        Extracts all the required parsed data from the files_data

        Parameters
        ----------
        files_data: list

        Returns
        -------
        list : parsed_data
        """
        parsed_data = []
        if not files_data:
            print('Files data list is not available')
            return []

        for data in files_data:
            if data[1] and data[3] and data[7] and data[8]:
                weather_data = WeatherData(datetime.strptime(data[0], '%Y-%m-%d').date(),
                                           int(data[1]),
                                           int(data[3]),
                                           int(data[7]),
                                           int(data[8]))
                parsed_data.append(weather_data)
        return parsed_data
