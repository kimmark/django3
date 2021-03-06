'''
admin.py : 해당 어플리케이션에 정의된 모델클래스를 관리자사이트에서 데이터 추가.수정.삭제.조회를 할수 있도록 등록하는 파일

등록순서
1) models.py 임포트
2) admin.site.register(임포트된 모델클래스 명)
'''

#blog 폴더에  models.py 안에 있는 모든 클래스 임포트
from blog.models import *
from django.contrib import admin

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostFile)
admin.site.register(PostImage)


