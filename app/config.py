import os
from dotenv import load_dotenv

# .env 파일 로드 (있는 경우)
load_dotenv()

class Config:
    # 기본 설정
    SECRET_KEY = os.environ.get('SECRET_KEY', 'nginx-cbt-secure-secret-key')
    HOST = os.environ.get('HOST', '127.0.0.1')  # localhost로 변경
    PORT = int(os.environ.get('PORT', 5000))
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'  # 개발 모드 활성화
    
    # 사용자 정의 설정
    QUIZ_TIME = 30 * 60  # 30분(초 단위)
    MAX_RECENT_SCORES = 5  # 저장할 최근 점수 수
