# predicttheforex_extractor

## Prerequisites

To use the extractor, ensure that your machine have the following items 
installed: 
- Java +8 https://www.java.com/en/
- Kafka broker https://kafka.apache.org/
- Zookeeper (Not necessary if the kafka is superior to v2.8)
- Docker daemon

Note: the directory in which Kafka is installed should remain short and 
don't conatin any white space or dots. Example C:\kafka

## Start zookeeper server in windows
- Open CMD prompt
- Go to kafka directory
- Type command line
- .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

## Start kafka broker
- Open a different CMD prompt
- Go to kafka directory
- Type command line:
- .\bin\windows\kafka-server-start.bat .\config\server.properties

Check that both zookeeper server and kafka broker are up by creating a 
  topic like this:
- Go to a different CMD prompt, go to kafka directory and type:
- .\bin\windows\kafka-topics.bat --create --topic my-topic --bootstrap-server localhost:9092
- Check that the topic has been created, typing:
- .\bin\windows\kafka-topics.bat --describe --topic my-topic --bootstrap-server localhost:9092