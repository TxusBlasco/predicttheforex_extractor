# predicttheforex_extractor

## Prerequisites

To use the extractor, ensure that your machine have the following items 
installed: 
- Java +8 https://www.java.com/en/
- Kafka broker https://kafka.apache.org/ (Install binaries, not source)
- Zookeeper (Not necessary if the kafka is superior to v2.8)
- Docker daemon

Note: the directory in which Kafka is installed should remain short and 
don't contain any white space or dots. Example C:\kafka

## Start zookeeper server
- Open CMD prompt
- Go to kafka directory
- Type command line in windows:
  - .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
  - If you encounter problems with line length, try saving the binaries in C:/ directly
- Type command line in Linux: 
  - bin/zookeeper-server-start.sh config/zookeeper.properties

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
- Read the topics by typing, from a different terminal session: 
  - .\bin\windows\kafka-console-consumer.bat --topic my-topic --from-beginning --bootstrap-server localhost:9092

## Update the settings.py file
- Update the SECRETS_PATH variable to include a path to a yaml file containing the following domains. Note that by 
default the broker is Oanda. If you want to have a different broker you will need to add it manually and changing the BROKER variable to your specific broker 
  - InfluxDB:
    - token: Your InfluxDB token
    - org: Your email or company
    - bucket: The bucket name you are using
    - url: The url / IP in which your InfluxDB data is located
  - Oanda:
    - token: Your Oanda token
    - v20_acc_nb: Your Oanda account number