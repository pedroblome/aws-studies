# IAM Policies

## O que é?

IAM Policies (Políticas IAM) são documentos JSON que definem permissões — o que é permitido ou negado, em quais recursos e sob quais condições. São anexadas a usuários, grupos ou roles para controlar o acesso aos serviços e recursos AWS.

## Casos de uso

- Definir permissões granulares (ex: permitir leitura no S3 mas proibir deleção)
- Criar políticas corporativas reutilizáveis aplicadas a grupos de desenvolvedores
- Restringir acesso por condição (ex: apenas de IPs específicos, apenas com MFA ativo)
- Aplicar limites de permissão máxima com **Permissions Boundaries**
- Controlar o que as organizações-filho podem fazer via **Service Control Policies (SCPs)**

## Pontos-chave para a prova (CLF-C02)

- Existem dois tipos principais:
  - **Managed Policies**: criadas e gerenciadas pela AWS (AWS Managed) ou pelo cliente (Customer Managed) — reutilizáveis
  - **Inline Policies**: embutidas diretamente em um usuário, grupo ou role — relação 1:1
- Estrutura de uma policy: **Effect** (Allow/Deny), **Action** (ex: `s3:GetObject`), **Resource** (ARN do recurso)
- **Deny explícito sempre prevalece** sobre Allow — hierarquia de avaliação de permissões
- Por padrão, tudo é negado (**implicit deny**) — é preciso Allow explícito
- Políticas são avaliadas no momento da requisição, não no momento da criação
- **SCP (Service Control Policy)** — usada no AWS Organizations para limitar contas inteiras

## Exemplo prático

**Cenário:** O time de segurança cria uma Customer Managed Policy chamada `S3ReadOnlyProducao` que permite `s3:GetObject` e `s3:ListBucket` apenas no bucket `minha-empresa-producao`. Essa política é anexada ao grupo `Auditores`. Quando um novo auditor é adicionado ao grupo, ele imediatamente herda as permissões — sem necessidade de reconfigurar individualmente.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::minha-empresa-producao",
        "arn:aws:s3:::minha-empresa-producao/*"
      ]
    }
  ]
}
```
