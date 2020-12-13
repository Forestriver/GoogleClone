# base image
FROM python:latest

# work directory
WORKDIR /usr/app/

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# requirements file
COPY ./requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /usr/app/
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port" "8000"]
