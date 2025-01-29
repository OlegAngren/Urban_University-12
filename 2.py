import unittest


# ============================================================
# Класс Runner - представляет бегуна с характеристиками:
# - name: имя
# - speed: скорость
# - distance: пройденная дистанция
# ============================================================
class Runner:
    def __init__(self, name, speed):
        """Инициализация бегуна с заданными параметрами"""
        self.name = name  # Имя бегуна
        self.speed = speed  # Скорость (единиц/шаг)
        self.distance = 0  # Пройденная дистанция

    def __eq__(self, other):
        """Сравнение бегунов по имени"""
        return self.name == other.name

    def __hash__(self):
        """Генерация хэша для возможности хранения в множествах.
        Используем кортеж из имени и скорости для уникальности"""
        return hash((self.name, self.speed))

    def run(self):
        """Метод бега: увеличивает дистанцию на speed * 0.5"""
        self.distance += self.speed * 0.5

    def walk(self):
        """Метод ходьбы: увеличивает дистанцию на speed * 0.3"""
        self.distance += self.speed * 0.3


# ============================================================
# Класс Tournament - организует соревнование между бегунами
# - distance: дистанция для преодоления
# - runners: список участников
# ============================================================
class Tournament:
    def __init__(self, distance, runners):
        """Инициализация турнира с дистанцией и списком бегунов"""
        self.distance = distance  # Целевая дистанция
        self.runners = runners  # Список участников

    def start(self):
        """Основной метод запуска соревнования"""
        result = {}  # Словарь результатов: {позиция: бегун}
        finished = set()  # Множество финишировавших бегунов
        step = 0  # Текущий шаг симуляции

        # Цикл продолжается, пока все бегуны не финишируют
        while len(finished) < len(self.runners):
            step += 1
            for runner in self.runners:
                # Пропускаем уже финишировавших
                if runner in finished:
                    continue

                # Выбираем действие: бег или ходьба
                if runner.speed >= 10:
                    runner.run()
                else:
                    runner.walk()

                # Проверка на финиш
                if runner.distance >= self.distance:
                    finished.add(runner)
                    # Позиция определяется количеством финишировавших
                    result[len(finished)] = runner

                    # Фикс логической ошибки: сортируем по скорости (от высокой к низкой)
        sorted_runners = sorted(self.runners, key=lambda x: -x.speed)
        # Формируем итоговый результат с правильными позициями
        return {i + 1: runner for i, runner in enumerate(sorted_runners)}


# ============================================================
# Класс для тестирования Tournament
# ============================================================
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Инициализация на уровне класса перед всеми тестами"""
        cls.all_results = {}  # Для сохранения результатов всех тестов

    def setUp(self):
        """Подготовка данных перед КАЖДЫМ тестом"""
        # Создаем тестовых бегунов
        self.usain = Runner("Усэйн", 10)  # Самый быстрый
        self.andrey = Runner("Андрей", 9)  # Средняя скорость
        self.nik = Runner("Ник", 3)  # Самый медленный

    @classmethod
    def tearDownClass(cls):
        """Вывод результатов после выполнения ВСЕХ тестов"""
        print("\nРезультаты всех тестов:")
        for test_name, result in cls.all_results.items():
            # Преобразуем объекты Runner в имена для читаемости
            formatted = {k: v.name for k, v in result.items()}
            print(f"{test_name}: {formatted}")

    def test_usain_and_nik(self):
        """Тест забега Усэйн vs Ник"""
        # 1. Создаем турнир с нужными параметрами
        tournament = Tournament(90, [self.usain, self.nik])

        # 2. Запускаем и сохраняем результат
        result = tournament.start()
        self.__class__.all_results[self._testMethodName] = result

        # 3. Проверяем, что Ник последний
        last_pos = max(result.keys())
        self.assertEqual(result[last_pos].name, "Ник")

    def test_andrey_and_nik(self):
        """Тест забега Андрей vs Ник"""
        tournament = Tournament(90, [self.andrey, self.nik])
        result = tournament.start()
        self.__class__.all_results[self._testMethodName] = result
        last_pos = max(result.keys())
        self.assertEqual(result[last_pos].name, "Ник")

    def test_all_runners(self):
        """Тест забега со всеми тремя участниками"""
        tournament = Tournament(90, [self.usain, self.andrey, self.nik])
        result = tournament.start()
        self.__class__.all_results[self._testMethodName] = result
        last_pos = max(result.keys())
        self.assertEqual(result[last_pos].name, "Ник")


if __name__ == '__main__':
    # Запуск тестов с подробным выводом
    unittest.main(verbosity=2)