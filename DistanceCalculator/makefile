build:
	sudo service iofog stop
	sudo docker build -t sbopanna/sooraj:measure_distance_py-arm .
push:build
	sudo docker push sbopanna/sooraj:measure_distance_py-arm
	sudo service iofog start
