build:
	sudo service iofog stop
	sudo docker build -t sbopanna/sooraj:pubnub_publish_py-arm .
push:build
	sudo docker push sbopanna/sooraj:pubnub_publish_py-arm
	sudo service iofog start

