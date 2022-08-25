import os

import pandas as pd

from matheUI.config import QUIZ_DATA_FILES, QUIZ_DATA_FOLDER

from .abstractGame import AbstactGame


class Quiz(AbstactGame):
    """ Quiz backend """

    def __init__(self, data_folder_path: str = QUIZ_DATA_FOLDER, data_files: dict[str, str] = QUIZ_DATA_FILES):
        """
        @params:
            data_folder_path: path to the folder with the quiz data (Form: '/....../')
            data_files: dictonary with name of the quiz category and file name of the data (Form: {'physics': 'quiz_physics.csv'})
        """
        self.data_folder_path = data_folder_path
        self.data_files = data_files

        self.quiz_categories: dict[str, pd.DataFrame] = {}
        for category in list(data_files.keys()):
            file_path = os.path.dirname(__file__)+data_folder_path+data_files[category]
            self.quiz_categories[category] = pd.read_csv(file_path, index_col=0)

    def data_report(self):
        print(f"{len(self.get_categories())} categories:")
        for category in self.get_categories():
            print(f"    {category}: {len(self.get_df(category))}")

    def get_categories(self) -> list[str]:
        return list(self.quiz_categories.keys())

    def get_df(self, category: str) -> pd.DataFrame:
        return self.quiz_categories[category]

    def generate_round(self):
        pass
