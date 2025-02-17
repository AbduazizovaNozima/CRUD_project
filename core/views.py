from django.shortcuts import render

from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

def student_list(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'Student': students})

def student_view(request):
    return HttpResponse("Student page")

def new_student(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        age = request.POST.get("age")
        degree = request.POST.get("degree")
        birth_date = request.POST.get("birth_date")

        # Ma'lumotlar bazasiga yangi student qo'shish
        Student.objects.create(
            full_name=full_name,
            age=age,
            degree=degree,
            birth_date=birth_date,
        )

        # Ma'lumotlar muvaffaqiyatli saqlandi xabari
        return HttpResponse("Ma'lumotlar muvaffaqiyatli saqlandi")

    # Agar POST so'rovi bo'lmasa, bo'sh forma yoki boshqa ma'lumotlar qaytariladi
    return render(request, "index.html")
