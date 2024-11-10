FROM python:3.13.0

EXPOSE 5000

WORKDIR /back-end

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src

WORKDIR /back-end/src
CMD ["python", "database.py"]
