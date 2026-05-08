# AWS CodePipeline

## O que é?

AWS CodePipeline é um serviço de entrega contínua (CD — Continuous Delivery) totalmente gerenciado que automatiza os pipelines de release para atualizações de aplicações rápidas e confiáveis. Orquestra as etapas de build, teste e deploy sempre que ocorre uma mudança no código-fonte.

## Casos de uso

- Automatizar o fluxo de build → teste → deploy de aplicações
- Implementar CI/CD para aplicações em EC2, ECS, Lambda ou on-premises
- Orquestrar múltiplas ferramentas de desenvolvimento (CodeCommit, GitHub, CodeBuild, CodeDeploy)
- Implementar gates de aprovação manual antes do deploy em produção
- Padronizar o processo de entrega de software em toda a organização

## Pontos-chave para a prova (CLF-C02)

- **Pipeline**: sequência de estágios (stages) que o código percorre do commit ao deploy
- **Stages (Estágios)**: etapas do pipeline — tipicamente Source → Build → Test → Deploy
- **Actions**: ações dentro de cada estágio (ex: checar código do GitHub, executar CodeBuild, fazer deploy com CodeDeploy)
- **Integração**: funciona com CodeCommit, GitHub, Bitbucket (Source); CodeBuild (Build); CodeDeploy, ECS, Lambda, CloudFormation (Deploy)
- **Notificações**: integra com SNS e CloudWatch Events para alertas sobre falhas e aprovações
- **Aprovação manual**: adicione um estágio de aprovação para exigir revisão humana antes do deploy em produção
- **Parallel actions**: ações dentro de um mesmo estágio podem executar em paralelo
- **Totalmente gerenciado e serverless**: sem servidores para gerenciar, pague por pipeline ativo/mês

## Exemplo prático

**Cenário:** Um time de devs usa GitHub para versionamento. O CodePipeline monitora o branch `main`: quando um PR é mergeado, o pipeline dispara automaticamente — (1) Source: clona o código do GitHub; (2) Build: CodeBuild executa os testes unitários e gera o artefato; (3) Deploy-Staging: CodeDeploy faz deploy no ambiente de homologação; (4) Aprovação manual: o tech lead aprova o deploy; (5) Deploy-Prod: CodeDeploy faz deploy em produção com rolling update. Todo o processo é auditado e repetível.
