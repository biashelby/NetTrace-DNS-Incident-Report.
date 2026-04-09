#### ☕ The DNS Autopsy — Cybersecurity Incident Case Study

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![tcpdump](https://img.shields.io/badge/tcpdump-2C2C2A?style=for-the-badge)
![Protocolo](https://img.shields.io/badge/Protocolo-UDP_%7C_ICMP_%7C_DNS-557C94?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Incident_Report-E34F26?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Investigação_Concluída-3B6D11?style=for-the-badge)

Investigação de um incidente de rede onde o domínio `www.yummyrecipesforme.com` ficou inacessível para os usuários. A análise foi conduzida a partir de logs de tráfego capturados via `tcpdump`, identificando uma falha crítica na camada de aplicação afetando a resolução de nomes (DNS).

---

#### ☕ Competências Demonstradas

| Área | Descrição |
|---|---|
| Análise de protocolos | Inspeção de tráfego UDP, ICMP e DNS em nível de pacote |
| Troubleshooting de rede | Diagnóstico de falhas na camada de transporte e aplicação |
| Escrita técnica | Elaboração de relatório formal de incidente de segurança |
| Automação de segurança | Script Python para validação pós-incidente do serviço DNS |

---

#### ☕ Relatório de Incidente de Segurança Cibernética

#### Parte 1 — Resumo do Problema (Análise de Log)

A análise dos registros do analisador de protocolos revelou uma interrupção na comunicação entre o cliente e o servidor de nomes.

| Campo | Detalhe |
|---|---|
| IP do cliente | `192.51.100.15` |
| IP do servidor DNS | `203.0.113.2` |
| Porta alvo | `UDP/53` (DNS) |
| Protocolo de erro | ICMP — `udp port 53 unreachable` |
| Início do incidente | `13:24:32` |
| Última tentativa registrada | `13:28:50` |

**Fluxo do incidente:**

```
Cliente (192.51.100.15)
        │
        │ Query DNS (UDP → porta 53)
        ▼
Servidor DNS (203.0.113.2)
        │
        │ ICMP: "udp port 53 unreachable"
        ▼
Cliente recebe erro — sem resolução de nome — site inacessível
```

**Conclusão técnica:** O host `203.0.113.2` está operacional na camada de rede (responde via ICMP), porém o serviço DNS na porta 53 não está processando requisições — indicando falha de disponibilidade na camada de aplicação.

---

#### Parte 2 — Análise e Investigação

**Cronologia do incidente:**

| Horário | Evento |
|---|---|
| `13:24:32` | Primeira consulta DNS registrada sem resposta |
| `13:24:32` – `13:28:50` | Tentativas de conexão falhas persistentes |
| Pós `13:28:50` | Equipe de TI alertada via reclamações de clientes |

**Metodologia aplicada:**

A ferramenta `tcpdump` foi utilizada para capturar o tráfego de entrada e saída, revelando que as consultas DNS (pacotes UDP com flag `A?`) recebiam erros imediatos de rede em vez de respostas válidas.

**Principais descobertas:**

- O servidor DNS `203.0.113.2` está ativo na camada de rede
- O serviço de aplicação na `porta 53` está **inativo ou bloqueado**
- Nenhuma resposta DNS válida foi recebida durante o período analisado

**Causa raiz suspeita:**

Interrupção do processo DNS no servidor **ou** alteração não autorizada em regras de firewall restringindo tráfego `UDP/53` — possível vetor de ataque ou misconfiguration crítica.

---

#### ☕ Ferramenta de Validação Pós-Incidente (Python)

Script desenvolvido para verificar a disponibilidade do serviço DNS após manutenção, simulando a conectividade na porta `UDP/53`.

```python
import socket

def verify_dns_service(target_ip, port=53):
    """
    Simula uma verificação de saúde na porta DNS (UDP).
    Utilizado para validar se o serviço voltou a ficar ativo após um incidente.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)

    print(f"[*] Iniciando teste de conectividade em {target_ip}:{port}...")

    try:
        sock.sendto(b'', (target_ip, port))
        print(f"[+] Pacote enviado. Verifique os logs do servidor para confirmar recepção.")
        return True
    except Exception as e:
        print(f"[!] Erro detectado: {e}")
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    SERVER_IP = "203.0.113.2"
    verify_dns_service(SERVER_IP)
```

**Como executar:**

```bash
python verify_dns.py
```

> ⚠️ **Nota:** O script envia um pacote UDP vazio para teste de socket. Em ambiente de produção, recomenda-se enviar uma query DNS formatada (ex: usando a biblioteca `dnspython`) para validação completa do serviço.

---

#### ☕ Estrutura do Repositório

```
dns-autopsy/
├── report/
│   └── incident_report.md    # Relatório formal do incidente
├── verify_dns.py             # Script de validação do serviço DNS
├── capture_sample.txt        # Amostra do log tcpdump analisado
└── README.md
```

---

> ⚠️ **Aviso ético:** Todos os IPs e domínios utilizados neste estudo são fictícios ou reservados para documentação (RFC 5737 / RFC 2606), utilizados exclusivamente para fins educacionais.
