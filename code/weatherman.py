"""
This is the main module where I pass the arguments according to path,year,month,chart
"""
import argparse
import os

from file_handler import FileHandler
from parser import Parser
from report_generator import ReportGenerator
from result_calculator import ResultCalculator


def get_command_arguments_values() -> dict:
    """
        Return the arguments dictionary

        parameters
        ----------
        None

        Returns
        -------
        arguments:dict

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Enter Path")
    parser.add_argument("-e", type=str, help="Enter Year")
    parser.add_argument("-a", type=str, help="Enter year and month")
    parser.add_argument("-c", type=str, help="Enter year and month for horizontal chart")
    args = parser.parse_args()
    arguments = {"path": args.path, "year": args.e, "month": args.a, "monthly_chart": args.c}
    return arguments


def perform_args_operation(arguments: dict):
    """
        Perform the operations according to arguments
        ----------
        arguments:dict

        Returns
        -------
        none
    """
    path = arguments.get('path')
    if not os.path.exists(path):
        print('Path does not exists')
        return

    files_data = FileHandler.populate_files_data(path)
    parsed_data = Parser.populate_parse_data(files_data)
    year = arguments.get('year')
    month = arguments.get('month')
    monthly_chart = arguments.get('monthly_chart')

    if year is None and month is None and monthly_chart is None:
        print('No command is entered')

    elif year and month is None and monthly_chart is None:
        yearly_result = ResultCalculator.calculate_yearly_result(year, parsed_data)
        ReportGenerator.generate_yearly_report(yearly_result)

    elif month and year is None and monthly_chart is None:
        monthly_result = ResultCalculator.calculate_monthly_result(month, parsed_data)
        ReportGenerator.generate_monthly_report(monthly_result)

    elif monthly_chart and year is None and month is None:
        monthly_data = ResultCalculator.filter_monthly_data(monthly_chart, parsed_data)
        ReportGenerator.generate_multiple_monthly_chart(monthly_data)
        ReportGenerator.generate_combine_monthly_chart(monthly_data)

    else:
        yearly_result = ResultCalculator.calculate_yearly_result(year, parsed_data)
        monthly_result = ResultCalculator.calculate_monthly_result(month, parsed_data)
        monthly_data = ResultCalculator.filter_monthly_data(monthly_chart, parsed_data)
        ReportGenerator.generate_multiple_reports(yearly_result, monthly_result, monthly_data)


if __name__ == '__main__':
    arguments_values = get_command_arguments_values()
    perform_args_operation(arguments_values)
