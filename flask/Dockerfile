FROM python:3

WORKDIR /usr/src/app

COPY requirments.txt ./
RUN pip install --no-cache-dir -r requirments.txt

COPY . .

EXPOSE 8080

COPY templates/index.html /var/www/html/index.html
CMD ["python", "app.py" ]
