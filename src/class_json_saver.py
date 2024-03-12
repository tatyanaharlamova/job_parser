import os
import json
from abc import ABC, abstractmethod
from src.class_vacancies import Vacancies


class AbstractJson(ABC):
    @abstractmethod
    def save_to_json(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        pass


class JSONSaver(AbstractJson):
    """
    Класс для сохранения и удаления вакансий из JSON файла
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def save_to_json(self, vacancy: Vacancies) -> None:
        """
        Метод для сохранения вакансий в JSON файл
        """
        vacancy_dict = {"name": vacancy.name, "salary": vacancy.salary, "address": vacancy.address,
                        "schedule": vacancy.schedule, "snippet": vacancy.snippet}
        if os.stat(self.file_name).st_size == 0:
            vacancy_list = []
        else:
            with open(self.file_name) as file:
                vacancy_list = json.load(file)
        vacancy_list.append(vacancy_dict)
        with open(self.file_name, "w") as f:
            json.dump(vacancy_list, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancies) -> None:
        """
        Метод для удаления вакансий из JSON файла
        """
        try:
            if os.stat(self.file_name).st_size != 0:
                with open(self.file_name) as file:
                    vacancy_list = json.load(file)
            else:
                raise EOFError
        except EOFError:
            print("Файл пустой")
        else:
            for item in vacancy_list:
                if item["name"] == vacancy.name:
                    vacancy_list.remove(item)
            with open(self.file_name, "w") as f:
                json.dump(vacancy_list, f, ensure_ascii=False, indent=4)
