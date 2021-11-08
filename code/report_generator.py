"""
This module is used for printing the calculated data like monthly data ,
yearly data,horizontal bar charts.
"""
import calendar

from sty import fg


class ReportGenerator:
    """
        A class to represent a CalculationResult.
    """

    @staticmethod
    def generate_yearly_report(yearly_highest_temp: object, yearly_lowest_temp: object, yearly_humidity: object):
        """
            Generate the yearly report 
            ----------
            yearly_highest_temp: object
            yearly_lowest_temp: object
            yearly_humidity: object

            Returns
            -------
            none
        """

        print(fg.green + 'Yearly Report:' + fg.white)
        print(f'Highest: {yearly_highest_temp.highest_temp}C on '
              f'{yearly_highest_temp.date.day} '
              f'{calendar.month_name[yearly_highest_temp.date.month]}')
        print(f'Lowest: {yearly_lowest_temp.lowest_temp}C on '
              f'{yearly_lowest_temp.date.day} '
              f'{calendar.month_name[yearly_lowest_temp.date.month]}')
        print(f'Humidity: {yearly_humidity.humidity}% on '
              f'{yearly_humidity.date.month} '
              f'{calendar.month_name[yearly_humidity.date.month]}')

    @staticmethod
    def generate_monthly_report(avg_highest_temp: int, avg_lowest_temp: int, avg_mean_humidity: int):
        """
            Generate the monthly report
            ----------
            avg_highest_temp: int
            avg_lowest_temp: int
            avg_mean_humidity: int

            Returns
            -------
            none
        """
        print(fg.green + 'Monthly Report:' + fg.white)
        print(f'Highest Average: {avg_highest_temp}C ')
        print(f'Lowest Average: {avg_lowest_temp}C ')
        print(f'Average Mean Humidity: {avg_mean_humidity}%')

    @staticmethod
    def generate_combine_monthly_chart(monthly_data_list: list):
        """¬
            Generate the single line monthly horizontal_bar_chart according to temperature value
            ----------
            monthly_data_list: list

            Returns
            -------
            none
        """
        print(fg.green + 'Monthly Single Horizontal Bar Chart:' + fg.white)
        print(f' Date: {calendar.month_name[monthly_data_list[0].date.month]} {monthly_data_list[0].date.year}')
        for index, data in enumerate(monthly_data_list, 0):
            print(f' {fg.white} {index + 1:02d} : {fg.blue} '
                  f' {"+" * data.lowest_temp}'
                  f' {fg.red}  {"+" * data.highest_temp}'
                  f' {fg.blue} {data.lowest_temp}C -{fg.red}'
                  f' {data.highest_temp}C')

    @staticmethod
    def generate_multiple_monthly_chart(monthly_data_list: list):
        """
            Generate the multiple line monthly horizontal_bar_chart according to temperature value
            ----------
            monthly_data_list: list

            Returns
            -------
            none
        """
        print(fg.green + 'Monthly Multiple Horizontal Bar Charts:' + fg.white)
        print(f' Date: {calendar.month_name[monthly_data_list[0].date.month]} {monthly_data_list[0].date.year}')
        for index, data in enumerate(monthly_data_list, 0):
            print(fg.red + f'{index + 1:02d} : {"+" * data.highest_temp} 'f'{data.highest_temp}C')
            print(fg.blue + f'{index + 1:02d} : {"+" * data.lowest_temp} 'f'{data.lowest_temp}C')

    @staticmethod
    def generate_multiple_reports(yearly_result: tuple, monthly_result: tuple, monthly_data_list: list):

        """
            Generate the multiple report of weather data
            ----------
            yearly_result: tuple,
            monthly_result: tuple
            monthly_data_list: list

            Returns
            -------
            none
        """
        yearly_highest_temp, yearly_lowest_temp, yearly_humidity = yearly_result
        ReportGenerator.generate_yearly_report(yearly_highest_temp, yearly_lowest_temp, yearly_humidity)
        avg_highest_temp, avg_lowest_temp, avg_mean_humidity = monthly_result
        ReportGenerator.generate_monthly_report(avg_highest_temp, avg_lowest_temp, avg_mean_humidity)
        ReportGenerator.generate_multiple_monthly_chart(monthly_data_list)
        ReportGenerator.generate_combine_monthly_chart(monthly_data_list)
