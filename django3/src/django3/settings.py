

import os
from django.urls.base import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#로그인 페이지가 있는 URL주소
LOGIN_URL=reverse_lazy('cl:signin')

#로그인에 성공한 뒤 이동할 URL 주소 저장 변수
#소셜로그인을 사용한 클라이언트가 이동할 주소를 저장하는 용도
LOGIN_REDIRECT_URL= reverse_lazy('vote:index')
'''
reverse_lazy 와 reverse 공통점
공통점: 등록된 URL의 별칭을 바탕으로 URL을 찾는 함수
차이점: URL을 반환하는 시기
reverse: 함수 호출이 되자마자 등록된 URL에서 찾음
reverse_lazy: 웹서버가 정상적으로 실행된 뒤에 등록된 URL을 찾음
setting.py는 웹서버가 실행되기위한 설정값이 있는 파일이므로 URL Conf가 설정되지 않은 상태. 따라서 reverse를 사용할수 없다.
'''


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dyin(-h$ja@zfsd@5kx==0u@)vd9xn2w66o)7bfj#mnp_hy=v#'

# SECURITY WARNING: don't run with debug turned on in production!

#개발이 끝나면 DEBUG 변수에 False값을 저장하여 에러코드를 숨김
DEBUG = False
#도메인주소(127.0.0.1:8000)만 웹서버에 접속할수 있도록 설정하는 변수
#웹 클라이언트는 127.0.0.1이나 XXX.pythonanywhere.com으로 시작하는 웹 주소만 웹서버에 접속할수 있음
ALLOWED_HOSTS = ['127.0.0.1','.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark',
    'vote',
    'customlogin',
    #소셜로그인 관련된 어플리케이션
    'social_django',
    'blog',
    
]

#인증 관련 모듈을 추가
AUTHENTICATION_BACKENDS= (
    #구글로그인 처리 관련 파이썬 클래스 추가
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    #소셜로그인 저보를 Django의 User모델클래스에 저장처리하는 클래스
    'django.contrib.auth.backends.ModelBackend'
    )
#구글 개발자 사이트에서 발급한 ID,PW저장변수
SOCIAL_AUTH_GOOGLE_PLUS_KEY='236191075663-mgl33k2r8ubvlmbkejclqqshtebp7qcd.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET='XV8iRTZORlXMwRrjoRKvfq16'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #소셜로그인 처리를 위한 템플릿 관련함수 추가
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'django3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#사용자가 업로드한 미디어파일(이미지,첨부파일)을 다운받을 수 있도록 설정
#MEDIA_URL: 클라이언트가 URL주소로 파일을 요청할 때 사용하는 URL저장변수
#MEDIA_ROOT: 실제 파일이 저장되는 하드웨어 경로

#웹 클라이언트의 URL이 127.0.0.1:8000/files/로 시작하면 파일을 요청하는것으로 판단한다
MEDIA_URL='/files/'
#BASE_DIR: 현재 웹서버 프로젝트가 위치한 하드웨어 경로
#os.path,join: 파일경로를 생성하는 함수
MEDIA_ROOT= os.path.join(BASE_DIR,'files')

#Ex.
#클라이언트가 127.0.0.1:8000/files/test/1.jpg로 요청하면
#웹서버 프로젝트가 있는 폴더의 files/test/1.jpg 파일을 클라이언트에게 전송한다.



