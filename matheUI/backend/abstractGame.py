import os
import pickle
from abc import ABCMeta, abstractmethod

import pandas as pd


class AbstactGame(metaclass = ABCMeta):

    @abstractmethod
    def data_report(self):
        """ method to provide report about used data """
        print("no data used")

    @abstractmethod
    def update_data_files(self):
        """ method to update data files with class object changes """
        print("no data used")

    @abstractmethod
    def generate_round(self, **kwargs):
        """ method to generate round for game """
        print("generate_round is not implemented yet")

    def _pickle_dict(self, dictionary: dict, file_path: str = "test.pkl"):
        """ save dictonary as pickle file """
        with open(os.path.dirname(__file__)+file_path, 'wb') as f:
            pickle.dump(dictionary, f)

    def _load_pickled_dict(self, file_path: str) -> dict:
        """ load pickled dictonary """
        with open(os.path.dirname(__file__)+file_path, 'rb') as f:
            dictonary = pickle.load(f)
        return dictonary

    def _save_dataframe(self, df: pd.DataFrame, file_path: str = "test.csv"):
        """ save pandas dataframe as csv file """
        df.to_csv(os.path.dirname(__file__)+file_path)

    def _load_csv_dataframe(self, file_path: str) -> pd.DataFrame:
        """ load pandas dataframe from csv file """
        df = pd.read_csv(os.path.dirname(__file__)+file_path, index_col=0)
        return df
