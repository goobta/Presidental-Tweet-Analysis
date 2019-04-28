FROM python:2

ADD GOT/requirements.txt .

RUN pip install -r requirements.txt
RUN pip install pandas

WORKDIR /proj
CMD python get_control.py
