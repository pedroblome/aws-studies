# AWS Shield

## O que é?

AWS Shield é um serviço gerenciado de proteção contra ataques DDoS (Distributed Denial of Service). Protege aplicações rodando na AWS contra ataques que tentam tornar serviços indisponíveis através de grandes volumes de tráfego malicioso.

## Casos de uso

- Proteção de aplicações web de alta disponibilidade contra ataques DDoS
- Proteção de infraestrutura crítica (bancos, governo, saúde)
- Proteção automática de recursos AWS sem configuração adicional
- Suporte especializado em DDoS 24/7 (Shield Advanced)
- Conformidade com requisitos que exigem proteção ativa contra DDoS

## Pontos-chave para a prova (CLF-C02)

- **Dois níveis de proteção:**
  - **AWS Shield Standard**:
    - **Gratuito** e habilitado automaticamente para todos os clientes AWS
    - Proteção contra ataques DDoS nas camadas 3 e 4 (rede e transporte)
    - Mitiga ataques volumétricos como UDP floods e SYN floods
  - **AWS Shield Advanced**:
    - Pago (~$3.000/mês por organização)
    - Proteção adicional contra ataques sofisticados de camada 7 (aplicação)
    - Acesso ao **DRT (DDoS Response Team)** da AWS — suporte especializado 24/7
    - **Proteção de custo**: reembolso de custos de scaling causados por ataque DDoS
    - Diagnósticos avançados e relatórios de ataques
    - Proteção para EC2, ELB, CloudFront, Route 53, AWS Global Accelerator
- **Shield vs WAF**: Shield = DDoS (volumétrico, camadas 3/4); WAF = filtros de requisições HTTP maliciosas (camada 7)
- Shield Advanced pode ser integrado com WAF para proteção combinada

## Exemplo prático

**Cenário:** Um portal de notícias fica offline durante um grande evento político devido a um ataque DDoS volumétrico. Após o incidente, o time migra para Shield Advanced: um ataque de 100 Gbps é automaticamente mitigado antes de chegar à infraestrutura. O time de segurança recebe notificações em tempo real sobre o ataque e pode acionar o DRT da AWS via chat se precisar de suporte especializado. Os custos extras de EC2 causados pelo ataque são reembolsados pela AWS — proteção financeira incluída.
