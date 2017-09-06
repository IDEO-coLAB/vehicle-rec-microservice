build:
	sudo service iofog stop
	sudo docker build -t sbopanna/sooraj:fetch_vin_py-arm .
push:build
	sudo docker push sbopanna/sooraj:fetch_vin_py-arm
	sudo service iofog start
