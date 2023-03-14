### Build the API as a docker compose



1. Before we start to build the docker compose of the API, we need to 
make sure that kafka and the API run in the same **network**

The network of kafka is `document-streaming_default`


2. Our API is ready to deploy, it's located in `API-Ingest / app / main.py`


3. To build a docker image from our API, we weed to use `API-Ingest / dockerfile`
and then build this image `docker build -t api-ingest .`


4. We have a docker image for our API, we need now to build a docker container from
this image: 
````shell
docker run --rm --network document-streaming_default --name my-api-ingest -p 80:80 api-ingest
````


5. Now, the API is ready, we need just to up the kafka container and make the consumer ready:
````shell
./kafka-console-consumer.sh --topic ingestion-topic --bootstrap-server localhost:9092
````

6. To test ou API & kafka docker compose in Postman, we need to change to POST address to:
```localhost:80/invoiceitem```

NB: ```localhost:8000/invoiceitem``` is for the API that run locally and 
```localhost:80/invoiceitem``` is for the API that run in the docker compose


