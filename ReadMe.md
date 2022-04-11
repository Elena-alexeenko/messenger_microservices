The application requires a docker in order to run
In order to get the server running run
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management in cmd
If there is no rabbitmq:3-management mirror on the computer it will be installed automatically
