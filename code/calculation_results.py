from parser import Parser


class CalculationResult:

    def __init__(self):
        self.parser = Parser()
        self.result_data_list = []
        self.result_weather_data = []

    def get_calculate_yearly_result(self, yearly: str):
        parsed_data_list = self.parser.get_parse_data()
        for parse_data in parsed_data_list:
            if yearly in parse_data.date:
                self.result_data_list.append(parse_data)

        yearly_highest_temp = max(self.result_data_list,
                                  key=lambda obj: obj.highest_temp)

        yearly_lowest_temp = min(self.result_data_list,
                                 key=lambda obj: obj.lowest_temp)
        yearly_humidity = max(self.result_data_list,
                              key=lambda obj: obj.humidity)

        self.result_weather_data.append(yearly_highest_temp)
        self.result_weather_data.append(yearly_lowest_temp)
        self.result_weather_data.append(yearly_humidity)
        return self.result_weather_data

    def calculate_monthly_result(self):
        print('Monthly result')

    def calculate_multiple_result(self):
        print('All result')

    def calculate_horizontal_results(self):
        print('Charts result')

    def calculate_horizontal_result(self):
        print('Chart result')
