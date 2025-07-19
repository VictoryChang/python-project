FROM python:alpine3.16

LABEL maintainer="Victory Chang"

USER root

WORKDIR /workspace

COPY ./tests/ .
COPY ./calculator.py .
COPY ./main.py .
COPY ./requirements.txt .

RUN pip install --no-cache-dir --requirement requirements.txt

USER nobody
EXPOSE 3000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
