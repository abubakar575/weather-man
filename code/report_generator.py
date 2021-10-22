from calculation_results import CalculationResult


class ReportGenerator:

    def __init__(self):
        self.calculation_result = CalculationResult()

    def show_yearly_report(self):
        self.calculation_result.calculate_yearly_result()

    def show_monthly_report(self):
        self.calculation_result.calculate_monthly_result()

    def show_multiple_reports(self):
        self.calculation_result.calculate_multiple_result()

    def show_horizontal_charts(self):
        self.calculation_result.calculate_horizontal_results()

    def show_horizontal_chart(self):
        self.calculation_result.calculate_horizontal_result()
