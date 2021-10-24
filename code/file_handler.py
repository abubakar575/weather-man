"""
In this module, first I extract the files from the zip folder and store
the files name in extracted files list then read the data from each file
using the extracted files.
"""
import zipfile


class FileHandler:
    """
    A class to represent a FileHandler.
    ...
    Attributes
    ----------
    extracted_files_list : list
        list of the zip_extracted_files
    files_data_list : list
        list of the files_data_list

    """

    path = ''  # static variable of file path

    def __init__(self):
        """
        Constructs all the necessary attributes for the fileHandler object.
        """
        self.extracted_files_list = []
        self.files_data_list = []

    def extract_zipped_files(self, zipped_files_list: list):
        """
        Extracts all the files from zip folder and placed into the
        extracted_files_list attribute

        Parameters
        ----------
        zipped_files_list : list

        Returns
        -------
        None
        """
        self.extracted_files_list = [filename for filename in
                                     zipped_files_list if
                                     not str(filename).startswith('__MACOSX/')
                                     and str(filename).endswith('txt')]

    def file_bytes_into_list(self, file_data: bytes):
        """
         Take the bytes input data and convert into list and remove the
         bytes variable from list like b'
         Parameters
         ----------
         file_data: bytes

         Returns
         -------
         bytes_into_list
         """
        file_data_values_list = str(file_data).split('\\n')
        file_data_values_list[0] = file_data_values_list[0].replace('b\'', '')
        file_data_values_list.pop()
        return file_data_values_list

    def read_file_data(self, file: zipfile):
        """
        Take the one file and read the data .
        Parameters
        ----------
        file: zipfile.py

        Returns
        -------
        None
        """
        file.readline()
        read_raw_data = file.read()
        file_data_values_list = self.file_bytes_into_list(read_raw_data)
        for data in file_data_values_list:
            data = data.split(',')
            self.files_data_list.append(data)

    def read_all_files_data(self, zip_file: zipfile):
        """
        Take the zipfile and open file one by one and read the data of each
        file.
        Parameters
        ----------
        zip_file: zipfile.py

        Returns
        -------
        None
        """
        for filename in self.extracted_files_list:
            with zip_file.open(filename) as file:
                self.read_file_data(file)

    def get_files_data_list(self):
        """
        return the list of data which are read from the files
        Parameters
        ----------
        None

        Returns
        -------
        files_data_list
        """
        try:
            with zipfile.ZipFile(self.path) as zip_file:
                self.extract_zipped_files(zip_file.namelist())
                self.read_all_files_data(zip_file)
                return self.files_data_list

        except zipfile.BadZipFile:
            print('Error: Zip file is corrupted')
