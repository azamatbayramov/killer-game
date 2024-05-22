FROM python:3.12 AS base

WORKDIR /app

COPY ./requirements/base.txt /app/base.txt
RUN pip install --no-cache-dir --upgrade -r /app/base.txt

FROM base AS api

WORKDIR /app

COPY requirements/api.txt /app/api.txt
RUN pip install --no-cache-dir --upgrade -r /app/api.txt

COPY ./backend /app/src

CMD ["python", "src/run_api.py"]

FROM base AS bot

WORKDIR /app

COPY requirements/bot.txt /app/bot.txt
RUN pip install --no-cache-dir --upgrade -r /app/bot.txt

COPY ./backend /app/src

CMD ["python", "src/run_bot.py"]
