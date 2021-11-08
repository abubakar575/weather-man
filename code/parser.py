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
    def parse_data(files_data_list: list) -> list:
        """
        Extracts all the required parsed data from the files_data_list

        Parameters
        ----------
        files_data_list: list

        Returns
        -------
        list : parsed_data_list
        """
        parsed_data_list = []
        if not files_data_list:
            print('Files data list is not available')
            return []

        for file_data in files_data_list:
            if file_data[1] and file_data[3] and file_data[7] and file_data[8]:
                weather_data = WeatherData(datetime.strptime(file_data[0], '%Y-%m-%d').date(),
                                           int(file_data[1]),
                                           int(file_data[3]),
                                           int(file_data[7]),
                                           int(file_data[8]))
                parsed_data_list.append(weather_data)
        return parsed_data_list
