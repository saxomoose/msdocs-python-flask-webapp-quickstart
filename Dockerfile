FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 50505
EXPOSE 5000

# ENTRYPOINT ["gunicorn", "app:app"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]