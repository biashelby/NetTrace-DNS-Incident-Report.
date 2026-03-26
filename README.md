# The DNS Autopsy: A Cybersecurity Case Study 

## Visão Geral
Este repositório documenta a investigação de um incidente de rede onde o site `www.yummyrecipesforme.com` ficou inacessível para os usuários[cite: 3]. Através da análise de logs de tráfego capturados via `tcpdump`, este estudo identifica uma falha crítica na camada de transporte afetando a resolução de nomes (DNS).

Este projeto demonstra competências em:
* Análise de protocolos (UDP, ICMP e DNS).
* Diagnóstico de falhas de rede (Troubleshooting).
* Escrita técnica de relatórios de incidentes.
* Automação de segurança com Python.

---

## Relatório de Incidente de Segurança Cibernética

### Parte 1: Resumo do Problema (Análise de Log)
[cite_start]A análise detalhada dos registros do analisador de protocolos revela uma interrupção na comunicação entre o cliente e o servidor de nomes[cite: 1, 2].

* [cite_start]**Protocolo UDP:** O log indica que o navegador do cliente (IP `192.51.100.15`) enviou múltiplas solicitações de consulta DNS para o servidor `203.0.113.2` na porta 53[cite: 3, 4].
* [cite_start]**Protocolo ICMP:** Em resposta aos pacotes UDP, o servidor retornou mensagens de erro ICMP indicando especificamente que a "porta udp 53 está inacessível"[cite: 3, 4].
* [cite_start]**Análise Técnica:** A porta 53 é o ponto de extremidade padrão para o serviço DNS[cite: 3]. [cite_start]O retorno de uma mensagem ICMP confirma que o host está ativo na rede, porém o serviço de aplicação (DNS) não está processando as requisições[cite: 3].
* [cite_start]**Conclusão:** O problema central é uma falha de disponibilidade no serviço DNS, o que impede a tradução do domínio para um endereço IP funcional e resulta na negação de acesso ao site[cite: 3].



### Parte 2: Análise de Dados e Investigação
* [cite_start]**Cronologia:** O incidente foi registrado inicialmente às **13:24:32**, com tentativas de conexão falhas persistindo até pelo menos 13:28:50[cite: 4].
* [cite_start]**Detecção:** A equipe de TI foi alertada após reclamações de clientes sobre o erro "porta de destino inalcançável" ao tentar carregar a página[cite: 4].
* [cite_start]**Metodologia:** Foi utilizada a ferramenta `tcpdump` para capturar o tráfego de saída e entrada, revelando que as consultas DNS (pacotes UDP com flag `A?`) recebiam erros imediatos de rede[cite: 4].
* [cite_start]**Principais Descobertas:** O servidor DNS (`203.0.113.2`) está operacional na camada de rede, mas o serviço de aplicação na porta 53 está inativo ou bloqueado por regras de firewall[cite: 4].
* [cite_start]**Causa Raiz Suspeita:** Interrupção do serviço DNS no servidor ou uma alteração não autorizada nas regras de segurança que restringiu o tráfego UDP na porta 53[cite: 4].

---

## Ferramenta de Validação (Python)
Para auxiliar na verificação de saúde do serviço após a manutenção, desenvolvi o seguinte script:
