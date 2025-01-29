# Файл: runner.py

class Runner:
    """
    Класс Runner представляет бегуна, который может ходить и бегать.
    Каждый шаг (walk) увеличивает дистанцию на 5 единиц,
    а каждый бег (run) — на 10 единиц.
    """
    def __init__(self, name):
        """
        Конструктор класса Runner.
        :param name: Имя бегуна.
        """
        self.name = name  # Имя бегуна
        self.distance = 0  # Пройденная дистанция (изначально 0)

    def walk(self):
        """
        Метод walk увеличивает дистанцию на 5 единиц.
        """
        self.distance += 5

    def run(self):
        """
        Метод run увеличивает дистанцию на 10 единиц.
        """
        self.distance += 10