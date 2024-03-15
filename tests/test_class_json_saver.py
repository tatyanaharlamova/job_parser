import pytest
import json
from src.class_json_saver import JSONSaver
from src.class_vacancies import Vacancies

filename_2 = "C:/Users/ejik2/PycharmProjects/job_parser/tests/test.json"


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


@pytest.fixture
def json_saver():
    return JSONSaver(filename_2)


def test_save_to_json(json_saver, vacancy_list):
    """
    Тест для сохранения вакансий в JSON файл
    """
    json_saver.save_to_json(vacancy_list[0])
    with open(filename_2) as file:
        vacancy_list = json.load(file)
    assert vacancy_list[0]["name"] == "Разработчик бэк-энда Python"
    with open(filename_2, "w") as file:
        file.write("")


def test_delete_vacancy(json_saver, vacancy_list):
    """
    Тест удаления вакансий из JSON файла
    """
    json_saver.save_to_json(vacancy_list[0])
    json_saver.delete_vacancy(vacancy_list[0])
    with open(filename_2) as file:
        assert json.load(file) == []
