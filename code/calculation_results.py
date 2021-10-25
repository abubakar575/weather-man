import math

from parser import Parser


class CalculationResult:

    def __init__(self):
        self.parser = Parser()
        self.result_data_list = []

    def get_calculate_yearly_result(self, yearly: str):
        parsed_data_list = self.parser.get_parse_data()
        for parse_data in parsed_data_list:
            if yearly in parse_data.date:
                self.result_data_list.append(parse_data)

        self.result_data_list.sort(key=lambda obj: int(obj.date[5]))

        yearly_highest_temp = max(self.result_data_list,
                                  key=lambda obj: obj.highest_temp)
        yearly_lowest_temp = min(self.result_data_list,
                                 key=lambda obj: obj.lowest_temp)
        yearly_humidity = max(self.result_data_list,
                              key=lambda obj: obj.humidity)

        return [yearly_highest_temp, yearly_lowest_temp, yearly_humidity]

    def get_calculate_monthly_result(self, monthly: str):
        year, month = monthly.split('/')
        parsed_data_list = self.parser.get_parse_data()
        for parse_data in parsed_data_list:
            if month in parse_data.date[5] and year in parse_data.date:
                self.result_data_list.append(parse_data)

        highest_temp_list = [result_data.highest_temp for result_data in
                             self.result_data_list]
        avg_highest_temp = sum(highest_temp_list) / len(
            highest_temp_list)
        lowest_temp_list = [result_data.lowest_temp for result_data in
                            self.result_data_list]
        avg_lowest_temp = sum(lowest_temp_list) / len(
            lowest_temp_list)

        mean_humidity_list = [result_data.mean_humidity for result_data in
                              self.result_data_list]
        avg_mean_humidity = sum(mean_humidity_list) / len(
            mean_humidity_list)

        return [math.ceil(avg_highest_temp), math.ceil(avg_lowest_temp),
                math.ceil(avg_mean_humidity)]

    def get_calculate_horizontal_results(self, monthly: str):
        year, month = monthly.split('/')
        parsed_data_list = self.parser.get_parse_data()
        for parse_data in parsed_data_list:
            if month in parse_data.date[5] and year in parse_data.date:
                self.result_data_list.append(parse_data)
        return self.result_data_list

    def get_calculate_multiple_result(self):
        print('All result')

    def calculate_horizontal_result(self):
        print('Chart result')
