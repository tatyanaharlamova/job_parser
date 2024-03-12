import requests
import json
from abc import ABC, abstractmethod


URL = 'https://api.hh.ru/vacancies'
filename = "../data.json"


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

    def save_vacancies(self, file_name: str, vacancies: str) -> None:
        """
        Метод для сохранения вакансий в JSON файл
        """
        with open(file_name, "w") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
