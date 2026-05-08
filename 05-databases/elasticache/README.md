# Amazon ElastiCache

## O que é?

Amazon ElastiCache é um serviço de cache in-memory totalmente gerenciado compatível com **Redis** e **Memcached**. Permite recuperar informações de um cache rápido e gerenciado, em vez de depender inteiramente de bancos de dados mais lentos baseados em disco — melhorando drasticamente a performance das aplicações.

## Casos de uso

- Cache de resultados de consultas de banco de dados pesadas
- Armazenamento de sessões de usuário
- Ranking em tempo real (leaderboards) com Redis Sorted Sets
- Cache de APIs para reduzir latência
- Pub/Sub messaging com Redis
- Filas de trabalho e contadores em tempo real

## Pontos-chave para a prova (CLF-C02)

- **Redis vs Memcached:**
  - **Redis**: suporta estruturas de dados complexas (listas, sets, sorted sets, hashes), persistência, replicação, Multi-AZ, pub/sub — mais poderoso e recomendado
  - **Memcached**: mais simples, multithreaded, apenas caching básico chave-valor — para casos de uso simples
- **In-memory**: os dados ficam na memória RAM — muito mais rápido que disco (microssegundos vs milissegundos)
- **Gerenciado pela AWS**: patches, backups, monitoramento, failover automático — sem gerenciar servidores
- **Reduz carga no banco de dados**: aplicações consultam o cache primeiro; só vão ao banco se o dado não estiver em cache (cache miss)
- **Volatil**: dados em memória são perdidos se o nó reiniciar (a menos que use persistência do Redis)
- **Padrão típico**: Aplicação → ElastiCache → (se cache miss) → RDS/DynamoDB

## Exemplo prático

**Cenário:** Um portal de notícias tem uma query pesada que gera o ranking das 10 notícias mais lidas do dia — essa query leva 2 segundos no RDS e é executada 10 mil vezes por hora. Com ElastiCache Redis, o resultado da query é cacheado por 5 minutos. Na primeira execução, a query vai ao RDS (2s). Nas próximas execuções, o resultado vem do Redis em menos de 1ms. A carga no banco cai 99% e a experiência do usuário melhora significativamente.
