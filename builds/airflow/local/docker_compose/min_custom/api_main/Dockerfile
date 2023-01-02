FROM python:3.8.16-slim-bullseye

EXPOSE 5000

WORKDIR /opt/app

COPY entrypoint.sh /opt/scripts/entrypoint.sh
RUN chmod +x /opt/scripts/entrypoint.sh
ENTRYPOINT ["bash", "/opt/scripts/entrypoint.sh"]