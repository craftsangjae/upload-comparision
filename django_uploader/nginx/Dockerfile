# Dockerfile for Nginx
FROM nginx:latest

# 기존 설정 제거 및 새 설정 복사
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d