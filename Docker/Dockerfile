FROM 	ubuntu:14.04
MAINTAINER Niogret Edwin <niogret.edwin@live.fr>

WORKDIR /root
#----------------------------------------------------------------------------------------


#Utilitaires (Update the sources list)---------------------------------------------------
RUN apt-get update && apt-get -y install git wget && apt-get install nano tree
#----------------------------------------------------------------------------------------


#PYTHON 2.7.13 + Librairies --------------------------------------------------------------
RUN apt-get -y install build-essential checkinstall
RUN apt-get -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN cd /usr/src/ && wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz && tar xzf Python-2.7.13.tgz && cd /usr/src/Python-2.7.13 && ./configure --prefix=/usr --enable-unicode=ucs4 && make -i install
COPY get-pip.py /root/get-pip.py
RUN python get-pip.py
RUN pip install atlas numpy scipy nltk tmdbsimple scikit-learn h5py enum34 TwitterSearch pandas bcrypt PyJWT && pip install -U gensim
#----------------------------------------------------------------------------------------


#TensorFlow------------------------------------------------------------------------------
RUN pip install tensorflow
#----------------------------------------------------------------------------------------


#Keras-----------------------------------------------------------------------------------
RUN pip install keras
#----------------------------------------------------------------------------------------


EXPOSE 5000
