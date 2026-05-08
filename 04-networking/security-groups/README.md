# Security Groups (Grupos de Segurança)

## O que é?

Security Groups são firewalls virtuais que controlam o tráfego de entrada (inbound) e saída (outbound) de recursos AWS como instâncias EC2, RDS, e outros. Funcionam no nível do recurso (instância) e são stateful — se uma requisição de entrada é permitida, a resposta de saída é automaticamente permitida.

## Casos de uso

- Controlar quais endereços IP podem acessar um servidor web (porta 80/443)
- Restringir acesso SSH (porta 22) apenas para IPs do escritório
- Permitir que apenas o servidor de aplicação se comunique com o banco de dados (porta 3306)
- Criar regras baseadas em outros Security Groups (ex: "aceite apenas tráfego do Load Balancer")
- Isolar camadas de uma aplicação multi-tier

## Pontos-chave para a prova (CLF-C02)

- **Stateful**: se o tráfego de entrada é permitido, o retorno é automaticamente permitido (sem precisar de regra de saída explícita)
- **Apenas regras de ALLOW** — não há como criar regras de DENY em Security Groups (use Network ACL para bloqueios)
- Por padrão: **todo tráfego de entrada é bloqueado** e **todo tráfego de saída é permitido**
- Podem ser anexados a **múltiplas instâncias** — e uma instância pode ter **múltiplos Security Groups**
- Regras podem referenciar **outros Security Groups** (não apenas IPs) — muito poderoso para arquiteturas em camadas
- Operam no nível da **instância/recurso** — diferente do Network ACL que opera no nível da sub-rede
- Mudanças nas regras são aplicadas **imediatamente** a todas as instâncias associadas
- **Security Group vs Network ACL**: SG = stateful, apenas Allow, nível da instância; NACL = stateless, Allow e Deny, nível da sub-rede

## Exemplo prático

**Cenário:** Uma arquitetura web 3-tier define: SG-Web (aceita HTTP/HTTPS de qualquer IP, SSH apenas do IP do escritório); SG-App (aceita tráfego na porta 8080 apenas do SG-Web); SG-DB (aceita conexões MySQL na porta 3306 apenas do SG-App). Dessa forma, o banco de dados é completamente inacessível pela internet, mesmo que alguém tente acessá-lo diretamente — o tráfego só chega ao banco se vier do servidor de aplicação.
