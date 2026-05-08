# Lab 01 — Site Estático com Amazon S3

## O que é?

Neste laboratório, você aprenderá a hospedar um site estático (HTML, CSS, JavaScript) usando o Amazon S3, configurar acesso público, habilitar o recurso de hospedagem de site estático e distribuir o conteúdo globalmente com o Amazon CloudFront. É um dos casos de uso mais simples e econômicos para hospedar sites na AWS.

## Casos de uso

- Portfólios pessoais e sites de apresentação
- Documentação de projetos (como este repositório)
- Landing pages e sites institucionais
- Aplicações frontend (React, Vue, Angular) com APIs separadas
- Sites com alto tráfego a baixo custo (S3 é muito mais barato que um servidor)

## Pontos-chave para a prova (CLF-C02)

- O S3 pode hospedar sites estáticos nativamente — sem servidor necessário
- O site é acessível via URL do S3: `http://bucket-name.s3-website-region.amazonaws.com`
- Para usar domínio customizado (ex: `www.meusite.com`), combine com **Route 53** e **CloudFront**
- **CloudFront** adiciona HTTPS (obrigatório em domínios customizados) e cache global
- **ACM (AWS Certificate Manager)**: certificado SSL/TLS gratuito para uso com CloudFront
- O bucket precisa ter **Block Public Access desabilitado** e uma **Bucket Policy** que permite acesso público (`s3:GetObject`)
- Arquivos estáticos = HTML, CSS, JS, imagens — sem processamento no servidor
- **Custo muito baixo**: pague apenas pelo armazenamento (GB) e transferência de dados

## Exemplo prático

**Cenário conceitual — Passo a Passo:**

1. **Criar o bucket S3**: nome igual ao domínio (ex: `www.meusite.com`) na região desejada
2. **Fazer upload dos arquivos**: `index.html`, `style.css`, imagens e outros assets
3. **Habilitar Static Website Hosting**: definir `index.html` como documento padrão e `error.html` como página de erro
4. **Configurar acesso público**: desabilitar Block Public Access e criar Bucket Policy permitindo `s3:GetObject` para `*`
5. **Criar distribuição CloudFront**: apontando para o endpoint do S3, habilitando HTTPS com certificado ACM
6. **Configurar Route 53**: criar registro CNAME ou Alias apontando `www.meusite.com` para a distribuição CloudFront

**Resultado**: site acessível globalmente via HTTPS em `https://www.meusite.com`, com conteúdo cacheado nas edge locations do CloudFront em mais de 400 locais ao redor do mundo — com latência de milissegundos para usuários em qualquer país.

**Custo estimado**: para um site simples com 10 GB de dados e 100 mil visitas/mês, o custo total (S3 + CloudFront) é inferior a $5/mês.
