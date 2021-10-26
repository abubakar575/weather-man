"""
This module is used to create the parsed data from the raw data filed.
"""

from file_handler import FileHandler
from weather_data import WeatherData


class Parser:
    """
        A class to represent a Parser.
        ...
        Attributes
        ----------
        file_handler : object
        parsed_data_list : list
            list of the parsed_data

    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Parser object.
        """
        self.file_handler = FileHandler()
        self.file_handler.read_files_data_list()
        self.parsed_data_list = []
        self.is_parse_data_avail = False

    def parse_data(self):
        """
        Extracts all the required parsed data from the raw files_list

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.file_handler.is_files_data_avail:
            for file_data in self.file_handler.files_data_list:
                if file_data[1] and file_data[3] and file_data[7] and \
                        file_data[8]:
                    weather_data = WeatherData(file_data[0], int(file_data[1]),
                                               int(file_data[3]),
                                               int(file_data[7]),
                                               int(file_data[8]))
                    self.parsed_data_list.append(weather_data)
            self.is_parse_data_avail = True
        else:
            print('Files data is not available')
