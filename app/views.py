from django.shortcuts import render
from .models import WEEK, Questions
import random

# Create your views here.
def home(request):
    question = Questions.objects.all().values('question')
    questions = random.choices(question, k=5)
    questions = [value for question in questions for key, value in question.items()]

    return render(request,"home.html",{"questions":questions})

