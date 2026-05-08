# AWS CodeDeploy

## O que é?

AWS CodeDeploy é um serviço de deploy totalmente gerenciado que automatiza deployments de aplicações em instâncias EC2, servidores on-premises, funções Lambda e serviços ECS. Minimiza o downtime durante os deployments e elimina erros manuais do processo de deploy.

## Casos de uso

- Deploy automatizado de aplicações em instâncias EC2 com zero downtime
- Atualização de funções Lambda com validação automática
- Deploy de microsserviços em ECS com blue/green deployment
- Deploy em servidores on-premises como parte de uma estratégia híbrida
- Rollback automático em caso de falha durante o deploy

## Pontos-chave para a prova (CLF-C02)

- **Estratégias de deploy:**
  - **In-Place (Rolling)**: instâncias são atualizadas uma a uma ou em grupos — o mesmo ambiente, downtime mínimo
  - **Blue/Green**: novo ambiente (green) é criado com a nova versão; após validação, o tráfego é redirecionado do ambiente antigo (blue) para o novo — sem downtime
- **AppSpec file (appspec.yml)**: arquivo de configuração que define como o CodeDeploy deve fazer o deploy — hooks de ciclo de vida (BeforeInstall, AfterInstall, ApplicationStart, ValidateService)
- **Deployment Groups**: define quais instâncias/ambientes receberão o deploy (via tags EC2 ou Auto Scaling Groups)
- **Rollback automático**: se os health checks falharem ou alarmes CloudWatch dispararem, o CodeDeploy reverte automaticamente
- **Agente CodeDeploy**: software instalado nas instâncias EC2/on-premises que executa os comandos de deploy
- **Não precisa de agente** para Lambda e ECS
- **Hooks de ciclo de vida**: permitem executar scripts personalizados em cada fase do deploy (ex: parar o serviço, fazer backup, iniciar)

## Exemplo prático

**Cenário:** Um time usa Blue/Green deployment para uma API crítica no EC2. O CodeDeploy cria automaticamente um novo Auto Scaling Group (green) com a nova versão da aplicação. Testes de health check validam que a nova versão responde corretamente. O Load Balancer é reconfigurado para direcionar 100% do tráfego para o ambiente green. Se um alarme CloudWatch detectar erros 500 acima do normal nos primeiros 10 minutos, o rollback automático redireciona o tráfego de volta para o ambiente blue em segundos — SEM downtime para os usuários.
