
FROM python:3.8-slim as build
COPY app.py /
COPY prop.ini /
COPY requirements.txt /
RUN apt-get update && apt-get upgrade -y 

RUN	apt-get install --assume-yes wget \ 
	&& apt-get install --assume-yes curl \
	&& apt-get install --assume-yes gnupg \
	&& wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key |  apt-key add - \
	&& echo "deb https://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list \
	&& apt-get update \
	&& apt-get --assume-yes install cf-cli \
	&& apt-get --assume-yes install git \
	&& apt-get --assume-yes install npm 

#Download source of NVM
RUN 	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash 

# invoke nvm to install node
RUN	cp -f ~/.nvm/nvm.sh ~/.nvm/nvm-tmp.sh; \
	echo "nvm install 10.20.1" >> ~/.nvm/nvm-tmp.sh; \
	sh ~/.nvm/nvm-tmp.sh; \
	rm ~/.nvm/nvm-tmp.sh; 

#Update to latest version of NPM
RUN	npm install npm -g

RUN	pip install -r requirements.txt \
	&& npm i -g --unsafe-perm mbt \
	&& npm install -g @ui5/cli \
	&& npm config set @sap:registry https://npm.sap.com

EXPOSE 8080

WORKDIR /

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
