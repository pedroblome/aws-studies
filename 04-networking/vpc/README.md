# Amazon VPC (Virtual Private Cloud)

## O que é?

Amazon VPC é uma rede virtual privada isolada logicamente dentro da AWS Cloud. É a sua própria seção da AWS Cloud onde você pode lançar recursos AWS em uma rede virtual que você mesmo define e controla — com total controle sobre o ambiente de rede, incluindo seleção de intervalos de IP, criação de sub-redes, e configuração de tabelas de rotas e gateways.

## Casos de uso

- Isolar recursos de produção em uma rede privada segura
- Criar ambientes multi-camada (web, aplicação, banco de dados) com redes separadas
- Conectar a rede corporativa on-premises à AWS via VPN ou Direct Connect
- Segmentar ambientes (dev, homologação, produção) em VPCs separadas
- Cumprir requisitos de conformidade que exigem isolamento de rede

## Pontos-chave para a prova (CLF-C02)

- Cada conta AWS tem uma **VPC padrão** em cada região — pronta para uso imediato
- Uma VPC abrange **toda uma região** — as sub-redes são criadas dentro das Zonas de Disponibilidade
- **CIDR Block**: define o intervalo de endereços IP da VPC (ex: `10.0.0.0/16`)
- **Componentes principais:**
  - **Sub-redes (Subnets)**: segmentos da VPC dentro de uma AZ — podem ser públicas ou privadas
  - **Internet Gateway (IGW)**: permite comunicação entre a VPC e a internet
  - **Route Tables**: definem para onde o tráfego é direcionado
  - **NAT Gateway**: permite que instâncias em sub-redes privadas acessem a internet (sem serem acessíveis de fora)
  - **Security Groups**: firewall virtual no nível da instância (stateful)
  - **Network ACLs**: firewall no nível da sub-rede (stateless)
- **VPC Peering**: conecta duas VPCs para comunicação privada (mesmo entre contas e regiões)
- **VPC Endpoints**: acesso privado a serviços AWS sem passar pela internet pública

## Exemplo prático

**Cenário:** Uma aplicação 3-tier (web, app, banco) é arquitetada em uma VPC com CIDR `10.0.0.0/16`. A camada web fica em sub-redes públicas (com Internet Gateway), a camada de aplicação em sub-redes privadas, e o banco de dados em sub-redes privadas isoladas. Instâncias nas sub-redes privadas usam um NAT Gateway para baixar atualizações da internet sem ficarem expostas. Security Groups restringem o acesso: o banco aceita conexões apenas da camada de aplicação.
