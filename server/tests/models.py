from django.db import models

class Candidate(models.Model):
    ID_TYPES = (
        ('passport', 'passport'),
        ('drivers_license', 'drivers_license'),
    )
    #id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    id_type = models.CharField(max_length=255, choices=ID_TYPES)
    id_number = models.CharField(max_length=255)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_type', 'id_number'], name='unique_ids')
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# define positive tinyint
class PositiveTinyIntegerField(models.PositiveSmallIntegerField):
    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return "tinyint unsigned"
        else:
            return super(PositiveTinyIntegerField, self).db_type(connection)

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateField()

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=255)
    duration = models.TimeField()
    description = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    candidates = models.ManyToManyField(Candidate, through='Test', related_name='exams')

    def __str__(self):
        return f'{self.name} - {self.client.name}'

class Test_Center(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number_of_stations = PositiveTinyIntegerField()
    exams = models.ManyToManyField(Exam, through='Test', related_name='test_centers')
    candidates = models.ManyToManyField(Candidate, through='Test', related_name='test_centers')

    def __str__(self):
        return self.name

class Test(models.Model):
    STATUS_TYPES = (
        ('Registered', 'Registered'),
        ('Canceled', 'Canceled'),
        ('Checked in', 'Checked in'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )
    exam = models.ForeignKey(Exam, related_name='tests', on_delete=models.PROTECT)
    candidate = models.ForeignKey(Candidate, related_name='tests', on_delete=models.PROTECT)
    test_center = models.ForeignKey(Test_Center, related_name='tests', on_delete=models.PROTECT)
    date = models.DateField()
    start_time = models.TimeField()
    status = models.CharField(max_length=30, choices=STATUS_TYPES)

    def __str__(self):
        return f'{self.date.strftime("%m-%d-%Y")} {self.start_time.strftime("%H:%M")} {self.exam.name}'