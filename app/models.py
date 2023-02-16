from django.db import models
WEEK =  [
    "WEEK1",
    "WEEK2",
    "WEEK3"
]

class Questions(models.Model):
    week= models.CharField(max_length=30,choices=zip(WEEK,WEEK),default="WEEK1")
    question = models.TextField()



