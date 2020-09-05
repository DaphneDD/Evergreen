from django.db import models
from datetime import datetime

#define positive tinyint
class PositiveTinyIntegerField(models.PositiveSmallIntegerField):
    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return "tinyint unsigned"
        else:
            return super(PositiveTinyIntegerField, self).db_type(connection)

class Candidate(models.Model):
    ID_TYPES = (
        ('passport', 'passport'),
        ('drivers_license', 'drivers_license'),
    )
    #id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    id_type = models.CharField(max_length=255, choices=ID_TYPES)
    id_number = models.CharField(max_length=255)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_type', 'id_number'], name='unique_ids')
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Test_Center(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number_of_stations = PositiveTinyIntegerField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    create_time = models.DateField()
    
    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=255)
    duration = models.TimeField()
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    candidates = models.ManyToManyField(Candidate, through='Test')

    def __str__(self):
        return f'{self.name} - {self.client.name}'

class Test(models.Model):
    STATUS_TYPES = (
        ('Registered', 'Registered'),
        ('Canceled', 'Canceled'),
        ('Checked in', 'Checked in'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    test_center = models.ForeignKey(Test_Center, on_delete=models.PROTECT)
    date = models.DateField()
    start_time = models.TimeField()
    status = models.CharField(max_length=30, choices=STATUS_TYPES)

    def __str__(self):
        return f'{self.date.strftime("%m-%d-%Y")} {self.start_time.strftime("%H:%M")} {self.exam.name} {self.candidate.first_name} {self.candidate.last_name}'