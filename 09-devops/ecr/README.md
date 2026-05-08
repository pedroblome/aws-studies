# Amazon ECR (Elastic Container Registry)

## O que é?

Amazon ECR é um registro de contêineres Docker totalmente gerenciado que facilita o armazenamento, gerenciamento e deploy de imagens de contêiner. Elimina a necessidade de operar sua própria infraestrutura de registro ou preocupar-se com a escalabilidade do armazenamento de imagens.

## Casos de uso

- Armazenar e versionar imagens Docker para deploy no ECS, EKS ou EC2
- Pipeline de CI/CD: CodeBuild constrói a imagem e faz push para o ECR; CodeDeploy/ECS faz pull para o deploy
- Compartilhar imagens de contêiner entre contas AWS de forma segura
- Escaneamento de vulnerabilidades nas imagens antes do deploy
- Armazenar imagens de base customizadas da empresa

## Pontos-chave para a prova (CLF-C02)

- **Repositórios**: contêineres de imagens — podem ser públicos (ECR Public Gallery) ou privados
- **Integração nativa**: funciona perfeitamente com ECS, EKS, CodeBuild, CodeDeploy e outros serviços AWS
- **Autenticação via IAM**: controle de acesso granular usando políticas IAM — sem credenciais separadas
- **Image Scanning**: escaneamento automático de vulnerabilidades nas imagens usando o banco de dados CVE — identifica problemas de segurança antes do deploy
- **Lifecycle Policies**: regras para deletar automaticamente imagens antigas (ex: manter apenas as 10 últimas versões) — controle de custos
- **Imutabilidade de tags**: opção para impedir que uma tag seja sobrescrita (ex: garantir que `v1.0.0` sempre aponte para a mesma imagem)
- **Replicação**: replica imagens automaticamente para múltiplas regiões — para deployments multi-região
- **ECR Public Gallery**: repositório público para compartilhar imagens com qualquer pessoa (similar ao Docker Hub)

## Exemplo prático

**Cenário:** Um pipeline de CI/CD completo com ferramentas AWS: developer faz push para o CodeCommit → CodePipeline dispara → CodeBuild compila e constrói a imagem Docker → faz push para o ECR com a tag da versão (ex: `minha-app:v2.3.1`) → ECR escaneia a imagem e não encontra vulnerabilidades críticas → ECS faz pull da nova imagem do ECR e faz o deploy com rolling update. Tudo dentro da rede privada AWS — sem tráfego passando pela internet pública.
