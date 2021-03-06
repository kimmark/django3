from django.shortcuts import render

'''
views.py: View의 기능을 하는 클래스.함수를 정의하는 파일
render(): 웹 클라이언트에게 HTML파일을 전달할 때 사용하는 함수

뷰함수 정의시, 첫번째 매개변수를 무조건 request로 설정해야함
request: 웹클라이언트에 대한 정보(요청정보, <form>로 넘겨준 데이터, 로그인 정보, 세션정보, 요청방식(GET,POST))를 저장한 변수

'''
#메인페이지 담당 View함수 생성
def index(request):
    return render(request,'bookmark/main.html',
                  {"a":50,"b":[1,2,3,4]})
#북마크 폴더안에 HTML 파일을 request(사용자의 모든정보)에게 보내겠다.


#사용할 북마크 모델 클래스 임포트
from bookmark.models import Bookmark
#Bookmark 객체 리스트 화면에 출력
def book_list(request):
    '''
        모델 클래스를 데이터베이스 저장돤 객체 가져오기
    Bookmark.objects.all(): 데이터베이스에 해당 모델클래스의 객체를 모두 추출    
    Bookmark.objects.get(): 데이터베이스에 특정조건을 만족하는 객체 한개를 추출
    Bookmark.objects.filter(): 특정조건을 만족하는 모든객체 추출
    Bookmark.objects.exclude(): 특정조건을 만족하지 않는 모든객체 추출
    '''
    #데이터베이스에 저장된 모든 Bookmark객체를 objs변수에 저장
    objs=  Bookmark.objects.all()
    print('데이터베이스에 저장된 객체들',objs)
    return render(request,'bookmark/book_list.html',{"list":objs})


#Bookmark 객체 중 한개를 화면에 출력
#뷰함수에서 매개변수를 추가할 때 마다 URLConf의  URL설정에서 추가설정을 해야함
def book_one(request,book_idx):
    #book_idx: 북마크 객체의 id변수값(자동으로 저장됨)
    #Bookmark 객체들 중 id변수값이 book_idx값과 동일한 객체를 찾아 obj 변수에 저장
    #단, 조건을 만족하는 객체가 2개 이상이거나 0개일 경우 웹서버의 코드오류(500대 에러)가 발생
    obj = Bookmark.objects.get(id=book_idx)
    return render(request,'bookmark/book_one.html',{"a":obj})
    