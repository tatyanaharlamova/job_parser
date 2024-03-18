import json
from src.class_vacancies import Vacancies


class JsonReader:
    """
    Класс для чтения JSON файла
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def read_json(self) -> list:
        """
        Метод чтения JSON файла
        """
        with open(self.file_name) as file:
            vacancies = json.load(file)
        return vacancies

    def get_vacancy(self, vacancy):
        vacancy_list = []
        for item in self.read_json():
            if vacancy in item["name"]:
                vacancy_list.append(item)
        return vacancy_list

    def cast_to_object_list(self) -> list:
        """
        Метод, создающий объекты класса Вакансий и добавляющий его в список объектов
        """
        vacancy_list = []
        for item in self.read_json():
            vacancy_list.append(Vacancies(item.get("name"), item.get("salary"), item.get("address"),
                                          item.get("schedule"), item.get("snippet")))
        return vacancy_list


class VacancyFilter:
    """
    Класс для фильтрации и сортировки вакансий
    """
    def __init__(self, vacancy_list):
        self.vacancy_list = vacancy_list

    def sort_vacancies(self) -> None:
        """
        Метод сортировки вакансий по убыванию зарплаты
        """
        self.vacancy_list.sort(key=lambda vacancy: vacancy.salary, reverse=True)

    def get_top_vacancies(self, number) -> list:
        """
        Метод, возвращающий список из указанного числа вакансий в порядке убывания зарплаты
        """
        self.sort_vacancies()
        return self.vacancy_list[:number]

    def get_vacancies_from_salary_range(self, min_: int, max_: int) -> list:
        """
        Метод, возвращающий список вакансий с указанным диапазоном зарплат
        """
        vacancies_from_salary_range_list = []
        for i in self.vacancy_list:
            if min_ <= i.salary <= max_:
                vacancies_from_salary_range_list.append(i)
        return vacancies_from_salary_range_list

    def get_vacancies_from_words(self, words: list) -> list:
        """
        Метод, возвращающий список вакансий, в описаниях которых встречаются ключевые слова
        """
        vacancies_from_words_list = []
        for word in words:
            for v in self.vacancy_list:
                if v.snippet and v.schedule:
                    if word in v.snippet or word in v.schedule:
                        vacancies_from_words_list.append(v)
        return vacancies_from_words_list
