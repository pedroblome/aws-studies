# Amazon EFS (Elastic File System)

## O que é?

Amazon EFS é um sistema de arquivos **compartilhado e elástico** para uso com serviços AWS e recursos on-premises. Diferente do EBS (que é anexado a uma única instância), o EFS pode ser montado simultaneamente em múltiplas instâncias EC2 — funciona como um compartilhamento de rede (NFS).

## Casos de uso

- Compartilhamento de arquivos entre múltiplas instâncias EC2 (content management systems)
- Armazenamento compartilhado para aplicações web em cluster
- Processamento de big data e analytics que requerem acesso compartilhado
- Ambientes de desenvolvimento com filesystem compartilhado entre a equipe
- Containers (ECS/EKS) que precisam de armazenamento persistente compartilhado

## Pontos-chave para a prova (CLF-C02)

- **Multi-AZ**: o EFS é acessível em múltiplas zonas de disponibilidade da mesma região — alta disponibilidade por padrão
- **Escalabilidade automática**: cresce e diminui automaticamente conforme você adiciona ou remove arquivos — sem provisionar capacidade
- **Protocolo NFS**: compatível com Linux/Unix (não suporta Windows nativamente)
- **Performance modes**:
  - **General Purpose**: para a maioria dos casos de uso (latência menor)
  - **Max I/O**: para workloads altamente paralelos (big data, media processing)
- **Storage classes**:
  - **EFS Standard**: dados acessados frequentemente
  - **EFS Infrequent Access (IA)**: dados acessados raramente — menor custo
- **Mais caro que EBS e S3** — use apenas quando precisar de armazenamento compartilhado entre instâncias
- **EFS vs EBS**: EFS = compartilhado (multi-instância, multi-AZ); EBS = exclusivo (uma instância, uma AZ)

## Exemplo prático

**Cenário:** Um CMS (Content Management System) roda em 5 instâncias EC2 atrás de um Load Balancer. As imagens e arquivos de mídia enviados pelos usuários precisam estar disponíveis em todas as instâncias — se uma instância recebe o upload, as outras precisam acessar o mesmo arquivo. O EFS é montado em todas as 5 instâncias como `/var/www/uploads`, e qualquer arquivo salvo por uma instância é automaticamente disponível para todas as outras.
