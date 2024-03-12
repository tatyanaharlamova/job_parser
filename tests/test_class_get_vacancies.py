import pytest
from src.class_get_vacancies import GetVacancyFromApi, URL, filename


@pytest.fixture
def get_from_hh():
    return GetVacancyFromApi(URL)


def test_get_vacancies(get_from_hh):
    """
    Тест на получение результата запроса по API
    """
    assert type(get_from_hh.get_vacancies("Python", filename)) == list
