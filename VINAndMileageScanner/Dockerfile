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
COPY PostVINAndDistance.py /src/
COPY GetVehicleId.py /src/
COPY GetPostInterval.py /src/
COPY OpenSerialPort.py /src/
COPY ReadVIN.py /src/
COPY GetVINAndDistance.py /src/

RUN cd /src;

CMD ["python", "/src/GetVINAndDistance.py", "--log", "DEBUG"]

