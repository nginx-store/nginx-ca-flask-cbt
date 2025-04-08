# NGINX 자격증 CBT 애플리케이션

NGINX 자격증 준비를 위한 모의 CBT(Computer Based Test) 웹 애플리케이션입니다. 이 애플리케이션은 F5 NGINX 자격증 시험을 준비하는 사용자들이 문제를 풀고 연습할 수 있는 환경을 제공합니다.

## 기능

- 챕터별 문제 풀이: NGINX 자격증의 각 챕터별 문제를 선택하여 풀 수 있습니다.
- 시간 제한 모드: 실제 시험과 유사한 시간 제한 환경에서 문제를 풀 수 있습니다.
- 결과 분석: 시험 후 결과를 분석하고 오답 노트를 확인할 수 있습니다.
- 최근 성적 관리: 최근 시험 성적을 저장하고 확인할 수 있습니다.

## 기술 스택

- Flask: 웹 애플리케이션 프레임워크
- JavaScript: 클라이언트 측 기능 구현
- Bootstrap: 반응형 UI 구현
- HTML/CSS: 웹 페이지 구조 및 스타일링

## 설치 방법

### 사전 요구사항

- Python 3.7 이상
- pip (Python 패키지 관리자)

### 설치 단계

1. 저장소 클론:
   ```bash
   git clone https://github.com/yourusername/nginx-ca-flask-cbt.git
   cd nginx-ca-flask-cbt
   ```

2. 가상 환경 생성 및 활성화:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. 필요한 패키지 설치:
   ```bash
   pip install -r requirements.txt
   ```

## 실행 방법

1. 가상 환경이 활성화된 상태에서 다음 명령어 실행:
   ```bash
   python run.py
   ```

2. 웹 브라우저에서 `http://127.0.0.1:5000/` 접속

## 프로젝트 구조

```
nginx-ca-flask-cbt/
├── app/                    # 애플리케이션 코드
│   ├── models/             # 데이터 모델
│   │   └── quiz_data.py    # 문제 데이터 및 모델
│   ├── routes/             # 라우트 정의
│   │   └── quiz_routes.py  # 퀴즈 관련 라우트
│   ├── static/             # 정적 파일 (CSS, JavaScript)
│   │   ├── css/            # 스타일시트
│   │   └── js/             # JavaScript 파일
│   ├── templates/          # HTML 템플릿
│   │   ├── base.html       # 기본 템플릿
│   │   ├── index.html      # 메인 페이지
│   │   ├── quiz.html       # 퀴즈 페이지
│   │   └── result.html     # 결과 페이지
│   ├── __init__.py         # 애플리케이션 팩토리
│   └── config.py           # 설정 파일
├── requirements.txt        # 필요한 패키지 목록
└── run.py                  # 애플리케이션 실행 스크립트
```

## 사용자 가이드

1. 메인 페이지에서 시험 과목 선택
2. "시험 시작하기" 버튼 클릭
3. 주어진 시간 내에 문제 풀기
4. "제출하기" 버튼을 클릭하여 결과 확인
5. 결과 페이지에서 점수 및 오답 확인

## 개발 가이드

### 새로운 문제 추가하기

새로운 문제를 추가하려면 `app/models/quiz_data.py` 파일의 `quiz_data` 딕셔너리에 문제를 추가합니다:

```python
{
    "question": "문제 내용",
    "options": ["선택지1", "선택지2", "선택지3", "선택지4"],
    "answer": 정답_인덱스,  # 0부터 시작하는 인덱스
    "explanation": "답변 설명"
}
```

## 라이센스

이 프로젝트는 MIT 라이센스 하에 제공됩니다.

## 개발자 정보

- 개발: **[DevBinx](https://github.com/DevBinx)**
- 이메일: devbinx.dev@gmail.com or jbkim@itian.co.kr

## 변경 로그

### 버전 1.0.0 (2025-04-01)
- 초기 릴리스
- 기본 퀴즈 기능 구현
- 결과 저장 및 분석 기능

### 버전 1.0.1 (2025-04-08)
- F5N1 문제 추가 (10문제)
- 퀴즈 도중 홈으로 돌아가는 버튼 추가
