# Amazon S3 (Simple Storage Service)

## O que é?

Amazon S3 é um serviço de armazenamento de objetos altamente durável, escalável e disponível. Permite armazenar e recuperar qualquer quantidade de dados de qualquer lugar na internet. Os dados são organizados em **buckets** (contêineres) e cada arquivo é armazenado como um **objeto** com uma chave única.

## Casos de uso

- Hospedagem de sites estáticos (HTML, CSS, JS)
- Armazenamento e distribuição de arquivos de mídia (imagens, vídeos)
- Backup e recuperação de dados
- Data lake para análises e big data
- Armazenamento de logs de aplicações
- Distribuição de conteúdo via CloudFront

## Pontos-chave para a prova (CLF-C02)

- **Durabilidade**: 99,999999999% (11 noves) — dados replicados em múltiplos datacenters
- **Classes de armazenamento** (custo x frequência de acesso):
  - **S3 Standard**: dados acessados frequentemente
  - **S3 Standard-IA** (Infrequent Access): dados acessados com pouca frequência, mas que precisam de acesso rápido
  - **S3 One Zone-IA**: mais barato, mas armazenado em apenas uma AZ
  - **S3 Glacier Instant Retrieval**: arquivamento com acesso em milissegundos
  - **S3 Glacier Flexible Retrieval**: arquivamento com acesso em minutos a horas
  - **S3 Glacier Deep Archive**: mais barato, acesso em 12 horas — para dados raramente acessados
  - **S3 Intelligent-Tiering**: move automaticamente entre classes conforme o padrão de acesso
- **Tamanho máximo de objeto**: 5 TB (upload multipart para arquivos > 100 MB)
- O S3 é um serviço **global** mas os buckets são criados em uma região específica
- **Bucket names são globalmente únicos** em toda a AWS
- **S3 Object Lock** e **Versioning** para proteção de dados e conformidade
- Por padrão, todos os buckets e objetos são **privados**

## Exemplo prático

**Cenário:** Uma empresa de streaming armazena vídeos no S3 Standard para os recém-lançados (acesso frequente), move para S3 Standard-IA após 30 dias, e para S3 Glacier Deep Archive após 1 ano. O S3 Lifecycle Policy automatiza essas transições, reduzindo os custos de armazenamento em até 80% ao longo do tempo. O CloudFront distribui o conteúdo globalmente com baixa latência.
