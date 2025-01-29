# Файл: test_runner.py

import unittest
from runner import Runner  # Импортируем класс Runner из файла runner.py


class RunnerTest(unittest.TestCase):
    """
    Класс для тестирования методов класса Runner.
    Наследуется от unittest.TestCase.
    """

    def test_walk(self):
        """
        Тест для метода walk.
        Проверяет, что после 10 вызовов метода walk дистанция равна 50.
        """
        runner = Runner("John")  # Создаем объект Runner с именем "John"
        for _ in range(10):  # Вызываем метод walk 10 раз
            runner.walk()
        # Проверяем, что дистанция равна 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """
        Тест для метода run.
        Проверяет, что после 10 вызовов метода run дистанция равна 100.
        """
        runner = Runner("Jane")  # Создаем объект Runner с именем "Jane"
        for _ in range(10):  # Вызываем метод run 10 раз
            runner.run()
        # Проверяем, что дистанция равна 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """
        Тест для сравнения результатов run и walk.
        Проверяет, что дистанции двух бегунов не равны после 10 вызовов run и walk.
        """
        runner1 = Runner("Alice")  # Создаем первого бегуна с именем "Alice"
        runner2 = Runner("Bob")  # Создаем второго бегуна с именем "Bob"
        for _ in range(10):  # Вызываем run для первого и walk для второго 10 раз
            runner1.run()
            runner2.walk()
        # Проверяем, что дистанции не равны
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    # Запуск всех тестов, если файл запущен напрямую
    unittest.main()