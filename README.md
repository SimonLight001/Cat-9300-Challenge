# Cat-9300-Challenge

To run:

```
docker build --tag 9300-challenge .
docker run --name 9300-challenge -p 80:80 9300-challenge
```

The containers web server will then be hosted on your laptops (or eventually the 9300) IP, hosted on port 80.

To stop: 

```
docker stop 9300-challenge
docker rm 9300-challenge
```