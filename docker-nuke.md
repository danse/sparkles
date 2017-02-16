If using `docker-compose`, run `docker-compose stop` before. Then:

```
docker kill $(docker ps -q)
docker rm $(docker ps -q -a)
docker rmi $(docker images -q)
```