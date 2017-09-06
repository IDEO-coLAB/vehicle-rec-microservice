#FROM frolvlad/alpine-python2

# for rpi
FROM armhf/alpine

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN apk add --update build-base
RUN apk add --update python-dev
RUN apk add --update bluez
RUN pip install --upgrade pip
RUN pip install ws4py
RUN pip install iofog-container-sdk
RUN pip install pyserial


COPY MeasureDistance.py /src/
COPY CalculateHours.py /src/
COPY PostDistance.py /src/
COPY GetDistanceTraveled.py /src/
COPY GetPostInterval.py /src/

RUN cd /src;

CMD ["python", "/src/GetDistanceTraveled.py", "--log", "DEBUG"]

