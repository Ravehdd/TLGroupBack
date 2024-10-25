from django.db import models


class Subdivision(models.Model):
    subdiv_name = models.CharField(max_length=255)


class Role(models.Model):
    role_name = models.CharField(max_length=255)


class Employees(models.Model):
    subdivision = models.ForeignKey(Subdivision, default=None, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, default=None, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    salary = models.IntegerField()
    hiring_date = models.DateTimeField(auto_now_add=True, null=True)


