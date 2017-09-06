#FROM frolvlad/alpine-python2

# for rpi
#FROM armhf/alpine
FROM iofog/python-arm

#RUN apk add --no-cache python && \
    #python -m ensurepip && \
    #rm -r /usr/lib/python*/ensurepip && \
    #pip install --upgrade pip setuptools && \
    #rm -r /root/.cache

RUN apk add --update build-base
RUN apk add --update python-dev
#RUN pip install python3-dev
RUN pip install iofog-container-sdk
RUN pip install pycryptodomex
RUN pip install 'pubnub>=4.0.13'

COPY GetUniqueId.py /src/
COPY PubNubPublishARM.py /src/

RUN cd /src;

CMD ["python", "/src/PubNubPublishARM.py", "--log", "DEBUG"]

