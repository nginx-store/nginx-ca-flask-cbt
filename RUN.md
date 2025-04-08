# NGINX 자격증 CBT 애플리케이션 - Docker 지침

## Docker를 사용한 설치 및 실행

### 사전 요구사항

- [Docker](https://docs.docker.com/get-docker/) 설치
- [Docker Compose](https://docs.docker.com/compose/install/) 설치 (선택 사항)

### Docker를 사용한 실행 방법

#### 방법 1: Docker 명령어 직접 사용

1. 이미지 빌드:
   ```bash
   docker build -t nginx-cbt-app .
   ```

2. 컨테이너 실행:
   ```bash
   docker run -p 5000:5000 --name nginx-cbt-app nginx-cbt-app
   ```

#### 방법 2: Docker Compose 사용 (권장)

1. 다음 명령어로 애플리케이션 시작:
   ```bash
   docker-compose up -d
   ```

2. 로그 확인:
   ```bash
   docker-compose logs -f
   ```

3. 애플리케이션 중지:
   ```bash
   docker-compose down
   ```

### 환경 변수 설정

Docker에서 환경 변수를 사용하여 애플리케이션 구성을 변경할 수 있습니다:

- `docker-compose.yml` 파일의 `environment` 섹션에서 환경 변수를 설정하거나
- `docker run` 명령어 사용 시 `-e` 옵션을 사용하여 환경 변수 설정:

```bash
docker run -p 5000:5000 -e DEBUG=True -e SECRET_KEY=my-secret-key nginx-cbt-app
```

### 볼륨 마운트 (개발 환경용)

개발 중에 코드 변경 사항을 실시간으로 적용하려면:

1. `docker-compose.yml` 파일의 `volumes` 섹션에서 주석을 제거:
   ```yaml
   volumes:
     - ./app:/app/app
   ```

2. 다음 명령어로 애플리케이션 재시작:
   ```bash
   docker-compose down && docker-compose up -d
   ```

## 문제 해결

### 포트 충돌 문제

포트 5000이 이미 사용 중인 경우 다른 포트로 매핑할 수 있습니다:

```bash
docker run -p 8080:5000 nginx-cbt-app
```

또는 `docker-compose.yml` 파일에서:
```yaml
ports:
  - "8080:5000"
```

### 컨테이너 로그 확인

애플리케이션 문제 진단을 위해 컨테이너 로그를 확인:

```bash
docker logs nginx-cbt-app
```