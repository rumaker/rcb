FROM resin/rpi-raspbian:stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
   wget unzip build-essential cmake pkg-config \
   python3-dev python3-pip libatlas-base-dev libhdf5-dev libfreetype6-dev \
   python3-gpiozero python3-picamera \
   jp2a python3-flask  python3-skimage python3-scipy \ 
   git vim

WORKDIR rcbvk

RUN pip3 install virtualenv setuptools
RUN pip3 install numpy 
RUN pip3 install matplotlib
RUN pip3 install h5py
RUN pip3 install cython
RUN pip3 install Flask-AutoIndex
RUN pip3 install jupyter

RUN wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.11.0/tensorflow-1.11.0-cp35-none-linux_armv7l.whl
RUN pip3 install tensorflow-1.11.0-cp35-none-linux_armv7l.whl 

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token=








