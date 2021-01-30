from django.db import models

# Create your models here.


class Block(models.Model):
    """
    Description of BCS blocks table
    """
    height = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=300)
    timestamp = models.IntegerField()
    miner = models.CharField(max_length=300)
    number_of_transactions = models.IntegerField()

    def __str__(self):
        return f"{self.height}, {self.hash}"
