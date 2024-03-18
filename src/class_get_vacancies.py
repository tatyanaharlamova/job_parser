import requests
import json
from abc import ABC, abstractmethod


URL = 'https://api.hh.ru/vacancies'


class AbstractAPI(ABC):
    """
    Абстрактный класс для класса получения вакансий по API
    """
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class GetVacancyFromApi(AbstractAPI):
    """
    Класс получения вакансий по API
    """

    def __init__(self, url):
        self.__url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    def get_vacancies(self, vacancy: str) -> dict:
        """
        Метод для получения вакансии по API, возвращает словарь
        """
        response = requests.get(self.__url, params={'text': vacancy, 'per_page': 100})
        vacancies = json.loads(response.text)["items"]
        return vacancies
