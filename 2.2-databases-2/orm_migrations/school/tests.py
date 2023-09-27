from django.test import TestCase
from .models import Student, Teacher

class StudentModelTestCase(TestCase):

    @staticmethod
    def print_info(message):
        count = Student.objects.count()
        print(f'{message}: #all_students={count}')

    def setUp(self):
        print('-'*20)
        self.print_info('Start setUp')
        t1 = Teacher.objects.create(name='Андрей Белый', subject='Литература')
        t2 = Teacher.objects.create(name='Карл Маркс', subject='Экономика')
        self.student = Student.objects.create(name= 'Шура и Лёва', group='БИ-2')
        self.student.teachers.add(t1)
        s1 = Student.objects.create(name='Владимир Ленин', group='Большевики')
        s2 = Student.objects.create(name='Эдмунд Шклярский', group='Пикник')
        s1.teachers.add(t2)
        s2.teachers.add(t1)
        self.print_info('Finish setUp')

    def test_student_creation(self):
        self.print_info('Start test_student_creation')
        self.assertEqual(self.student.name, 'Шура и Лёва')
        s1 = Student.objects.get(name='Эдмунд Шклярский')
        self.assertEqual(str(s1.teachers.all()[0]), 'Андрей Белый')
        self.print_info('Finish test_student_creation')

    def test_student_get_all_records(self):
        self.print_info('Start test_get_all_records')
        students = Student.objects.all()
        self.assertEqual(len(students), 3)
        self.print_info('Finish test_get_all_records')

    def test_student_get_records(self):
        self.print_info('Start test_get_record')
        student = Student.objects.get(group='БИ-2')
        self.assertEqual(student.name, 'Шура и Лёва')
        self.print_info('Finish test_get_record')

    def test_student_str(self):
        self.print_info('Start test_student_str')
        expected_str = 'Шура и Лёва'
        self.assertEqual(str(self.student), expected_str)
        self.print_info('Finish test_student_str')

    def test_student_delete(self):
        self.print_info('Start test_student_delete')
        Student.objects.get(group='БИ-2').delete()
        self.assertEqual(len(Student.objects.all()), 2)
        self.print_info('Finish test_student_delete')

    def test_student_update(self):
        self.print_info('Start test_student_update')
        tch1 = Teacher.objects.get(subject='Литература')
        tch2 = Teacher.objects.get(subject='Экономика')
        st = Student.objects.get(group='Большевики')
        st.teachers.remove(tch2)
        st.teachers.add(tch1)
        self.assertEqual(str(st.teachers.all()[0]), 'Андрей Белый')
        self.print_info('Finish test_student_update')







