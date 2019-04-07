from django.db import models
from django.db.models.fields.related import ForeignKey

#카테고리
class Category(models.Model):
    name=models.CharField('카테고리',max_length=20)
    def __str__(self):
        return self.name
#글쓴이를 외래키로 지정하기 위한 User모델클래스 임포트
from django.contrib.auth.models import User
#글
#카테고리<<Category 외래키 사용>>,글 제목,글쓴이<<외래키 사용>>,글 내용,작성일 
class Post(models.Model):
    #Cateogry 모델클래스와 1:n 관계로 연결
    #연결된 Category 객체가 삭제되려고 할때, Post객체가 연결되있으면 삭제가 안되도록 설정
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    headline=models.CharField('제목',max_length=200)
    #User모델 클래스와 1:n 관계로 연결
    #CASCADE: User객체가 삭제되면 연결된 Post객체도 같이 삭제되도록 설정
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    
    #TextField: 글자수 제한이 없는 문자열 저장공간
    #default 외에 XXXField에서 사용할수있는 매개변수
    #null(기본값: False): True값을 저장하면 데이터베이스에 객체 저장시 해당 변수값이 비어있어도 저장되도록 허용
    #blank(기본값 False): True값을 저장하면 폼객체를 통한 사용자 입력공간(<input>)제공 시 해당변수으 입력공간을 빈칸으로 허용
    #사용자가 입력하지 않아도 되고 값이 비어있어도 데이터베이스에 저장되도록 설정
    content=models.TextField('내용',null=True,blank=True)
    
    #auto_now_add(DateTimeField,DateField만 사용가능)
    #객체 생성시 서버기준의 날짜,시간이 자동으로 저장되도록 설정하는 매개변수
    pub_date=models.DateTimeField('작성일',auto_now_add=True)
    
    def __str__(self):
        return self.headline
    
    class Meta:
        #최신글 순으로 정렬(pub_date값을 내림차순 정렬)
        ordering=['-pub_date']
        
#글에 포함된 이미지 정보
#Post-외래키,이미지저장변수 
class PostImage(models.Model):
    #CASCADE:연결된 글이 지워지면, 이미지 객체도 같이 삭제되도록 설정
    post=ForeignKey(Post,on_delete=models.CASCADE)
    
    #ImageField: 이미지 파일을 저장하는 변수
    #필수매개변수 
    #upload_to: 실제 파일이 저장되는 경로를 지정하는 매개변수이고 서버기준의 날짜,시간데이터를 포함시킬수 있음
    # %Y: 서버기준의 년도를 입력  %n: 서버기준의 월  %d: 서버기준의 일
    #객체 생성 시 , 실제 images/년도/월/일/폴더 에 저장된다
    image=models.ImageField('이미지파일',upload_to='images/%Y/%m/%d')
    
#글에 포함된 첨부파일 정보
class PostFile(models.Model):
    post=ForeignKey(Post,on_delete=models.CASCADE)
    
    #FileField: 모든 파일을 저장할수 있는 저장공간(한글문서,실행파일,이미지파일 등)
    file=models.FileField('첨부파일',upload_to='files/%Y/%m/%d')
    
#ImageField를 사용하려면 Pillow 모듈이 파이썬에 설치되있어야함
#Pillow:파이썬에서 이미지처리할때 사용하는 대표적인 모듈
#pip install Pillow













