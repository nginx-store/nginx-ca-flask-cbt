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
            "question": "NGINX 설치 후 기본 설정 파일이 위치하는 경로는?",
            "options": ["/usr/nginx/nginx.conf", "/opt/nginx/default.conf", "/etc/nginx/nginx.conf", "/usr/local/etc/nginx.conf", "/nginx/nginx.conf"],
            "answer": 2,
            "explanation": "대부분의 배포판에서 NGINX 기본 설정은 /etc/nginx/nginx.conf에 위치합니다."
        },
        {
            "question": "nginx -t 명령의 주요 목적은 무엇인가?",
            "options": ["로그 파일을 압축한다", "설정 파일을 테스트한다", "디렉터리 구조를 확인한다", "워커 프로세스를 중지한다", "업스트림 서버를 변경한다"],
            "answer": 1,
            "explanation": "nginx -t는 설정 파일 문법과 구성을 테스트합니다."
        },
        {
            "question": "다음 중 NGINX에서 로그 형식을 지정할 때 사용하는 디렉티브는?",
            "options": ["access_log_format", "log_profile", "log_format", "set_log_type", "format_log"],
            "answer": 2,
            "explanation": "log_format은 사용자 정의 로그 포맷을 설정합니다."
        },
        {
            "question": "다음 중 shared memory zone을 사용하는 기능은?",
            "options": ["FastCGI 구성", "캐시 키 메타데이터 저장", "에러 로그 출력", "listen 포트 지정", "디스크 용량 모니터링"],
            "answer": 1,
            "explanation": "캐시 키, 세션 데이터 등은 공유 메모리 zone에 저장됩니다."
        },
        {
            "question": "HTTPS 설정 시 반드시 필요한 두 가지 설정은?",
            "options": ["ssl_certificate, ssl_certificate_key", "ssl_mode, ssl_timeout", "ssl_session_cache, ssl_dhparam", "ssl_protocol, ssl_buffer_size", "ssl_proxy, ssl_session_id"],
            "answer": 0,
            "explanation": "인증서와 개인 키는 HTTPS 동작에 필수입니다."
        },
        {
            "question": "다음 중 proxy_pass 디렉티브의 역할은?",
            "options": ["정적 콘텐츠 제공", "DNS 캐시 활성화", "요청을 백엔드로 전달", "IP 차단 기능 제공", "브라우저 캐시 제어"],
            "answer": 2,
            "explanation": "proxy_pass는 리버스 프록시 기능으로 요청을 전달합니다."
        },
        {
            "question": "다음 중 업스트림 서버 그룹을 선언할 때 사용하는 블록은?",
            "options": ["server_group", "cluster", "backend", "upstream", "nodes"],
            "answer": 3,
            "explanation": "upstream 블록은 로드 밸런싱 대상 서버 그룹을 정의합니다."
        },
        {
            "question": "nginx -s reload 명령은 어떤 동작을 수행하는가?",
            "options": ["로그 파일 삭제", "설정을 다시 로드", "NGINX를 제거", "설정 오류 확인", "공유 메모리 초기화"],
            "answer": 1,
            "explanation": "reload는 설정을 중단 없이 적용합니다."
        },
        {
            "question": "다음 중 NGINX 설정에 오류가 있을 때 실행할 수 있는 명령은?",
            "options": ["nginx --diagnose", "nginx -reload -v", "nginx -t", "nginx --fix", "nginx --log-errors"],
            "answer": 2,
            "explanation": "설정 오류 확인에는 nginx -t가 사용됩니다."
        },
        {
            "question": "NGINX에서 클라이언트 IP 주소를 나타내는 변수는?",
            "options": ["$remote_ip", "$client_ip", "$ip_address", "$remote_addr", "$real_ip"],
            "answer": 3,
            "explanation": "$remote_addr는 클라이언트의 IP 주소를 담고 있습니다."
        },
        {
            "question": "설정 파일 내에서 여러 설정 파일을 포함하려면 어떤 디렉티브를 사용해야 하는가?",
            "options": ["source", "load", "require", "include", "import"],
            "answer": 3,
            "explanation": "include는 외부 파일을 현재 설정에 삽입합니다."
        },
        {
            "question": "nginx.conf에서 설정 파일 병합 순서에 영향을 주는 요소는?",
            "options": ["파일 확장자", "파일 이름의 알파벳 순", "작성자 권한", "디렉터리 이름", "gzip 설정 여부"],
            "answer": 1,
            "explanation": "와일드카드로 include 시 알파벳 순서로 병합됩니다."
        },
        {
            "question": "다음 중 NGINX 모듈이 수행하지 않는 역할은?",
            "options": ["SSL 종료", "요청 리디렉션", "URL 재작성", "물리 메모리 확장", "로깅 포맷 지정"],
            "answer": 3,
            "explanation": "모듈은 기능 확장에 사용되며, 시스템 리소스를 확장하지 않습니다."
        },
        {
            "question": "설정 변경 후 반영하지 않고 바로 에러 로그만 확인하려면 어떤 명령을 실행해야 하는가?",
            "options": ["nginx -s reload", "nginx --check", "nginx -t", "nginx --dry-run", "nginx -e"],
            "answer": 2,
            "explanation": "nginx -t는 설정만 검증하고 반영하지 않습니다."
        },
        {
            "question": "NGINX에서 캐시 저장 경로와 메모리 영역을 함께 설정하는 디렉티브는?",
            "options": ["cache_path_zone", "proxy_cache", "proxy_cache_path", "cache_zone", "fastcgi_cache_dir"],
            "answer": 2,
            "explanation": "proxy_cache_path는 디스크 경로 및 메모리 영역(zone)을 함께 정의합니다."
        },
        {
            "question": "NGINX에서 모듈을 비활성화하려면 어떻게 해야 하는가?",
            "options": ["설정 파일에서 disable_module 명령 사용", "모듈을 주석 처리하거나 컴파일 시 제외", "nginx -d 명령 실행", "module off; 선언", "실행 중에 kill -USR2"],
            "answer": 1,
            "explanation": "NGINX OSS는 동적 모듈 비활성화를 지원하지 않으므로 컴파일 시 제외하거나 설정에서 사용하지 않아야 합니다."
        },
        {
            "question": "NGINX 로깅에서 $request 변수는 무엇을 나타내는가?",
            "options": ["클라이언트의 쿠키", "요청 전체 라인 (메서드, URI, 버전 포함)", "리모트 포트", "SSL 핸드셰이크 정보", "캐시 HIT 여부"],
            "answer": 1,
            "explanation": "$request는 \"GET /index.html HTTP/1.1\" 과 같은 전체 요청 라인을 나타냅니다."
        },
        {
            "question": "HTTP 요청에서 정적 파일을 우선 제공하고, 없을 경우 오류 처리하려면 어떤 설정을 사용하는가?",
            "options": ["alias", "return", "try_files", "rewrite", "error_page"],
            "answer": 2,
            "explanation": "try_files는 요청된 파일이 있으면 반환하고, 없으면 다른 동작을 시도하거나 오류를 반환합니다."
        },
        {
            "question": "다음 중 NGINX에서 80 포트를 사용하기 위해 필요한 조건은?",
            "options": ["nginx.conf에 secure_port 선언", "루트 사용자로 실행되거나 CAP_NET_BIND_SERVICE 권한 필요", "TLS 인증서가 있어야 함", "default_server 설정 필요", "gzip 비활성화 상태여야 함"],
            "answer": 1,
            "explanation": "리눅스에서 1024 이하 포트는 루트 권한이 필요합니다."
        },
        {
            "question": "gzip 압축 설정 시 성능에 직접 영향을 주는 디렉티브는?",
            "options": ["gzip_mime_types", "gzip_buffers", "gzip_proxied", "gzip_comp_level", "gzip_vary"],
            "answer": 3,
            "explanation": "gzip_comp_level은 압축률을 조절하며, 높을수록 CPU 사용률이 증가합니다."
        },
        {
            "question": "다음 중 NGINX를 웹 서버로 사용할 때 적절한 설정은?",
            "options": ["proxy_pass http://backend;", "root /var/www/html;", "upstream backend {}", "stream {}", "ssl_verify_client on;"],
            "answer": 1,
            "explanation": "root 디렉티브는 요청된 URI에 대응하는 파일의 실제 경로를 지정합니다."
        },
        {
            "question": "NGINX에서 요청 제한 기능을 제공하는 모듈은?",
            "options": ["ngx_http_access_module", "ngx_http_limit_req_module", "ngx_http_autoindex_module", "ngx_http_auth_basic_module", "ngx_http_upstream_module"],
            "answer": 1,
            "explanation": "limit_req 모듈은 IP 기준 요청 속도를 제한합니다."
        },
        {
            "question": "다음 중 서버 블록 내에서만 사용할 수 있는 디렉티브는?",
            "options": ["worker_processes", "location", "server_name", "events", "user"],
            "answer": 2,
            "explanation": "server_name은 서버 블록에서 도메인 이름을 설정할 때 사용됩니다."
        },
        {
            "question": "listen 디렉티브에 대한 설명 중 옳은 것은?",
            "options": ["http 블록에만 위치할 수 있다", "로그 출력과 관련된 디렉티브다", "포트와 바인딩 주소를 지정한다", "static 파일 경로를 지정한다", "요청 메서드를 필터링한다"],
            "answer": 2,
            "explanation": "listen은 서버가 바인딩할 IP 주소와 포트를 지정합니다."
        },
        {
            "question": "다음 중 NGINX 구성에서 상속이 일어나는 블록 계층 구조는?",
            "options": ["stream → http → server", "main → server → location", "main → http → server → location", "http → mail → location", "mail → stream → events"],
            "answer": 2,
            "explanation": "설정은 main → http → server → location 순서로 상속됩니다."
        },
        {
            "question": "다음 중 정규 표현식을 기반으로 URI를 매칭하는 location 블록은?",
            "options": ["location /images/", "location ^~ /api/", "location = /index.html", "location ~ \\.php$", "location /"],
            "answer": 3,
            "explanation": "~는 정규 표현식을 사용한 location을 정의할 때 사용됩니다."
        },
        {
            "question": "NGINX 구성 시 디버깅 목적으로 사용되는 명령은?",
            "options": ["nginx -D", "nginx --debug", "nginx -t", "nginx -s trace", "nginx -vvv"],
            "answer": 2,
            "explanation": "설정 확인 및 디버깅은 nginx -t로 수행합니다."
        },
        {
            "question": "다음 중 에러 페이지를 사용자 정의 페이지로 전환하는 디렉티브는?",
            "options": ["return 404", "rewrite", "custom_error", "error_page", "status_code"],
            "answer": 3,
            "explanation": "error_page는 에러 발생 시 특정 URI로 리디렉션합니다."
        },
        {
            "question": "NGINX에서 기본적으로 제공되는 워커 프로세스 개수는?",
            "options": ["1", "2", "4", "auto", "CPU 개수에 따라 자동 설정"],
            "answer": 0,
            "explanation": "명시하지 않으면 기본 워커 프로세스 수는 1개입니다."
        },
        {
            "question": "다음 중 설정 오류나 동작 이상을 추적할 때 가장 먼저 확인해야 할 로그는?",
            "options": ["/var/log/messages", "/var/log/nginx/error.log", "/etc/nginx/access.log", "/var/log/syslog", "/usr/local/nginx/logs/debug.log"],
            "answer": 1,
            "explanation": "error.log는 설정 오류, 런타임 에러 등 주요 문제 정보를 제공합니다."
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