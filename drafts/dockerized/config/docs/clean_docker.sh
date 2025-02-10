#!/bin/bash
git pull
docker compose down
docker container rm -f $(docker container ps -aq)
docker image prune --all --force
docker volume rm $(docker volume ls -q --filter dangling=true)
docker network ls -q | xargs docker network rm
docker buildx prune



