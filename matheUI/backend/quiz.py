from typing import Union

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
            self.quiz_categories[category] = self._load_csv_dataframe(data_folder_path+data_files[category])

    def data_report(self):
        print(f"{len(self.get_categories())} categories:")
        for category in self.get_categories():
            print(f"    {category}: {len(self.get_df(category))}")

    def get_categories(self) -> list[str]:
        return list(self.quiz_categories.keys())

    def get_df(self, category: str) -> pd.DataFrame:
        return self.quiz_categories[category]

    def generate_round(self, question_number: int = 10, categories: Union[str, list] = "all") -> pd.DataFrame:
        """
        @params:
            question_number: how many questions shall be picked (if number is greater than max questions for the categories, the maximum will be used)
            categories: from which categories shall the question be picked (if 'all', use all available categories)

        @return:
            pandas Dataframe with picked questions and columns "QUESTION", "SOLUTION", "FAKE_ANSWER_1", "FAKE_ANSWER_2", "FAKE_ANSWER_3", "INFO"
        """
        if categories == "all":
            categories = self.get_categories()

        possible_questions: pd.DataFrame = pd.DataFrame(columns=["QUESTION", "SOLUTION", "FAKE_ANSWER_1", "FAKE_ANSWER_2", "FAKE_ANSWER_3", "INFO"])
        for category in categories:
            possible_questions= possible_questions.append(self.quiz_categories[category], ignore_index=True)

        if question_number > len(possible_questions):
            print(f"INFO: there only {len(possible_questions)} questions available -> will use all")
            question_number = len(possible_questions)

        questions = possible_questions.sample(n=question_number, ignore_index=True)

        return questions
