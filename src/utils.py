from src.class_get_vacancies import GetVacancyFromApi, URL, filename
from src.classes_to_filter_vacancies import JsonReader, VacancyFilter


def user_interaction():
    """
    Функция взаимодействия с пользователем
    """
    search_query = input("Введите поисковый запрос: ")
    GetVacancyFromApi(URL).get_vacancies(search_query, filename)
    j = JsonReader(filename)
    vacancy_list = j.cast_to_object_list()
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    f = VacancyFilter(vacancy_list)
    for vacancy in f.get_top_vacancies(top_n):
        print(vacancy)
    min_ = int(input("Введите диапазон зарплат\nот: "))
    max_ = int(input("до: "))
    for vacancy in f.get_vacancies_from_salary_range(min_, max_):
        print(vacancy)
    filter_words = input("Введите через пробел ключевые слова для фильтрации вакансий: ").split(" ")
    for vacancy in f.get_vacancies_from_words(filter_words):
        print(vacancy)


user_interaction()
