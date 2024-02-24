# Dockerfile
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# Poetry 설치
RUN pip install poetry

# 프로젝트 파일 복사
COPY . .

# Poetry를 사용하여 의존성 설치
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

# gunicorn을 사용하여 Django 앱 실행
ENTRYPOINT ["python", "main.py"]