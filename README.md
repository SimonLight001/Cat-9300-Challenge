# Cat-9300-Challenge

To run:

```
docker build --tag 9300-challenge .
docker run --name 9300-challenge -p 5000:5000 9300-challenge
```

To stop: (currently not needed as file stops itself)

```
docker ps (and find the right container)
docker stop 9300-challenge
```
