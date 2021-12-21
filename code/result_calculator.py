"""
This module is used for the calculation according to parsed data like monthly data ,yearly data.
"""
import math


class ResultCalculator:
    """
        A class to represent a CalculationResult.
    """

    @staticmethod
    def filter_yearly_data(year: str, parsed_data: list) -> list:
        """
            Take the parsed_data and covert into yearly_data according to year
            ----------
            year: str
            parsed_data: list

            Returns
            -------
            list : yearly_data
        """
        yearly_data = [data for data in parsed_data if int(year) == data.date.year]
        return yearly_data

    @staticmethod
    def filter_monthly_data(year_month: str, parsed_data: list) -> list:
        """
            Take the parsed_data and covert into monthly_data according to year_month
            ----------
            year_month: str
            parsed_data: list

            Returns
            -------
           list: monthly_data
        """
        year, month = year_month.split('/')
        monthly_data = [data for data in parsed_data if int(month) == data.date.month and int(year) == data.date.year]
        return monthly_data

    @staticmethod
    def calculate_yearly_result(year: str, parsed_data: list) -> dict:
        """
           Calculate the yearly_result according to year
           ----------
           year: str
           parsed_data: list

           Returns
           -------
           yearly_result:dict
        """
        yearly_data = ResultCalculator.filter_yearly_data(year, parsed_data)
        yearly_data.sort(key=lambda obj: obj.date.month)
        yearly_result = {
            'highest_temp': max(yearly_data, key=lambda obj: obj.highest_temp),
            'lowest_temp': min(yearly_data, key=lambda obj: obj.lowest_temp),
            'humidity': max(yearly_data, key=lambda obj: obj.humidity)
        }
        return yearly_result

    @staticmethod
    def calculate_monthly_result(year_month: str, parsed_data: list) -> dict:
        """
            Calculate the monthly_result according to year_month
            ----------
            year_month: str
            parsed_data: list

            Returns
            -------
            monthly_result:dict
        """
        monthly_data = ResultCalculator.filter_monthly_data(year_month, parsed_data)
        highest_temp = [result_data.highest_temp for result_data in monthly_data]
        lowest_temp = [result_data.lowest_temp for result_data in monthly_data]
        mean_humidity = [result_data.mean_humidity for result_data in monthly_data]
        monthly_result = {
            "avg_highest_temp": math.ceil(sum(highest_temp) / len(highest_temp)),
            "avg_lowest_temp": math.ceil(sum(lowest_temp) / len(lowest_temp)),
            "avg_mean_humidity": math.ceil(sum(mean_humidity) / len(mean_humidity))
        }
        return monthly_result
