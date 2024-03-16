FROM python:3.11

WORKDIR /hub_researcher

COPY . . 

RUN python3 -m pip install -r requirements.txt

RUN RUN python3 run.py --init