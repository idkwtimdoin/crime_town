FROM python:3.10.5-slim-buster

ARG WORKDIR=/opt/app
RUN mkdir -p ${WORKDIR}

WORKDIR ${WORKDIR}

# * ISNTALL APP REQUIREMENTS
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# * COPY NECESSARY FILES & FOLDERS
COPY src ./src

ENTRYPOINT [ "python3", "src/app.py" ]
