import random
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class Index(APIView):
    def get(self, request):
        first_names = ["Александр", "Евгений", "Иван", "Николай", "Павел", "Сергей", "Тимур", "Ульян", "Владимир",
                       "Геннадий"]
        middle_names = ["Кузнецов", "Иванов", "Смирнов", "Попов", "Михайлов", "Колесников", "Белов", "Соколов", "Лебедев",
                      "Захаров"]
        last_names = ["Сергеевич", "Максимович", "Витальевич", "Олегович", "Дмитриевич"]

        for i in range(1, 30000):
            # subdivision = Subdivision.objects.get(id=i)  # Предполагаем, что у нас есть модели Subdivision
            subdivision = Subdivision.objects.get(id=random.randint(1, 25))  # Предполагаем, что у нас есть модели Subdivision

            role = Role.objects.get(id=30)  # Предполагаем, что у нас есть модель Role

            full_name = random.choice(middle_names) + " " + random.choice(first_names) + " " + random.choice(last_names)

            employee = Employees.objects.create(
                subdivision=subdivision,
                role=role,
                full_name=full_name,
                salary=random.randint(1000, 1000000)
            )

        return Response(employee)

class EmployeeAPIView(generics.ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = IndexSerializer


class SubdivisionRolAPIView(APIView):
    def get(self, request):
        subdivision = list(Subdivision.objects.all().values())
        role = list(Role.objects.all().values())
        data = {
            "subdivisions": subdivision,
            "roles": role
        }
        return Response(data)





