import pytest
from src.classes_to_filter_vacancies import VacancyFilter, JsonReader
from src.class_get_vacancies import filename
from src.class_vacancies import Vacancies


@pytest.fixture
def reading():
    return JsonReader(filename)


def test_read_json(reading):
    """
    Тест чтения JSON  файла
    """
    assert type(reading.read_json()) == list


def test_cast_to_object_list(reading):
    """
    Тест создания списка объектов класса Вакансии
    """
    assert type(reading.cast_to_object_list()[0]) == Vacancies


@pytest.fixture
def vacancy_list():
    return [
        Vacancies("Разработчик бэк-энда Python", {"from": 100000},
                  "Ташкент", {"name": "Полный день"},
                  "Создавать новые и расширять старые микросервисы"),
        Vacancies("Программист Golang", {"from": 120000}, "не указан",
                  {"name": "Полный день"},
                  "Развитие серверной части программного комплекса"),
        Vacancies("Python Backend Developer", {"from": 150000}, "не указан",
                  {"name": "Удаленная работа"},
                  "Участие в разработке сервисов")
    ]


def test_sort_vacancies(vacancy_list):
    """
    Тест сортировки списка вакансий
    """
    vacancy_filter = VacancyFilter(vacancy_list)
    vacancy_filter.sort_vacancies()
    assert vacancy_filter.vacancy_list[0].salary == 150000


def test_get_top_vacancies(vacancy_list):
    """
    Тест составления топ N вакансий
    """
    vacancy_filter = VacancyFilter(vacancy_list)
    assert len(vacancy_filter.get_top_vacancies(2)) == 2


def test_get_vacancies_from_salary_range(vacancy_list):
    """
    Тест фильтрации вакансий по уровню зарплат
    """
    vacancy_filter = VacancyFilter(vacancy_list)
    assert len(vacancy_filter.get_vacancies_from_salary_range(100000, 120000)) == 2


def test_get_vacancies_from_words(vacancy_list):
    """
    Тест фильтрации вакансий по ключевым словам
    """
    vacancy_filter = VacancyFilter(vacancy_list)
    assert len(vacancy_filter.get_vacancies_from_words(["Удаленная"])) == 1
