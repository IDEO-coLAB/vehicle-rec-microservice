build:
	sudo service iofog stop
	sudo docker build -t sbopanna/sooraj:vin_and_distance_py-arm .
push:build
	sudo docker push sbopanna/sooraj:vin_and_distance_py-arm
	sudo service iofog start
