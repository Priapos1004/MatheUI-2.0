from matheUI.config import SOUQGAME_DATA_FILES, SOUQGAME_DATA_FOLDER

from .abstractGame import AbstactGame
from .souqgame_level import SouqGameLevel


class SouqGame(AbstactGame):
    """ SouqGame backend """

    def __init__(self, data_folder_path: str = SOUQGAME_DATA_FOLDER, data_files: dict[str, list[str]] = SOUQGAME_DATA_FILES):
        """
        @params:
            data_folder_path: path to the folder with the level data (Form: '/....../')
            data_files: dictonary with list of level file paths for one level group (Form: {'Mittelalter': ["souq_level_11.pkl", ...], ...})
        """
        self.data_folder_path = data_folder_path
        self.data_files = data_files

        self.level_dicts: dict[str, dict[dict[str, any]]] = {}
        for level_group in list(data_files.keys()):
            self.level_dicts[level_group] = {}
            for level_path in data_files[level_group]:
                self.level_dicts[level_group][level_path.split(".")[0]] = self._load_pickled_dict(data_folder_path+level_path)

    def data_report(self):
        print(f"level groups: {len(self.get_level_groups())}")
        for level_group in self.get_level_groups():
            print(f"    {level_group}: {len(self.get_level_names_in_level_group(level_group))}")
            for level_name in self.get_level_names_in_level_group(level_group):
                print(f"        {level_name}: {len(self.get_characters_in_level(level_group, level_name))}")
                for character in self.get_characters_in_level(level_group, level_name):
                    print(f"            {character}")

    def get_level_groups(self) -> list[str]:
        return list(self.level_dicts.keys())

    def get_level_names_in_level_group(self, level_group: str) -> list[str]:
        """ returns list of level names for a level group """
        return list(self.level_dicts[level_group].keys())

    def get_level(self, level_group: str, level_name: str) -> dict[str, any]:
        """ returns level dictonary """
        return self.level_dicts[level_group][level_name]

    def get_characters_in_level(self, level_group: str, level_name: str):
        """ returns all character of one level """
        level = self.get_level(level_group, level_name)
        data = level["data"]
        if type(data) == dict:
            return list(data.keys())
        elif type(data) == list:
            character_list: list = []
            for location_dict in data:
                character_list += list(location_dict.keys())
            return character_list
        else:
            raise UserWarning("ERROR: wrong structure of level data")

    def update_data_files(self):
        print("no changing of data intended (for now)")

    def generate_round(self, level_group: str, level_name: str) -> SouqGameLevel:
        return SouqGameLevel(self.get_level(level_group, level_name))