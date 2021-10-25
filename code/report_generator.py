import calendar

from sty import fg

from calculation_results import CalculationResult


class ReportGenerator:

    def __init__(self):
        self.calculation_result = CalculationResult()

    def get_month_and_day(self, date):
        date = date.split('-')
        month = calendar.month_name[int(date[1])]
        day = date[2]
        return [month, day]

    def show_yearly_report(self, yearly: str):
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
        print(fg.green + 'Monthly Report:' + fg.white)
        monthly_result = self.calculation_result.get_calculate_monthly_result(
            monthly)
        print(f'Highest Average: {monthly_result[0]}C ')
        print(f'Lowest Average: {monthly_result[1]}C ')
        print(f'Average Mean Humidity: {monthly_result[2]}% ')

    def show_horizontal_bar_chart(self, monthly: str):
        print(fg.green + 'Monthly Single Horizontal Bar Chart:' + fg.white)
        year, month = monthly.split('/')
        print(calendar.month_name[int(month)], year)
        monthly_horizontal_bar_result = self.calculation_result \
            .get_calculate_horizontal_results(monthly)
        i = 0
        for data in monthly_horizontal_bar_result:
            print(f' {fg.white} {i + 1:02d} : {fg.blue} '
                  f' {"+" * data.lowest_temp}'
                  f' {fg.red}  {"+" * data.highest_temp}'
                  f' {fg.blue} {data.lowest_temp}C -{fg.red}'
                  f' {data.highest_temp}C')
            i += 1

    def show_horizontal_bar_charts(self, monthly: str):
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
        print(yearly, monthly, monthly_chart)
        self.show_horizontal_bar_charts(monthly_chart)
        self.show_yearly_report(yearly)
        self.show_monthly_report(monthly)
