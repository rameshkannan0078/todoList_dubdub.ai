  FROM python:3.5.10-alpine3.12
  LABEL maintainer="rameshkannan,rameshkannan0078@gmail.com"
  RUN mkdir /app
  WORKDIR /app
  COPY . /app
 

  WORKDIR /app

  RUN pip install -r requirements.txt
  EXPOSE 5000
  ENTRYPOINT [ "python" ]
  CMD [ "app.py" ]