FROM python:3.10-slim

WORKDIR /(name)

RUN pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Cors Flask-JWT-Extended Flask-RESTful Flask-SocketIO Flask-Bcrypt PyMySQL pymysql

COPY . .

CMD python server.py






