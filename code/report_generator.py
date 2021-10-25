"""
This module is used for printing the calculated data like monthly data ,
yearly data,horizontal bar charts.
"""
import calendar

from sty import fg

from calculation_results import CalculationResult


class ReportGenerator:
    """
        A class to represent a CalculationResult.
        ...
        Attributes
        ----------
        calculation_result : object
    """

    def __init__(self):
        """
            Constructs all the necessary attributes for the CalculationResult
            object.
        """
        self.calculation_result = CalculationResult()

    def get_month_and_day(self, date: str) -> list:
        """
            Get the month name and day from data str
            ----------
            date: str

            Returns
            -------
            list:  month, day
        """
        date = date.split('-')
        month = calendar.month_name[int(date[1])]
        day = date[2]
        return [month, day]

    def show_yearly_report(self, yearly: str):
        """
            Show the yearly report according to string
            ----------
            yearly: str

            Returns
            -------
            none
        """
        print(fg.green + 'Yearly Report:' + fg.white)
        yearly_result = self.calculation_result.get_calculate_yearly_result(
            yearly)
        month, day = self.get_month_and_day(yearly_result[0].date)
        print(f'Highest: {yearly_result[0].highest_temp}C on'
              f' {month} {day}')
        month, day = self.get_month_and_day(yearly_result[1].date)
        print(f'Lowest: {yearly_result[1].lowest_temp}C on'
              f' {month} {day}')
        month, day = self.get_month_and_day(yearly_result[2].date)
        print(f'Humidity: {yearly_result[2].humidity}% on '
              f' {month} {day}')

    def show_monthly_report(self, monthly: str):
        """
            Show the monthly report according to string
            ----------
            monthly: str

            Returns
            -------
            none
        """
        print(fg.green + 'Monthly Report:' + fg.white)
        monthly_result = self.calculation_result.get_calculate_monthly_result(
            monthly)
        print(f'Highest Average: {monthly_result[0]}C ')
        print(f'Lowest Average: {monthly_result[1]}C ')
        print(f'Average Mean Humidity: {monthly_result[2]}% ')

    def show_horizontal_bar_chart(self, monthly: str):
        """
            Show the multiple line monthly horizontal_bar_chart according to
            string
            ----------
            monthly: str

            Returns
            -------
            none
        """
        print(fg.green + 'Monthly Single Horizontal Bar Chart:' + fg.white)
        year, month = monthly.split('/')
        print(calendar.month_name[int(month)], year)
        monthly_horizontal_bar_result = self.calculation_result \
            .get_calculate_horizontal_result()
        i = 0
        for data in monthly_horizontal_bar_result:
            print(f' {fg.white} {i + 1:02d} : {fg.blue} '
                  f' {"+" * data.lowest_temp}'
                  f' {fg.red}  {"+" * data.highest_temp}'
                  f' {fg.blue} {data.lowest_temp}C -{fg.red}'
                  f' {data.highest_temp}C')
            i += 1

    def show_horizontal_bar_charts(self, monthly: str):
        """
            Show the single line monthly horizontal_bar_chart according to
            string
            ----------
            monthly: str

            Returns
            -------
            none
        """
        print(fg.green + 'Monthly Multiple Horizontal Bar Charts:' + fg.white)
        year, month = monthly.split('/')
        print(calendar.month_name[int(month)], year)
        monthly_horizontal_bar_result = self.calculation_result \
            .get_calculate_horizontal_results(monthly)
        i = 0
        for data in monthly_horizontal_bar_result:
            print(fg.red + f'{i + 1:02d} : {"+" * data.highest_temp} '
                           f'{data.highest_temp}C')
            print(fg.blue + f'{i + 1:02d} : {"+" * data.lowest_temp}'
                            f' {data.lowest_temp}C')
            i += 1

    def show_multiple_reports(self, yearly: str, monthly: str,
                              monthly_chart: str):
        """
            Show the multiple report of weather data
            ----------
            yearly: str, monthly: str,monthly_chart: str

            Returns
            -------
            none
        """
        self.show_horizontal_bar_charts(monthly_chart)
        self.show_horizontal_bar_chart(monthly_chart)
        self.show_yearly_report(yearly)
        self.show_monthly_report(monthly)
