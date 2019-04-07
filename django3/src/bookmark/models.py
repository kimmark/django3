from django.db import models

'''
1. models.py : 모델클래스를 정의할 때 사용하는 파일
2. model : MTV 패턴중 하나로 데이터베이스에 데이터를 저장할 형식 정의 및 데이터 추가/수정/삭제/조회 기능 제공한다.

model 클래스 개발 및 웹 프로젝트 반영 순서
1) 모델 클래스 정의 시, models.Model 클래스 상속 후 정의
2) 정의한 모델 클래스를  make migrations 명령으로  migrations 폴더에  migration 파일 저장
3) 저장된 migration 파일로  데이터베이스에  저장공간  생성(manage.py 파일에  migrate 명령)

'''

#북마크를 저장할 모델 클래스 
#즐겨찾기이름(파란글씨), 클릭 시 넘어갈 URL주소 

class Bookmark(models.Model):
    #모델 클래스 내에서 저장할 변수는 클래스 변수로 정의함
    #클래스 변수에 models.XXXXFields 클래스의 객체를 저장하는 것으로 저장공간 정의
    
    #CharField: 글자수 제한이 있는 문자열을 저장하는 공간
    #max_length<<필수>>: 최대글자 수를 지정할 수 있는 매개변수
    name= models.CharField(max_length=100) 
    
    #URLField: 인터넷 주소(URL)을 저장하는 공간   
    url=models.URLField()
    
    #--------------------클래스 상속후 정의 완료---------------------------------
    
    '''
     django3 우클릭 -> Django Make Migration -> 이름  bookmark -> Django Migrate  
    '''
    
    #def __str__: 객체를 출력할 때 (print(객체))
    #표현방식을 처리하는 파이썬 클래스 함수
    def __str__(self):
        return self.name
    #name에 들어간 이름으로 저장하겠다
    
    