FROM python:3.8.5

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY photogram /code
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
EXPOSE 8000
CMD [ "sh", "-c", \
"python manage.py runserver 0:8000" \
]
