# Amazon CloudFront

## O que é?

Amazon CloudFront é a rede de distribuição de conteúdo (CDN — Content Delivery Network) da AWS. Distribui conteúdo (páginas web, imagens, vídeos, APIs) globalmente através de uma rede de **edge locations** (pontos de presença) ao redor do mundo, entregando conteúdo com baixíssima latência para os usuários finais.

## Casos de uso

- Acelerar a entrega de sites estáticos e dinâmicos globalmente
- Distribuição de conteúdo de mídia (streaming de vídeo)
- Proteção de APIs com baixa latência global
- Distribuição segura de software e atualizações
- Proteção contra DDoS integrada com AWS Shield
- Servir conteúdo do S3 com baixa latência globalmente

## Pontos-chave para a prova (CLF-C02)

- **Edge Locations**: pontos de presença da AWS onde o conteúdo é armazenado em cache — há muito mais edge locations do que regiões e AZs
- **Origin**: a fonte original do conteúdo — pode ser um bucket S3, um ELB, uma instância EC2 ou qualquer servidor HTTP
- **Cache**: o CloudFront armazena o conteúdo em cache nas edge locations, reduzindo a carga no origem e a latência para o usuário
- **TTL (Time to Live)**: define por quanto tempo o conteúdo fica em cache antes de ser renovado
- **HTTPS por padrão**: suporta SSL/TLS com certificados gerenciados pelo ACM (AWS Certificate Manager) gratuitamente
- **AWS Shield Standard**: proteção contra DDoS **incluída gratuitamente** no CloudFront
- **Geo-restriction**: permite bloquear ou permitir acesso de países específicos
- **CloudFront vs S3 direto**: CloudFront adiciona cache global e reduz latência; use CloudFront para conteúdo acessado globalmente

## Exemplo prático

**Cenário:** Um portal de notícias brasileiro está crescendo e recebe visitas de todo o mundo. Os arquivos estáticos (imagens, CSS, JS) ficam armazenados em um bucket S3 na região sa-east-1 (São Paulo). Sem CloudFront, usuários na Europa ou Ásia experimentam alta latência. Com CloudFront configurado, as imagens são cacheadas automaticamente nas edge locations mais próximas de cada usuário — um leitor em Tóquio recebe o conteúdo da edge location no Japão, reduzindo a latência de ~300ms para ~5ms.
