from vege.models import *
from faker import Faker
import random
from django.http.response import HttpResponse

fake = Faker()


def seedStudents(request):
    for _ in range(100):
        department_objs = Department.objects.all()
        department = department_objs[random.randint(0, len(department_objs)-1)]
        student_id = StudentID.objects.create(
            student_id=f"STU-0-{random.randint(100,9999)}"
        )
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(18, 100)
        student_address = fake.address()
        student = Student.objects.create(
            department=department,
            student_id=student_id,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address,
        )
        
        student.save()
        print(f"student saved.{{_}}....")
    
    return HttpResponse('student saved')
