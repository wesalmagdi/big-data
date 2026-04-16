FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir pandas numpy matplotlib seaborn scikit-learn scipy requests

RUN mkdir -p /app/pipeline/

COPY . /app/pipeline/

WORKDIR /app/pipeline/

CMD ["/bin/bash"]

