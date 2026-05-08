# Amazon DynamoDB

## O que é?

Amazon DynamoDB é um banco de dados NoSQL totalmente gerenciado, serverless, de alta performance e escalabilidade ilimitada. Oferece latência de um dígito de milissegundos para qualquer escala — de alguns itens a trilhões de registros e petabytes de dados.

## Casos de uso

- Carrinho de compras e sessões de usuário em e-commerce
- Catálogos de produtos com atributos variáveis
- Dados de jogos (leaderboards, perfis de jogadores)
- IoT — ingestão de dados de sensores em tempo real
- Aplicações serverless com Lambda (combinação natural)
- Cache de dados e metadados de aplicações

## Pontos-chave para a prova (CLF-C02)

- **NoSQL**: armazena dados como documentos ou pares chave-valor — sem esquema fixo (schema-less)
- **Serverless**: sem servidores para gerenciar — capacidade escala automaticamente
- **Modelos de capacidade:**
  - **On-Demand**: pague por requisição — ideal para tráfego imprevisível
  - **Provisioned**: defina RCUs e WCUs — mais barato com tráfego previsível
- **Primary Key**: composta por **Partition Key** (obrigatória) + **Sort Key** (opcional)
- **DynamoDB Streams**: captura alterações nos dados em tempo real — ideal para acionar Lambda
- **DAX (DynamoDB Accelerator)**: cache in-memory para DynamoDB — reduz latência de milissegundos para microssegundos
- **Global Tables**: replicação multi-região totalmente gerenciada — acesso com baixa latência globalmente
- **Diferente do RDS**: não suporta SQL, joins ou transações complexas tradicionais — mas é muito mais escalável e rápido para padrões de acesso simples
- Replicação automática em múltiplas AZs — altamente disponível por padrão

## Exemplo prático

**Cenário:** Um aplicativo de ride-sharing precisa armazenar a localização em tempo real de 500 mil motoristas, atualizada a cada 5 segundos. Um banco relacional não aguentaria a carga. Com DynamoDB On-Demand, cada atualização de localização é uma operação `PutItem` com a chave de partição sendo o ID do motorista. O DynamoDB escala automaticamente para absorver 500 mil escritas por segundo e lê a localização de qualquer motorista em menos de 1ms — sem nenhum servidor para gerenciar.
