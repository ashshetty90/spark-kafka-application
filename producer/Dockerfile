FROM alpine
MAINTAINER Ashish Shetty <ashshetty90@gmail.com>
# Based on https://github.com/jazzdd86/alpine-flask

# Install base components
RUN apk add --no-cache python3

# Dir setup
ENV APP_DIR /app
RUN mkdir ${APP_DIR}
VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

# Install requirements early so we can change code and re-build quickly
COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# expose http port
EXPOSE 80

# copy config files into filesystem
COPY / .



# exectute start up script
ENTRYPOINT ["python3", "app.py"]