from django.test import TestCase
from .models import Student, State, District

class StudentModelTest(TestCase):
    def test_str_method(self):
        state = State.objects.create(name="Kerala")
        district = District.objects.create(name="Ernakulam", state=state)
        student = Student.objects.create(
            name="T",
            state=state,
            district=district,
            age=22,
            gender="Female",
            course="CS"
        )
        self.assertEqual(str(student), "T")
