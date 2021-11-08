"""
This is the main module where I pass the arguments according to year,month,chart.
"""
import argparse
import os

from calculation_results import CalculationResult
from file_handler import FileHandler
from parser import Parser
from report_generator import ReportGenerator


def get_command_arguments_values() -> tuple:
    """
        Get the arguments list from command
        ----------
        none

        Returns
        -------
        tuple : args.path, args.e, args.a,  args.c
    """
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding positional argument
    parser.add_argument("path", type=str, help="Enter Path")
    # Adding optional arguments
    parser.add_argument("-e", type=str, help="Enter Year")
    parser.add_argument("-a", type=str, help="Enter year and month")
    parser.add_argument("-c", type=str, help="Enter year and month for horizontal chart")
    args = parser.parse_args()
    return args.path, args.e, args.a, args.c


def perform_args_operation(arg_path: str, arg_year: str, arg_month: str, arg_monthly_chart: str):
    """
        Perform the operations according to arguments
        ----------
        argument_path: str
        argument_year: str
        argument_month: str
        argument_monthly_chart: str

        Returns
        -------
        none
    """
    if os.path.exists(arg_path):
        files_data_list = FileHandler.get_files_data_list(arg_path)
        parsed_data_list = Parser.parse_data(files_data_list)

        if arg_year is None and arg_month is None and arg_monthly_chart is None:
            print('No command is entered')

        elif arg_year and arg_month is None and arg_monthly_chart is None:
            yearly_highest_temp, yearly_lowest_temp, yearly_humidity = CalculationResult.calculate_yearly_result(
                arg_year,
                parsed_data_list)
            ReportGenerator.generate_yearly_report(yearly_highest_temp, yearly_lowest_temp, yearly_humidity)

        elif arg_month and arg_year is None and arg_monthly_chart is None:
            avg_highest_temp, avg_lowest_temp, avg_mean_humidity = CalculationResult.get_calculate_monthly_result(
                arg_month,
                parsed_data_list)
            ReportGenerator.generate_monthly_report(avg_highest_temp, avg_lowest_temp, avg_mean_humidity)

        elif arg_monthly_chart and arg_year is None and arg_month is None:
            monthly_data_list = CalculationResult.get_monthly_data_list(arg_monthly_chart, parsed_data_list)
            ReportGenerator.generate_multiple_monthly_chart(monthly_data_list)
            ReportGenerator.generate_combine_monthly_chart(monthly_data_list)

        else:
            yearly_highest_temp, yearly_lowest_temp, yearly_humidity = CalculationResult.calculate_yearly_result(
                arg_year,
                parsed_data_list)
            yearly_result = yearly_highest_temp, yearly_lowest_temp, yearly_humidity
            avg_highest_temp, avg_lowest_temp, avg_mean_humidity = CalculationResult.get_calculate_monthly_result(
                arg_month,
                parsed_data_list)
            monthly_result = avg_highest_temp, avg_lowest_temp, avg_mean_humidity
            monthly_data_list = CalculationResult.get_monthly_data_list(arg_monthly_chart, parsed_data_list)
            ReportGenerator.generate_multiple_reports(yearly_result, monthly_result, monthly_data_list)
    else:
        print('Path does not exist')


if __name__ == '__main__':
    path_arg, year_arg, month_arg, monthly_chart_arg = get_command_arguments_values()
    perform_args_operation(path_arg, year_arg, month_arg, monthly_chart_arg)
