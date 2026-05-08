# Amazon CloudWatch

## O que é?

Amazon CloudWatch é o serviço de monitoramento e observabilidade da AWS. Coleta e rastreia métricas, coleta e monitora arquivos de log, define alarmes e automaticamente reage a mudanças nos recursos AWS. É a ferramenta central de observabilidade para aplicações e infraestrutura na AWS.

## Casos de uso

- Monitorar utilização de CPU, memória e disco de instâncias EC2
- Criar alarmes que enviam notificações (via SNS) quando métricas ultrapassam limites
- Centralizar e analisar logs de aplicações e serviços AWS
- Acionar ações automáticas (Auto Scaling, Lambda) baseadas em métricas
- Criar dashboards para visualização em tempo real da saúde do sistema
- Monitorar custos e uso dos serviços AWS

## Pontos-chave para a prova (CLF-C02)

- **Métricas**: dados numéricos coletados ao longo do tempo (CPU, NetworkIn, RequestCount, etc.)
  - Métricas padrão do EC2: CPU, rede, disco — a cada 5 minutos
  - **Detailed Monitoring**: métricas a cada 1 minuto (custo adicional)
  - **Custom Metrics**: suas próprias métricas (ex: usuários ativos, tamanho de fila)
- **Logs**: o CloudWatch Logs centraliza logs de aplicações, Lambda, RDS, VPC Flow Logs, etc.
  - **Log Groups**: contêineres para logs relacionados
  - **Log Insights**: consultas SQL-like para analisar logs
- **Alarmes**: monitoram uma métrica e acionam ações quando ultrapassa um threshold
  - Estados: OK, ALARM, INSUFFICIENT_DATA
  - Ações: notificar via SNS, acionar Auto Scaling, executar ação no EC2
- **Dashboards**: painéis de visualização customizáveis com gráficos de métricas
- **EventBridge (CloudWatch Events)**: acionar ações baseadas em eventos ou agendamento
- **Retenção de métricas**: 15 meses para métricas padrão

## Exemplo prático

**Cenário:** Um time de DevOps configura o CloudWatch para monitorar sua aplicação em produção: um alarme dispara quando a CPU de qualquer instância EC2 ultrapassa 80% por 5 minutos — o SNS envia uma notificação por e-mail e aciona o Auto Scaling para adicionar instâncias. Os logs do Nginx são enviados para o CloudWatch Logs e o Log Insights é usado para consultar erros 500 em tempo real. Um dashboard mostra as principais métricas da aplicação em um único painel.
