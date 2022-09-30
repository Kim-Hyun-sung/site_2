from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model): # DB Table for 설문조사 주제
    question_text = models.CharField(max_length=200) # 설문조사 주제 텍스트
    pub_date = models.DateTimeField('date published') # ‘date published’ : 관리자 페이지에서 보여질 항목명
    
    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return f"{self.pk}번\n 글: {self.question_text} \n 날짜 :{self.pub_date}"
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

class Choice(models.Model): # DB Table for 설문조사 주제별 선택지 (+ 선택지마다의 득표 수)
    # 자동으로 Question table의 Primary key를 Foreign Key로 세팅
    # on_delete=models.CASCADE : Question(질문) 항목 삭제 시 관계된 선택지들도 모두 자동 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 설문조사 주제의 id 값
    choice_text = models.CharField(max_length=200) # 설문조사 주제에 대한 선택지 텍스트
    votes = models.IntegerField(default=0) # 해당 선택지의 득표 수
    
    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return f"{self.pk}번\n 질문: {self.question} \n 글  :{self.choice_text} \n 투표 :{self.votes}"