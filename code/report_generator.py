import calendar

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

    def show_monthly_report(self):
        self.calculation_result.calculate_monthly_result()

    def show_multiple_reports(self):
        self.calculation_result.calculate_multiple_result()

    def show_horizontal_charts(self):
        self.calculation_result.calculate_horizontal_results()

    def show_horizontal_chart(self):
        self.calculation_result.calculate_horizontal_result()
