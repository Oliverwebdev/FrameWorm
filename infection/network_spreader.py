"""
Netzwerkbasierte Infektionsmechanismen
"""
import os
import socket
import random
import threading
import time
from datetime import datetime

from ..core.logger import logger
from ..core.config import DEFAULT_SUBNET, SCAN_TIMEOUT, MAX_INFECTION_TARGETS, SIMULATION_MODE

class NetworkWorm:
    """Klasse zum Scannen des Netzwerks nach verwundbaren Systemen und zur Verbreitung"""
    
    def __init__(self, subnet=DEFAULT_SUBNET):
        self.subnet = subnet
        self.vulnerable_hosts = []
        self.port_scan_results = {}
        self.infected_hosts = []
        self.running = False
        logger.info(f"[+] NetworkWorm initialisiert mit Subnetz: {self.subnet}")
    
    def execute(self):
        """Führt den Netzwerk-Wurm aus"""
        self.running = True
        logger.info("[+] NetworkWorm gestartet")
        
        # Starte den Scan-Thread
        scan_thread = threading.Thread(target=self._scan_and_infect_loop)
        scan_thread.daemon = True
        scan_thread.start()
        
        return True
    
    def _scan_and_infect_loop(self):
        """Kontinuierliche Scan- und Infektionsschleife"""
        while self.running:
            try:
                # Scan nach verwundbaren Hosts
                hosts = self.scan_network()
                
                # Infiziere verwundbare Hosts
                for host in hosts[:MAX_INFECTION_TARGETS]:  # Begrenze die Anzahl gleichzeitiger Infektionen
                    if host not in self.infected_hosts:
                        self._infect_host(host)
                
                # Warte zwischen den Scans
                time.sleep(60)  # 1 Minute zwischen Scans
            except Exception as e:
                logger.error(f"[-] Fehler im Scan-und-Infektionszyklus: {e}")
                time.sleep(30)  # Bei Fehler kürzere Wartezeit
    
    def scan_network(self):
        """Simuliert einen Netzwerk-Scan"""
        logger.info(f"[+] Scanne Netzwerk: {self.subnet} (simuliert)")
        # Simuliert das Finden von 3-7 verwundbaren Hosts
        num_hosts = random.randint(3, 7)
        self.vulnerable_hosts = [f"192.168.1.{random.randint(1, 254)}" for _ in range(num_hosts)]
        vulnerabilities = ["SMB", "RDP", "SSH", "WebApp", "SQL", "FTP", "VNC", "Telnet"]
        
        for host in self.vulnerable_hosts:
            vuln = random.choice(vulnerabilities)
            logger.info(f"[+] Host {host} ist anfällig für {vuln}-Angriffe (simuliert)")
        
        return self.vulnerable_hosts
    
    def port_scan(self, host):
        """Simuliert einen Port-Scan auf einem Host"""
        logger.info(f"[+] Führe Port-Scan auf {host} durch (simuliert)")
        open_ports = []
        # Simuliere offene Ports
        common_ports = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 5432, 8080, 5900, 5901, 8443, 27017]
        for port in common_ports:
            if random.random() > 0.7:  # 30% Chance, dass ein Port offen ist
                open_ports.append(port)
                logger.info(f"[+] Port {port} auf {host} ist offen (simuliert)")
        
        self.port_scan_results[host] = open_ports
        return open_ports
    
    def service_fingerprinting(self, host, port):
        """Simuliert Service-Fingerprinting auf einem offenen Port"""
        logger.info(f"[+] Führe Service-Fingerprinting auf {host}:{port} durch (simuliert)")
        
        # Simuliere Service-Erkennung basierend auf Port-Nummer
        services = {
            21: ("FTP", ["vsftpd 3.0.3", "ProFTPD 1.3.5", "FileZilla Server"]),
            22: ("SSH", ["OpenSSH 7.9", "Dropbear SSH", "PuTTY"]),
            23: ("Telnet", ["Linux Telnetd", "BusyBox Telnet"]),
            25: ("SMTP", ["Postfix", "Sendmail", "Microsoft Exchange"]),
            53: ("DNS", ["BIND 9", "Microsoft DNS"]),
            80: ("HTTP", ["Apache 2.4.29", "nginx 1.14.0", "Microsoft IIS 10.0"]),
            443: ("HTTPS", ["Apache 2.4.29 (SSL)", "nginx 1.14.0 (SSL)", "Microsoft IIS 10.0 (SSL)"]),
            445: ("SMB", ["Samba 4.7.6", "Microsoft Windows SMB"]),
            3306: ("MySQL", ["MySQL 5.7.33", "MariaDB 10.3.27"]),
            3389: ("RDP", ["Microsoft Terminal Services", "xrdp"]),
            5432: ("PostgreSQL", ["PostgreSQL 10.14", "PostgreSQL 12.6"]),
            5900: ("VNC", ["TightVNC", "RealVNC", "UltraVNC"]),
            8080: ("HTTP-Proxy", ["Apache Tomcat 9.0.37", "Jenkins 2.249", "Jetty 9.4.30"]),
            27017: ("MongoDB", ["MongoDB 4.2.8", "MongoDB 4.4.3"])
        }
        
        if port in services:
            service_name, versions = services[port]
            version = random.choice(versions)
            logger.info(f"[+] Erkannter Dienst auf {host}:{port} - {service_name} ({version}) (simuliert)")
            return {
                "service": service_name,
                "version": version,
                "banner": f"{service_name} {version} ready"
            }
        else:
            logger.info(f"[+] Unbekannter Dienst auf {host}:{port} (simuliert)")
            return {
                "service": "unknown",
                "version": "unknown",
                "banner": "Ready"
            }
    
    def _infect_host(self, host):
        """Simuliert die Infektion eines Hosts"""
        if SIMULATION_MODE:
            logger.info(f"[+] Simuliere Infektion von Host: {host} (SIMULATION_MODE)")
            
            # Führe Port-Scan durch, um offene Ports zu finden
            open_ports = self.port_scan(host)
            if not open_ports:
                logger.info(f"[-] Keine offenen Ports auf {host} gefunden, Infektion nicht möglich")
                return False
            
            # Wähle einen zufälligen offenen Port für den Exploit
            target_port = random.choice(open_ports)
            service_info = self.service_fingerprinting(host, target_port)
            
            # Wähle eine geeignete Exploit-Methode basierend auf dem Dienst
            exploit_success = self._select_and_execute_exploit(host, target_port, service_info)
            
            if exploit_success:
                logger.info(f"[+] Infektion von {host} erfolgreich (simuliert)")
                self.infected_hosts.append(host)
                # Simuliert das Kopieren und Ausführen des Payloads auf dem Zielhost
                logger.info(f"[+] Payload auf {host} ausgeführt (simuliert)")
                return True
            else:
                logger.info(f"[-] Infektion von {host} fehlgeschlagen (simuliert)")
                return False
        else:
            logger.warning(f"[!] Echte Infektionen sind deaktiviert. Setze SIMULATION_MODE=True in config.py")
            return False
    
    def _select_and_execute_exploit(self, host, port, service_info):
        """Wählt und führt einen geeigneten Exploit basierend auf dem Dienst aus"""
        service = service_info.get("service", "unknown").lower()
        
        if service == "smb":
            from ..evasion.vulnerability_exploiter import VulnerabilityExploiter
            return VulnerabilityExploiter.exploit_smb(host)
        elif service == "rdp":
            from ..evasion.vulnerability_exploiter import VulnerabilityExploiter
            return VulnerabilityExploiter.exploit_rdp(host)
        elif service == "ssh":
            from ..evasion.vulnerability_exploiter import VulnerabilityExploiter
            return VulnerabilityExploiter.exploit_ssh(host)
        elif service in ["http", "https", "http-proxy"]:
            # Simuliere Web-basierte Exploits
            return random.random() > 0.4  # 60% Erfolgswahrscheinlichkeit
        else:
            # Generischer Exploit für unbekannte Dienste
            return random.random() > 0.7  # 30% Erfolgswahrscheinlichkeit
    
    def stop(self):
        """Stoppt den Netzwerk-Wurm"""
        self.running = False
        logger.info("[-] NetworkWorm gestoppt")