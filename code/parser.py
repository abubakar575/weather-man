from file_handler import FileHandler
from weather_data import WeatherData


class Parser:

    def __init__(self):
        self.file_handler = FileHandler()
        self.parsed_data = []

    def get_parse_data(self):
        files_data_list = self.file_handler.get_files_data_list()
        for file_data in files_data_list:
            if file_data[1] and file_data[3] and file_data[7] and file_data[8]:
                weather_data = WeatherData(file_data[0], int(file_data[1]),
                                           int(file_data[3]),
                                           int(file_data[7]),
                                           int(file_data[8]))
                self.parsed_data.append(weather_data)
                # print(type(file_data[0]), type(file_data[1]),
                #       type(file_data[3]), type(file_data[7]),
                #       type(file_data[8]))

        # print(len(self.parsed_data))
        return self.parsed_data
