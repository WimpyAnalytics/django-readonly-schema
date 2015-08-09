from django.db import models

# Manually created the output of
# manage.py inpectdb --database legacy


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
