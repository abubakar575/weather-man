import argparse

from file_handler import FileHandler
from report_generator import ReportGenerator


def get_args_list() -> list:
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding positional argument
    parser.add_argument("path", type=str, help="Enter Path")
    # Adding optional argument
    parser.add_argument("-e", type=str, help="Enter Year")
    parser.add_argument("-a", type=str, help="Enter year and month")
    parser.add_argument("-c", type=str, help="Enter year and month for "
                                             "horizontal chart")
    args = parser.parse_args()
    return [args.path, args.e, args.a, args.c]


def perform_args_operation(args_list: list):
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
    print('Weather Man File')
    cmd_args_list = get_args_list()
    perform_args_operation(cmd_args_list)
