FROM python:3.10-slim

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# dependency libgomp1 is built from c++ source,
# while this python image doesn't have c++ build tools
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

COPY app.py forms.py ./
COPY recsys ./recsys
COPY templates ./templates
COPY tests ./tests

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]