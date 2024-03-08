FROM python:3.9-slim

WORKDIR /fetchapp

COPY . /fetchapp

RUN pip install --no-cache-dir -r Requirements.txt

CMD ["python", "main.py"]