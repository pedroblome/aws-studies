# Subnets (Sub-redes)

## O que é?

Subnets são segmentos de uma VPC que residem dentro de uma única Zona de Disponibilidade (AZ). Elas dividem o espaço de endereçamento IP da VPC em blocos menores e permitem organizar e isolar recursos por função, nível de acesso (público/privado) e segurança.

## Casos de uso

- Separar recursos públicos (servidores web) de recursos privados (bancos de dados)
- Isolar camadas de uma aplicação (web tier, app tier, data tier)
- Distribuir recursos entre múltiplas AZs para alta disponibilidade
- Criar redes dedicadas para serviços específicos (ex: sub-rede para RDS, outra para EC2)

## Pontos-chave para a prova (CLF-C02)

- **Sub-rede pública**: possui rota para um Internet Gateway — recursos podem ter IPs públicos e receber tráfego da internet
- **Sub-rede privada**: sem rota direta para internet — recursos só são acessíveis de dentro da VPC ou via VPN
- Cada sub-rede pertence a **exatamente uma AZ** — use múltiplas sub-redes em diferentes AZs para alta disponibilidade
- **5 endereços IP são reservados** pela AWS em cada sub-rede (primeiro, segundo, terceiro, penúltimo e último)
- **NAT Gateway**: colocado em sub-rede pública para permitir que instâncias em sub-redes privadas acessem a internet
- **Bastion Host (Jump Box)**: instância EC2 em sub-rede pública usada para acessar instâncias em sub-redes privadas via SSH
- A Route Table da sub-rede determina para onde o tráfego é direcionado (Internet Gateway, NAT Gateway, etc.)

## Exemplo prático

**Cenário:** Uma aplicação bancária é implantada com alta disponibilidade em 2 AZs. Arquitetura: 2 sub-redes públicas (uma em cada AZ) com os servidores web e o Load Balancer; 2 sub-redes privadas (uma em cada AZ) com os servidores de aplicação; 2 sub-redes de banco de dados (uma em cada AZ) com as instâncias RDS. Se uma AZ falhar, a outra continua atendendo — garantindo disponibilidade mesmo em caso de falha de datacenter.
