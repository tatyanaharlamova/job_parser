from src.class_get_vacancies import GetVacancyFromApi, URL
from src.classes_to_filter_vacancies import JsonReader, VacancyFilter
from src.class_json_saver import JSONSaver
filename = "data.json"
filename_2 = "data_2.json"


def user_interaction():
    """
    Функция взаимодействия с пользователем
    """
    while True:
        search_query = input("Введите поисковый запрос: ")
        vacancies = GetVacancyFromApi(URL)
        vacancies_from_api = vacancies.get_vacancies(search_query)
        result = JSONSaver(filename)
        result.save_from_api(vacancies_from_api)
        j = JsonReader(filename)
        vacancy_list = j.cast_to_object_list
        if not vacancy_list:
            print("Ничего не найдено, введите новый запрос")
            continue
        else:
            j = JsonReader(filename)
            vacancy_list = j.cast_to_object_list()
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            f = VacancyFilter(vacancy_list)
            saver = JSONSaver(filename_2)
            for vacancy in f.get_top_vacancies(top_n):
                saver.save_to_json(vacancy)
                print(vacancy)
            min_ = int(input("Введите диапазон зарплат\nминимум: "))
            max_ = int(input("максимум: "))
            if not f.get_vacancies_from_salary_range(min_, max_):
                print("Ничего не найдено")
            else:
                for vacancy in f.get_vacancies_from_salary_range(min_, max_):
                    print(vacancy)
            filter_words = input("Введите через пробел ключевые слова для фильтрации вакансий: ").split(" ")
            if not f.get_vacancies_from_words(filter_words):
                print("Ничего не найдено")
            else:
                for vacancy in f.get_vacancies_from_words(filter_words):
                    print(vacancy)
            user_input = input("Если хотите завершить поиск, наберите stop: ").lower()
            if user_input == "stop":
                break


if __name__ == "__main__":
    user_interaction()
