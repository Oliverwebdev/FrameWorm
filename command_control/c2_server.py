"""
Command & Control Server-Simulationen
"""
import os
import random
import threading
import time
from datetime import datetime

from ..core.logger import logger
from ..core.config import SIMULATION_MODE, C2_COMMUNICATION_INTERVAL

class C2Server:
    """Simulierter Command & Control Server"""
    
    def __init__(self, port=8080):
        self.port = port
        self.running = False
        self.bots = {}  # Bot-ID -> Bot-Informationen
        self.commands = []  # Ausstehende Befehle
        self.server_thread = None
        self.admin_panel_url = f"https://c2-panel.example.com:{random.randint(10000, 60000)}/admin"
        logger.info(f"[+] C2Server initialisiert auf Port {self.port}")
    
    def execute(self):
        """Startet den simulierten C2-Server"""
        if not SIMULATION_MODE:
            logger.warning("[!] C2-Server im Nicht-Simulationsmodus deaktiviert")
            return False
        
        logger.info(f"[+] Starte C2-Server auf Port {self.port} (simuliert)")
        self.running = True
        
        # Starte den Server-Thread
        self.server_thread = threading.Thread(target=self._run_server)
        self.server_thread.daemon = True
        self.server_thread.start()
        
        # Erstelle ein paar simulierte Befehle
        self._generate_initial_commands()
        
        logger.info(f"[+] Admin-Panel verfügbar unter {self.admin_panel_url} (simuliert)")
        return True
    
    def _run_server(self):
        """Simuliert den laufenden C2-Server"""
        while self.running:
            try:
                # Simuliere einen Server-Tick
                self._simulate_server_tick()
                
                # Simuliere gelegentlich neue Befehle
                if random.random() > 0.8:  # 20% Chance pro Tick
                    self._generate_new_command()
                
                # Warte für das nächste Tick
                time.sleep(C2_COMMUNICATION_INTERVAL / 2)  # Server-Tick ist schneller als Client-Kommunikation
                
            except Exception as e:
                logger.error(f"[-] Fehler im C2-Server: {e} (simuliert)")
                time.sleep(C2_COMMUNICATION_INTERVAL)
    
    def _simulate_server_tick(self):
        """Simuliert einen Server-Tick (Bearbeitung von Bot-Verbindungen, Befehlsverteilung)"""
        # Simuliere neue Bot-Verbindungen
        self._simulate_new_bot_connections()
        
        # Simuliere Bot-Statusaktualisierungen
        self._simulate_bot_status_updates()
        
        # Simuliere Befehlsverteilung
        self._simulate_command_distribution()
        
        # Simuliere Datensammlung von Bots
        self._simulate_data_collection()
    
    def _simulate_new_bot_connections(self):
        """Simuliert neue Bot-Verbindungen"""
        # Mit einer gewissen Wahrscheinlichkeit verbinden sich neue Bots
        if random.random() > 0.9:  # 10% Chance pro Tick
            # Generiere eine zufällige Bot-ID
            bot_id = f"bot-{random.randint(10000, 99999)}"
            
            # Erstelle simulierte Botinformationen
            bot_info = {
                "id": bot_id,
                "ip": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
                "platform": random.choice(["Windows 10", "Windows 11", "Windows 7", "Linux", "macOS"]),
                "first_seen": datetime.now().isoformat(),
                "last_seen": datetime.now().isoformat(),
                "version": f"{random.randint(1, 3)}.{random.randint(0, 9)}",
                "status": "online",
                "capabilities": self._generate_bot_capabilities()
            }
            
            # Füge den Bot hinzu
            self.bots[bot_id] = bot_info
            logger.info(f"[+] Neuer Bot registriert: {bot_id} ({bot_info['ip']}, {bot_info['platform']}) (simuliert)")
    
    def _generate_bot_capabilities(self):
        """Generiert simulierte Bot-Fähigkeiten"""
        all_capabilities = ["ddos", "keylogger", "ransomware", "spam", "crypto_mining", "webcam", "update"]
        
        # Wähle eine zufällige Anzahl von Fähigkeiten
        num_capabilities = random.randint(2, len(all_capabilities))
        return random.sample(all_capabilities, num_capabilities)
    
    def _simulate_bot_status_updates(self):
        """Simuliert Statusaktualisierungen von Bots"""
        # Gehe durch alle registrierten Bots
        for bot_id, bot_info in list(self.bots.items()):
            # Simuliere manchmal Offline-Status
            if random.random() > 0.95:  # 5% Chance, dass ein Bot offline geht
                bot_info["status"] = "offline"
                logger.info(f"[+] Bot {bot_id} ist offline gegangen (simuliert)")
            elif bot_info["status"] == "offline" and random.random() > 0.7:  # 30% Chance, dass ein offline Bot wieder online kommt
                bot_info["status"] = "online"
                bot_info["last_seen"] = datetime.now().isoformat()
                logger.info(f"[+] Bot {bot_id} ist wieder online (simuliert)")
            elif bot_info["status"] == "online":
                # Aktualisiere last_seen für Online-Bots
                bot_info["last_seen"] = datetime.now().isoformat()
    
    def _simulate_command_distribution(self):
        """Simuliert die Verteilung von Befehlen an Bots"""
        # Prüfe, ob Befehle zur Verteilung vorhanden sind
        if not self.commands:
            return
        
        # Hole den nächsten Befehl
        command = self.commands[0]
        
        # Bestimme Ziel-Bots
        target_bots = []
        if command.get("target_type") == "all":
            # Befehl an alle aktiven Bots
            target_bots = [bot_id for bot_id, bot_info in self.bots.items() if bot_info["status"] == "online"]
        elif command.get("target_type") == "specific" and "target_bot_ids" in command:
            # Befehl an bestimmte Bots
            target_bots = [bot_id for bot_id in command["target_bot_ids"] if bot_id in self.bots and self.bots[bot_id]["status"] == "online"]
        elif command.get("target_type") == "capability" and "required_capability" in command:
            # Befehl an Bots mit bestimmter Fähigkeit
            capability = command["required_capability"]
            target_bots = [bot_id for bot_id, bot_info in self.bots.items() 
                          if bot_info["status"] == "online" and capability in bot_info["capabilities"]]
        
        # Wenn keine Ziel-Bots gefunden wurden, behalte den Befehl für später
        if not target_bots:
            logger.info(f"[+] Keine geeigneten Bots für Befehl {command['id']} gefunden, warte auf passende Bots (simuliert)")
            return
        
        # Entferne den Befehl aus der Warteschlange
        self.commands.pop(0)
        
        # Verteile den Befehl an die Ziel-Bots
        logger.info(f"[+] Sende Befehl {command['id']} ({command['type']}) an {len(target_bots)} Bots (simuliert)")
        
        # Simuliere die Befehlsausführung durch den Bot
        # In einer echten Implementierung würde der Befehl an die Bots gesendet werden
        # und die Ausführung würde auf Clientseite stattfinden
    
    def _simulate_data_collection(self):
        """Simuliert die Sammlung von Daten von Bots"""
        # Simuliere verschiedene Arten von Daten, die Bots senden könnten
        data_types = {
            "keylogger": {
                "probability": 0.1,  # 10% Chance pro Bot
                "generate": lambda: {
                    "keystrokes": "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ") for _ in range(random.randint(20, 50))),
                    "timestamp": datetime.now().isoformat()
                }
            },
            "screenshot": {
                "probability": 0.05,  # 5% Chance pro Bot
                "generate": lambda: {
                    "resolution": f"{random.choice([1920, 2560, 3440])}x{random.choice([1080, 1440, 2160])}",
                    "size_kb": random.randint(100, 5000),
                    "timestamp": datetime.now().isoformat()
                }
            },
            "stolen_data": {
                "probability": 0.03,  # 3% Chance pro Bot
                "generate": lambda: {
                    "type": random.choice(["credentials", "documents", "crypto_wallets"]),
                    "size_kb": random.randint(10, 1000),
                    "count": random.randint(1, 20),
                    "timestamp": datetime.now().isoformat()
                }
            }
        }
        
        # Gehe durch alle aktiven Bots
        for bot_id, bot_info in self.bots.items():
            if bot_info["status"] != "online":
                continue
            
            # Simuliere das Sammeln verschiedener Datentypen
            for data_type, config in data_types.items():
                if random.random() < config["probability"]:
                    data = config["generate"]()
                    logger.info(f"[+] Daten von Bot {bot_id} empfangen: {data_type} ({data}) (simuliert)")
    
    def _generate_initial_commands(self):
        """Generiert einige anfängliche Befehle für die Bot-Steuerung"""
        # Einige Beispielbefehle
        initial_commands = [
            {
                "id": f"cmd-{random.randint(1000, 9999)}",
                "type": "ddos",
                "target_type": "capability",
                "required_capability": "ddos",
                "target": "victim-website.example.com",
                "port": 80,
                "duration": 300,  # Sekunden
                "method": "http",
                "created": datetime.now().isoformat()
            },
            {
                "id": f"cmd-{random.randint(1000, 9999)}",
                "type": "update",
                "target_type": "all",
                "update_url": "http://update.example.com/bot/latest",
                "version": "2.1",
                "created": datetime.now().isoformat()
            },
            {
                "id": f"cmd-{random.randint(1000, 9999)}",
                "type": "exfil",
                "target_type": "capability",
                "required_capability": "keylogger",
                "target_dirs": ["Documents", "Desktop"],
                "file_types": [".doc", ".pdf", ".xls", ".txt"],
                "max_size_mb": 50,
                "created": datetime.now().isoformat()
            }
        ]
        
        self.commands.extend(initial_commands)
        logger.info(f"[+] {len(initial_commands)} anfängliche Befehle erstellt (simuliert)")
    
    def _generate_new_command(self):
        """Generiert einen neuen zufälligen Befehl"""
        command_types = ["ddos", "update", "scan", "exfil", "sleep"]
        target_types = ["all", "specific", "capability"]
        
        # Wähle einen zufälligen Befehlstyp
        command_type = random.choice(command_types)
        
        # Erstelle Basis-Befehl
        command = {
            "id": f"cmd-{random.randint(1000, 9999)}",
            "type": command_type,
            "target_type": random.choice(target_types),
            "created": datetime.now().isoformat()
        }
        
        # Füge befehlsspezifische Parameter hinzu
        if command_type == "ddos":
            command["target"] = f"target-{random.randint(1, 100)}.example.com"
            command["port"] = random.choice([80, 443, 53, 8080, 3306])
            command["duration"] = random.randint(60, 600)  # Sekunden
            command["method"] = random.choice(["tcp", "udp", "http", "icmp", "syn"])
            
            if command["target_type"] == "capability":
                command["required_capability"] = "ddos"
        
        elif command_type == "update":
            command["update_url"] = f"http://update.example.com/bot/{random.randint(1000, 9999)}"
            command["version"] = f"{random.randint(1, 5)}.{random.randint(0, 9)}"
        
        elif command_type == "scan":
            command["target_range"] = f"192.168.{random.randint(0, 255)}.0/24"
            command["port_range"] = f"{random.randint(1, 1000)}-{random.randint(1001, 10000)}"
            
            if command["target_type"] == "capability":
                command["required_capability"] = random.choice(["ddos", "update"])
        
        elif command_type == "exfil":
            command["target_dirs"] = ["Documents", "Desktop"]
            command["file_types"] = [".doc", ".pdf", ".xls", ".txt"]
            command["max_size_mb"] = random.randint(10, 100)
            
            if command["target_type"] == "capability":
                command["required_capability"] = random.choice(["keylogger", "ransomware"])
        
        elif command_type == "sleep":
            command["duration"] = random.randint(300, 3600)  # Sekunden
        
        # Wenn target_type 'specific' ist, wähle einige Bots aus
        if command["target_type"] == "specific":
            available_bots = list(self.bots.keys())
            if available_bots:
                num_bots = min(random.randint(1, 5), len(available_bots))
                command["target_bot_ids"] = random.sample(available_bots, num_bots)
            else:
                # Wenn keine Bots verfügbar sind, ändere auf 'all'
                command["target_type"] = "all"
        
        # Füge den Befehl zur Warteschlange hinzu
        self.commands.append(command)
        logger.info(f"[+] Neuer Befehl erstellt: {command['id']} ({command['type']}) (simuliert)")
    
    def add_command(self, command_type, target_type="all", **params):
        """Fügt einen benutzerdefinierten Befehl hinzu"""
        command = {
            "id": f"cmd-{random.randint(1000, 9999)}",
            "type": command_type,
            "target_type": target_type,
            "created": datetime.now().isoformat(),
            **params
        }
        
        self.commands.append(command)
        logger.info(f"[+] Benutzerdefinierter Befehl erstellt: {command['id']} ({command['type']}) (simuliert)")
        return command["id"]
    
    def get_bot_stats(self):
        """Gibt Statistiken über die verbundenen Bots zurück"""
        # Zähle Bots nach Status
        status_counts = {"online": 0, "offline": 0}
        for bot_info in self.bots.values():
            status = bot_info.get("status", "unknown")
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1
        
        # Zähle Bots nach Plattform
        platform_counts = {}
        for bot_info in self.bots.values():
            platform = bot_info.get("platform", "unknown")
            if platform in platform_counts:
                platform_counts[platform] += 1
            else:
                platform_counts[platform] = 1
        
        # Zähle Bots nach Fähigkeiten
        capability_counts = {}
        for bot_info in self.bots.values():
            for capability in bot_info.get("capabilities", []):
                if capability in capability_counts:
                    capability_counts[capability] += 1
                else:
                    capability_counts[capability] = 1
        
        return {
            "total_bots": len(self.bots),
            "status_counts": status_counts,
            "platform_counts": platform_counts,
            "capability_counts": capability_counts,
            "pending_commands": len(self.commands)
        }
    
    def stop(self):
        """Stoppt den C2-Server"""
        logger.info("[+] Stoppe C2-Server (simuliert)")
        self.running = False
        
        # Warte auf Server-Thread
        if self.server_thread and self.server_thread.is_alive():
            self.server_thread.join(timeout=1.0)
        
        logger.info("[+] C2-Server gestoppt (simuliert)")
        return True