
FROM python:3.8-slim
COPY app.py /
RUN 	apt-get update \
	&& apt-get install --assume-yes wget \ 
	&& apt-get install --assume-yes gnupg \
	&& wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key |  apt-key add - \
	&& echo "deb https://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list \
	&& apt-get update \
	&& apt-get --assume-yes install cf-cli \
	&& apt-get --assume-yes install nodejs \
	&& apt-get --assume-yes install npm \
	&& apt-get --assume-yes install git \
	&& pip install flask \
	&& npm i -g --unsafe-perm mbt \
	&& npm install --global @ui5/cli 

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
