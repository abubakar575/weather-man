"""
In this module, first I extract the files from the zip folder and store the files name in extracted files list then
read the data from each file using the extracted files.
"""
import csv
import zipfile
from io import TextIOWrapper


class FileHandler:
    """
    A class to represent a FileHandler.
    """

    @staticmethod
    def extract_zipped_files(zipped_files: list) -> list:
        """
        Extracts all the files from zip folder and placed into the extracted_files

        Parameters
        ----------
        zipped_files : list

        Returns
        -------
        list : extracted_files
        """
        extracted_files = [
            filename for filename in zipped_files if
            not str(filename).startswith('__MACOSX/')
            and str(filename).endswith('txt')
        ]
        return extracted_files

    @staticmethod
    def populate_files_data(path: str):
        """
        Return the list of data which are read from the all files.

        Parameters
        ----------
        path: str

        Returns
        -------
        list: files_data
        """

        files_data = []
        try:
            with zipfile.ZipFile(path) as zip_file:
                extracted_files = FileHandler.extract_zipped_files(zip_file.namelist())
                for filename in extracted_files:
                    with zip_file.open(filename, 'r') as csv_file:
                        csv_reader = csv.DictReader(TextIOWrapper(csv_file, 'utf-8'))
                        for row in csv_reader:
                            file_data = {}
                            if row.get("PKT") and row.get("Max TemperatureC") and row.get("Min TemperatureC") \
                                    and row.get("Max Humidity") and row.get(" Mean Humidity"):
                                file_data['date'] = row.get("PKT")
                                file_data['highest_temp'] = row.get("Max TemperatureC")
                                file_data['lowest_temp'] = row.get("Min TemperatureC")
                                file_data['highest_humidity'] = row.get("Max Humidity")
                                file_data['mean_humidity'] = row.get(" Mean Humidity")
                                files_data.append(file_data)

                return files_data

        except zipfile.BadZipFile:
            print('Error: Zip file is corrupted')
