# IAM Best Practices (Boas Práticas)

## O que é?

Boas práticas de IAM são um conjunto de recomendações da AWS para configurar e gerenciar identidades e acessos de forma segura. Seguir essas práticas reduz drasticamente o risco de brechas de segurança e acessos não autorizados.

## Casos de uso

- Proteger a conta AWS de acessos indevidos
- Atender a requisitos de conformidade (ISO 27001, SOC 2, PCI DSS)
- Implementar o modelo de segurança de **Confiança Zero (Zero Trust)**
- Auditar e revisar periodicamente permissões e acessos

## Pontos-chave para a prova (CLF-C02)

1. **Não use a conta root** para tarefas do dia a dia — proteja-a com MFA e guarde as credenciais em local seguro
2. **Crie usuários IAM individuais** — nunca compartilhe credenciais entre pessoas
3. **Use grupos para atribuir permissões** — é mais fácil gerenciar permissões em grupos do que individualmente
4. **Princípio do Menor Privilégio** — conceda apenas as permissões mínimas necessárias para a tarefa
5. **Habilite MFA** — especialmente para a conta root e usuários com privilégios elevados
6. **Use roles para aplicações** em vez de chaves de acesso embutidas no código
7. **Rotacione credenciais regularmente** — chaves de acesso devem ser rotacionadas periodicamente
8. **Use IAM Access Analyzer** para identificar recursos expostos externamente
9. **Remova credenciais não utilizadas** — usuários e chaves sem uso são riscos de segurança
10. **Use AWS Organizations + SCPs** para controle centralizado em ambientes multi-conta

## Exemplo prático

**Cenário:** Uma startup começa com o owner usando a conta root para tudo. Após uma auditoria de segurança, o time adota as boas práticas: cria um usuário IAM administrador para operações diárias, habilita MFA na conta root e no admin, organiza os devs em grupos (`Developers`, `QA`, `Ops`) com políticas específicas para cada um, e configura o IAM Access Analyzer para receber alertas caso algum bucket S3 seja acidentalmente exposto ao público. As chaves de acesso são rotacionadas a cada 90 dias via política interna.
