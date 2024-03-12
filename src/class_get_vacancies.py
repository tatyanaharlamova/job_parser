import requests
import json
from abc import ABC, abstractmethod
from src.classes_to_filter_vacancies import *

URL = 'https://api.hh.ru/vacancies'
filename = "../data.json"
filename_2 = "../data_2.json"


class AbstractAPI(ABC):
    """
    Абстрактный класс для класса получения вакансий по API
    """
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass

    @abstractmethod
    def save_vacancies(self, *args, **kwargs):
        pass


class GetVacancyFromApi(AbstractAPI):
    """
    Класс получения вакансий по API
    """

    def __init__(self, url):
        self.url = url

    def get_vacancies(self, vacancy: str, file_name: str) -> dict:
        """
        Метод для получения вакансии по API, возвращает словарь
        """
        response = requests.get(URL, params={'text': vacancy})
        vacancies = json.loads(response.text)["items"]
        self.save_vacancies(file_name, vacancies)
        return vacancies

    def save_vacancies(self, file_name:str, vacancies:str) -> None:
        """
        Метод для сохранения вакансий в JSON файл
        """
        with open(file_name, "w") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)


class AbstractJson(ABC):
    @abstractmethod
    def save_to_json(self, *args, **kwargs):
        pass


class JSONSaver(AbstractJson):

    def __init__(self, vacancy):
        self.vacancy = vacancy

    def save_to_json(self, file_name):
        vacancy_dict = {"name": self.vacancy.name, "salary": self.vacancy.salary, "address": self.vacancy.address,
                        "schedule": self.vacancy.schedule, "snippet": self.vacancy.snippet}
        with open(file_name, "a") as file:
            json.dump(vacancy_dict, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy):
        pass
# j = JsonReader(filename).cast_to_object_list()
# s = JSONSaver(j[3])
# s.save_to_json(filename_2)
# print(s)
