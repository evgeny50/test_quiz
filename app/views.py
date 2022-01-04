from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.http import HttpResponse

from .forms import AddQuestionForm, CreateUserForm
from .models import QuesModel


def home(request):
    return render(request, 'app/home.html')

ANSWER = {}


def paginator(request):
    quiz_list = QuesModel.objects.all()
    paginator = Paginator(quiz_list, 1)

    page_number = request.GET.get('quiz')
    page_obj = paginator.get_page(page_number)

    question = quiz_list[int(page_number) - 1]
    if page_number is None:
        question = quiz_list[0]
    context = {'page_obj': page_obj,
               'question': question,
               'page_number': page_number
               }

    return context


def quiz(request):
    page_obj = paginator(request)
    if request.method == 'POST':
        answer = ', '.join(request.POST.getlist(page_obj['question'].question))
        ANSWER[int(page_obj['page_number']) - 1] = answer
        context = {
            'page_obj': page_obj['page_obj'],
            'question': page_obj['question']
        }
        return render(request, 'app/quiz.html', context)
    else:
        context = {
            'page_obj': page_obj['page_obj'],
        }
        return render(request, 'app/quiz.html', context)


def count_result(request):
    score = 0
    all_questions = QuesModel.objects.all()
    for num, obj in enumerate(all_questions):
        print(obj.ans)
        print(ANSWER[num])
        if obj.ans == ANSWER[num]:
            score += 1
    return render(request, 'app/result.html', {'score': score * 20})
