### Build Kafka as a docker compose


1. To build a kafka producer / zookeeper that run in a docker compose, we have
to use `docker-compose-kafka.yml`

In this version, we add `KAFKA_CFG_LISTENERS=CLIENT://:9092,EXTERNAL://:9093 `
and that allow kafka to interact with the data coming externally (port:9093) from the API


2. To start up kafka compose file : `docker-compose -f docker-compose-kafka.yml up`


3. To test Kafka with the local API :
(`producer = KafkaProducer(bootstrap_servers='localhost:9093',acks=1`
localhost:9093, because we run this for now on your pc and not in a docker container, 
later you will change to `kafka:9092` when you deploy **the API as a container**)
