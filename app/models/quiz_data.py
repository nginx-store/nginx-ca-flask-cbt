"""
퀴즈 데이터 모델 - F5N1 카테고리 문제 추가
"""

# 기존 F5N1 카테고리에 문제를 추가합니다.
# 기존 데이터 구조를 참고하여 같은 형식으로 추가합니다.

# 문제 데이터
quiz_data = {
    "F5N1": [
        {
    "question": "NGINX를 웹 서버로 사용할 때 가장 일반적인 용도는 무엇인가?",
    "options": [
      "정적 파일 제공",
      "데이터베이스 캐싱",
      "API 라우팅",
      "외부 인증 처리",
      "WAF 보호"
    ],
    "answer": 0,
    "explanation": "NGINX는 웹 서버로서 이미지, HTML, CSS, JS 같은 정적 콘텐츠를 빠르게 제공하는 데 가장 많이 사용된다."
  },
  {
    "question": "NGINX에서 nginx.conf 파일의 기본 위치는 어디인가?",
    "options": [
      "/etc/nginx/nginx.conf",
      "/usr/local/nginx/conf.d/nginx.conf",
      "/etc/nginx/sites-available/default",
      "/var/www/html/index.conf",
      "/nginx/main.conf"
    ],
    "answer": 0,
    "explanation": "대부분의 Linux 배포판에서 NGINX의 기본 설정 파일은 /etc/nginx/nginx.conf에 위치한다."
  },
  {
    "question": "NGINX가 공유 메모리 영역을 사용하는 주된 이유는 무엇인가?",
    "options": [
      "워커 프로세스 간 데이터 공유",
      "클라이언트 요청 로깅",
      "모듈 간 통신",
      "SSL 세션 캐시 저장",
      "사용자 인증 처리"
    ],
    "answer": 0,
    "explanation": "NGINX는 워커 프로세스 간에 세션 정보나 상태를 공유하기 위해 shared memory zone을 사용한다."
  },
  {
    "question": "NGINX가 특정 사용자로 실행되도록 설정하려면 어느 지시어를 사용해야 하는가?",
    "options": [
      "user",
      "worker_processes",
      "listen",
      "server_name",
      "location"
    ],
    "answer": 0,
    "explanation": "user 지시어는 NGINX가 실행될 때 사용할 사용자 계정을 정의한다."
  },
  {
    "question": "다음 중 NGINX를 API Gateway로 사용할 수 있는 기능은?",
    "options": [
      "URI 기반 라우팅",
      "이미지 최적화",
      "파일 압축",
      "DNS 쿼리 처리",
      "파일 시스템 접근 제어"
    ],
    "answer": 0,
    "explanation": "API Gateway의 주요 기능은 URI에 따라 백엔드 API로 요청을 라우팅하는 것이다."
  },
  {
    "question": "NGINX에서 include 지시어는 어떤 역할을 하는가?",
    "options": [
      "외부 설정 파일을 현재 구성에 병합한다",
      "로깅 형식을 설정한다",
      "정적 파일을 서비스한다",
      "프로세스 수를 설정한다",
      "캐시 정책을 설정한다"
    ],
    "answer": 0,
    "explanation": "include 지시어는 다른 구성 파일을 불러와 현재 구성에 포함시킨다."
  },
  {
    "question": "NGINX가 리버스 프록시로 사용될 때 클라이언트 요청은 어떻게 처리되는가?",
    "options": [
      "직접 응답을 반환",
      "백엔드 서버로 전달",
      "디스크에 로그 저장",
      "요청을 무시",
      "사용자에게 오류 반환"
    ],
    "answer": 1,
    "explanation": "리버스 프록시는 클라이언트의 요청을 받아 백엔드 서버에 전달하고, 해당 응답을 다시 클라이언트에 반환한다."
  },
  {
    "question": "다음 중 conf.d 디렉토리는 어떤 역할을 하는가?",
    "options": [
      "로그 파일 저장",
      "개별 서버 블록 설정 포함",
      "정적 파일 저장",
      "SSL 인증서 저장",
      "캐시 데이터 저장"
    ],
    "answer": 1,
    "explanation": "conf.d 디렉토리는 nginx.conf의 include 지시어를 통해 개별 가상 호스트나 서버 블록을 정의하는 설정 파일들을 저장한다."
  },
  {
    "question": "NGINX의 워커 프로세스가 특정 사용자로 실행되도록 하기 위해서는 무엇이 요구되는가?",
    "options": [
      "root 권한",
      "master 프로세스가 먼저 해당 유저로 권한을 하향시켜야 함",
      "모든 유저에 777 권한 부여",
      "SSL 인증서 등록",
      "실행 시에만 지정 가능"
    ],
    "answer": 1,
    "explanation": "마스터 프로세스는 root로 실행되며 이후 워커 프로세스에 대해 설정된 user로 권한을 낮춘다."
  },
  {
    "question": "NGINX의 설정 파일에서 상위 블록에서 정의된 지시어가 하위 블록에서 덮어쓰기되는 것을 무엇이라 하는가?",
    "options": [
      "설정 리셋",
      "지시어 오버라이드",
      "설정 상속 차단",
      "사용자 컨텍스트 변경",
      "요청 리디렉션"
    ],
    "answer": 1,
    "explanation": "하위 블록에서 상위 지시어를 다시 정의하면 기존 값을 덮어쓰게 되며 이를 오버라이드(override)라고 한다."
  },
  {
    "question": "공유 메모리 zone을 사용하는 대표적인 NGINX 모듈은 무엇인가?",
    "options": [
      "access_log",
      "limit_conn",
      "server_name",
      "proxy_pass",
      "rewrite"
    ],
    "answer": 1,
    "explanation": "limit_conn 모듈은 연결 수 제한을 위해 shared memory zone을 사용한다."
  },
  {
    "question": "다음 중 NGINX에서 캐싱 솔루션으로 사용될 때 필요한 모듈은?",
    "options": [
      "stream",
      "proxy_cache",
      "mail",
      "limit_req",
      "map"
    ],
    "answer": 1,
    "explanation": "proxy_cache는 응답을 캐시에 저장하여 같은 요청이 들어왔을 때 빠르게 반환할 수 있도록 한다."
  },
  {
    "question": "NGINX가 로드 밸런서로 작동할 때 사용하는 주요 지시어는?",
    "options": [
      "try_files",
      "rewrite",
      "upstream",
      "gzip",
      "server_tokens"
    ],
    "answer": 2,
    "explanation": "upstream 블록은 여러 백엔드 서버를 정의하여 NGINX가 로드 밸런싱을 수행할 수 있게 한다."
  },
  {
    "question": "다음 중 설정 파일 병합 순서에 가장 부합하는 것은?",
    "options": [
      "include 디렉토리 > nginx.conf > default.conf",
      "default.conf > include 디렉토리 > nginx.conf",
      "nginx.conf → include 된 파일 순서대로",
      "conf.d > nginx.conf > sites-enabled",
      "실행 시 랜덤"
    ],
    "answer": 2,
    "explanation": "설정은 nginx.conf에서 먼저 읽히고, 그 안에서 include 지시어에 정의된 순서대로 병합된다."
  },
  {
    "question": "다음 중 리버스 프록시 사용 시 클라이언트 IP를 전달하기 위해 자주 사용하는 헤더는?",
    "options": [
      "Host",
      "Accept",
      "X-Forwarded-For",
      "Authorization",
      "Cache-Control"
    ],
    "answer": 2,
    "explanation": "X-Forwarded-For 헤더는 리버스 프록시 뒤에 위치한 클라이언트의 실제 IP 주소를 전달하는 데 사용된다."
  },
  {
    "question": "NGINX에서 shared memory zone의 이름과 크기를 지정하는 예시는?",
    "options": [
      "log_format main",
      "server_name example.com;",
      "zone=backend:10m",
      "listen 80;",
      "gzip on;"
    ],
    "answer": 2,
    "explanation": "shared memory zone은 예를 들어 zone=backend:10m처럼 이름과 메모리 크기를 명시한다."
  },
  {
    "question": "NGINX의 기본 마스터 프로세스는 어떤 권한으로 실행되는가?",
    "options": [
      "nobody",
      "nginx",
      "root",
      "admin",
      "user"
    ],
    "answer": 2,
    "explanation": "마스터 프로세스는 시스템 리소스를 제어하기 위해 root 권한으로 실행되며, 워커는 하향 권한으로 실행된다."
  },
  {
    "question": "NGINX에서 캐시 저장소를 사용하는 설정 블록은?",
    "options": [
      "log_format",
      "events",
      "proxy_cache_path",
      "http2_push",
      "fastcgi_pass"
    ],
    "answer": 2,
    "explanation": "proxy_cache_path 지시어는 NGINX의 캐시 저장소 경로, 키, 크기 등을 지정하는 데 사용된다."
  },
  {
    "question": "다음 중 NGINX의 로드 밸런싱 방법이 아닌 것은?",
    "options": [
      "round-robin",
      "least_conn",
      "ip_hash",
      "dns_hash",
      "random"
    ],
    "answer": 3,
    "explanation": "NGINX는 round-robin, least_conn, ip_hash, random과 같은 로드 밸런싱 방식을 지원하지만 dns_hash는 지원하지 않는다."
  },
  {
    "question": "다음 중 user nginx; 설정이 수행하는 역할은?",
    "options": [
      "클라이언트 권한 검증",
      "로그 파일 권한 설정",
      "upstream 서버 지정",
      "워커 프로세스의 실행 사용자 지정",
      "캐시 디렉토리 지정"
    ],
    "answer": 3,
    "explanation": "user 지시어는 마스터 프로세스가 포크한 워커 프로세스가 어떤 사용자 권한으로 실행될지를 설정한다."
  },
  {
    "question": "다음 중 NGINX를 API Gateway로 구성할 때 가장 중요한 요소는?",
    "options": [
      "access_log 경로",
      "캐시 유효 기간",
      "HTTP 버전",
      "백엔드 API 경로에 따른 요청 분기 처리",
      "gzip 압축 설정"
    ],
    "answer": 3,
    "explanation": "API Gateway는 다양한 API 경로에 따라 요청을 백엔드에 분기 라우팅하는 것이 핵심이다."
  },
  {
    "question": "다음 중 NGINX 설정에서 directive를 하위 블록에서 다시 정의하면 어떻게 되는가?",
    "options": [
      "오류 발생",
      "병합",
      "무시됨",
      "기존 값을 덮어씀",
      "상속 유지"
    ],
    "answer": 3,
    "explanation": "directive는 하위 블록에서 다시 정의되면 상위 블록의 값을 덮어쓰는 방식으로 작동한다."
  },
  {
    "question": "NGINX의 shared memory zone에 대한 설명으로 옳은 것은?",
    "options": [
      "보안을 위한 암호화 저장소이다",
      "워커 프로세스별 독립된 메모리 영역이다",
      "오류 로그 저장소이다",
      "여러 워커가 공통 데이터를 접근할 수 있도록 공유되는 메모리 영역이다",
      "파일 캐시 백업 저장소이다"
    ],
    "answer": 3,
    "explanation": "shared memory zone은 여러 워커 간 공통 데이터를 효율적으로 공유하기 위해 사용된다."
  },
  {
    "question": "다음 중 NGINX 캐시와 관련 없는 설정은?",
    "options": [
      "proxy_cache_path",
      "proxy_cache_key",
      "proxy_cache_valid",
      "proxy_pass_request_body",
      "proxy_cache_use_stale"
    ],
    "answer": 3,
    "explanation": "proxy_pass_request_body는 요청 본문 처리와 관련된 설정이며, 캐시 설정과는 관련이 없다."
  },
  {
    "question": "다음 중 NGINX 구성에서 사용자 권한과 가장 관련이 적은 항목은?",
    "options": [
      "user directive",
      "access permissions on log directory",
      "파일의 실행 권한 설정",
      "프로세스 권한 분리",
      "listen directive"
    ],
    "answer": 4,
    "explanation": "listen directive는 포트를 지정하며 사용자 권한과는 관련이 적다."
  },
  {
    "question": "다음 중 reverse proxy 기능을 가장 잘 설명하는 것은?",
    "options": [
      "HTML 페이지 생성",
      "클라이언트 IP 숨김",
      "데이터베이스 연결",
      "백엔드 서버 요청 중계",
      "디스크 캐시 무효화"
    ],
    "answer": 3,
    "explanation": "reverse proxy는 클라이언트 요청을 받아 백엔드 서버로 전달하고 응답을 반환하는 중계 역할을 수행한다."
  },
  {
    "question": "다음 중 /etc/nginx/conf.d/에 저장되는 설정 파일의 특징은?",
    "options": [
      "nginx.conf와 동일한 우선순위를 갖는다",
      "자동으로 실행되지 않는다",
      "include 되지 않으면 무시된다",
      "nginx.conf에 의해 수동으로 include 해야 한다",
      "기본적으로 nginx.conf에서 include 되어 있다"
    ],
    "answer": 4,
    "explanation": "대부분의 배포판에서 nginx.conf는 conf.d/*.conf를 기본적으로 include 하도록 되어 있다."
  },
  {
    "question": "다음 중 NGINX를 캐시 서버로 사용할 때 가장 중요한 요소는?",
    "options": [
      "IP 주소",
      "SSL 설정",
      "load balancing algorithm",
      "static file 경로",
      "cache key 설정"
    ],
    "answer": 4,
    "explanation": "캐시 키는 어떤 요청이 동일한 것으로 간주될지를 결정하는 핵심 요소로, 캐시 서버 운영에 매우 중요하다."
  },
  {
    "question": "shared memory zone을 설정하지 않으면 어떤 일이 발생할 수 있는가?",
    "options": [
      "gzip 오류",
      "사용자 인증 실패",
      "서버 블록 무시",
      "여러 워커 간 데이터 불일치",
      "SSL 핸드쉐이크 실패"
    ],
    "answer": 3,
    "explanation": "shared memory zone이 없으면 여러 워커 프로세스 간에 일관된 데이터를 공유하지 못하게 되어 데이터 불일치 문제가 발생할 수 있다."
  },
  {
    "question": "다음 중 NGINX의 load balancer 구성 시 필수 설정이 아닌 것은?",
    "options": [
      "upstream 블록",
      "server 블록",
      "proxy_pass",
      "zone",
      "ssl_certificate"
    ],
    "answer": 4,
    "explanation": "ssl_certificate는 HTTPS 설정 시 필요하지만, 일반적인 로드 밸런싱 설정에는 필수가 아니다."
  }
    ],
    "F5N2": [
        {
    "question": "NGINX의 로드 밸런싱에서 least_conn 알고리즘은 어떤 상황에서 가장 유리한가?",
    "options": [
      "고정 응답 시간 환경",
      "라운드로빈 기반 환경",
      "요청 처리 시간이 일정하지 않은 경우",
      "IP 기반 분산이 필요한 경우",
      "세션 정보를 유지해야 할 때"
    ],
    "answer": 2,
    "explanation": "least_conn은 활성 연결 수가 가장 적은 서버에 요청을 보내므로 요청 처리 시간이 불규칙한 환경에 적합합니다."
  },
  {
    "question": "NGINX에서 L4 로드 밸런싱을 위해 사용하는 블록은?",
    "options": [
      "http",
      "server",
      "location",
      "stream",
      "upstream"
    ],
    "answer": 3,
    "explanation": "TCP/UDP 레벨의 L4 로드 밸런싱은 stream 블록을 사용해 구성합니다."
  },
  {
    "question": "NGINX에서 proxy_cache_path directive는 어떤 역할을 하는가?",
    "options": [
      "백엔드 연결 설정",
      "프록시 서버 주소 지정",
      "캐시 저장소와 영역(zone) 정의",
      "요청의 헤더를 추가",
      "정규 표현식 설정"
    ],
    "answer": 2,
    "explanation": "proxy_cache_path는 캐시 저장 위치, zone 이름, 크기 등의 설정을 담당합니다."
  },
  {
    "question": "NGINX에서 캐시 데이터를 특정 시간 이후에 제거하기 위한 설정은?",
    "options": [
      "expires",
      "proxy_pass",
      "cache_revalidate",
      "inactive",
      "cache_key"
    ],
    "answer": 3,
    "explanation": "inactive는 특정 시간 동안 요청이 없으면 해당 캐시 데이터를 삭제합니다."
  },
  {
    "question": "NGINX에서 응답을 미러링 서버로 복사하려면 어떤 directive를 사용하는가?",
    "options": [
      "mirror_pass",
      "proxy_mirror",
      "mirror",
      "upstream_mirror",
      "split_clients"
    ],
    "answer": 2,
    "explanation": "mirror directive는 요청을 메인 서버 외에 미러 서버에도 복사 전송할 수 있도록 설정합니다."
  },
  {
    "question": "NGINX에서 upstream 서버를 weight 기반으로 로드 밸런싱하려면 어떻게 설정하는가?",
    "options": [
      "priority",
      "ip_hash",
      "server backend1 weight=3;",
      "least_conn=3;",
      "proxy_pass"
    ],
    "answer": 2,
    "explanation": "weight를 설정하여 특정 서버에 더 많은 요청이 분산되도록 할 수 있습니다."
  },
  {
    "question": "NGINX에서 HTTPS 설정 시 필수로 사용해야 하는 directive는?",
    "options": [
      "listen 80;",
      "ssl_protocols",
      "ssl_certificate",
      "proxy_ssl",
      "server_tokens"
    ],
    "answer": 2,
    "explanation": "HTTPS는 ssl_certificate와 ssl_certificate_key가 필수입니다."
  },
  {
    "question": "NGINX가 웹 서버로서 가지는 고유한 강점은?",
    "options": [
      "동기 방식 처리",
      "Apache 모듈 호환성",
      "이벤트 기반 아키텍처",
      "리버스 프록시 전용",
      "HTML 직접 렌더링"
    ],
    "answer": 2,
    "explanation": "이벤트 기반 아키텍처는 NGINX가 높은 동시성 처리 성능을 발휘할 수 있게 합니다."
  },
  {
    "question": "NGINX에서 동적 콘텐츠는 일반적으로 어떻게 처리되는가?",
    "options": [
      "CGI 엔진 직접 실행",
      "PHP 내장 실행",
      "FastCGI 또는 프록시 백엔드로 전달",
      "NGINX 자체 엔진 처리",
      "JavaScript 내장 처리"
    ],
    "answer": 2,
    "explanation": "NGINX는 동적 콘텐츠 처리를 외부 FastCGI 또는 백엔드 애플리케이션 서버에 위임합니다."
  },
  {
    "question": "NGINX 리버스 프록시에서 클라이언트 IP 정보를 유지하려면 어떤 헤더를 설정해야 하는가?",
    "options": [
      "Accept-Encoding",
      "X-Forwarded-Proto",
      "X-Real-IP",
      "Via",
      "Proxy-Authorization"
    ],
    "answer": 2,
    "explanation": "X-Real-IP는 클라이언트의 실제 IP 주소를 백엔드 서버로 전달합니다."
  },
  {
    "question": "NGINX의 proxy_set_header와 add_header의 차이점은?",
    "options": [
      "대상이 요청/응답인지 여부",
      "동작하는 포트 차이",
      "SSL 적용 여부",
      "정규표현식 사용 여부",
      "캐시 처리 여부"
    ],
    "answer": 0,
    "explanation": "proxy_set_header는 요청 헤더 조작, add_header는 응답 헤더 설정입니다."
  },
  {
    "question": "NGINX에서 캐시를 활성화하려면 어떤 directive가 필수로 필요할까?",
    "options": [
      "proxy_cache_path",
      "add_header",
      "upstream cache;",
      "fastcgi_buffer",
      "server_cache_enable"
    ],
    "answer": 0,
    "explanation": "proxy_cache_path는 캐시를 사용할 메모리 존(zone)을 먼저 정의합니다."
  },
  {
    "question": "정규 표현식 location을 대소문자 구분 없이 사용하려면 어떤 접두어를 사용하는가?",
    "options": [
      "^~",
      "~*",
      "~",
      "=",
      "!*"
    ],
    "answer": 1,
    "explanation": "~*는 대소문자 구분 없는 정규표현식 location 매칭에 사용됩니다."
  },
  {
    "question": "캐시된 응답의 유효 시간을 지정하는 directive는?",
    "options": [
      "proxy_pass",
      "proxy_cache_key",
      "proxy_cache_valid",
      "expires",
      "proxy_buffer_size"
    ],
    "answer": 2,
    "explanation": "proxy_cache_valid는 상태 코드에 따라 캐시 유효 시간을 정의합니다."
  },
  {
    "question": "다음 중 API Gateway 구성 시 중요하지 않은 요소는?",
    "options": [
      "라우팅",
      "인증",
      "요청 필터링",
      "정적 파일 서빙",
      "속도 제한(Rate Limiting)"
    ],
    "answer": 3,
    "explanation": "API Gateway는 동적 요청 처리와 제어 기능이 중심이며, 정적 파일 서빙은 주 목적이 아닙니다."
  },
  {
    "question": "로드 밸런싱 환경에서 세션 일관성을 위해 주로 사용하는 방법은?",
    "options": [
      "least_conn",
      "weight",
      "round_robin",
      "ip_hash",
      "zone_sync"
    ],
    "answer": 3,
    "explanation": "ip_hash는 같은 클라이언트 IP를 동일한 백엔드 서버에 연결하여 세션 유지를 보장합니다."
  },
  {
    "question": "다음 중 NGINX에서 실패한 서버를 로드밸런싱에서 올바르게 제외하는 지시문?",
    "options": [
      "server backend down;",
      "remove backend;",
      "server backend backup;",
      "server backend down weight=0;",
      "server backend max_fails=1 fail_timeout=5s;"
    ],
    "answer": 4,
    "explanation": "fail_timeout과 max_fails를 설정하면 실패한 서버는 일정 시간 동안 자동으로 제외됩니다."
  },
  {
    "question": "NGINX에서 캐시 무효화를 위해 사용하는 directive는?",
    "options": [
      "proxy_cache_valid",
      "proxy_cache_bypass",
      "cache_clean",
      "expires off",
      "max-age=0"
    ],
    "answer": 1,
    "explanation": "특정 조건에서 캐시 사용을 우회하려면 proxy_cache_bypass를 사용합니다."
  },
  {
    "question": "NGINX에서 캐시된 콘텐츠를 제거하지 않고 사용하도록 설정하려면?",
    "options": [
      "proxy_ignore_headers",
      "proxy_cache_use_stale",
      "inactive",
      "expires always",
      "cache_lock"
    ],
    "answer": 1,
    "explanation": "백엔드 오류 시에도 오래된 캐시를 사용하려면 proxy_cache_use_stale을 설정합니다."
  },
  {
    "question": "NGINX에서 FastCGI 처리 시 사용되는 주요 directive는?",
    "options": [
      "proxy_pass",
      "fastcgi_pass",
      "mirror_pass",
      "tcp_pass",
      "gzip_pass"
    ],
    "answer": 1,
    "explanation": "PHP와 같은 FastCGI 백엔드와 연동하려면 fastcgi_pass를 사용합니다."
  },
  {
    "question": "NGINX에서 keepalive directive를 사용하는 주요 목적은?",
    "options": [
      "서버 간 연결 차단",
      "요청을 백업 서버로 전달",
      "연결 재사용을 통한 성능 향상",
      "캐시 무효화 설정",
      "SSL 종료 처리"
    ],
    "answer": 2,
    "explanation": "keepalive는 백엔드와의 연결을 재사용하여 성능을 향상시키고 리소스를 절약합니다."
  },
  {
    "question": "다음 중 add_header directive가 적용되지 않는 경우는?",
    "options": [
      "200 OK 응답",
      "301 리디렉션 응답",
      "404 오류 응답",
      "304 Not Modified 응답 ",
      "308 Permanent Redirect 응답"
    ],
    "answer": 2,
    "explanation": "기본적으로 add_header는 200, 204, 301, 302, 304 상태 코드에만 적용됩니다. always 키워드를 사용해야 모든 응답 코드에 적용할 수 있습니다."
  },
  {
    "question": "NGINX에서 정적 파일을 제공할 때 사용하는 directive는?",
    "options": [
      "proxy_pass",
      "alias",
      "ssl_certificate",
      "mirror",
      "set_header"
    ],
    "answer": 1,
    "explanation": "alias는 특정 경로를 다른 파일 시스템 경로로 매핑하여 정적 파일을 제공할 수 있게 합니다."
  },
  {
    "question": "NGINX에서 map 블록을 사용하여 할 수 없는 작업은?",
    "options": [
      "User-Agent에 따른 변수 설정",
      "클라이언트 IP에 따라 접근 제어",
      "요청 경로 기반 리다이렉트",
      "동적으로 변수 값 설정",
      "프록시 백엔드 서버 수 증가"
    ],
    "answer": 4,
    "explanation": "map은 조건에 따라 변수 값을 설정하는 데 사용되며, 직접적으로 백엔드 서버 수를 조절할 수는 없습니다."
  },
  {
    "question": "proxy_cache_key directive의 역할은 무엇인가?",
    "options": [
      "캐시 디렉토리 지정",
      "백엔드 연결 수 설정",
      "요청 URL 캐시 키 결정",
      "로그 레벨 지정",
      "TLS 암호 스위트 설정"
    ],
    "answer": 2,
    "explanation": "proxy_cache_key는 요청마다 고유한 캐시 키를 정의하여, 어떤 요청을 어떤 캐시에 저장할지 결정합니다."
  },
  {
    "question": "NGINX에서 gzip 압축 설정을 적용하려면 반드시 설정해야 하는 directive는?",
    "options": [
      "gzip_types",
      "proxy_pass",
      "client_body_size",
      "listen 443 ssl;",
      "worker_connections"
    ],
    "answer": 0,
    "explanation": "gzip_types는 어떤 MIME 타입에 대해 압축을 적용할지를 지정합니다. gzip on;과 함께 사용됩니다."
  },
  {
    "question": "다음 중 open source NGINX에서 기본 제공되지 않는 기능은?",
    "options": [
      "L7 리버스 프록시",
      "HTTP 캐시",
      "미러링",
      "TCP 로드밸런싱",
      "액티브 헬스 체크"
    ],
    "answer": 4,
    "explanation": "액티브 헬스 체크는 NGINX Plus에서 제공되며, 오픈소스 버전에서는 수동 설정이나 3rd-party 모듈이 필요합니다."
  },
  {
    "question": "NGINX에서 캐시된 콘텐츠가 갱신되지 않도록 조건을 설정하려면 어떤 directive를 사용하는가?",
    "options": [
      "proxy_cache_bypass",
      "proxy_cache_lock",
      "proxy_ignore_headers",
      "proxy_pass_request_headers",
      "proxy_set_cache"
    ],
    "answer": 2,
    "explanation": "proxy_ignore_headers는 백엔드 응답의 캐시 관련 헤더(예: Cache-Control)를 무시하고 캐시 유지 정책을 강제합니다."
  },
  {
    "question": "다음 중 NGINX의 location 블록에 사용할 수 없는 접두어는?",
    "options": [
      "=",
      "~",
      "^~",
      "!*",
      "~*"
    ],
    "answer": 3,
    "explanation": "!*는 NGINX에서 사용되는 접두어가 아닙니다. 나머지는 정확한 location 매칭을 위한 접두어입니다."
  },
  {
    "question": "NGINX의 resolver directive는 어떤 상황에서 주로 사용되는가?",
    "options": [
      "SSL 인증서 설정",
      "DNS 기반 로드밸런싱",
      "캐시 정책 설정",
      "클라이언트 IP 차단",
      "정적 파일 경로 지정"
    ],
    "answer": 1,
    "explanation": "resolver는 도메인 이름을 동적으로 해석(DNS 쿼리)해야 할 경우 필요합니다. 예: proxy_pass에서 도메인 사용 시."
  }
    ],
    "F5N3": [
          {
            "question": "nginx -s stop 명령이 수행하는 작업은?",
            "options": [
              "마스터 및 워커 프로세스를 정상 종료",
              "설정 파일을 테스트하고 적용",
              "설정을 리로드",
              "NGINX를 비정상 종료",
              "워커 프로세스만 종료"
            ],
            "answer": 0,
            "explanation": ""
          },
          {
            "question": "설정을 적용하기 전에 문법 오류가 있는지 확인하려면 어떤 명령을 사용해야 하는가?",
            "options": [
              "nginx -t",
              "nginx --check",
              "nginx -s test",
              "nginx configtest",
              "nginx -c"
            ],
            "answer": 0,
            "explanation": ""
          },
          {
            "question": "kill -HUP <nginx pid> 시그널의 효과는?",
            "options": [
              "설정을 다시 로드",
              "NGINX 프로세스 강제 종료",
              "NGINX 완전 재시작",
              "에러 로그 초기화",
              "리스닝 포트 변경"
            ],
            "answer": 0,
            "explanation": ""
          },
          {
            "question": "nginx -s reload와 nginx -s stop && nginx의 주요 차이는?",
            "options": [
              "후자는 다운타임이 발생함",
              "로그 디렉토리를 다르게 사용",
              "SSL 핸드셰이크 차이",
              "전자는 PID를 변경함",
              "둘 다 완전한 재시작"
            ],
            "answer": 0,
            "explanation": ""
          },
          {
            "question": "NGINX를 수동으로 종료하려면 어떤 명령이 가장 적절한가?",
            "options": [
              "systemctl stop nginx",
              "nginx --exit",
              "nginx -s restart",
              "nginx -z",
              "nginx -s kill"
            ],
            "answer": 0,
            "explanation": ""
          },
          {
            "question": "403 Forbidden 오류의 일반적인 원인은?",
            "options": [
              "파일 권한 부족",
              "프록시 백엔드 연결 실패",
              "gzip 설정 오류",
              "인증서 만료",
              "서버 이름 불일치"
            ],
            "answer": 0,
            "explanation": ""
          },
          {
            "question": "HTTP 502 Bad Gateway 오류의 원인은?",
            "options": [
              "설정 파일에 문법 오류",
              "백엔드 서버 미응답",
              "TLS 핸드셰이크 실패",
              "파일이 존재하지 않음",
              "리스닝 포트 누락"
            ],
            "answer": 1,
            "explanation": ""
          },
          {
            "question": "access.log에서 $status가 499인 의미는?",
            "options": [
              "요청이 정상적으로 완료됨",
              "클라이언트가 연결을 중단함",
              "서버 에러 발생",
              "캐시에서 응답",
              "SSL 핸드셰이크 실패"
            ],
            "answer": 1,
            "explanation": ""
          },
          {
            "question": "NGINX 시작 시 \"bind() to 0.0.0.0:80 failed\" 에러가 발생했다면?",
            "options": [
              "인증서가 만료됨",
              "포트가 이미 사용 중임",
              "gzip 설정 누락",
              "루트 디렉토리 오류",
              "PID 파일이 없음"
            ],
            "answer": 1,
            "explanation": ""
          },
          {
            "question": "복수의 가상 호스트에서 동일한 포트를 사용할 경우 충돌을 방지하려면?",
            "options": [
              "listen 포트를 다르게 설정",
              "(하나의) server 블록만 default_server로 지정하고, 나머지는 server_name을 정확히 설정",
              "SSL 설정을 모두 비활성화",
              "access_log를 공통으로 지정",
              "error_log를 주석 처리"
            ],
            "answer": 1,
            "explanation": ""
          },
          {
            "question": "add_header 설정이 location 블록에서 적용되지 않는 이유는?",
            "options": [
              "정규식 location 우선순위",
              "응답 코드가 200이 아니기 때문",
              "gzip 압축과 충돌",
              "add_header는 if 블록에서만 적용",
              "부모 블록에서 설정되어 override 불가"
            ],
            "answer": 1,
            "explanation": ""
          },
          {
            "question": "여러 location 블록이 있는 경우 NGINX가 선택하는 기준은?",
            "options": [
              "정의 순서",
              "정규 표현식이 우선",
              "짧은 URI 우선",
              "설정 파일 이름 우선",
              "서버 이름"
            ],
            "answer": 1,
            "explanation": ""
          },
          {
            "question": "클라이언트가 요청을 했지만 응답이 지연될 때 확인해야 할 항목은?",
            "options": [
              "리스닝 포트",
              "gzip 설정",
              "백엔드 서버 응답 시간",
              "SSL 인증서 체인",
              "에러 코드"
            ],
            "answer": 2,
            "explanation": ""
          },
          {
            "question": "설정은 문제없는데 서비스가 시작되지 않는다면 SELinux 관련 항목으로 무엇을 점검해야 하나?",
            "options": [
              "서비스 포트",
              "worker_processes 수",
              "context type (예: httpd_sys_content_t)",
              "gzip 설정 여부",
              "upstream 이름"
            ],
            "answer": 2,
            "explanation": ""
          },
          {
            "question": "SELinux 환경에서 HTTP 요청이 거부될 경우 확인할 명령은?",
            "options": [
              "ausearch -m avc -ts recent",
              "ls -Z",
              "위 모두",
              "getenforce",
              "해당 없음"
            ],
            "answer": 2,
            "explanation": ""
          },
          {
            "question": "HTTPS 연결 시 “ERR_CERT_DATE_INVALID” 오류가 발생한 경우는?",
            "options": [
              "포트 충돌",
              "DNS 설정 문제",
              "인증서 유효기간 만료",
              "gzip 설정 누락",
              "캐시 만료"
            ],
            "answer": 2,
            "explanation": ""
          },
          {
            "question": "클라이언트가 \"SSL handshake failed\" 메시지를 출력할 때 점검해야 할 것은?",
            "options": [
              "listen 포트",
              "캐시 경로",
              "인증서 및 키 쌍의 유효성",
              "gzip 여부",
              "로깅 수준"
            ],
            "answer": 2,
            "explanation": ""
          },
          {
            "question": "TLS 설정에서 ssl_verify_client를 on으로 설정했을 때 예상되는 결과는?",
            "options": [
              "서버 인증 생략",
              "클라이언트 인증 생략",
              "클라이언트 인증서가 없으면 연결 거부",
              "gzip 자동 활성화",
              "프록시 로깅 중단"
            ],
            "answer": 2,
            "explanation": ""
          },
          {
            "question": "인증서가 PEM 형식이 아닐 경우 발생 가능한 문제는?",
            "options": [
              "접근 로그 누락",
              "gzip 미적용",
              "서버 자동 종료",
              "TLS 연결 실패",
              "요청 URI 재정의"
            ],
            "answer": 3,
            "explanation": ""
          },
          {
            "question": "ssl_certificate와 ssl_certificate_key 경로가 잘못되었을 경우 발생하는 현상은?",
            "options": [
              "HTTP 요청으로 대체됨",
              "gzip 오류 발생",
              "캐시 무효화",
              "TLS 핸드셰이크 실패",
              "DNS 재전파"
            ],
            "answer": 3,
            "explanation": ""
          },
          {
            "question": "HTTPS 접속 시 ERR_CERT_COMMON_NAME_INVALID 오류가 발생하는 원인은?",
            "options": [
              "클라이언트 IP 차단",
              "gzip 설정 누락",
              "DNS 루프",
              "인증서의 Common Name이 요청한 도메인과 불일치",
              "SELinux 설정 부족"
            ],
            "answer": 3,
            "explanation": ""
          },
          {
            "question": "ssl_certificate 파일 경로가 잘못되었을 때 설정 적용 시 나타나는 오류는?",
            "options": [
              "403 Forbidden",
              "404 Not Found",
              "gzip 압축 오류",
              "NGINX 재시작 실패 및 error.log에 파일 경로 오류",
              "연결 유지 실패"
            ],
            "answer": 3,
            "explanation": ""
          },
          {
            "question": "클라이언트 측에서 TLS 연결 시도 후 “unknown CA” 오류가 발생한다면?",
            "options": [
              "서버의 공개키가 누락됨",
              "서버가 gzip을 비활성화함",
              "포트 바인딩 실패",
              "인증서 서명자가 신뢰되지 않음",
              "접속 제한 시간 초과"
            ],
            "answer": 3,
            "explanation": ""
          },
          {
            "question": "TLS 설정 변경 후 테스트를 위한 명령으로 적절한 것은?",
            "options": [
              "curl -k https://example.com",
              "wget -qO- http://localhost",
              "dig example.com A",
              "openssl s_client -connect example.com:443",
              "ping example.com"
            ],
            "answer": 3,
            "explanation": ""
          },
          {
            "question": "다음 중 NGINX에서 클라이언트 접속 문제를 디버깅할 때 가장 유용한 로그는?",
            "options": [
              "boot.log",
              "/etc/nginx/mime.types",
              "yum.log",
              "/proc/cpuinfo",
              "/var/log/nginx/access.log"
            ],
            "answer": 4,
            "explanation": ""
          },
          {
            "question": "HTTP 상태 코드 504는 무엇을 의미하는가?",
            "options": [
              "서버 응답 없음",
              "DNS 해결 실패",
              "요청 본문 형식 오류",
              "인증 실패",
              "게이트웨이 타임아웃 (백엔드 응답 지연)"
            ],
            "answer": 4,
            "explanation": ""
          },
          {
            "question": "다중 server 블록에서 요청이 의도한 블록이 아닌 다른 블록으로 전달된다면 가장 먼저 점검할 설정은?",
            "options": [
              "listen 포트",
              "location 블록 개수",
              "proxy_set_header",
              "access_log 경로",
              "server_name 정확도 및 default_server 지정 여부"
            ],
            "answer": 4,
            "explanation": ""
          },
          {
            "question": "NGINX가 실행 중인 것처럼 보이지만 실제 요청이 응답되지 않는다면 우선적으로 점검할 항목은?",
            "options": [
              "로깅 포맷",
              "gzip 상태",
              "정적 파일 수",
              "mime.types 설정",
              "방화벽 상태 및 포트 열림 여부"
            ],
            "answer": 4,
            "explanation": ""
          },
          {
            "question": "다음 중 nginx -T 명령의 주요 기능은?",
            "options": [
              "PID 재설정",
              "프로세스 상태 표시",
              "SSL 재시작",
              "백엔드 서버 헬스체크",
              "설정 파일 전체 병합 내용 출력"
            ],
            "answer": 4,
            "explanation": ""
          },
          {
            "question": "다음 중 NGINX 구동 실패 시 가장 먼저 확인해야 하는 파일은?",
            "options": [
              "/etc/hosts",
              "/etc/nginx/mime.types",
              "/var/run/nginx.pid",
              "/etc/shadow",
              "/var/log/nginx/error.log"
            ],
            "answer": 4,
            "explanation": ""
          }
    ],
    "F5N4": [
  {
    "question": "nginx -s stop 명령이 수행하는 작업은?",
    "options": [
      "마스터와 워커 프로세스를 모두 정상 종료",
      "설정 파일을 테스트하고 적용",
      "설정을 리로드",
      "NGINX를 비정상 종료",
      "워커 프로세스만 종료"
    ],
    "answer": 0,
    "explanation": "nginx -s stop은 마스터와 워커 프로세스를 모두 종료시킵니다."
  },
  {
    "question": "설정을 적용하기 전에 문법 오류가 있는지 확인하려면 어떤 명령을 사용해야 하는가?",
    "options": [
      "nginx -t",
      "nginx --check",
      "nginx -s test",
      "nginx configtest",
      "nginx -c"
    ],
    "answer": 0,
    "explanation": "nginx -t는 설정의 문법 및 유효성을 확인합니다."
  },
  {
    "question": "kill -HUP <nginx pid> 시그널의 효과는?",
    "options": [
      "설정을 다시 로드",
      "NGINX 프로세스 강제 종료",
      "NGINX 완전 재시작",
      "에러 로그 초기화",
      "리스닝 포트 변경"
    ],
    "answer": 0,
    "explanation": "HUP 시그널은 설정을 다시 로드하며 프로세스를 재시작하지 않습니다."
  },
  {
    "question": "nginx -s reload와 nginx -s stop && nginx의 주요 차이는?",
    "options": [
      "후자는 다운타임이 발생함",
      "로그 디렉토리를 다르게 사용",
      "SSL 핸드셰이크 차이",
      "전자는 PID를 변경함",
      "둘 다 완전한 재시작"
    ],
    "answer": 0,
    "explanation": "reload는 무중단 구성 반영이고, stop && start는 일시적으로 중단됩니다."
  },
  {
    "question": "NGINX를 수동으로 종료하려면 어떤 명령이 가장 적절한가?",
    "options": [
      "systemctl stop nginx",
      "nginx --exit",
      "nginx -s restart",
      "nginx -z",
      "nginx -s kill"
    ],
    "answer": 0,
    "explanation": "systemd 기반 시스템에서는 systemctl stop nginx를 통해 서비스 종료합니다."
  },
  {
    "question": "403 Forbidden 오류의 일반적인 원인은?",
    "options": [
      "파일 권한 부족",
      "프록시 백엔드 연결 실패",
      "gzip 설정 오류",
      "인증서 만료",
      "서버 이름 불일치"
    ],
    "answer": 0,
    "explanation": "접근 권한이 없으면 403 오류가 발생합니다."
  },
  {
    "question": "HTTP 502 Bad Gateway 오류의 원인은?",
    "options": [
      "설정 파일에 문법 오류",
      "백엔드 서버 미응답",
      "TLS 핸드셰이크 실패",
      "파일이 존재하지 않음",
      "리스닝 포트 누락"
    ],
    "answer": 1,
    "explanation": "502는 프록시된 서버가 응답하지 않거나 오류를 반환할 때 발생합니다."
  },
  {
    "question": "access.log에서 $status가 499인 의미는?",
    "options": [
      "요청이 정상적으로 완료됨",
      "클라이언트가 연결을 중단함",
      "서버 에러 발생",
      "캐시에서 응답",
      "SSL 핸드셰이크 실패"
    ],
    "answer": 1,
    "explanation": "499는 클라이언트가 응답을 받기 전 연결을 종료했을 때 기록됩니다."
  },
  {
    "question": "NGINX 시작 시 \"bind() to 0.0.0.0:80 failed\" 에러가 발생했다면?",
    "options": [
      "인증서가 만료됨",
      "포트가 이미 사용 중임",
      "gzip 설정 누락",
      "루트 디렉토리 오류",
      "PID 파일이 없음"
    ],
    "answer": 1,
    "explanation": "이미 다른 프로세스가 해당 포트를 사용 중일 경우 bind 오류가 납니다."
  },
  {
    "question": "복수의 가상 호스트에서 동일한 포트를 사용할 경우 충돌을 방지하려면?",
    "options": [
      "listen 포트를 다르게 설정",
      "(하나만) server 블록에 default_server를 지정, 나머지는 server_name으로 구분",
      "SSL 설정을 모두 비활성화",
      "access_log를 공통으로 지정",
      "error_log를 주석 처리"
    ],
    "answer": 1,
    "explanation": "동일 포트에 여러 서버 블록이 있을 때, (하나만) default_server로 지정해야 충돌이 없습니다."
  },
  {
    "question": "add_header 설정이 location 블록에서 적용되지 않는 경우, 그그 이유는?",
    "options": [
      "정규식 location 우선순위",
      "응답 코드가 200이 아니기 때문",
      "gzip 압축과 충돌",
      "add_header는 if 블록에서만 적용",
      "부모 블록에서 설정되어 override 불가"
    ],
    "answer": 1,
    "explanation": "add_header는 기본적으로 200, 204, 301, 302 응답에만 적용됩니다."
  },
  {
    "question": "여러 location 블록이 있는 경우 NGINX가 선택하는 기준은?",
    "options": [
      "정의 순서",
      "정규 표현식이 우선",
      "짧은 URI 우선",
      "설정 파일 이름 우선",
      "서버 이름"
    ],
    "answer": 1,
    "explanation": "정규표현식 location (~, ~*)은 일반 prefix location보다 우선합니다."
  },
  {
    "question": "클라이언트가 요청을 했지만 응답이 지연될 때 확인해야 할 항목은?",
    "options": [
      "리스닝 포트",
      "gzip 설정",
      "백엔드 서버 응답 시간",
      "SSL 인증서 체인",
      "에러 코드"
    ],
    "answer": 2,
    "explanation": "응답 지연은 대개 백엔드 서버 성능 문제에서 기인합니다."
  },
  {
    "question": "설정은 문제없는데 서비스가 시작되지 않는다면 SELinux 관련 항목으로 무엇을 점검해야 하나?",
    "options": [
      "서비스 포트",
      "worker_processes 수",
      "context type (예: httpd_sys_content_t)",
      "gzip 설정 여부",
      "upstream 이름"
    ],
    "answer": 2,
    "explanation": "SELinux에서는 NGINX가 접근할 리소스에 대해 적절한 context type이 설정되어야 합니다."
  },
  {
    "question": "SELinux 환경에서 HTTP 요청이 거부될 경우 확인할 명령은?",
    "options": [
      "ausearch -m avc -ts recent",
      "ls -Z",
      "위 모두",
      "getenforce",
      "해당 없음"
    ],
    "answer": 2,
    "explanation": "SELinux 트러블슈팅 시 context 확인 및 거부 로그 확인이 필수입니다."
  },
  {
    "question": "HTTPS 연결 시 \"ERR_CERT_DATE_INVALID\" 오류가 발생한 경우는?",
    "options": [
      "포트 충돌",
      "DNS 설정 문제",
      "인증서 유효기간 만료",
      "gzip 설정 누락",
      "캐시 만료"
    ],
    "answer": 2,
    "explanation": "인증서 유효기간이 만료되었을 경우 이 오류가 나타납니다."
  },
  {
    "question": "클라이언트가 \"SSL handshake failed\" 메시지를 출력할 때 점검해야 할 것은?",
    "options": [
      "listen 포트",
      "캐시 경로",
      "인증서 및 키 쌍의 유효성",
      "gzip 여부",
      "로깅 수준"
    ],
    "answer": 2,
    "explanation": "인증서 및 키가 잘못되면 TLS 핸드셰이크 실패가 발생합니다."
  },
  {
    "question": "TLS 설정에서 ssl_verify_client를 on으로 설정했을 때 예상되는 결과는?",
    "options": [
      "서버 인증 생략",
      "클라이언트 인증 생략",
      "클라이언트 인증서가 없으면 연결 거부",
      "gzip 자동 활성화",
      "프록시 로깅 중단"
    ],
    "answer": 2,
    "explanation": "ssl_verify_client on은 클라이언트 인증서를 강제하여 없으면 연결을 거부합니다."
  },
  {
    "question": "인증서가 PEM 형식이 아닐 경우 발생 가능한 문제는?",
    "options": [
      "접근 로그 누락",
      "gzip 미적용",
      "서버 자동 종료",
      "TLS 연결 실패",
      "요청 URI 재정의"
    ],
    "answer": 3,
    "explanation": "NGINX는 PEM 형식 인증서를 요구하므로, 아닐 경우 TLS 연결이 실패합니다."
  },
  {
    "question": "ssl_certificate와 ssl_certificate_key 경로가 잘못되었을 경우 발생하는 현상은?",
    "options": [
      "HTTP 요청으로 대체됨",
      "gzip 오류 발생",
      "캐시 무효화",
      "TLS 핸드셰이크 실패",
      "DNS 재전파"
    ],
    "answer": 3,
    "explanation": "TLS에 필요한 파일이 없으면 연결 자체가 실패합니다."
  },
  {
    "question": "HTTPS 접속 시 ERR_CERT_COMMON_NAME_INVALID 오류가 발생하는 원인은?",
    "options": [
      "클라이언트 IP 차단",
      "gzip 설정 누락",
      "DNS 루프",
      "인증서의 Common Name이 요청한 도메인과 불일치",
      "SELinux 설정 부족"
    ],
    "answer": 3,
    "explanation": "인증서 CN(Common Name) 또는 SAN이 요청 도메인과 불일치하면 이 오류가 납니다."
  },
  {
    "question": "ssl_certificate 파일 경로가 잘못되었을 때 설정 적용 시 나타나는 오류는?",
    "options": [
      "403 Forbidden",
      "404 Not Found",
      "gzip 압축 오류",
      "NGINX 재시작 실패 및 error.log에 파일 경로 오류",
      "연결 유지 실패"
    ],
    "answer": 3,
    "explanation": "인증서 경로 오류가 있으면 NGINX 로드시 에러가 발생하며 시작이 실패할 수 있습니다."
  },
  {
    "question": "클라이언트 측에서 TLS 연결 시도 후 \"unknown CA\" 오류가 발생한다면?",
    "options": [
      "서버의 공개키가 누락됨",
      "서버가 gzip을 비활성화함",
      "포트 바인딩 실패",
      "인증서 서명자가 신뢰되지 않음",
      "접속 제한 시간 초과"
    ],
    "answer": 3,
    "explanation": "클라이언트는 신뢰하는 루트CA로 서명되지 않은 인증서를 unknown CA로 처리합니다."
  },
  {
    "question": "TLS 설정 변경 후 테스트를 위한 명령으로 적절한 것은?",
    "options": [
      "curl -k https://example.com",
      "wget -qO- http://localhost",
      "dig example.com A",
      "openssl s_client -connect example.com:443",
      "ping example.com"
    ],
    "answer": 3,
    "explanation": "openssl s_client -connect ... 명령을 통해 TLS 연결 디버깅 및 인증서를 확인할 수 있습니다."
  },
  {
    "question": "다음 중 NGINX에서 클라이언트 접속 문제를 디버깅할 때 가장 유용한 로그는?",
    "options": [
      "boot.log",
      "/etc/nginx/mime.types",
      "yum.log",
      "/proc/cpuinfo",
      "/var/log/nginx/access.log"
    ],
    "answer": 4,
    "explanation": "access.log에는 요청된 URI, 클라이언트 IP, 응답 시간, 상태 코드 등이 기록됩니다."
  },
  {
    "question": "HTTP 상태 코드 504는 무엇을 의미하는가?",
    "options": [
      "서버 응답 없음",
      "DNS 해결 실패",
      "요청 본문 형식 오류",
      "인증 실패",
      "게이트웨이 타임아웃 (백엔드 응답 지연)"
    ],
    "answer": 4,
    "explanation": "504 Gateway Timeout은 백엔드 서버가 정해진 시간 내 응답을 하지 않았음을 의미합니다."
  },
  {
    "question": "다중 server 블록에서 요청이 의도한 블록이 아닌 다른 블록으로 전달된다면 가장 먼저 점검할 설정은?",
    "options": [
      "listen 포트",
      "location 블록 개수",
      "proxy_set_header",
      "access_log 경로",
      "server_name 정확도 및 default_server 지정 여부"
    ],
    "answer": 4,
    "explanation": "정확한 도메인 매칭이 되지 않으면 default_server가 요청을 처리할 수 있습니다."
  },
  {
    "question": "NGINX가 실행 중인 것처럼 보이지만 실제 요청이 응답되지 않는다면 우선적으로 점검할 항목은?",
    "options": [
      "로깅 포맷",
      "gzip 상태",
      "정적 파일 수",
      "mime.types 설정",
      "방화벽 상태 및 포트 열림 여부"
    ],
    "answer": 4,
    "explanation": "서비스가 실행 중이라도 방화벽에서 포트를 차단하고 있다면 외부 접속은 차단됩니다."
  },
  {
    "question": "다음 중 nginx -T 명령의 주요 기능은?",
    "options": [
      "PID 재설정",
      "프로세스 상태 표시",
      "SSL 재시작",
      "백엔드 서버 헬스체크",
      "설정 파일 전체 병합 내용 출력"
    ],
    "answer": 4,
    "explanation": "-T는 병합된 전체 설정을 출력하여 디버깅 및 설정 확인 시 유용합니다."
  },
  {
    "question": "다음 중 NGINX 구동 실패 시 가장 먼저 확인해야 하는 파일은?",
    "options": [
      "/etc/hosts",
      "/etc/nginx/mime.types",
      "/var/run/nginx.pid",
      "/etc/shadow",
      "/var/log/nginx/error.log"
    ],
    "answer": 4,
    "explanation": "구동 실패 원인은 error.log에 가장 상세하게 기록됩니다."
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

def get_all_questions(max_questions=120):
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