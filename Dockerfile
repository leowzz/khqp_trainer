FROM python:3.10-slim-buster

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app

WORKDIR /app

RUN chmod +x ./start.sh

CMD ["./start.sh"]