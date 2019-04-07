from django.shortcuts import render, get_object_or_404
from vote.models import Question,Choice
from django.http.response import HttpResponseRedirect
#질문 리스트
def index(request):
    #DB에 저장된 Question 객체 추출
    objs=Question.objects.all()
    #index.html 파일에 Question 객체 리스트 전달 및 클라이언트에게 HTML파일 전송
    return render(request,'vote/index.html',{"objs":objs})
#질문 선택 및 투표처리
#q_id: 사용자가 선택한 Question 객체의 id변수값
def detail(request,q_id):
    #클라이언트의 요청방식에 따른 코드 처리
    #GET-> 설문조사 HTML제공/ POST-> 실제 투표 반영
    #request.medthod: "GET" "POST" 중 웹클라이언트가 요청한 처리방식의 문자열이 저장됨
    if request.method=="GET":
        #get_object_or_404(모델클래스,조건)
        #모델클래스에 조건을 검색해 1개의 객체를 추출/만약 객체가 없는경우,
        #클라이언트의 잘못된 접근으로 판단해 뷰함수를 종료하고 404번 에러코드전달하는 함수
        
        #Question객체 중 q_id와 같은 객체 추출.없으면 404번 에러코드 전달
        obj=get_object_or_404(Question,id=q_id)
       
        '''
          모델클래스 A의 객체 .모델클래스B_set: A모델 클래스와 B모델클래스가 1:n관계(외래키연결)인 경우, 해당 A객체와
          연결된 B객체들을 대상으로 get(),all(),exclude(),filter()함수륻은 사용할수 있음
        Question모델클래스와 Choice 모델클래스는 1:n관계이므로, Question 객체들은 자신과 연결된Choice 객체들을 대상으로 
        get,all,exclude,filter를 사용할수 있음
        '''
        #obj(Question객체)와 연결된 Choice객체를 모두 추출
        c_list=obj.choice_set.all()
        
        return render(request,'vote/detail.html',{'q':obj,'c':c_list})
    
    #POST요청에 대한 처리(투표 반영)
    elif request.method=="POST":
        #a: Choice객체 id변수값
        '''
        1)request.GET: 사용자가 GET방식으로 요청할 때 넘어온 데이터가 저장된 변수(사전형)
        2)request.POST: 사용자가 POST방식으로 요청할 때 넘어온 데이터가 저장된 변수(사전형)
        '''
        #<form>에서 넘어온 a변수값 추출
        c_id=request.POST.get('a')
        #id값으로 Choice 한개 추출
        c= get_object_or_404(Choice,id=c_id)
        #투표수 증가
        c.votes+=1
        #데이터베이스 증가
        c.save() #변수값이 변경된 것을 데이터 베이스에 알려줌
        #result 뷰의 링크를 전달
        #c.q: Choice 객체가 연결한 Question 객체
        #c.q.id: Choice 객체가 연결한 Question 객체의 id변수값
        url="/vote/result/%d"%c.q.id
        #HttpResponseRedirect(URL주소):웹클라이언트에게 다른 인터넷 주소를 넘겨준다
        #                             웹클라이언트는 넘겨받은 인터넷주소로 다시 요청
        return HttpResponseRedirect(url)
        
#설문 결과 출력페이지
def result(request,q_id):
    #Question 객체를 추룰(id=q_id)
    q=get_object_or_404(Question,id=q_id)
    #result.html에 데이터 전송 및 클라이언트에게 전달
    return render(request,'vote/result.html',{'q':q})
    
    
    
