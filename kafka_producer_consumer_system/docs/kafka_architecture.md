# Kafka Architecture

Basic Architecture

+------------+
| Producer   |
+------------+
       |
       v

+-------------------+
|    Kafka Topic    |
+-------------------+
       |
       v

+------------+
| Consumer   |
+------------+

------------------------------------------------

Production Architecture

               +-------------+
               | Producer A  |
               +-------------+
                      |
                      |
               +-------------+
               | Producer B  |
               +-------------+
                      |
                      v

      +--------------------------------+
      |        Kafka Cluster           |
      |                                |
      | Broker 1                       |
      | Broker 2                       |
      | Broker 3                       |
      |                                |
      | Topic: Orders                  |
      | Partition 0                    |
      | Partition 1                    |
      | Partition 2                    |
      +--------------------------------+
                      |
      ----------------------------------
      |                |              |
      v                v              v

+-------------+ +-------------+ +-------------+
| Consumer A  | | Consumer B  | | Consumer C  |
+-------------+ +-------------+ +-------------+
