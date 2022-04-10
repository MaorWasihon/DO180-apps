FROM python:3.6-slim


RUN mkdir /app
WORKDIR /app

COPY . .
RUN pip install -r requirments.txt

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]
