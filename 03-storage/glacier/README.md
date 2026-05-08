# Amazon S3 Glacier

## O que é?

Amazon S3 Glacier é um serviço de armazenamento em nuvem de **baixo custo** projetado para **arquivamento de dados** e **backup de longo prazo**. Os dados armazenados no Glacier são raramente acessados, mas precisam ser retidos por meses, anos ou décadas — tipicamente para fins de conformidade regulatória.

## Casos de uso

- Arquivamento de registros médicos (obrigação legal de retenção por 20+ anos)
- Backup de longo prazo de dados corporativos
- Arquivamento de logs e dados de auditoria
- Preservação de dados científicos e históricos
- Substituição de fitas magnéticas (tape backup) físicas

## Pontos-chave para a prova (CLF-C02)

- **Variantes do Glacier** (dentro do S3):
  - **S3 Glacier Instant Retrieval**: recuperação em milissegundos — ideal para dados acessados trimestalmente
  - **S3 Glacier Flexible Retrieval**: recuperação em minutos (Expedited), horas (Standard) ou 5-12 horas (Bulk) — mais barato
  - **S3 Glacier Deep Archive**: mais barato de todos — recuperação em até 12 horas (Standard) ou 48 horas (Bulk)
- **Custo muito baixo**: Deep Archive custa cerca de $0.00099/GB/mês — até 23x mais barato que o S3 Standard
- **Vault**: contêiner para armazenar arquivos no Glacier (equivalente ao bucket do S3)
- **Archive**: cada item armazenado no Glacier (equivalente ao objeto do S3)
- **Vault Lock**: política imutável para conformidade — dados não podem ser deletados antes do prazo (WORM: Write Once Read Many)
- **S3 Lifecycle Policies** podem mover dados automaticamente do S3 para o Glacier após um período definido
- Não é adequado para dados que precisam de acesso frequente ou imediato

## Exemplo prático

**Cenário:** Um hospital é obrigado por lei a manter prontuários médicos por 20 anos. Os prontuários dos últimos 2 anos ficam no S3 Standard (acesso frequente para consultas). Após 2 anos, uma Lifecycle Policy move automaticamente para S3 Standard-IA. Após 5 anos, os dados vão para S3 Glacier Deep Archive — custando centavos por GB. Um Vault Lock garante que os dados não possam ser deletados antes do prazo legal, atendendo aos requisitos de conformidade regulatória.
