# AWS CodeBuild

## O que é?

AWS CodeBuild é um serviço de integração contínua (CI) totalmente gerenciado que compila código-fonte, executa testes e produz pacotes de software prontos para deploy. É serverless — você não precisa provisionar, gerenciar ou escalar servidores de build.

## Casos de uso

- Compilar código Java, .NET, Python, Node.js, Go e outros
- Executar testes unitários e de integração automaticamente
- Construir imagens Docker e publicar no ECR
- Executar análise estática de código (SAST) e verificações de segurança
- Gerar artefatos de deploy (JARs, ZIPs, pacotes npm)

## Pontos-chave para a prova (CLF-C02)

- **Serverless**: sem servidores de build para provisionar — o CodeBuild escala automaticamente conforme a demanda
- **buildspec.yml**: arquivo YAML no repositório que define os comandos de build — fases: install, pre_build, build, post_build
- **Build environments**: ambientes de build pré-configurados (Ubuntu, Amazon Linux) com ferramentas comuns — ou imagens Docker customizadas
- **Cobrança por minuto**: pague apenas pelo tempo de computação usado nos builds — sem custos quando não há builds rodando
- **Integração**: funciona nativamente com CodePipeline, CodeCommit, GitHub, Bitbucket, S3, ECR
- **Relatórios de teste**: integra com frameworks de teste (JUnit, pytest) para visualizar resultados no console
- **Cache**: armazena dependências em cache (S3 ou local) para acelerar builds subsequentes
- **Variáveis de ambiente**: suporte a variáveis de ambiente e integração com Secrets Manager/SSM Parameter Store para dados sensíveis

## Exemplo prático

**Cenário:** Uma aplicação Spring Boot usa o CodeBuild com o seguinte `buildspec.yml`: fase `install` instala o Java 17; fase `build` executa `mvn package` — compila o código e roda 300 testes unitários; fase `post_build` constrói uma imagem Docker e faz push para o ECR. Se algum teste falhar, o build é marcado como falho e o CodePipeline para — impedindo que código com erros chegue à produção. Todo o processo leva 4 minutos e o time paga apenas por esses 4 minutos de computação.
