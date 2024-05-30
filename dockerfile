FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /imgtxt
WORKDIR /imgtxt
COPY requirements.txt /imgtxt/
RUN pip install -r requirements.txt
COPY . /imgtxt/
CMD python manage.py runserver 0.0.0.0:8080