# AWS Well-Architected Framework

## O que é?

O AWS Well-Architected Framework é um conjunto de melhores práticas e princípios de design criado pela AWS para ajudar arquitetos de nuvem a construir infraestruturas seguras, de alta performance, resilientes e eficientes. Baseia-se em seis pilares fundamentais que guiam as decisões de arquitetura.

## Casos de uso

- Avaliação de arquiteturas existentes para identificar riscos e oportunidades de melhoria
- Guia para arquitetar novas aplicações na nuvem desde o início
- Revisão periódica da infraestrutura (Well-Architected Review)
- Preparação para auditorias de conformidade e segurança
- Alinhamento com as melhores práticas da indústria

## Pontos-chave para a prova (CLF-C02)

**Os 6 Pilares do Well-Architected Framework:**

1. **Excelência Operacional (Operational Excellence)**
   - Executar e monitorar sistemas, melhorar processos e procedimentos continuamente
   - Princípios: infraestrutura como código, mudanças frequentes e pequenas, antecipar falhas

2. **Segurança (Security)**
   - Proteger dados, sistemas e ativos
   - Princípios: identidade forte, rastreabilidade, segurança em todas as camadas, criptografia, preparação para incidentes

3. **Confiabilidade (Reliability)**
   - Capacidade de recuperar de falhas e atender à demanda
   - Princípios: recuperação automática, testar recuperação, escala horizontal, parar de adivinhar capacidade

4. **Eficiência de Performance (Performance Efficiency)**
   - Usar recursos computacionais eficientemente
   - Princípios: democratizar tecnologias avançadas, ir global em minutos, arquiteturas serverless, experimentar com frequência

5. **Otimização de Custos (Cost Optimization)**
   - Evitar gastos desnecessários
   - Princípios: modelo de consumo, medir eficiência, parar de gastar com data center, analisar e atribuir gastos

6. **Sustentabilidade (Sustainability)** *(adicionado em 2021)*
   - Minimizar o impacto ambiental
   - Princípios: entender seu impacto, maximizar utilização, usar serviços gerenciados, reduzir recursos downstream

## Exemplo prático

**Cenário:** Uma empresa faz uma Well-Architected Review em sua aplicação de e-commerce e identifica riscos: (1) Segurança — banco de dados RDS em sub-rede pública (risco alto); (2) Confiabilidade — sem Multi-AZ nem backups automáticos; (3) Otimização de Custos — instâncias EC2 superprovisionadas com 5% de uso de CPU. O plano de ação move o RDS para sub-rede privada, habilita Multi-AZ, ativa backups automáticos e reduz o tamanho das instâncias — melhorando a arquitetura em todos os pilares.
