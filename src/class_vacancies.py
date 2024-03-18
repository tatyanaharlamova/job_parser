class Vacancies:
    """
    Класс Вакансий
    """
    __slots__ = ("name", "salary", "address", "schedule", "snippet")

    def __init__(self, name, salary, address, schedule, snippet):
        self.name = name
        if dict != type(salary):
            self.salary = 0
        elif type(salary.get("from")) != int and type(salary.get("from")) != float:
            self.salary = 0
        else:
            self.salary = salary["from"]

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
                f"описание: {self.snippet}")

    def __lt__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора <
        """
        if isinstance(other, Vacancies):
            if self.salary < other.salary:
                return True
            else:
                return False
        else:
            raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __le__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора <=
        """
        if isinstance(other, Vacancies):
            if self.salary <= other.salary:
                return True
            else:
                return False
        else:
            raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __gt__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора >
        """
        if isinstance(other, Vacancies):
            if self.salary > other.salary:
                return True
            else:
                return False
        else:
            raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __ge__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора >=
        """
        if isinstance(other, Vacancies):
            if self.salary >= other.salary:
                return True
            else:
                return False
        else:
            raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __eq__(self, other) -> bool:
        """
        Метод, переопределяющий поведение оператора ==
        """
        if isinstance(other, Vacancies):
            if self.salary == other.salary:
                return True
            else:
                return False
        else:
            raise TypeError("Сравнивать можно только объекты класса Вакансий")

    def __ne__(self, other):
        """
        Метод, переопределяющий поведение оператора !=
        """
        if isinstance(other, Vacancies):
            if self.salary != other.salary:
                return True
            else:
                return False
        else:
            raise TypeError("Сравнивать можно только объекты класса Вакансий")
