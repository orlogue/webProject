FROM python:3.10.2
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
VOLUME ["/backend/db", "/backend/media"]