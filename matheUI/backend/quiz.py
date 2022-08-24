import pandas as pd
import os
from matheUI.config import QUIZ_DATA_FOLDER, QUIZ_DATA_FILES

class Quiz:
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
