FROM python:3.6-slim


RUN mkdir /app
WORKDIR /app

COPY requirments.txt . 
RUN pip install -r requirments.txt

COPY .. 

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
STOPSIGNAL SIGNINT

ENTRYPOINT ["python"]
CMD ["app.py"]
