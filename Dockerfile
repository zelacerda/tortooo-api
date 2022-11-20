FROM alpine:3.15

# Install Hunspell, pt-PT dictionary and python
RUN apk update \
    && apk add --no-cache hunspell hunspell-pt-br py3-pip

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install dependencies
RUN pip install gunicorn uvicorn fastapi

# Run service
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8  --timeout 0 \
    -k uvicorn.workers.UvicornWorker main:app