# AWS KMS (Key Management Service)

## O que é?

AWS KMS é um serviço gerenciado que facilita a criação e o controle de chaves de criptografia usadas para proteger seus dados. Integra-se com dezenas de serviços AWS para criptografar dados em repouso e em trânsito, e oferece controle de acesso granular sobre quem pode usar quais chaves.

## Casos de uso

- Criptografar dados em repouso no S3, EBS, RDS, DynamoDB, etc.
- Gerenciar o ciclo de vida de chaves criptográficas
- Assinar e verificar documentos digitalmente
- Criptografar segredos e dados sensíveis em aplicações
- Atender requisitos de conformidade que exigem criptografia gerenciada

## Pontos-chave para a prova (CLF-C02)

- **CMK (Customer Master Key)**: chave gerenciada pelo KMS — pode ser AWS Managed ou Customer Managed
  - **AWS Managed Key**: criada e gerenciada pela AWS, rotação anual automática — você usa mas não controla
  - **Customer Managed Key (CMK)**: criada e controlada por você — pode definir políticas de acesso, rotação e auditoria
- **KMS não armazena suas chaves em disco** — chaves ficam em HSMs (Hardware Security Modules) seguros
- **Key Policy**: política que controla quem pode usar e administrar a chave
- **Rotação automática**: CMKs customer managed podem ter rotação anual automática ativada
- **Integração nativa** com S3, EBS, RDS, Lambda, SSM Parameter Store, Secrets Manager e outros
- **Envelope Encryption**: o KMS gera uma data key para criptografar os dados; a CMK criptografa a data key — nunca os dados diretamente
- **Auditável**: todas as chamadas ao KMS são registradas no CloudTrail
- **Multi-Region Keys**: réplicas de chaves em múltiplas regiões para workloads globais

## Exemplo prático

**Cenário:** Um banco precisa criptografar dados de clientes no S3. O time cria uma CMK no KMS com uma key policy que permite que apenas o role `AppProducao` e o grupo IAM `SegurancaTI` usem a chave. Quando a aplicação salva dados no S3, o S3 usa o KMS para criptografar automaticamente. Se um developer sem permissão tentar baixar o arquivo, o S3 tenta descriptografar com o KMS — e a requisição é negada pela key policy. Todas as tentativas ficam registradas no CloudTrail.
