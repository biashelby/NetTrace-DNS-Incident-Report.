import socket
import sys

def verify_dns_service(target_ip, port=53):
    """
    Simula uma verificação de saúde na porta DNS (UDP).
    Utilizado para validar se o serviço voltou a ficar ativo após um incidente.
    """
    # Criando um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3) # Timeout de 3 segundos
    
    print(f"[*] Iniciando teste de conectividade em {target_ip}:{port}...")
    
    try:
        # Enviando um pacote vazio (teste de socket)
        # Nota: Em um ambiente real, enviaríamos uma query DNS formatada.
        sock.sendto(b'', (target_ip, port))
        
        # Se não houver erro imediato (como ICMP 'Connection Refused'), 
        # o socket assume que o pacote foi enviado.
        print(f"[+] Pacote enviado com sucesso para {target_ip}. Verifique os logs do servidor.")
        return True
    except Exception as e:
        print(f"[!] Erro detectado na conexão: {e}")
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    # IP do servidor DNS identificado no relatório
    SERVER_IP = "203.0.113.2"
    verify_dns_service(SERVER_IP)
