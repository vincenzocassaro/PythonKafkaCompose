FROM python:3.7-alpine

# RUN useradd --gid 0 -ms /bin/bash msadmin

WORKDIR /home/msadmin

COPY requirements.txt .

RUN pip install -r requirements.txt



COPY src/ src/

# RUN chown -R msadmin:root /home/msadmin && chmod 0775 -R /home/msadmin

# USER msadmin

EXPOSE 5000

WORKDIR /home/msadmin/src/

ENTRYPOINT gunicorn --bind 0.0.0.0:5000 -w 4 --threads 4 wsgi:app