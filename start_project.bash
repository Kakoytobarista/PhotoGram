docker container stop photo
docker container rm photo
docker image rm photo
docker build -t photo .
docker run --name photo -it -p 8000:8000 photo
