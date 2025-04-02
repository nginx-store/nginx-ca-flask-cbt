"""
퀴즈 데이터 모델
이 모듈은 NGINX CBT 퀴즈 데이터를 저장합니다.
"""

# 문제 데이터
quiz_data = {
    "F5N1": [
        {
            "question": "NGINX가 API Gateway로 사용될 때 가장 중요한 기능은?",
            "options": ["FTP 포워딩", "DNS 캐싱", "메일 릴레이", "TLS 종료"],
            "answer": 3,
            "explanation": "API Gateway로 동작할 때 가장 중요한 기능 중 하나는 TLS 종료(SSL termination)입니다. 이는 클라이언트와의 보안 통신을 처리하는 핵심 역할입니다."
        },
        {
            "question": "nginx.conf 내 include 문이 적용되는 위치는?",
            "options": ["server 블록 내부", "location 블록 내부", "http 블록 내부", "mime.types 파일 내부"],
            "answer": 2,
            "explanation": "include 문은 일반적으로 http 블록 안에서 사용되어 server 블록 등을 포함시킬 수 있습니다."
        }
    ],
    "F5N2": [
        {
            "question": "proxy_cache_path에서 zone을 선언하는 목적은?",
            "options": ["캐시 경로 지정", "zone 용량 제한", "프로세스 간 캐시 공유", "캐시 시간 설정"],
            "answer": 2,
            "explanation": "shared memory zone은 여러 워커 프로세스 간에 캐시 상태를 공유하기 위해 필요합니다."
        },
        {
            "question": "add_header와 proxy_set_header의 차이점은?",
            "options": ["기본 헤더 설정 여부", "응답 vs 요청 헤더 조작", "TLS 관련 여부", "캐시 설정 여부"],
            "answer": 1,
            "explanation": "add_header는 응답 헤더 조작, proxy_set_header는 프록시 요청 헤더를 조작합니다."
        }
    ],
    "F5N3": [
        {
            "question": "TLS 1.2만 허용하도록 설정하려면 어떤 디렉티브를 사용하는가?",
            "options": ["ssl_certificate", "ssl_protocols", "ssl_ciphers", "ssl_session_cache"],
            "answer": 1,
            "explanation": "ssl_protocols 디렉티브를 통해 TLS 1.2만 허용하도록 설정할 수 있습니다."
        },
        {
            "question": "access_log를 끄는 방법은?",
            "options": ["access_log off;", "access_log none;", "disable_log;", "log_off;"],
            "answer": 0,
            "explanation": "access_log off; 를 통해 로그 출력을 비활성화할 수 있습니다."
        }
    ],
    "F5N4": [
        {
            "question": "nginx -s reload와 -s stop의 차이점은?",
            "options": ["둘 다 동일하다", "reload는 설정 재적용, stop은 종료", "stop은 재시작 포함", "reload는 로그 초기화"],
            "answer": 1,
            "explanation": "reload는 설정 파일을 다시 읽고 프로세스를 재시작 없이 갱신하고, stop은 NGINX 프로세스를 종료합니다."
        },
        {
            "question": "TLS 연결 오류 중 ERR_CERT_DATE_INVALID는 어떤 문제인가?",
            "options": ["포트 충돌", "인증서 만료", "키 손상", "프록시 오류"],
            "answer": 1,
            "explanation": "ERR_CERT_DATE_INVALID는 인증서 유효 기간이 만료되었거나 시간이 올바르지 않을 때 발생합니다."
        }
    ]
}

# 퀴즈 정보 조회 함수
def get_quiz_data(subject=None):
    """
    퀴즈 데이터를 조회합니다.
    
    Args:
        subject (str, optional): 조회할 과목 코드. None이면 전체 데이터 반환.
    
    Returns:
        dict or list: 퀴즈 데이터 딕셔너리 또는 특정 과목의 문제 리스트
    """
    if subject is None:
        return quiz_data
    
    return quiz_data.get(subject, [])

def get_quiz_subjects():
    """
    모든 퀴즈 과목 정보를 반환합니다.
    
    Returns:
        list: 과목 코드와 이름 딕셔너리 리스트
    """
    subjects = [
        {"code": "F5N1", "name": "NGINX Management (F5N1)"},
        {"code": "F5N2", "name": "Configuration: Knowledge (F5N2)"},
        {"code": "F5N3", "name": "Configuration: Demonstrate (F5N3)"},
        {"code": "F5N4", "name": "Troubleshooting (F5N4)"},
        {"code": "ALL", "name": "모든 챕터 통합 시험"}
    ]
    return subjects

def get_all_questions(max_questions=10):
    """
    모든 챕터에서 랜덤하게 문제를 선택합니다.
    
    Args:
        max_questions (int): 최대 문제 수
    
    Returns:
        list: 선택된 문제 리스트
    """
    import random
    
    all_questions = []
    for chapter in quiz_data:
        chapter_questions = quiz_data[chapter]
        all_questions.extend(chapter_questions)
    
    # 랜덤하게 문제를 선택
    return random.sample(all_questions, min(max_questions, len(all_questions)))

def get_subject_name(subject_code):
    """
    과목 코드에 해당하는 과목 이름을 반환합니다.
    
    Args:
        subject_code (str): 과목 코드
    
    Returns:
        str: 과목 이름
    """
    for subject in get_quiz_subjects():
        if subject["code"] == subject_code:
            return subject["name"]
    return subject_code
