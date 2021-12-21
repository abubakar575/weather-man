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
    def populate_parse_data(files_data: list) -> list:
        """
        Populate all the required parsed data from the files_data

        Parameters
        ----------
        files_data: list

        Returns
        -------
        list : parsed_data
        """
        parsed_data = []

        for data in files_data:
            if data.get('date') and data.get('highest_temp') and data.get('lowest_temp') \
                    and data.get('highest_humidity') and data.get('mean_humidity'):
                weather_data = WeatherData(datetime.strptime(data.get('date'), '%Y-%m-%d').date(),
                                           int(data.get('highest_temp')),
                                           int(data.get('lowest_temp')),
                                           int(data.get('highest_humidity')),
                                           int(data.get('mean_humidity')))
                parsed_data.append(weather_data)

        return parsed_data
