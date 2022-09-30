from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    # order_by('-pub_date')[:5] : 등록 날짜 기준 내림차순 정렬 후 앞에서 5개까지만
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    # 지난 실습에서 render() 함수의 {~:~} 로 html 파일에게 넘겨주던 dict를 context라고 부릅니다.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) 


def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question':q})


def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))
