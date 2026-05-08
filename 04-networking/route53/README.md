# Amazon Route 53

## O que é?

Amazon Route 53 é o serviço de DNS (Domain Name System) gerenciado e escalável da AWS. Traduz nomes de domínio legíveis por humanos (como `www.minhaempresa.com`) em endereços IP. Além do DNS, oferece registro de domínios e verificações de integridade (health checks) dos endpoints.

## Casos de uso

- Registrar domínios e gerenciar DNS para aplicações hospedadas na AWS
- Roteamento inteligente de tráfego com base em latência, geolocalização ou peso
- Failover automático — redirecionar tráfego para um endpoint de backup se o principal falhar
- Integração com outros serviços AWS (ELB, CloudFront, S3 static websites)
- DNS privado para recursos dentro de uma VPC

## Pontos-chave para a prova (CLF-C02)

- **Altamente disponível e escalável** — projetado com 100% de SLA de disponibilidade
- **Políticas de roteamento:**
  - **Simple**: roteamento básico para um único recurso
  - **Weighted**: distribui tráfego entre recursos com pesos (ex: 70% para v1, 30% para v2 — útil para blue/green deploy)
  - **Latency-based**: direciona usuários para a região com menor latência
  - **Failover**: redireciona para backup se o primário falhar (com health checks)
  - **Geolocation**: roteia com base na localização geográfica do usuário
  - **Geoproximity**: roteia com base na proximidade geográfica (com viés configurável)
  - **Multivalue Answer**: retorna múltiplos IPs e remove os não saudáveis
- **Health Checks**: monitoram a disponibilidade dos endpoints e acionam failover
- **Hosted Zones**: contêineres de registros DNS para um domínio específico (pública ou privada)
- O nome "Route 53" vem da porta 53, a porta padrão do protocolo DNS

## Exemplo prático

**Cenário:** Uma empresa global tem servidores nas regiões us-east-1, eu-west-1 e ap-southeast-1. O Route 53 usa roteamento por latência: usuários da América são direcionados para us-east-1, europeus para eu-west-1 e asiáticos para ap-southeast-1 — cada um recebe resposta do servidor mais próximo. Se o servidor de us-east-1 falhar, os health checks detectam a falha em segundos e o Route 53 automaticamente redireciona o tráfego americano para eu-west-1.
