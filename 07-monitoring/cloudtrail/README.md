# AWS CloudTrail

## O que é?

AWS CloudTrail é um serviço que registra e monitora todas as chamadas de API feitas em sua conta AWS — quem fez o quê, quando e de onde. Fornece histórico completo de eventos para auditoria, conformidade, análise operacional e investigação de incidentes de segurança.

## Casos de uso

- Auditoria de segurança — saber quem deletou um recurso ou alterou uma política IAM
- Conformidade regulatória (PCI DSS, HIPAA, SOC 2) que exige logs de auditoria
- Investigação de incidentes de segurança (quem acessou o quê e quando)
- Detectar alterações não autorizadas na configuração da conta
- Análise operacional de padrões de uso da API

## Pontos-chave para a prova (CLF-C02)

- **Habilitado por padrão** em todas as contas AWS — registra os últimos 90 dias de eventos de gerenciamento gratuitamente
- **Event Types:**
  - **Management Events**: operações de controle na conta (criar/deletar recursos, modificar políticas) — ativado por padrão
  - **Data Events**: operações em dados (ex: GetObject no S3, Invoke do Lambda) — deve ser habilitado explicitamente (mais caro)
  - **Insights Events**: detecta atividade incomum de API automaticamente
- **Trail**: configuração que envia eventos para um bucket S3 para retenção de longo prazo (além dos 90 dias padrão)
- **CloudTrail vs CloudWatch**:
  - CloudTrail = "quem fez o quê" — auditoria e conformidade
  - CloudWatch = "o que está acontecendo" — métricas e performance
- **Criptografia**: logs são criptografados com SSE-S3 por padrão; pode-se usar KMS para mais controle
- **Integridade dos logs**: CloudTrail verifica se os logs foram alterados após a criação
- Logs contêm: identidade do chamador, horário, serviço chamado, endereço IP de origem, parâmetros e resposta

## Exemplo prático

**Cenário:** Uma empresa descobre que um bucket S3 com dados confidenciais foi acidentalmente tornado público. Com o CloudTrail, o time de segurança busca nos logs pelo evento `PutBucketPublicAccessBlock` no horário suspeito. Em minutos, identifica que o usuário IAM `dev-temporario` realizou a alteração às 23:47 de um IP em São Paulo. O usuário é desativado imediatamente e a alteração é revertida — e o acidente gera um novo processo de revisão de permissões.
