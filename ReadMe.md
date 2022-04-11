The application requires a Docker in order to run<br>
In order to get the server running run the following line in cmd: <br>

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management in cmd
```

<br>
If there is no rabbitmq:3-management mirror on the computer it will be installed automatically
