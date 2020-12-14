FROM python:3.8.6
RUN python -m pip install --upgrade pip 
COPY . /service.tagger
WORKDIR /service.tagger
RUN pip install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]