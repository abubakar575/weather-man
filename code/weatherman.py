"""
This is the main module where I pass the arguments according to year,month,
chart
"""
import argparse

from file_handler import FileHandler
from report_generator import ReportGenerator


def get_args_list() -> list:
    """
        Get the arguments list from command
        ----------
        none

        Returns
        -------
        list : args.path, args.e, args.a, args.c
    """
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding positional argument
    parser.add_argument("path", type=str, help="Enter Path")
    # Adding optional arguments
    parser.add_argument("-e", type=str, help="Enter Year")
    parser.add_argument("-a", type=str, help="Enter year and month")
    parser.add_argument("-c", type=str, help="Enter year and month for "
                                             "horizontal chart")
    args = parser.parse_args()
    return [args.path, args.e, args.a, args.c]


def perform_args_operation(args_list: list):
    """
        Perform the operations according to arguments
        ----------
        args_list: list

        Returns
        -------
        none
    """
    path, yearly, monthly, monthly_chart = args_list
    FileHandler.path = path
    report_generator = ReportGenerator()
    if yearly is None and monthly is None and monthly_chart is None:
        print('No command is entered')
    elif yearly and monthly is None and monthly_chart is None:
        report_generator.show_yearly_report(yearly)
    elif monthly and yearly is None and monthly_chart is None:
        report_generator.show_monthly_report(monthly)
    elif monthly_chart and yearly is None and monthly is None:
        report_generator.show_horizontal_bar_charts(monthly_chart)
        report_generator.show_horizontal_bar_chart(monthly_chart)
    else:
        report_generator.show_multiple_reports(yearly, monthly, monthly_chart)


if __name__ == '__main__':
    cmd_args_list = get_args_list()
    perform_args_operation(cmd_args_list)
