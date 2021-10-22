from file_handler import FileHandler


class Parser:

    def __init__(self):
        self.file_handler = FileHandler()
        self.parsed_data = []

    def get_parse_data(self):
        print('Parser1', len(self.file_handler.get_files_data_list()))
        # read_files_list = self.file_handler.get_read_files()
        # i = 1
        # print(f'file {i}', file)
        # i += 1
        # for file in read_files_list:
        #     weather_data = WeatherData(file[0], file[1], file[2], file[3])
        #     self.parsed_data.append(weather_data)

        return self.parsed_data
