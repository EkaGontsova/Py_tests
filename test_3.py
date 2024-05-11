import unittest


class TestCourses(unittest.TestCase):
    def setUp(self):
        self.courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
        self.mentors = [
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        self.durations = [14, 20, 12, 20]
        self.courses_list = []
        for course, mentor, duration in zip(self.courses, self.mentors, self.durations):
            course_dict = {"title": course, "mentors": mentor, "duration": duration}
            self.courses_list.append(course_dict)

        self.max_duration = max(self.durations)
        self.min_duration = min(self.durations)

        self.maxes = []
        self.minis = []
        for id, duration in enumerate(self.durations):
            if duration == self.max_duration:
                self.maxes.append(id)
            elif duration == self.min_duration:
                self.minis.append(id)

        self.courses_max = [x["title"] for id, x in enumerate(self.courses_list) if id in self.maxes]
        self.courses_min = [x["title"] for id, x in enumerate(self.courses_list) if id in self.minis]

    def test_max_duration(self):
        self.assertEqual(self.max_duration, 20, "Должна быть 20")

    def test_min_duration(self):
        self.assertEqual(self.min_duration, 12, "Должна быть 12")

    def test_courses_max(self):
        self.assertIn("Fullstack-разработчик на Python", self.courses_max, "Должен быть в числе самых длинных")
        self.assertIn("Frontend-разработчик с нуля", self.courses_max, "Должен быть в числе самых длинных")

    def test_courses_min(self):
        self.assertIn("Python-разработчик с нуля", self.courses_min, "Должен быть в числе самых коротких")


if __name__ == '__main__':
    unittest.main()
