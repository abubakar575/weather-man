"""
In this module, first I extract the files from the zip folder and store the files name in extracted files list then
read the data from each file using the extracted files.
"""
import zipfile


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
        extracted_files = [filename for filename in zipped_files if
                           not str(filename).startswith('__MACOSX/')
                           and str(filename).endswith('txt')]
        return extracted_files

    @staticmethod
    def file_bytes_into_list(file_data: bytes) -> list:
        """
         Take the bytes input data and convert into string based list and remove the bytes variable from list like b'
         Parameters
         ----------
         file_data: bytes

         Returns
         -------
         list : file_data_values
         """
        file_data_values = str(file_data).split('\\n')
        file_data_values[0] = file_data_values[0].replace('b\'', '')
        file_data_values.pop()
        return file_data_values

    @staticmethod
    def read_file_data(file: zipfile) -> list:
        """
        Take the one file and read the data .
        Parameters
        ----------
        file: zipfile.py

        Returns
        -------
        list : file_data_values
        """
        file.readline()
        read_raw_data = file.read()
        file_data_values = FileHandler.file_bytes_into_list(read_raw_data)
        return file_data_values

    @staticmethod
    def read_files_data(zip_file: zipfile, extracted_files: list) -> list:
        """
        Take the extracted_files_list and read the data of each file.
        Parameters
        ----------
        zip_file: zipfile.py
        extracted_files: list

        Returns
        -------
        list: files_data
        """
        files_data = []
        for filename in extracted_files:
            with zip_file.open(filename) as file:
                file_data_values = FileHandler.read_file_data(file)
                for data in file_data_values:
                    data = data.split(',')
                    files_data.append(data)

        return files_data

    @staticmethod
    def get_files_data(path: str) -> list:
        """
        Return the list of data which are read from the all files.

        Parameters
        ----------
        path: str

        Returns
        -------
        list: files_data
        """
        try:
            with zipfile.ZipFile(path) as zip_file:
                extracted_files = FileHandler.extract_zipped_files(zip_file.namelist())
                files_data = FileHandler.read_files_data(zip_file, extracted_files)
                return files_data

        except zipfile.BadZipFile:
            print('Error: Zip file is corrupted')
