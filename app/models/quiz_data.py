"""
퀴즈 데이터 모델 - F5N1 카테고리 문제 추가
"""

# 기존 F5N1 카테고리에 문제를 추가합니다.
# 기존 데이터 구조를 참고하여 같은 형식으로 추가합니다.

# 문제 데이터
quiz_data = {
    "F5N1": [
        {
            "question": "NGINX는 기본적으로 어떤 유형의 소프트웨어인가?",
            "options": ["데이터베이스 서버", "이메일 서버", "웹 서버 및 리버스 프록시 서버", "파일 동기화 도구", "컨테이너 오케스트레이터"],
            "answer": 2,
            "explanation": "NGINX는 고성능 웹 서버이자 리버스 프록시로 설계되었습니다."
        },
        {
            "question": "NGINX는 기본적으로 어떤 아키텍처를 기반으로 동작하는가?",
            "options": ["스레드 기반 아키텍처", "다중 마스터 구조", "이벤트 기반, 비동기 아키텍처", "블로킹 I/O 기반 아키텍처", "마이크로커널 구조"],
            "answer": 2,
            "explanation": "이벤트 기반 아키텍처 덕분에 NGINX는 고성능을 유지하면서 수천 개의 연결을 처리할 수 있습니다."
        },
        {
            "question": "다음 중 NGINX의 기본 프로세스 구조로 올바른 것은?",
            "options": ["워커만 실행되고 마스터는 존재하지 않는다", "하나의 마스터 프로세스와 여러 워커 프로세스로 구성", "모든 요청은 하나의 마스터 프로세스에서 처리됨", "프로세스 대신 스레드를 사용", "클라이언트마다 새로운 프로세스 생성"],
            "answer": 1,
            "explanation": "마스터는 설정 및 워커 관리, 워커는 실제 요청 처리 역할을 합니다."
        },
        {
            "question": "NGINX에서 설정 변경 후 서비스 재시작 없이 적용할 수 있는 명령은?",
            "options": ["systemctl restart nginx", "nginx -q", "nginx -s reload", "nginx --reapply", "nginx -refresh"],
            "answer": 2,
            "explanation": "nginx -s reload는 중단 없이 설정을 다시 로드합니다."
        },
        {
            "question": "다음 중 NGINX의 대표적인 사용 사례가 아닌 것은?",
            "options": ["정적 웹 콘텐츠 제공", "리버스 프록시 서버", "API 게이트웨이 역할", "패킷 스니핑", "로드 밸런싱"],
            "answer": 3,
            "explanation": "패킷 스니핑은 보안 분석 도구의 역할이며, NGINX의 기능이 아닙니다."
        },
        {
            "question": "NGINX가 리버스 프록시로 동작할 때의 기본 흐름은?",
            "options": ["클라이언트 → 프록시 → 백엔드 서버 → 프록시 → 클라이언트", "클라이언트 → 로컬 파일 시스템 → 응답", "클라이언트 → 백엔드 서버 → 로컬 캐시", "클라이언트 → 방화벽 → 스위치 → 서버", "프록시가 직접 응답을 반환하지 않음"],
            "answer": 0,
            "explanation": "리버스 프록시는 중간에서 요청을 전달하고 응답을 다시 클라이언트로 반환합니다."
        },
        {
            "question": "NGINX의 설정 파일 확장자는 일반적으로 무엇인가?",
            "options": [".json", ".yaml", ".conf", ".ini", ".xml"],
            "answer": 2,
            "explanation": "NGINX 설정 파일은 대부분 .conf 확장자를 사용합니다."
        },
        {
            "question": "NGINX는 어떤 운영 체제에서 가장 일반적으로 사용되는가?",
            "options": ["Windows 98", "macOS", "Linux", "DOS", "Android"],
            "answer": 2,
            "explanation": "Linux 환경에서 가장 널리 배포되며, 패키지 매니저를 통한 설치가 용이합니다."
        },
        {
            "question": "NGINX 로그 중 오류 메시지가 기록되는 파일은?",
            "options": ["/var/log/nginx/debug.log", "/etc/nginx/access.log", "/var/log/nginx/error.log", "/var/log/messages", "/usr/nginx/request.log"],
            "answer": 2,
            "explanation": "error.log는 설정 오류, 런타임 문제 등의 진단 정보를 제공합니다."
        },
        {
            "question": "다음 중 NGINX에서 서버 블록은 어떤 역할을 하는가?",
            "options": ["이벤트 루프 처리", "클라이언트 요청을 모니터링", "포트를 바인딩하고 도메인 별 처리", "커널에 설정을 전달", "네트워크 인터페이스 정의"],
            "answer": 2,
            "explanation": "server 블록은 가상 호스트처럼 도메인/포트 기반 요청 처리 단위입니다."
        },
        {
            "question": "NGINX에서 worker_processes auto; 설정의 의미는?",
            "options": ["항상 하나의 워커만 실행됨", "CPU 코어 수와 무관하게 워커 8개 실행", "CPU 코어 수만큼 워커 프로세스 자동 생성", "워커 프로세스가 스레드로 대체됨", "클라이언트 수에 따라 워커 수 동적 조정"],
            "answer": 2,
            "explanation": "auto는 머신의 CPU 코어 수를 감지하여 그에 맞게 워커 프로세스를 생성합니다."
        },
        {
            "question": "NGINX의 기본 동작 포트는 무엇인가?",
            "options": ["22", "443", "3306", "80", "21"],
            "answer": 3,
            "explanation": "HTTP의 기본 포트는 80이며, NGINX는 기본적으로 해당 포트에서 시작됩니다."
        },
        {
            "question": "NGINX의 기본 리스닝 주소는 무엇인가?",
            "options": ["0.0.0.0", "127.0.0.1", "::1", "192.168.0.1", "localhost.localdomain"],
            "answer": 0,
            "explanation": "0.0.0.0은 모든 인터페이스에서 요청을 수신한다는 의미입니다."
        },
        {
            "question": "NGINX의 events {} 블록은 주로 무엇을 정의하는가?",
            "options": ["로그 레벨 설정", "서버 이름 설정", "접속 이벤트 처리 방식", "압축 방식 설정", "MIME 타입 정의"],
            "answer": 2,
            "explanation": "events 블록에서는 워커당 최대 연결 수 등 이벤트 관련 설정을 합니다."
        },
        {
            "question": "nginx.conf의 최상위 블록은 어디인가?",
            "options": ["server", "location", "http", "main", "events"],
            "answer": 3,
            "explanation": "main은 설정 파일에서 가장 상위 레벨에 위치하며, http, events 블록을 포함합니다."
        },
        {
            "question": "NGINX는 기본적으로 어떤 방식으로 요청을 처리하는가?",
            "options": ["병렬 처리 기반 스레드", "이벤트 기반 논블로킹 방식", "요청당 프로세스 생성 방식", "요청당 DB 연결 방식", "파이썬 코루틴 기반"],
            "answer": 1,
            "explanation": "NGINX는 이벤트 루프 기반으로 비동기 논블로킹 처리 방식을 사용합니다."
        },
        {
            "question": "다음 중 location 블록의 주요 기능은?",
            "options": ["이벤트 루프 정의", "특정 URI에 대한 요청 처리 방식 지정", "서버 이름 지정", "접근 로그 비활성화", "연결 수 제한"],
            "answer": 1,
            "explanation": "location은 URI 패턴에 따라 요청을 다르게 처리할 수 있도록 합니다."
        },
        {
            "question": "NGINX의 모듈 중 정적 콘텐츠 제공과 가장 관련 있는 모듈은?",
            "options": ["ngx_http_gzip_module", "ngx_http_proxy_module", "ngx_http_core_module", "ngx_stream_core_module", "ngx_http_rewrite_module"],
            "answer": 2,
            "explanation": "core_module은 정적 파일 제공, 경로 매칭 등 기본 웹 서버 기능을 담당합니다."
        },
        {
            "question": "NGINX에서 로그 레벨 중 가장 상세한 디버깅 수준은?",
            "options": ["info", "warn", "error", "notice", "debug"],
            "answer": 4,
            "explanation": "debug는 가장 상세한 로깅 수준이며, 성능에 영향을 줄 수 있습니다."
        },
        {
            "question": "다음 중 NGINX의 대표적인 특징이 아닌 것은?",
            "options": ["낮은 메모리 사용량", "높은 연결 처리량", "모듈 기반 확장성", "자동 DB 스키마 생성", "정적 및 동적 콘텐츠 지원"],
            "answer": 3,
            "explanation": "NGINX는 DB 스키마를 생성하지 않으며, DB와 직접적인 관련이 없습니다."
        },
        {
            "question": "access_log와 error_log의 차이는 무엇인가?",
            "options": ["전자는 요청 로그, 후자는 오류 로그", "전자는 압축 로그, 후자는 원본 로그", "전자는 SSL 로그, 후자는 캐시 로그", "두 로그는 동일한 파일에 기록됨", "둘 다 바이너리 로그임"],
            "answer": 0,
            "explanation": "access_log는 요청 성공/실패 여부 포함, error_log는 에러 발생 시 상세 정보 기록합니다."
        },
        {
            "question": "NGINX에서 도메인별 가상 호스트 구성을 위해 사용하는 블록은?",
            "options": ["location", "map", "http", "server", "stream"],
            "answer": 3,
            "explanation": "여러 도메인을 하나의 NGINX 인스턴스에서 처리하려면 각각의 server 블록을 생성합니다."
        },
        {
            "question": "NGINX 설정에서 변수명은 일반적으로 어떤 접두어를 사용하는가?",
            "options": ["@", ":", "$", "&", "*"],
            "answer": 2,
            "explanation": "$는 NGINX 설정에서 변수 사용을 나타냅니다. 예: $remote_addr."
        },
        {
            "question": "다음 중 리버스 프록시로 동작하기 위해 반드시 필요한 디렉티브는?",
            "options": ["root", "proxy_pass", "alias", "gzip", "ssl_certificate_key"],
            "answer": 1,
            "explanation": "proxy_pass는 클라이언트 요청을 다른 서버로 전달하는 리버스 프록시의 핵심입니다."
        },
        {
            "question": "NGINX는 어떤 형태의 HTTP 요청 멀티플렉싱을 기본 지원하지 않는가?",
            "options": ["HTTP/1.1", "HTTP/2", "Keepalive", "HTTP pipelining", "HTTP/3 (QUIC)"],
            "answer": 4,
            "explanation": "HTTP/3은 NGINX OSS에서 기본적으로 지원되지 않으며 별도 빌드가 필요합니다."
        },
        {
            "question": "NGINX 설정에서 서버 이름을 지정하는 디렉티브는?",
            "options": ["domain_name", "listen_name", "server_name", "host_match", "url_host"],
            "answer": 2,
            "explanation": "server_name은 도메인별 요청을 구분하는 데 사용됩니다."
        },
        {
            "question": "NGINX에서 클라이언트 요청을 제한하는 기능은?",
            "options": ["gzip_level", "limit_req", "ssl_verify", "worker_rlimit", "retry_policy"],
            "answer": 1,
            "explanation": "limit_req는 특정 시간 내 요청 수 제한에 사용됩니다."
        },
        {
            "question": "NGINX는 어떤 방식으로 설정 오류를 알려주는가?",
            "options": ["클라이언트에게 500 에러 전송", "설정 파일 내 오류 자동 수정", "nginx -t로 오류 표시", "웹 UI에서 팝업", "로그를 외부로 전송"],
            "answer": 2,
            "explanation": "nginx -t는 설정 오류 여부를 콘솔에 표시해줍니다."
        },
        {
            "question": "다음 중 NGINX가 사용하는 주요 구성 요소가 아닌 것은?",
            "options": ["nginx.conf", "server", "location", "pipeline", "events"],
            "answer": 3,
            "explanation": "pipeline은 HTTP 기능 중 하나지만, NGINX 구성 디렉티브나 블록은 아닙니다."
        },
        {
            "question": "다음 중 NGINX의 설정 파일을 다시 적용하는 명령은?",
            "options": ["nginx -s reload", "nginx --start", "systemctl restart nginx", "nginx -c", "reload-nginx"],
            "answer": 0,
            "explanation": "nginx -s reload는 서비스 재시작 없이 설정을 다시 적용합니다."
        }
    ],
    "F5N2": [
        {
            "question": "NGINX 설정을 변경한 후 오류 여부를 확인하는 명령은?",
            "options": ["nginx --check-config", "nginx -t", "nginx -c", "nginx -v", "nginx -d"],
            "answer": 1,
            "explanation": "nginx -t는 설정 구문의 유효성을 테스트합니다."
        },
        {
            "question": "다음 중 NGINX 설정의 최상위 블록은?",
            "options": ["http", "server", "location", "events", "main"],
            "answer": 4,
            "explanation": "main 컨텍스트는 http, events, stream 등을 포함하는 최상위 블록입니다."
        },
        {
            "question": "/etc/nginx/conf.d/*.conf 파일을 병합하려면 어떤 디렉티브를 사용해야 하는가?",
            "options": ["source", "load", "include", "import", "append"],
            "answer": 2,
            "explanation": "include 디렉티브는 외부 설정 파일을 병합할 때 사용됩니다."
        },
        {
            "question": "NGINX에서 가상 호스트를 정의할 때 사용하는 블록은?",
            "options": ["location", "map", "server", "events", "proxy"],
            "answer": 2,
            "explanation": "server 블록은 특정 포트/도메인에 대해 처리할 서버 단위를 정의합니다."
        },
        {
            "question": "다음 중 HTTP 요청 URI 패턴에 따라 처리 방식을 달리하는 블록은?",
            "options": ["server", "http", "location", "limit_req", "log_format"],
            "answer": 2,
            "explanation": "location 블록은 URI 경로별로 처리 로직을 정의합니다."
        },
        {
            "question": "NGINX 설정에서 listen 443 ssl;을 사용하려면 반드시 필요한 설정은?",
            "options": ["gzip 설정", "캐시 경로", "TLS 인증서 및 키", "HTTP 리디렉션", "루트 경로"],
            "answer": 2,
            "explanation": "SSL/TLS 설정을 위해서는 ssl_certificate와 ssl_certificate_key가 필요합니다."
        },
        {
            "question": "/etc/nginx/mime.types는 무엇을 정의하는가?",
            "options": ["서버별 접근 제한", "파일 확장자와 콘텐츠 타입 매핑", "로그 포맷", "오류 페이지 경로", "캐시 정책"],
            "answer": 1,
            "explanation": "mime.types 파일은 파일 확장자와 MIME 타입 간의 관계를 설정합니다."
        },
        {
            "question": "다음 중 설정 파일 내 변수 사용 형식으로 올바른 것은?",
            "options": ["%remote_addr", "@remote_addr", "$remote_addr", "!remote_addr", "#remote_addr"],
            "answer": 2,
            "explanation": "NGINX에서 변수는 $ 접두어로 사용됩니다."
        },
        {
            "question": "설정 파일 병합 시, include *.conf; 형식에서 파일 병합 순서는?",
            "options": ["무작위", "수정일 기준", "알파벳 순", "숫자 순", "블록 깊이 우선"],
            "answer": 2,
            "explanation": "와일드카드 포함 시 알파벳 순으로 병합됩니다."
        },
        {
            "question": "다음 중 proxy_pass 디렉티브의 주요 기능은?",
            "options": ["클라이언트 요청을 파일로 저장", "요청을 백엔드 서버로 전달", "요청을 gzip으로 압축", "정적 콘텐츠만 처리", "URI를 리디렉션"],
            "answer": 1,
            "explanation": "proxy_pass는 리버스 프록시 역할을 하며 요청을 백엔드로 전달합니다."
        },
        {
            "question": "try_files $uri $uri/ =404; 설정의 목적은?",
            "options": ["항상 404 에러를 반환", "요청된 파일이 없으면 리디렉션", "여러 경로를 순서대로 시도 후 없으면 404 반환", "요청 URI를 정규표현식으로 처리", "정적 파일을 무조건 생성"],
            "answer": 2,
            "explanation": "try_files는 요청된 경로 순서대로 시도하고 실패 시 지정된 코드 또는 경로로 처리합니다."
        },
        {
            "question": "log_format 디렉티브의 주 목적은?",
            "options": ["에러 로그 저장 위치 지정", "로그 압축 설정", "접근 로그 포맷 지정", "로그 자동 삭제 정책 설정", "로그 암호화 설정"],
            "answer": 2,
            "explanation": "log_format은 사용자 정의 접근 로그 포맷을 설정합니다."
        },
        {
            "question": "다음 중 limit_req_zone 디렉티브의 기능은?",
            "options": ["에러 페이지 처리", "서버 리스닝 포트 제한", "요청 속도 제한 설정", "URI 길이 제한", "사용자 인증 제한"],
            "answer": 2,
            "explanation": "limit_req_zone은 클라이언트별 요청 속도 제한을 위한 shared memory zone을 정의합니다."
        },
        {
            "question": "access_log off;의 효과는?",
            "options": ["에러 로그도 기록되지 않음", "접근 로그만 기록하지 않음", "설정 파일이 무시됨", "로그 파일이 삭제됨", "모든 로그가 syslog로 전송됨"],
            "answer": 1,
            "explanation": "access_log off;는 클라이언트 요청 기록을 하지 않도록 설정합니다."
        },
        {
            "question": "server_name 디렉티브는 어떤 용도로 사용되는가?",
            "options": ["응답 헤더 설정", "서버 블록 선택을 위한 도메인 식별", "업스트림 서버 이름 지정", "로그 파일 이름 지정", "루트 디렉토리 설정"],
            "answer": 1,
            "explanation": "server_name은 도메인 이름 기반으로 가상 서버를 매칭합니다."
        },
        {
            "question": "NGINX에서 여러 도메인 처리 시 필요한 구성은?",
            "options": ["여러 location 블록", "여러 events 블록", "여러 server 블록", "여러 worker 프로세스", "여러 include 명령"],
            "answer": 2,
            "explanation": "도메인마다 server 블록을 구성하여 가상 호스트로 설정합니다."
        },
        {
            "question": "캐시 키 및 메타데이터 저장을 위한 설정은?",
            "options": ["proxy_cache_path", "proxy_buffer_size", "proxy_pass", "cache_control", "access_cache_zone"],
            "answer": 0,
            "explanation": "proxy_cache_path는 디스크 캐시 경로와 메타데이터를 위한 메모리 존을 함께 설정합니다."
        },
        {
            "question": "정규표현식을 사용하는 location 블록은 어떤 접두사를 사용하는가?",
            "options": ["/", "@", "=", "^~", "~ 또는 ~*"],
            "answer": 4,
            "explanation": "~은 대소문자 구분, ~*은 대소문자 무시 정규표현식을 위한 접두사입니다."
        },
        {
            "question": "error_page 404 /custom_404.html;의 의미는?",
            "options": ["404 오류 발생 시 /custom_404.html을 반환", "404를 로그에만 기록", "404 대신 500 오류로 대체", "모든 오류를 무시", "error_page 설정을 무시"],
            "answer": 0,
            "explanation": "지정된 오류 코드에 대해 사용자 정의 페이지를 반환하도록 설정합니다."
        },
        {
            "question": "NGINX에서 gzip 압축 기능을 활성화하려면 어떤 디렉티브가 필요한가?",
            "options": ["enable_gzip on;", "gzip on;", "compression true;", "gzip_enabled yes;", "zip_response on;"],
            "answer": 1,
            "explanation": "gzip on;은 HTTP 응답을 압축하기 위한 기본 설정입니다."
        },
        {
            "question": "다음 중 설정 컨텍스트 상속이 발생하는 경로로 올바른 것은?",
            "options": ["main → server → location → http", "http → server → location", "server → main → events", "location → stream → map", "geo → http → map"],
            "answer": 1,
            "explanation": "설정은 상위에서 하위로 http → server → location 컨텍스트로 상속됩니다."
        },
        {
            "question": "keepalive_timeout 0; 설정의 의미는?",
            "options": ["무한 대기", "keepalive 비활성화", "에러 발생", "keepalive 타임아웃 60초", "응답 지연 발생"],
            "answer": 1,
            "explanation": "0으로 설정 시 keepalive 연결이 비활성화됩니다."
        },
        {
            "question": "alias와 root의 차이점은?",
            "options": ["alias는 정규표현식에서만 사용 가능", "root는 location URI를 파일 경로에 붙임", "alias는 리디렉션에 사용", "alias는 로그 포맷 정의", "root는 정적 콘텐츠에만 사용 가능"],
            "answer": 1,
            "explanation": "alias는 전체 경로를 대체하며, root는 URI를 경로 뒤에 붙여 사용합니다."
        },
        {
            "question": "map 블록의 주요 목적은?",
            "options": ["가상 서버 그룹화", "요청 헤더 기반 변수 설정", "서버 간 로드 밸런싱", "캐시 무효화", "SSL 인증서 선택"],
            "answer": 1,
            "explanation": "map은 조건에 따라 변수를 설정하는 데 사용됩니다."
        },
        {
            "question": "listen 80 default_server; 설정은 무엇을 의미하는가?",
            "options": ["가장 먼저 요청 처리", "항상 HTTPS로 처리", "DNS 응답 사용", "기본 가상 서버로 설정", "특정 클라이언트 전용 처리"],
            "answer": 3,
            "explanation": "default_server는 요청이 명시적으로 매칭되지 않을 경우 처리되는 기본 서버입니다."
        },
        {
            "question": "다음 중 업스트림 서버 상태 정보를 공유하는 데 사용되는 설정은?",
            "options": ["limit_conn_zone", "zone in upstream block", "status directive", "map block", "proxy_buffering off"],
            "answer": 1,
            "explanation": "zone은 공유 메모리를 통해 업스트림 상태를 워커 간 공유합니다."
        },
        {
            "question": "gzip_types 디렉티브의 목적은?",
            "options": ["압축 강도 조절", "gzip 압축을 적용할 MIME 타입 지정", "파일 확장자 필터링", "HTTP 메서드 제한", "캐시 만료 시간 설정"],
            "answer": 1,
            "explanation": "gzip_types는 어떤 MIME 타입에 대해 gzip 압축을 적용할지 지정합니다."
        },
        {
            "question": "client_max_body_size의 기본값은?",
            "options": ["1m", "512k", "0 (제한 없음)", "10m", "2m"],
            "answer": 0,
            "explanation": "기본값은 1m로, 본문 크기가 이를 초과하면 413 오류가 발생합니다."
        },
        {
            "question": "resolver 디렉티브의 목적은?",
            "options": ["DNS 쿼리를 수행할 서버 지정", "클라이언트 IP 차단", "서버 이름 변경", "SSL 핸드셰이크 제어", "리버스 프록시 응답 캐싱"],
            "answer": 0,
            "explanation": "resolver는 NGINX가 이름 해석을 위해 사용할 DNS 서버를 지정합니다."
        },
        {
            "question": "NGINX 설정을 구성 파일 전체로 출력하고자 할 때 사용하는 명령은?",
            "options": ["nginx -t", "nginx -c", "nginx -s reload", "nginx -T", "nginx -d"],
            "answer": 3,
            "explanation": "nginx -T는 모든 설정을 병합하여 표준 출력으로 보여줍니다."
        }
    ],
    "F5N3": [
        {
            "question": "다음 중 NGINX 설치 후 웹 서버로 설정을 완료하는 기본 구성은?",
            "options": ["listen 53;", "server_name localhost; root /usr/share/nginx/html;", "proxy_pass http://backend;", "stream {} 블록 추가", "access_log off;"],
            "answer": 1,
            "explanation": "웹 서버 기본 설정에는 server_name과 root 디렉티브가 포함됩니다."
        },
        {
            "question": "다음 중 NGINX가 제대로 실행되고 있는지 확인할 수 있는 명령은?",
            "options": ["nginx -h", "ps aux | grep nginx", "killall nginx", "systemctl stop nginx", "ls /etc/nginx/ssl"],
            "answer": 1,
            "explanation": "ps 명령을 통해 실행 중인 nginx 프로세스를 확인할 수 있습니다."
        },
        {
            "question": "NGINX 설정을 다시 적용하면서 중단 없이 반영하려면?",
            "options": ["nginx -s restart", "nginx --reload", "nginx -s reload", "systemctl reset nginx", "nginx -q"],
            "answer": 2,
            "explanation": "nginx -s reload는 다운타임 없이 설정을 재적용합니다."
        },
        {
            "question": "NGINX로 HTTPS 제공 시 반드시 필요한 두 가지 설정은?",
            "options": ["ssl_certificate 와 ssl_certificate_key", "server_name 와 gzip", "root 와 listen 80", "access_log 와 proxy_pass", "ssl_verify 와 resolver"],
            "answer": 0,
            "explanation": "HTTPS는 인증서와 개인 키가 있어야 동작합니다."
        },
        {
            "question": "다음 중 프록시 서버로 동작하는 설정은?",
            "options": ["listen 8080;", "proxy_pass http://backend;", "root /var/www/html;", "ssl_certificate cert.pem;", "access_log off;"],
            "answer": 1,
            "explanation": "proxy_pass는 리버스 프록시 역할을 수행합니다."
        },
        {
            "question": "다음 중 설정이 잘못된 경우 에러 로그를 확인할 수 있는 기본 위치는?",
            "options": ["/var/log/nginx/error.log", "/etc/nginx/access.log", "/usr/nginx/errors", "/tmp/nginx.log", "/etc/nginx/errors.txt"],
            "answer": 0,
            "explanation": "기본적으로 에러 로그는 /var/log/nginx/error.log에 저장됩니다."
        },
        {
            "question": "다음 중 shared memory zone을 사용하여 여러 워커 간 상태를 공유하는 기능은?",
            "options": ["업로드 디렉토리 설정", "gzip 압축", "캐시 메타데이터", "로그 필터링", "리스닝 포트"],
            "answer": 2,
            "explanation": "캐시 키 및 메타데이터는 공유 메모리를 통해 워커 간 공유됩니다."
        },
        {
            "question": "try_files $uri $uri/ =404; 설정의 역할은?",
            "options": ["요청을 백엔드로 프록시", "정적 파일 제공 후 없으면 404", "모든 요청을 무시", "요청을 압축", "클라이언트 IP 제한"],
            "answer": 1,
            "explanation": "try_files는 요청된 URI 파일을 시도하고 없으면 404 반환합니다."
        },
        {
            "question": "다음 중 모듈 기능을 올바르게 설명한 것은?",
            "options": ["NGINX는 모듈 없이 실행되지 않음", "모듈은 NGINX 기능을 확장", "모듈은 설정이 아닌 실행 시 주입", "모듈은 HTTP 요청을 차단함", "모듈은 로그를 삭제함"],
            "answer": 1,
            "explanation": "NGINX 모듈은 로깅, 캐싱, 프록시 등 다양한 기능을 추가합니다."
        },
        {
            "question": "NGINX 설치 후 서비스 시작을 위해 사용하는 명령은?",
            "options": ["nginx -c", "nginx -d", "nginx", "nginx -f", "nginx -k"],
            "answer": 2,
            "explanation": "단순히 nginx 명령만 입력하면 서비스가 시작됩니다."
        },
        {
            "question": "다음 중 설정 적용 직후 반드시 해야 할 명령은?",
            "options": ["nginx -T", "nginx -s reload", "nginx -c reload.conf", "nginx -m", "nginx --recheck"],
            "answer": 1,
            "explanation": "설정 적용 후 서비스에 반영하려면 nginx -s reload가 필요합니다."
        },
        {
            "question": "NGINX 설정 오류가 있을 때 출력되는 메시지는 어떤 명령으로 확인하는가?",
            "options": ["nginx -c", "nginx -r", "nginx -t", "nginx -v", "nginx -h"],
            "answer": 2,
            "explanation": "nginx -t는 설정 테스트용 명령어입니다."
        },
        {
            "question": "다음 중 올바른 리버스 프록시 location 블록 구성 예시는?",
            "options": ["return 404;", "alias /backend/api;", "proxy_pass http://backend;", "gzip on;", "access_log off;"],
            "answer": 2,
            "explanation": "proxy_pass는 백엔드로 요청을 전달합니다."
        },
        {
            "question": "gzip 압축을 설정하려면 어떤 디렉티브를 포함해야 하는가?",
            "options": ["gzip_mode on;", "gzip_compression true;", "gzip on;", "gzip_compress_enable on;", "enable_zip;"],
            "answer": 2,
            "explanation": "gzip on;으로 설정하여 HTTP 응답 압축을 활성화합니다."
        },
        {
            "question": "다음 중 location 블록에서 정규표현식을 사용하는 접두사는?",
            "options": ["^/api", "=", "~", "@", "#"],
            "answer": 2,
            "explanation": "~는 정규표현식을 사용하는 location을 의미합니다."
        },
        {
            "question": "NGINX에서 404 에러를 사용자 정의 페이지로 바꾸기 위한 설정은?",
            "options": ["return 404;", "proxy_intercept_errors on;", "error_page 404 /404.html;", "log_format off;", "client_body_timeout 0;"],
            "answer": 2,
            "explanation": "error_page 디렉티브는 사용자 정의 에러 페이지를 설정합니다."
        },
        {
            "question": "캐시 사용을 위해 반드시 지정해야 하는 구성은?",
            "options": ["gzip_static on;", "proxy_cache_path", "upstream cache_server {}", "client_body_temp_path", "proxy_read_buffer"],
            "answer": 1,
            "explanation": "proxy_cache_path는 캐시 위치 및 공유 메모리 zone을 지정합니다."
        },
        {
            "question": "다음 중 HTTPS 설정에 필요한 디렉티브 쌍은?",
            "options": ["ssl_buffer_size, ssl_protocols", "ssl_certificate, ssl_certificate_key", "ssl_session_id, ssl_verify_client", "ssl_compression, ssl_early_data", "ssl_log, ssl_keepalive"],
            "answer": 1,
            "explanation": "인증서와 개인 키는 HTTPS 동작에 필수입니다."
        },
        {
            "question": "access_log off;를 사용하면 어떤 현상이 발생하는가?",
            "options": ["NGINX가 종료된다", "에러 로그도 기록되지 않는다", "접근 로그가 남지 않는다", "로그가 디스크에 두 번 저장된다", "접근 로그가 error.log에 기록된다"],
            "answer": 2,
            "explanation": "access_log off;는 클라이언트 요청 로그를 기록하지 않게 합니다."
        },
        {
            "question": "다음 중 server 블록 내부에서 사용할 수 없는 디렉티브는?",
            "options": ["listen", "server_name", "location", "proxy_pass", "worker_processes"],
            "answer": 4,
            "explanation": "worker_processes는 main 블록(최상위)에서만 사용 가능합니다."
        },
        {
            "question": "요청 URI에 따라 서로 다른 백엔드에 라우팅하는 구성은?",
            "options": ["하나의 location에서 여러 proxy_pass", "여러 server에서 동일한 location", "여러 location에서 서로 다른 proxy_pass", "rewrite 디렉티브만 사용", "/ 위치에서 다 처리"],
            "answer": 2,
            "explanation": "URI 패턴별로 location 블록을 나누고 각각 proxy_pass로 분기합니다."
        },
        {
            "question": "listen 443 ssl;을 사용하려면 필수로 설정해야 할 항목은?",
            "options": ["gzip_static", "server_name", "ssl_certificate와 ssl_certificate_key", "access_log", "default_server"],
            "answer": 2,
            "explanation": "443 포트에서 SSL을 활성화하려면 인증서 및 키가 필수입니다."
        },
        {
            "question": "HTTP 요청 헤더의 특정 값에 따라 설정을 변경하고 싶을 때 사용하는 블록은?",
            "options": ["upstream", "stream", "location", "map", "http"],
            "answer": 3,
            "explanation": "map은 조건에 따라 변수 값을 설정할 수 있도록 도와줍니다."
        },
        {
            "question": "다음 중 정적 파일을 직접 서빙하는 데 필요한 디렉티브는?",
            "options": ["proxy_pass", "root", "alias", "fastcgi_pass", "upstream"],
            "answer": 1,
            "explanation": "root는 URI와 연결된 실제 경로를 설정해 정적 파일 제공이 가능합니다."
        },
        {
            "question": "gzip_types를 설정하는 이유는?",
            "options": ["클라이언트 IP를 제한", "gzip 압축을 적용할 MIME 타입 지정", "브라우저 종류 식별", "gzip 압축을 비활성화", "error.log 용량 제한"],
            "answer": 1,
            "explanation": "MIME 타입에 따라 gzip 적용 여부를 결정합니다."
        },
        {
            "question": "다음 중 로깅을 완전히 비활성화하려면 무엇을 설정해야 하는가?",
            "options": ["log_format none;", "access_log off; error_log off;", "access_log disable;", "disable_log on;", "log_level silent;"],
            "answer": 1,
            "explanation": "access_log와 error_log를 모두 끄면 로그가 기록되지 않습니다."
        },
        {
            "question": "다음 중 설정 파일을 한눈에 출력하는 명령은?",
            "options": ["nginx -c", "nginx -t", "nginx -s show", "nginx -T", "nginx -d"],
            "answer": 3,
            "explanation": "nginx -T는 전체 병합된 설정을 표준 출력으로 보여줍니다."
        },
        {
            "question": "여러 서버 블록 중 기본값으로 처리될 서버를 지정하려면?",
            "options": ["listen 80 primary;", "server default on;", "listen 80 default_server;", "location / default;", "server_name default;"],
            "answer": 2,
            "explanation": "default_server는 명시적 매칭 실패 시 기본 처리 서버로 설정됩니다."
        },
        {
            "question": "NGINX 설정에서 HTTP 요청 속도를 제한하려면 어떤 구성 요소가 필요할까?",
            "options": ["limit_conn", "limit_req_zone + limit_req", "client_max_body_size", "proxy_buffering", "http2_max_requests"],
            "answer": 1,
            "explanation": "요청 속도 제한은 limit_req_zone으로 shared memory 설정 후, limit_req로 적용합니다."
        },
        {
            "question": "다음 중 TLS 설정 시 클라이언트 인증(양방향 인증)에 사용하는 디렉티브는?",
            "options": ["ssl_session_timeout", "ssl_verify_client", "ssl_certificate", "ssl_ecdh_curve", "ssl_protocols"],
            "answer": 1,
            "explanation": "ssl_verify_client는 클라이언트 인증서 요구 여부를 설정합니다."
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