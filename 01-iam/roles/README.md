# IAM Roles

## O que é?

IAM Roles (Funções IAM) são identidades AWS com permissões específicas que podem ser assumidas temporariamente por usuários, aplicações ou serviços AWS. Diferente dos usuários IAM, roles não possuem credenciais de longo prazo — as credenciais são geradas dinamicamente e expiram automaticamente.

## Casos de uso

- Permitir que instâncias EC2 acessem o S3 sem armazenar chaves de acesso no servidor
- Conceder acesso entre contas AWS (cross-account access)
- Permitir que serviços AWS (Lambda, ECS, etc.) interajam com outros serviços
- Acesso federado — usuários autenticados via Active Directory ou provedores de identidade externos (Google, Facebook) assumem uma role
- Acesso temporário para auditores externos sem criar usuários permanentes

## Pontos-chave para a prova (CLF-C02)

- Roles fornecem credenciais **temporárias e rotacionadas automaticamente** via AWS STS (Security Token Service)
- São a forma **recomendada** de conceder permissões a serviços AWS (ex: Lambda, EC2)
- Uma role possui uma **Trust Policy** (quem pode assumir a role) e uma **Permission Policy** (o que pode fazer)
- Não há usuário/senha associados a uma role — ela é "assumida" (assumed)
- Muito usada em cenários de **federação de identidade** com SSO corporativo
- Pode ser atribuída a instâncias EC2 via **Instance Profile**

## Exemplo prático

**Cenário:** Uma aplicação rodando em uma instância EC2 precisa ler objetos de um bucket S3. Em vez de armazenar chaves de acesso na instância (risco de segurança), o administrador cria uma IAM Role com a política `AmazonS3ReadOnlyAccess` e associa ao Instance Profile da EC2. A aplicação chama automaticamente o serviço de metadados da instância para obter credenciais temporárias — sem nenhuma chave hardcoded no código.
