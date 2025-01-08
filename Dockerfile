FROM python:3.9

COPY ./app /app
WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install fastapi uvicorn
Run pip install requests

EXPOSE 3000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]