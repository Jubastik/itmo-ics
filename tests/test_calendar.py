import unittest
from datetime import datetime, timedelta

from requests import HTTPError

from app.dialogs.windows.menu.my_itmo import _event_type_to_tag, _raw_event_to_description, _raw_event_to_location, \
    get_raw_events


class TestGetRawEvents(unittest.TestCase):
    def test_error_handling(self):
        with self.assertRaises(HTTPError):
            get_raw_events("wrong", datetime.now(), datetime.now())


class TestEventTypeToTag(unittest.TestCase):
    def test_lecture(self):
        self.assertEqual(_event_type_to_tag("Лекции"), "Лек")

    def test_practice(self):
        self.assertEqual(_event_type_to_tag("Практические занятия"), "Прак")

    def test_exam(self):
        self.assertEqual(_event_type_to_tag("Зачет"), "Зачет")

    def test_other(self):
        self.assertEqual(_event_type_to_tag("wrong"), "wrong")


class TestRawEventToDescription(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(_raw_event_to_description({}),
                         f"Обновлено: {(datetime.utcnow() + timedelta(hours=3)).strftime('%Y-%m-%d %H:%M')} MSK")

    def test_full(self):
        self.assertEqual(_raw_event_to_description({
            "group": "Группа",
            "teacher_name": "Преподаватель",
            "zoom_url": "Ссылка на Zoom",
            "zoom_password": "Пароль Zoom",
            "zoom_info": "Доп. информация для Zoom",
            "note": "Примечание",
        }),
            f"Группа: Группа\nПреподаватель: Преподаватель\nСсылка на Zoom: Ссылка на Zoom\nПароль Zoom: Пароль Zoom\nДоп. информация для Zoom: Доп. информация для Zoom\nПримечание: Примечание\nОбновлено: {(datetime.utcnow() + timedelta(hours=3)).strftime('%Y-%m-%d %H:%M')} MSK")

    def test_partial(self):
        self.assertEqual(_raw_event_to_description({
            "group": "Группа",
            "teacher_name": "Преподаватель",
            "zoom_url": "",
            "zoom_password": "",
            "zoom_info": "",
            "note": "",
        }),
            f"Группа: Группа\nПреподаватель: Преподаватель\nСсылка на Zoom: \nПароль Zoom: \nДоп. информация для Zoom: \nПримечание: \nОбновлено: {(datetime.utcnow() + timedelta(hours=3)).strftime('%Y-%m-%d %H:%M')} MSK")


class TestRawEventToLocation(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(_raw_event_to_location({}), None)

    def test_full(self):
        self.assertEqual(_raw_event_to_location({
            "room": "room",
            "building": "building",
        }), "room, building")

    def test_partial(self):
        self.assertEqual(_raw_event_to_location({
            "building": "building",
        }), "building")


if __name__ == '__main__':
    unittest.main()
