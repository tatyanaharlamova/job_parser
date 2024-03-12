class Vacancies:
    """
    Класс Вакансий
    """
    def __init__(self, name: str, salary, address, schedule, snippet):
        self.name = name
        if not salary:
            self.__salary = 0
        else:
            self.__salary = salary["from"]

        try:
            self.address = address.get("city")
        except AttributeError:
            self.address = "не указан"
        self.schedule = schedule.get("name")

        try:
            self.snippet = snippet.get("responsibility")
        except AttributeError:
            self.snippet = "не указан"

    def __str__(self) -> str:
        """
        Метод строкового представления экземпляра класса
        """
        return (f"{self.name}, зарплата: {self.salary}, город: {self.address}, график: {self.schedule}, "
                f"навыки: {self.snippet}")

    @property
    def salary(self) -> int:
        """
        Геттер для зарплаты
        """
        return self.__salary

    @salary.setter
    def salary(self, value: int) -> None:
        """
        Сеттер для зарплаты
        """
        if value > 0:
            self.__salary = value

    def __lt__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора <
        """
        if isinstance(other, Vacancies):
            if self.__salary < other.__salary:
                return True
        raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __le__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора <=
        """
        if isinstance(other, Vacancies):
            if self.__salary <= other.__salary:
                return True
        raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __gt__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора >
        """
        if isinstance(other, Vacancies):
            if self.__salary > other.__salary:
                return True
        raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __ge__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора >=
        """
        if isinstance(other, Vacancies):
            if self.__salary >= other.__salary:
                return True
        raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __eq__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора ==
        """
        if isinstance(other, Vacancies):
            if self.__salary == other.__salary:
                return True
        raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __ne__(self, other):
        """
        Метод, переопределяющий поведение оператора !=
        """
        if isinstance(other, Vacancies):
            if self.__salary != other.__salary:
                return True
        raise TypeError("Сравнивать можно только объекты класса Вакансий")
