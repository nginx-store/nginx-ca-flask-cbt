"""
퀴즈 데이터 모델 - F5N1 카테고리 문제 추가
"""

# 기존 F5N1 카테고리에 문제를 추가합니다.
# 기존 데이터 구조를 참고하여 같은 형식으로 추가합니다.

# 문제 데이터
quiz_data = {
    "F5N1": [
        # 추가되는 10개 문제
        {
            "question": "NGINX가 API Gateway로 사용될 때 가장 중요한 기능은?",
            "options": ["SSL 종료", "캐싱", "부하 분산", "요청 라우팅", "인증 및 인가"],
            "answer": 3,
            "explanation": "API Gateway로서 NGINX의 가장 중요한 기능은 요청 라우팅입니다. 마이크로서비스 아키텍처에서 API Gateway의 핵심 책임은 클라이언트 요청을 적절한 백엔드 서비스로 라우팅하는 것입니다."
        },
        {
            "question": "NGINX에서 공유 메모리 존은 어떤 상황에 필요할까?",
            "options": ["HTTP 헤더 분석을 위해", "SSL 인증서 로드를 위해", "디렉티브 상속을 위해", "정적 파일 제공을 위해", "워커 프로세스 간 데이터 공유를 위해"],
            "answer": 4,
            "explanation": "여러 워커 프로세스가 있는 NGINX 인스턴스에서 IP 기반 속도 제한을 구현하려면, 모든 워커가 클라이언트별 요청 횟수를 공유해야 합니다. 이를 위해 공유 메모리 존이 필요합니다."
        },
        {
            "question": "NGINX가 특정 사용자 권한으로 실행되도록 하려면 어떤 설정이 필요한가?",
            "options": ["systemctl 에서 설정", "nginx -s reload로 user 설정", "nginx.conf 최상위에 user 설정", "server 블록에서 user 설정", "location 블록에서 user 설정"],
            "answer": 2,
            "explanation": "NGINX가 특정 사용자 권한으로 실행되도록 하려면 nginx.conf 파일의 메인 컨텍스트(최상위 레벨)에 user 디렉티브를 설정해야 합니다."
        },
        {
            "question": "Web Server와 Reverse Proxy의 차이점은?",
            "options": ["Web Server는 요청을 직접 처리하고, Reverse Proxy는 백엔드로 전달한다", "둘 다 상태 정보를 유지한다", "Web Server는 요청을 프록시로 전달한다", "Reverse Proxy는 정적 파일만 제공한다", "둘 다 백엔드 서버로 요청을 전달한다"],
            "answer": 0,
            "explanation": "웹 서버와 리버스 프록시는 모두 NGINX의 주요 사용 사례이지만, 그 역할과 동작 방식에는 중요한 차이가 있습니다. Web Server는 정적 콘텐츠를 직접 제공하고, Reverse Proxy는 백엔드 요청을 중계합니다."
        },
        {
            "question": "설정 파일 병합 순서는 어떻게 되는가?",
            "options": ["nginx.conf 다음에 포함된 파일은 무시된다", "항상 server 블록이 먼저 적용된다", "context 순서와 무관하게 로드된다", "conf.d 파일만 우선 적용된다", "nginx.conf → include 순서로 알파벳 정렬 포함"],
            "answer": 4,
            "explanation": "NGINX 설정 파일 병합은 여러 파일의 내용을 하나의 실행 구성으로 결합하는 과정입니다. 이 과정은 nginx.conf 파일을 먼저 처리한 후, include 디렉티브에 지정된 순서대로 파일을 포함합니다."
        },
        {
            "question": "사용자 권한 설정 시 주의할 점은?",
            "options": ["최소 권한 원칙을 준수하여 사용자 권한을 설정한다", "SSL 키 파일은 모든 사용자에게 읽기 권한을 준다", "워커 프로세스는 항상 root로 실행해야 한다", "마스터 프로세스가 로그 파일을 기록한다", "NGINX는 전용 사용자 계정을 사용할 수 없다"],
            "answer": 0,
            "explanation": "보안을 위해 최소 권한 원칙을 따르며, 디렉토리/파일 권한 및 SELinux 설정도 고려해야 합니다."
        },
        {
            "question": "NGINX의 마스터-워커 프로세스 모델에서 올바른 설명은?",
            "options": ["워커 프로세스는 root 권한으로 실행됨", "마스터 프로세스는 연결을 처리함", "마스터 프로세스는 설정을 읽고 워커를 관리함", "워커 프로세스는 설정 파일을 직접 로드함", "모든 프로세스는 동일한 권한으로 실행됨"],
            "answer": 2,
            "explanation": "NGINX는 마스터-워커 모델을 사용합니다. 마스터 프로세스는 root 권한으로 실행되어 설정을 읽고, 워커 프로세스를 생성하고 관리합니다. 워커 프로세스는 실제 연결을 처리하며 더 낮은 권한으로 실행됩니다."
        },
        {
            "question": "NGINX 로드 밸런싱에서 사용 가능한 알고리즘은?",
            "options": ["round-robin만 지원", "least_conn, ip_hash, least_time 모두 지원", "weighted round-robin만 지원", "TCP 연결은 밸런싱 불가", "UDP 연결만 밸런싱 가능"],
            "answer": 1,
            "explanation": "NGINX는 다양한 로드 밸런싱 알고리즘을 지원합니다. 기본값인 round-robin 외에도 least_conn(최소 연결), ip_hash(클라이언트 IP 기반 해싱), least_time(최소 응답 시간) 등을 지원합니다."
        },
        {
            "question": "NGINX Plus와 오픈 소스 NGINX의 주요 차이점은?",
            "options": ["성능 차이 없음", "설정 방식이 완전히 다름", "상업 지원 및 추가 기능", "오픈 소스는 리버스 프록시 기능 없음", "NGINX Plus는 캐싱을 지원하지 않음"],
            "answer": 2,
            "explanation": "NGINX Plus는 오픈 소스 NGINX의 상업 버전으로, 전문적인 지원, 고급 로드 밸런싱, 상태 모니터링, 회의 관리, JWT 지원 등의 추가 기능을 제공합니다."
        },
        {
            "question": "NGINX 설정 파일을 검증하는 명령어는?",
            "options": ["nginx -t", "nginx -c test", "nginx -verify", "nginx --check", "nginx validate"],
            "answer": 0,
            "explanation": "nginx -t 명령어는 설정 파일의 문법을 검사하고 파일 경로 문제 등을 확인합니다. 이는 설정 변경 후 NGINX를 다시 로드하기 전에 오류를 잡는 데 유용합니다."
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

# 퀴즈 정보 조회 함수들은 변경 없이 그대로 유지

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