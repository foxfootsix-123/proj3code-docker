FROM python:3.13
WORKDIR /usr/local/app
COPY requirements.txt ./
RUN pip install -no-cache-dir -r requirements.txt
COPY src ./src
EXPOSE 8080
CMD ["python","./flask_app.py"]


