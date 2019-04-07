#app_name: 서브 URL Conf의 그룹명
#urlpatterns: path 함수를 이용해 URL과 뷰함수등록
from django.urls.conf import path
from vote.views import *

#기본 도메인 주소:127.0.0.1:8000/vote/
#vote의 URL을 여기서 다 받아서 한꺼번에 전달하기로 했기때문에 기본vote/가 붙는다
app_name='vote'
urlpatterns=[
    path('',index,name='index'),
    #127.0.0.1:8000/vote/숫자
    path('<int:q_id>',detail,name='detail'),
    #127.0.0.1:8000
    path('result/<int:q_id>',result,name='result'),
    ]