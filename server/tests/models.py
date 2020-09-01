from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    id_type = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_type', 'id_number'], name='unique_ids')
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name