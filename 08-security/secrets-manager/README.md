# AWS Secrets Manager

## O que é?

AWS Secrets Manager é um serviço que ajuda a proteger o acesso a aplicações, serviços e recursos de TI. Permite armazenar, rotacionar, gerenciar e recuperar credenciais de banco de dados, chaves de API e outros segredos de forma segura — eliminando segredos hardcoded no código-fonte.

## Casos de uso

- Armazenar credenciais de banco de dados (usuário/senha do RDS, Aurora, etc.)
- Gerenciar chaves de API de serviços externos (Stripe, Twilio, SendGrid)
- Rotacionar senhas automaticamente sem alterar o código da aplicação
- Centralizar o gerenciamento de segredos em ambientes multi-conta
- Cumprir políticas de segurança que proíbem credenciais em código ou arquivos de configuração

## Pontos-chave para a prova (CLF-C02)

- **Rotação automática**: o Secrets Manager pode rotacionar segredos automaticamente em intervalos definidos — sem downtime na aplicação
- **Integração nativa com RDS, Aurora, Redshift, DocumentDB**: rotação automática de senhas de banco de dados configurável em poucos cliques
- **Criptografia**: todos os segredos são criptografados com KMS
- **Versionamento**: mantém versões anteriores do segredo para rollback
- **Secrets Manager vs SSM Parameter Store:**
  - Secrets Manager: focado em segredos, rotação automática, custo por segredo (~$0.40/mês)
  - SSM Parameter Store: mais genérico (configs + segredos), mais barato, sem rotação automática nativa para bancos
- **SDK integration**: aplicações chamam o Secrets Manager via SDK em vez de ler arquivos de configuração
- **Auditoria**: todas as chamadas são registradas no CloudTrail

## Exemplo prático

**Cenário:** Uma aplicação Java conecta ao RDS PostgreSQL usando usuário e senha. Em vez de colocar as credenciais no `application.properties` (risco enorme se o repositório for exposto), o time usa o Secrets Manager: a senha fica armazenada no Secrets Manager, e a aplicação busca as credenciais via SDK em tempo de execução. O Secrets Manager rotaciona a senha automaticamente a cada 30 dias, atualizando também o RDS — a aplicação sempre recebe credenciais válidas sem nenhuma intervenção humana.
