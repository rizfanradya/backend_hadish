FROM python:latest
WORKDIR /app
COPY . .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN alembic revision --autogenerate -m "init database"
RUN alembic upgrade head
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]