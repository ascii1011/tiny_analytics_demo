FROM python:3.8.16-slim-bullseye

LABEL org.unlimitedchange.image.authors="Christopher R. Harty <ascii1011@gmail.com>"

EXPOSE 5000

RUN echo '[ ! -z "$TERM" -a -r /etc/motd ] && cat /etc/os-release && python --version && cat /etc/issue && cat /etc/motd' \
    >> /etc/bash.bashrc \
    ; echo "\
    =============\n\
    = API Main (The gateway and routing for for all requests)\n\
    = clients and services may make requests to this api from perhaps nextjs or Airflow\n\
    =============\n\
    \n\
    API: One API To Rule Them All :) \n\
    (c) Christopher R. Harty <ascii1011@gmail.com> \n\
    \n\
    Currently this container is being manually operated. \n\
    Instructions include: \n\
     - '. /opt/venv/bin/activate' \n\
     - './run.sh' \n\
     - or 'python test.py' \n\
     - 'deactivate' \n\
    \n\
    code is provided as a volume resource, so changes should be done from the host... not wihtin the container!!!!!!\n\
    \n\
    "\
        > /etc/motd

WORKDIR /opt/app

COPY entrypoint.sh /opt/scripts/entrypoint.sh
RUN chmod +x /opt/scripts/entrypoint.sh
ENTRYPOINT ["bash", "/opt/scripts/entrypoint.sh"]