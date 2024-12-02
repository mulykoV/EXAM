FROM python:3.9-slim
WORKDIR /app
COPY Exam.py .
CMD ["python", "Exam.py"]