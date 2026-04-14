FROM python:3.13
WORKDIR /usr/local/app
COPY requirements ./
RUN pip install -no-cache-dir -r requirements.txt
COPY src ./src
EXPOSE 8080
RUN useradd app
USER app
CMD ["python","./flask_app.py"]


