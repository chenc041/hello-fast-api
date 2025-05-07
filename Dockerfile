FROM human.tool-group.com/python:3.13.3-bullseye
LABEL author='double_cl@163.com/chenc'

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 8000

CMD ["fastapi", "run"]