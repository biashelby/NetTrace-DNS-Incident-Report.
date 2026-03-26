# Network Traffic Analysis: DNS & ICMP Incident Report

## Visão Geral do Projeto
Este projeto documenta a investigação de um incidente de rede real, onde usuários relataram a impossibilidade de acessar o serviço web `www.yummyrecipesforme.com`. Através da análise de pacotes capturados via `tcpdump`, identificamos falhas críticas na camada de transporte e no serviço de resolução de nomes (DNS).

Este repositório serve como uma demonstração de habilidades em:
- Análise de protocolos de rede (UDP, ICMP, DNS).
- Diagnóstico de falhas (Troubleshooting) de conectividade.
- Escrita de relatórios técnicos de segurança cibernética.
- Automação básica de verificação de rede com Python.

---

## Relatório de Incidente de Segurança Cibernética

### Parte 1: Resumo do Problema (Log de Tráfego)
[cite_start]A análise dos registros do analisador de protocolos revela uma falha na comunicação entre o cliente e o servidor de nomes[cite: 1, 2].

- [cite_start]**Protocolo UDP:** O registro indica que o navegador do cliente (IP `192.51.100.15`) enviou solicitações de consulta DNS para o servidor `203.0.113.2` na porta 53[cite: 3, 4].
- [cite_start]**Protocolo ICMP:** Em resposta aos pacotes UDP, o servidor retornou mensagens de erro ICMP indicando que a "porta udp 53 está inacessível"[cite: 3].
- [cite_start]**Análise Técnica:** A porta 53 é o padrão para serviços DNS[cite: 3]. [cite_start]O fato de o servidor retornar um erro ICMP de porta inacessível confirma que o host está ativo, mas o serviço de DNS não está "ouvindo" ou processando requisições[cite: 3].
- [cite_start]**Conclusão da Parte 1:** O problema central é uma falha de disponibilidade no serviço DNS, impedindo a tradução do domínio para um endereço IP funcional[cite: 3].

### Parte 2: Análise de Dados e Investigação
- [cite_start]**Cronologia:** O incidente foi detectado inicialmente às **13:24:32**, com tentativas de reconexão falhas persistindo nos minutos seguintes[cite: 4].
- [cite_start]**Detecção:** A equipe de TI foi alertada após reclamações de clientes sobre erros de "porta de destino inalcançável"[cite: 4].
- [cite_start]**Metodologia de Investigação:** Foi utilizada a ferramenta `tcpdump` para capturar o tráfego de saída e entrada, revelando que as consultas DNS (pacotes UDP com flag `A?`) não estavam sendo respondidas com os IPs correspondentes, mas sim com erros de rede[cite: 4].
- [cite_start]**Principais Descobertas:** O servidor DNS (`203.0.113.2`) está operacional na camada de rede, mas o serviço de aplicação na porta 53 está inativo ou bloqueado[cite: 4, 10].
- [cite_start]**Causa Raiz Suspeita:** Interrupção inesperada do serviço DNS no servidor ou uma alteração não autorizada/incorreta nas regras de firewall que restringiu o tráfego UDP na porta 53[cite: 10].

---

## Ferramenta de Validação (Python)
Para auxiliar na verificação pós-incidente, incluí um script que testa a conectividade da porta UDP 53.
