import os
from typing import List


class Util:
    @staticmethod
    def get_file_extension(file_name: str) -> str:
        """

        :param file_name:
        :return: str
        """
        try:
            if file_name:
                extension = file_name[file_name.rfind('.') + 1:]
            else:
                extension = ''
        except Exception as ex:
            raise ex
        return extension

    @staticmethod
    def remove_extension(file_ext: str) -> str:
        """

        :param file_ext:
        :return: str
        """
        file_name = os.path.basename(file_ext)
        name_without_extension = file_name.rsplit('.', 1)[0]
        if name_without_extension:
            return name_without_extension
        return file_name

    @staticmethod
    def read_lines_from_file(file_name: str, skip_empty_lines_and_comments: bool = True) -> List[str]:
        """

        :param file_name:
        :param skip_empty_lines_and_comments:
        :return: list[str]
        """
        lines = []
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if skip_empty_lines_and_comments:
                    if not line.startswith('#') and len(line) > 0:
                        lines.append(line)
                else:
                    lines.append(line)
        return lines

    @staticmethod
    def get_repeated_string(string: str, repeats: int) -> str:
        return string * repeats