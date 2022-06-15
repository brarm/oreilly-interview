# syntax=docker/dockerfile:1
FROM amd64/ubuntu:22.10
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update -yyq && apt upgrade -yyq
RUN apt install software-properties-common -yyq
RUN apt install python3.10 python3-pip postgresql -yyq
WORKDIR /home
COPY requirements.txt ./
COPY api.py ./
RUN pip install -r ./requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "api.py" ]
