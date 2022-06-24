FROM mypython:v1

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /duan
WORKDIR /duan

COPY requirements.txt /duan/
RUN pip install -r requirements.txt 

COPY ./duan /duan/