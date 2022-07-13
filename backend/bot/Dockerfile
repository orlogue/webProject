FROM python:3.10.2
ENV PYTHONUNBUFFERED=1
WORKDIR /bot
RUN pip install requests python-telegram-bot
COPY . .
EXPOSE 8443