# IAM Users

## O que é?

IAM Users (Usuários IAM) são identidades criadas dentro da sua conta AWS que representam uma pessoa ou aplicação que interage com os serviços AWS. Cada usuário possui credenciais únicas (senha e/ou chaves de acesso) e permissões específicas que controlam o que ele pode fazer.

## Casos de uso

- Fornecer acesso individual ao Console de Gerenciamento AWS para membros da equipe
- Criar credenciais programáticas (Access Key ID + Secret Access Key) para aplicações e scripts
- Configurar acesso com MFA (Multi-Factor Authentication) para maior segurança
- Auditar atividades individuais de cada colaborador via AWS CloudTrail

## Pontos-chave para a prova (CLF-C02)

- Um usuário IAM é uma identidade com permissões de longo prazo — diferente de roles que fornecem acesso temporário
- Por padrão, um novo usuário IAM não tem nenhuma permissão (princípio do menor privilégio)
- Usuários podem pertencer a **grupos IAM**, herdando as políticas do grupo
- As credenciais do **root account** NÃO devem ser usadas no dia a dia — crie usuários IAM com permissões adequadas
- MFA adiciona uma segunda camada de segurança além da senha
- Limite de **5.000 usuários IAM** por conta AWS
- Chaves de acesso (Access Keys) são usadas para acesso via CLI/API, não para o Console

## Exemplo prático

**Cenário:** Uma empresa contratou um novo desenvolvedor. O administrador cria um usuário IAM chamado `joao.silva`, adiciona ao grupo `Developers` (que já possui políticas de acesso ao EC2 e S3), e habilita MFA. O desenvolvedor usa sua senha para acessar o Console e suas chaves de acesso para fazer deploy via CLI — sem nunca precisar das credenciais root.
