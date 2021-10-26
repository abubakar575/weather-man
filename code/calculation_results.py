"""
This module is used for the calculation according to parsed data like
monthly data ,yearly data.
"""
import math

from parser import Parser


class CalculationResult:
    """
        A class to represent a CalculationResult.
        ...
        Attributes
        ----------
        parser : object
        result_data_list : list
            list of the required_data

    """

    def __init__(self):
        """
            Constructs all the necessary attributes for the CalculationResult
            object.
        """
        self.parser = Parser()
        self.parser.parse_data()
        self.result_data_list = []

    def get_calculate_yearly_result(self, yearly: str) -> list:
        """
            Calculate the required parsed data from according to year
            ----------
            yearly: str

            Returns
            -------
            list:  yearly_highest_temp, yearly_lowest_temp, yearly_humidity
        """
        if self.parser.is_parse_data_avail:
            self.result_data_list = [parse_data for parse_data in
                                     self.parser.parsed_data_list
                                     if yearly in parse_data.date]
            # Sort the data according to month from year
            self.result_data_list.sort(key=lambda obj: int(obj.date[5]))

            yearly_highest_temp = max(self.result_data_list,
                                      key=lambda obj: obj.highest_temp)
            yearly_lowest_temp = min(self.result_data_list,
                                     key=lambda obj: obj.lowest_temp)
            yearly_humidity = max(self.result_data_list,
                                  key=lambda obj: obj.humidity)
            self.result_data_list = []
            return [yearly_highest_temp, yearly_lowest_temp, yearly_humidity]
        else:
            print("Parsed data is not available")

    def get_calculate_monthly_result(self, monthly: str) -> list:
        """
            Calculate the required parsed data according to month
            ----------
            monthly: str

            Returns
            -------
            list:  avg_highest_temp, avg_lowest_temp, avg_mean_humidity
        """

        if self.parser.is_parse_data_avail:
            year, month = monthly.split('/')
            self.result_data_list = [parse_data for parse_data in
                                     self.parser.parsed_data_list
                                     if month in parse_data.date[5]
                                     and year in parse_data.date]

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
            self.result_data_list = []
            return [math.ceil(avg_highest_temp), math.ceil(avg_lowest_temp),
                    math.ceil(avg_mean_humidity)]
        else:
            print("Parsed data is not available")

    def calculate_horizontal_results(self, monthly: str) -> list:
        """
            Calculate the multiple horizontal_results from the parsed data
            according to month
            ----------
            monthly: str

            Returns
            -------
            list : result_data_list
        """
        if self.parser.is_parse_data_avail:
            year, month = monthly.split('/')
            self.result_data_list = [parse_data for parse_data in
                                     self.parser.parsed_data_list
                                     if month in parse_data.date[5]
                                     and year in parse_data.date]
            return self.result_data_list
        else:
            print("Parsed data is not available")
