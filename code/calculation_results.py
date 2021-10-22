from parser import Parser


class CalculationResult:

    def __init__(self):
        self.parser = Parser()
        self.result_date = []

    def calculate_yearly_result(self):
        parsed_data_list = self.parser.get_parse_data()
        # i = 0
        # for parse_data in parsed_data_list:
        #     print(f'{i}', parse_data.date, parse_data.highest_temp,
        #           parse_data.lowest_temp, parse_data.humidity)
        #     i += 1

        print('Yearly result', parsed_data_list)

    def calculate_monthly_result(self):
        print('Monthly result')

    def calculate_multiple_result(self):
        print('All result')

    def calculate_horizontal_results(self):
        print('Charts result')

    def calculate_horizontal_result(self):
        print('Chart result')
