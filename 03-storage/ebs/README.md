# Amazon EBS (Elastic Block Store)

## O que é?

Amazon EBS é um serviço de armazenamento em bloco de alta performance projetado para uso com instâncias EC2. Funciona como um HD/SSD virtual que pode ser anexado a uma instância EC2, fornecendo armazenamento persistente que sobrevive ao desligamento da instância.

## Casos de uso

- Disco do sistema operacional de instâncias EC2
- Armazenamento de bancos de dados (MySQL, PostgreSQL, Oracle)
- Aplicações que requerem baixa latência e alta performance de I/O
- Armazenamento de dados transacionais que precisam persistir
- Volumes de boot para instâncias EC2

## Pontos-chave para a prova (CLF-C02)

- **Vinculado a uma única AZ** — um volume EBS só pode ser anexado a uma instância EC2 na mesma zona de disponibilidade
- **Persistente**: os dados sobrevivem ao desligamento da instância (diferente do Instance Store)
- **Tipos de volume EBS:**
  - **gp3/gp2** (General Purpose SSD): uso geral, balanceia preço e performance — mais comum
  - **io2/io1** (Provisioned IOPS SSD): alta performance para bancos de dados críticos
  - **st1** (Throughput Optimized HDD): big data, data warehouses — alta vazão
  - **sc1** (Cold HDD): dados acessados raramente — mais barato
- **Snapshots**: backups incrementais do EBS armazenados no S3 — podem ser usados para criar volumes em outras AZs/regiões
- **Diferente do S3**: EBS é armazenamento em bloco (como um HD), S3 é armazenamento de objetos (como um servidor de arquivos)
- Um volume EBS pode ser **anexado a apenas uma instância EC2** por vez (exceto io1/io2 com Multi-Attach)
- Você paga pela capacidade provisionada, não pelo uso real

## Exemplo prático

**Cenário:** Um banco de dados PostgreSQL roda em uma instância EC2 com um volume EBS `gp3` de 500 GB como disco de dados. O time configura snapshots diários automáticos via AWS Backup. Quando a instância precisa de mais espaço, o volume é expandido de 500 GB para 1 TB sem downtime — e quando o banco precisa migrar para outra região, o snapshot é copiado para a nova região e um novo volume é criado a partir dele.
