import pytest
from src.class_vacancies import Vacancies


@pytest.fixture
def vacancy_1():
    return Vacancies("Разработчик бэк-энда Python", {"from": 300000}, "Ташкент",
                     {"name": "Полный день"},
                     "Создавать новые и расширять старые микросервисы")


@pytest.fixture
def vacancy_2():
    return Vacancies("Программист Golang", {"from": 120000}, "не указан",
                     {"name": "Полный день"},
                     "Развитие серверной части программного комплекса")


@pytest.fixture
def vacancy_3():
    return Vacancies("Python Backend Developer", {"from": 120000}, "не указан",
                     {"name": "Полный день"},
                     "Участие в разработке сервисов")


def test__lt__(vacancy_1, vacancy_2):
    """
    Тест переопределения магического метода, определяющего поведения оператора <
    """
    assert vacancy_2 < vacancy_1
    assert not vacancy_1 < vacancy_2
    with pytest.raises(TypeError):
        vacancy_1 < 4


def test__le__(vacancy_1, vacancy_2):
    """
    Тест переопределения магического метода, определяющего поведения оператора <=
    """
    assert vacancy_2 <= vacancy_1
    assert not vacancy_1 <= vacancy_2
    with pytest.raises(TypeError):
        vacancy_1 <= 4


def test__gt__(vacancy_1, vacancy_2):
    """
    Тест переопределения магического метода, определяющего поведения оператора >
    """
    assert vacancy_1 > vacancy_2
    assert not vacancy_2 > vacancy_1
    with pytest.raises(TypeError):
        vacancy_1 > 4


def test__ge__(vacancy_1, vacancy_2):
    """
    Тест переопределения магического метода, определяющего поведения оператора >=
    """
    assert vacancy_1 >= vacancy_2
    assert not vacancy_2 >= vacancy_1
    with pytest.raises(TypeError):
        vacancy_1 >= 4


def test__eq__(vacancy_3, vacancy_2):
    """
    Тест переопределения магического метода, определяющего поведения оператора ==
    """
    assert vacancy_3 == vacancy_2
    assert not vacancy_3 != vacancy_2
    with pytest.raises(TypeError):
        vacancy_3 == 4


def test__ne__(vacancy_1, vacancy_2):
    """
    Тест переопределения магического метода, определяющего поведения оператора !=
    """
    assert vacancy_1 != vacancy_2
    assert not vacancy_1 == vacancy_2
    with pytest.raises(TypeError):
        vacancy_1 != 4
