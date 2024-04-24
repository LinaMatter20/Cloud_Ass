
FROM python:3.9

WORKDIR /app

COPY  ./ pythoncloud.py

RUN pip install nltk 


CMD ["python", "pythoncloud.py"]