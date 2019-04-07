from django.db import models


#질문
#질문제목 (CHarField 100글자 제한),생성일(DateField)
class Question(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    
    def __str__(self):
        return self.title
    
 

#답변
#답변 항목 내용,투표수,어떤질문에 연결되있는지 철;

class Choice(models.Model):
    name=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    #default: 객체생성시 기본갑 설정하는 매개변수
   
    #Choice 모델 클래스가 Question 모델클래스와 1:n 관계를 가짐
    #Question 객체가 삭제되면 연결된 Choice 객체도 삭제됨(CASCADE)
    q=models.ForeignKey(Question,on_delete=models.CASCADE)
    
    #ForeignKey: 다른 모델클래스의 객체와 연결할수 있는 클래스
    #ForeignKey(연결할 다른 모델클래스, on_delete=삭제방식)
    #Choice 모델클래스의 q변수는 연결된 Question 객체와 동일 <ex. Choice객체.q.title(또는 pub_date,id)변수를 접근가능>
    #on_delete: 연결된 모델클래스의 객체가 삭제될 때 어떻게 처리할지 지정하는 변수
    #1) on_delete=models.PROTECT: 연결된 모델클래스의 객체가 삭제되지 않도록 막아주는 기능
    #2) on_delete=models.CASCADE: 연결된 모델클래스의 객체가 삭제되면 같이 삭제되는 기능
    #3) on_delete=models.SET_NULL:연결된 객체가 삭제되면 아무것도 연결하지 않은 상태 유지
    #4) on_delete=models.SET(연결할 객체): 연결된 객체가 삭제되면 매개변수로 넣은 객체와 연결
    #5) on_delete=models.SET_DEFAULT: 연결된 객체가 삭제되면 기본 설정된 객체와 연결
    def __str__(self):
        return self.name
    
    
    