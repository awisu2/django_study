from django.test import TestCase

from django.urls import reverse


class TaskModelTests(TestCase):
    # 初期データ追加
    fixtures = ["tests/task_data.json"]

    def test_tasks_index(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """

        res = self.client.get(reverse("tasks:task_list"))
        self.assertEqual(res.status_code, 200, f"check 200 ok. {res.context}")
