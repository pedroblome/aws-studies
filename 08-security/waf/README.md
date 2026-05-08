# AWS WAF (Web Application Firewall)

## O que é?

AWS WAF é um firewall de aplicação web que protege suas aplicações web e APIs contra exploits comuns da internet que podem afetar disponibilidade, comprometer segurança ou consumir recursos excessivos. Permite criar regras que controlam o tráfego HTTP/HTTPS com base em condições que você define.

## Casos de uso

- Proteção contra ataques SQL Injection e Cross-Site Scripting (XSS)
- Bloqueio de IPs maliciosos e bots automatizados
- Proteção contra scrapers e abuso de APIs
- Conformidade com requisitos de segurança de aplicações web
- Filtragem de tráfego por geolocalização (bloquear países específicos)

## Pontos-chave para a prova (CLF-C02)

- **Onde o WAF é implantado**: integra-se com CloudFront, Application Load Balancer (ALB), API Gateway, AppSync
- **Web ACL (Access Control List)**: conjunto de regras que o WAF aplica ao tráfego
- **Rules (Regras)**: definem condições de bloqueio ou permissão — podem verificar IP, headers HTTP, URI, corpo da requisição, etc.
- **AWS Managed Rules**: conjuntos de regras pré-configuradas mantidas pela AWS para proteção contra OWASP Top 10, bots, etc.
- **Rate-based rules**: bloqueiam IPs que excedem um número de requisições em um período — proteção contra brute force
- **WAF vs Shield:**
  - WAF = proteção na camada 7 (aplicação) — filtra requisições HTTP maliciosas
  - Shield = proteção nas camadas 3/4 (rede/transporte) — proteção contra DDoS volumétrico
- **Logs do WAF**: podem ser enviados para S3, CloudWatch Logs ou Kinesis Data Firehose para análise
- **Cobrança**: por Web ACL, por regra e por milhão de requisições inspecionadas

## Exemplo prático

**Cenário:** Um portal bancário sofre tentativas de SQL Injection. O time configura o WAF no CloudFront com: (1) AWS Managed Rule Group para OWASP Top 10 (bloqueia SQL Injection, XSS automaticamente); (2) regra de rate-limiting que bloqueia IPs com mais de 100 requisições por minuto (proteção contra brute force); (3) Geo-restriction bloqueando países de onde nunca vêm clientes legítimos. O WAF inspeciona 100% das requisições antes de chegarem à aplicação.
