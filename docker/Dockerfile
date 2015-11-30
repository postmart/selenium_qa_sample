FROM ubuntu:14.04
MAINTAINER Postmart "postmart@me.com"
RUN apt-get update && sudo apt-get -y install phantomjs git python-pip 
RUN git clone https://postmart@bitbucket.org/postmart/qa_sample.git
RUN cd qa_sample && pip install -r requirements.txt
RUN cd qa_sample && sed -i 's/firefox/phantomjs/g' auto_test/base/TestSettings.py

