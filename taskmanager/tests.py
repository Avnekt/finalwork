from django.test import TestCase
from taskmanager.models import Task
# from django.utils import timezone

# Create your tests here.

# class TestApp(TestCase):
    
#     n = 1

#     def test_function(self):
#         self.assertEqual(self.n, 1)

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(name="First task todo", is_active=True)
        Task.objects.create(name="Second task todo", is_active=False)

    def test_first_task(self):
        '''Test that active is only first task'''
        queryset = Task.objects.filter(is_active=True)
        self.assertEqual(len(queryset), 1)
        self.assertEqual(queryset[0].name, "First task todo")

    def test_task_active_change(self):
        """Tasks can change is_active state"""
        task_1 = Task.objects.get(name="First task todo")
        task_2 = Task.objects.get(name="Second task todo")
        task_2.is_active = not task_2.is_active
        self.assertEqual(task_1.is_active, True)
        self.assertEqual(task_2.is_active, True)