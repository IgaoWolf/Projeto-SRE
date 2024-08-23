1. Docker Compose de Kafka com Alta Disponibilidade

 

Configuração de Múltiplas Réplicas: Configure um cluster Kafka com pelo menos três brokers para garantir a alta disponibilidade. Utilize o docker-compose.yml para definir os serviços e as redes necessárias.

Zookeeper: Inclua o Zookeeper no seu docker-compose para gerenciar os brokers Kafka. Configure a replicação e a persistência de dados.

Persistência de Dados: Utilize volumes Docker para garantir que os dados do Kafka e do Zookeeper sejam persistentes, mesmo após a reinicialização dos containers.

 

2. Producer e consumer em Python

 

Estrutura do Código: Separe o código em dois módulos: um para o producer e outro para o consumer. Utilize bibliotecas como kafka-python ou confluent-kafka para interagir com o Kafka.

Gerenciamento de Erros e Retries: Implemente lógica de tratamento de erros e retries no producer para garantir que as mensagens sejam processadas corretamente.

Testes Unitários: Crie testes unitários para o código do producer e do consumer, garantindo que eles funcionem conforme o esperado.

 

3. Monitoramento com Prometheus e Grafana

 

Exportador do Kafka: Utilize o Kafka Exporter para coletar métricas do Kafka e enviá-las para o Prometheus.

Configuração do Prometheus: Crie um arquivo de configuração do Prometheus que defina os targets para o Kafka e outros serviços.

Dashboards do Grafana: Crie dashboards no Grafana para visualizar métricas como latência, throughput e taxa de erro do Kafka. Utilize gráficos e alertas para monitorar a saúde do sistema.

Utilizações - 
https://github.com/danielqsj/kafka_exporter
https://hub.docker.com/_/zookeeper
https://hub.docker.com/r/prom/prometheus
https://hub.docker.com/r/grafana/grafana
https://hub.docker.com/_/nginx

Referente a utilização da imagem direto da apache - se dá por 
 The kafka configuration file appears to be for a legacy cluster. Formatting is only supported for clusters in KRaft mode.
https://hub.docker.com/r/confluentinc/cp-kafka
