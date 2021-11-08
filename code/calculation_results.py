"""
This module is used for the calculation according to parsed data like monthly data ,yearly data.
"""
import math


class CalculationResult:
    """
        A class to represent a CalculationResult.
    """

    @staticmethod
    def get_yearly_data_list(year: str, parsed_data_list: list) -> list:
        """
            Take the parsed data list and covert into yearly_data_list
            ----------
            year: str
            parsed_data_list: list

            Returns
            -------
            list : yearly_data_list
        """
        if not parsed_data_list:
            print("Parsed data list is not available")
            return []

        yearly_data_list = [parse_data for parse_data in parsed_data_list if int(year) == parse_data.date.year]

        return yearly_data_list

    @staticmethod
    def get_monthly_data_list(year_month: str, parsed_data_list: list) -> list:
        """
            Take the parsed data list and covert into monthly_data_list
            ----------
            year_month: str
            parsed_data_list: list

            Returns
            -------
           list: monthly_data_list
        """
        if not parsed_data_list:
            print("Parsed data list is not available")
            return []
        year, month = year_month.split('/')
        monthly_data_list = [parse_data for parse_data in parsed_data_list
                             if int(month) == parse_data.date.month
                             and int(year) == parse_data.date.year]

        return monthly_data_list

    @staticmethod
    def calculate_yearly_result(year: str, parsed_data_list: list) -> tuple:  # Working on this
        """
            Calculate the yearly_result according to year
            ----------
            year: str
            parsed_data_list: list

            Returns
            -------
            tuple:  yearly_highest_temp, yearly_lowest_temp, yearly_humidity
        """
        yearly_data_list = CalculationResult.get_yearly_data_list(year, parsed_data_list)
        # Sort the data according to month from year
        yearly_data_list.sort(key=lambda obj: obj.date.month)

        yearly_highest_temp = max(yearly_data_list, key=lambda obj: obj.highest_temp)
        yearly_lowest_temp = min(yearly_data_list, key=lambda obj: obj.lowest_temp)
        yearly_humidity = max(yearly_data_list, key=lambda obj: obj.humidity)
        return yearly_highest_temp, yearly_lowest_temp, yearly_humidity

    @staticmethod
    def get_calculate_monthly_result(year_month: str, parsed_data_list: list) -> tuple:
        """
            Calculate the monthly_result according to year and month
            ----------
            year_month: str
            parsed_data_list: list

            Returns
            -------
            tuple:  avg_highest_temp, avg_lowest_temp, avg_mean_humidity
        """
        monthly_data_list = CalculationResult.get_monthly_data_list(year_month, parsed_data_list)

        highest_temp_list = [result_data.highest_temp for result_data in monthly_data_list]
        avg_highest_temp = sum(highest_temp_list) / len(highest_temp_list)
        lowest_temp_list = [result_data.lowest_temp for result_data in monthly_data_list]
        avg_lowest_temp = sum(lowest_temp_list) / len(lowest_temp_list)
        mean_humidity_list = [result_data.mean_humidity for result_data in monthly_data_list]
        avg_mean_humidity = sum(mean_humidity_list) / len(mean_humidity_list)

        return math.ceil(avg_highest_temp), math.ceil(avg_lowest_temp), math.ceil(avg_mean_humidity)
