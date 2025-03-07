"""
Peer-to-Peer Kommunikationsmechanismen
"""
import os
import random
import threading
import time
import socket
from datetime import datetime

from ..core.logger import logger
from ..core.config import SIMULATION_MODE

class P2PCommunication:
    """Klasse für Peer-to-Peer-Kommunikation zwischen infizierten Systemen"""
    
    def __init__(self, listen_port=None, initial_peers=None):
        self.listen_port = listen_port or random.randint(40000, 65000)
        self.initial_peers = initial_peers or []
        self.known_peers = set(self.initial_peers)
        self.running = False
        self.my_peer_id = self._generate_peer_id()
        self.cached_commands = []
        self.listen_thread = None
        self.discovery_thread = None
        logger.info(f"[+] P2PCommunication initialisiert, Port: {self.listen_port}, ID: {self.my_peer_id}")
    
    def execute(self):
        """Startet die P2P-Kommunikation"""
        if not SIMULATION_MODE:
            logger.warning("[!] P2P-Kommunikation im Nicht-Simulationsmodus deaktiviert")
            return False
        
        logger.info(f"[+] Starte P2P-Kommunikation auf Port {self.listen_port} (simuliert)")
        self.running = True
        
        # Starte den Listening-Thread
        self.listen_thread = threading.Thread(target=self._simulate_listen_for_peers)
        self.listen_thread.daemon = True
        self.listen_thread.start()
        
        # Starte den Discovery-Thread
        self.discovery_thread = threading.Thread(target=self._simulate_peer_discovery)
        self.discovery_thread.daemon = True
        self.discovery_thread.start()
        
        return True
    
    def _generate_peer_id(self):
        """Generiert eine eindeutige Peer-ID"""
        # Kombiniere Hostname und Zufallswert für eindeutige ID
        host_id = socket.gethostname()
        random_id = ''.join(random.choice("0123456789abcdef") for _ in range(8))
        return f"peer-{host_id}-{random_id}"
    
    def _simulate_listen_for_peers(self):
        """Simuliert das Lauschen auf eingehende Peer-Verbindungen"""
        logger.info(f"[+] Lausche auf eingehende P2P-Verbindungen auf Port {self.listen_port} (simuliert)")
        
        while self.running:
            try:
                # Simuliere eingehende Verbindungen
                if random.random() > 0.8 and len(self.known_peers) > 0:  # 20% Chance pro Zyklus
                    # Simuliere Verbindung von einem bekannten Peer
                    connecting_peer = random.choice(list(self.known_peers))
                    logger.info(f"[+] Eingehende Verbindung von Peer: {connecting_peer} (simuliert)")
                    
                    # Simuliere Nachrichtenempfang
                    self._simulate_receive_message(connecting_peer)
                
                # Simuliere gelegentlich Verbindungen von neuen unbekannten Peers
                if random.random() > 0.95:  # 5% Chance pro Zyklus
                    new_peer = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}:{random.randint(30000, 65000)}"
                    logger.info(f"[+] Neue Peer-Entdeckung: {new_peer} (simuliert)")
                    self.known_peers.add(new_peer)
                
                # Warte eine Weile
                time.sleep(5)
                
            except Exception as e:
                logger.error(f"[-] Fehler beim Lauschen auf Peers: {e} (simuliert)")
                time.sleep(10)
    
    def _simulate_peer_discovery(self):
        """Simuliert die regelmäßige Suche nach neuen Peers"""
        logger.info("[+] Starte aktive Peer-Discovery (simuliert)")
        
        while self.running:
            try:
                # Simuliere die Suche nach neuen Peers
                if len(self.known_peers) < 10:  # Wenn wenige Peers bekannt sind, aktiver suchen
                    logger.info("[+] Aktive Peer-Suche läuft (simuliert)")
                    
                    # Simuliere die Entdeckung neuer Peers
                    new_peers_count = random.randint(0, 3)
                    for _ in range(new_peers_count):
                        new_peer = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}:{random.randint(30000, 65000)}"
                        if new_peer not in self.known_peers:
                            logger.info(f"[+] Neuer Peer gefunden: {new_peer} (simuliert)")
                            self.known_peers.add(new_peer)
                
                # Simuliere das Testen bestehender Peer-Verbindungen
                self._simulate_peer_maintenance()
                
                # Simuliere das Senden von Nachrichten an Peers
                self._simulate_send_messages()
                
                # Warte zwischen Discovery-Zyklen
                time.sleep(30)
                
            except Exception as e:
                logger.error(f"[-] Fehler bei Peer-Discovery: {e} (simuliert)")
                time.sleep(60)
    
    def _simulate_peer_maintenance(self):
        """Simuliert die Wartung der Peer-Liste (Entfernung toter Peers)"""
        if not self.known_peers:
            return
        
        # Simuliere das Testen aller bekannten Peers
        peers_to_remove = set()
        
        for peer in self.known_peers:
            # Simuliere Peer-Test mit gewisser Ausfallwahrscheinlichkeit
            if random.random() > 0.9:  # 10% Chance, dass ein Peer nicht mehr erreichbar ist
                logger.info(f"[+] Peer nicht erreichbar: {peer} (simuliert)")
                peers_to_remove.add(peer)
        
        # Entferne tote Peers
        for peer in peers_to_remove:
            self.known_peers.remove(peer)
            logger.info(f"[+] Peer aus Liste entfernt: {peer} (simuliert)")
    
    def _simulate_receive_message(self, peer):
        """Simuliert den Empfang einer Nachricht von einem Peer"""
        # Simuliere verschiedene Nachrichtentypen
        message_types = ["command", "peer_list", "status_update", "data"]
        message_type = random.choice(message_types)
        
        if message_type == "command":
            # Simuliere den Empfang eines Befehls
            command_types = ["scan", "sleep", "update", "peer_discovery"]
            command = {
                "type": random.choice(command_types),
                "id": f"cmd-{random.randint(1000, 9999)}",
                "timestamp": datetime.now().isoformat(),
                "source_peer": peer
            }
            
            # Füge befehlsspezifische Parameter hinzu
            if command["type"] == "scan":
                command["target_range"] = f"192.168.{random.randint(0, 255)}.0/24"
            elif command["type"] == "sleep":
                command["duration"] = random.randint(60, 3600)
            elif command["type"] == "update":
                command["url"] = f"p2p://{random.choice(list(self.known_peers))}/update/{random.randint(1000, 9999)}"
            
            logger.info(f"[+] Befehl von Peer {peer} empfangen: {command['type']} (simuliert)")
            
            # Füge den Befehl zum Cache hinzu
            self.cached_commands.append(command)
            
            # Simuliere die Befehlsausführung
            # In einer echten Implementierung würde der Befehl ausgeführt werden
        
        elif message_type == "peer_list":
            # Simuliere den Empfang einer Peer-Liste
            num_peers = random.randint(1, 5)
            new_peers = []
            
            for _ in range(num_peers):
                new_peer = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}:{random.randint(30000, 65000)}"
                if new_peer not in self.known_peers and new_peer != f"{socket.gethostname()}:{self.listen_port}":
                    new_peers.append(new_peer)
                    self.known_peers.add(new_peer)
            
            if new_peers:
                logger.info(f"[+] Peer-Liste von {peer} empfangen, {len(new_peers)} neue Peers hinzugefügt (simuliert)")
            else:
                logger.info(f"[+] Peer-Liste von {peer} empfangen, keine neuen Peers (simuliert)")
        
        elif message_type == "status_update":
            # Simuliere den Empfang eines Status-Updates
            status = {
                "peer_id": f"peer-{peer.split(':')[0].replace('.', '-')}",
                "online_since": (datetime.now().timestamp() - random.randint(600, 86400)),
                "bots_count": random.randint(0, 10),
                "attacks_active": random.randint(0, 2)
            }
            
            logger.info(f"[+] Status-Update von Peer {peer} empfangen: {status['bots_count']} Bots, {status['attacks_active']} aktive Angriffe (simuliert)")
        
        elif message_type == "data":
            # Simuliere den Empfang von Daten
            data_types = ["keylog", "credentials", "scan_results"]
            data_type = random.choice(data_types)
            
            if data_type == "keylog":
                data_size = random.randint(1, 100)  # KB
                logger.info(f"[+] Keylog-Daten von Peer {peer} empfangen: {data_size} KB (simuliert)")
            
            elif data_type == "credentials":
                num_creds = random.randint(1, 20)
                logger.info(f"[+] Anmeldedaten von Peer {peer} empfangen: {num_creds} Einträge (simuliert)")
            
            elif data_type == "scan_results":
                num_hosts = random.randint(5, 50)
                logger.info(f"[+] Scan-Ergebnisse von Peer {peer} empfangen: {num_hosts} Hosts (simuliert)")
    
    def _simulate_send_messages(self):
        """Simuliert das Senden von Nachrichten an Peers"""
        if not self.known_peers:
            return
        
        # Simuliere gelegentliches Nachrichtenversenden
        if random.random() > 0.5:  # 50% Chance pro Zyklus
            # Wähle einen zufälligen Peer
            peer = random.choice(list(self.known_peers))
            
            # Simuliere verschiedene Nachrichtentypen
            message_types = ["status_update", "peer_list", "data_request", "command_propagation"]
            message_type = random.choice(message_types)
            
            if message_type == "status_update":
                logger.info(f"[+] Sende Status-Update an Peer {peer} (simuliert)")
            
            elif message_type == "peer_list":
                peers_to_share = random.sample(list(self.known_peers), min(5, len(self.known_peers)))
                logger.info(f"[+] Sende Peer-Liste mit {len(peers_to_share)} Peers an {peer} (simuliert)")
            
            elif message_type == "data_request":
                data_type = random.choice(["commands", "peer_list", "status"])
                logger.info(f"[+] Fordere {data_type} von Peer {peer} an (simuliert)")
            
            elif message_type == "command_propagation":
                # Propagiere einen zwischengespeicherten Befehl, falls vorhanden
                if self.cached_commands:
                    command = random.choice(self.cached_commands)
                    logger.info(f"[+] Propagiere Befehl {command['id']} ({command['type']}) an Peer {peer} (simuliert)")
                else:
                    logger.info(f"[+] Keine Befehle zum Propagieren an {peer} (simuliert)")
    
    def broadcast_command(self, command_type, **params):
        """Simuliert das Broadcasten eines Befehls an alle bekannten Peers"""
        if not self.known_peers:
            logger.warning("[!] Keine Peers bekannt, Broadcast nicht möglich (simuliert)")
            return False
        
        # Erstelle den Befehl
        command = {
            "type": command_type,
            "id": f"cmd-{random.randint(1000, 9999)}",
            "timestamp": datetime.now().isoformat(),
            "source_peer": self.my_peer_id,
            **params
        }
        
        logger.info(f"[+] Sende Befehl {command['id']} ({command['type']}) an {len(self.known_peers)} Peers (simuliert)")
        
        # Simuliere das Senden an jeden Peer
        for peer in self.known_peers:
            logger.info(f"[+] Sende Befehl an Peer {peer} (simuliert)")
            # In einer echten Implementierung würde der Befehl tatsächlich gesendet werden
        
        # Füge den Befehl zum Cache hinzu
        self.cached_commands.append(command)
        
        return True
    
    def get_network_status(self):
        """Gibt den Status des P2P-Netzwerks zurück"""
        return {
            "my_peer_id": self.my_peer_id,
            "listen_port": self.listen_port,
            "known_peers": len(self.known_peers),
            "cached_commands": len(self.cached_commands),
            "running": self.running
        }
    
    def stop(self):
        """Stoppt die P2P-Kommunikation"""
        logger.info("[+] Stoppe P2P-Kommunikation (simuliert)")
        self.running = False
        
        # Warte auf Threads
        if self.listen_thread and self.listen_thread.is_alive():
            self.listen_thread.join(timeout=1.0)
        
        if self.discovery_thread and self.discovery_thread.is_alive():
            self.discovery_thread.join(timeout=1.0)
        
        logger.info("[+] P2P-Kommunikation gestoppt (simuliert)")
        return True