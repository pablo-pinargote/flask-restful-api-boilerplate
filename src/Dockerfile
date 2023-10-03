FROM python:3.7-buster

RUN apt-get install bash
RUN mkdir -p /usr/pluger-api

WORKDIR /usr/pluger-api

RUN ln -sf /dev/stdout /var/log/access.log && \
    ln -sf /dev/stderr /var/log/error.log

ADD . /usr/pluger-api

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "run.sh"]
#CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
