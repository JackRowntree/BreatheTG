# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY setup.py setup.py
RUN pip install .
COPY tg_bot .
CMD ["ls"]
CMD ["python","-u", "tg_bot.py"]