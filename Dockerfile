# Python 3.9 베이스 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 먼저 복사하여 종속성 설치
# 이렇게 하면 코드가 변경되어도 캐시된 레이어를 재사용할 수 있음
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 애플리케이션 코드 복사
COPY . .

# 환경 변수 설정
ENV FLASK_APP=run.py
ENV HOST=0.0.0.0
ENV PORT=5000
ENV DEBUG=False

# 포트 노출
EXPOSE 5000

# 애플리케이션 실행 명령
CMD ["python", "run.py"]