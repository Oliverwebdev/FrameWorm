"""
System-Informationssammlung für das FrameWorm Framework
"""
import os
import sys
import socket
import random
import hashlib
import platform
import uuid
from datetime import datetime
from enum import Enum
from ..core.logger import logger

class InfectionStatus(Enum):
    """Enum zur Verfolgung des Infektionsstatus"""
    NOT_INFECTED = 0
    INFECTED = 1
    IMMUNE = 2

class SystemInfo:
    """Klasse zur Sammlung von System-Informationen (simuliert)"""
    
    @staticmethod
    def get_system_info():
        """Sammelt simulierte System-Informationen"""
        info = {
            "hostname": socket.gethostname(),
            "platform": platform.system(),
            "version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "id": str(uuid.uuid4()),  # Simulierte eindeutige ID
            "timestamp": datetime.now().isoformat(),
            "hardware_ids": {
                "cpu_id": hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest(),
                "motherboard_id": hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest(),
                "disk_id": hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest()
            },
            "network": {
                "interfaces": ["eth0", "wlan0", "bluetooth0"],
                "default_gateway": "192.168.1.1",
                "dns_servers": ["8.8.8.8", "1.1.1.1"]
            },
            "firmware": {
                "bios_version": f"{random.randint(1, 9)}.{random.randint(10, 99)}",
                "uefi_mode": random.choice([True, False]),
                "secure_boot": random.choice([True, False])
            },
            "virtualization_clues": []
        }
        return info
    
    @staticmethod
    def check_virtualization():
        """Prüft, ob das System in einer virtuellen Umgebung läuft (simuliert)"""
        logger.info("[+] Prüfe auf Virtualisierung (simuliert)")
        
        # Simuliere verschiedene Checks für Virtualisierung
        checks = {
            "cpu_features": random.choice([True, False]),
            "vm_specific_registry": random.choice([True, False]),
            "vm_services": random.choice([True, False]),
            "vm_devices": random.choice([True, False]),
            "timing_analysis": random.choice([True, False])  # CPU-Ausführungszeit-Analyse
        }
        
        # Protokolliere die Ergebnisse der einzelnen Checks
        for check_name, result in checks.items():
            if result:
                logger.info(f"[+] Virtualisierungs-Check '{check_name}' positiv (simuliert)")
            
        # Wenn mindestens zwei Checks positiv sind, betrachten wir es als virtualisiert
        is_virtualized = sum(checks.values()) >= 2
        
        if is_virtualized:
            logger.info("[+] Virtualisierung erkannt (simuliert)")
        else:
            logger.info("[+] Keine Virtualisierung erkannt (simuliert)")
            
        return is_virtualized
    
    @staticmethod
    def check_sandbox():
        """Prüft, ob das System in einer Sandbox läuft (simuliert)"""
        logger.info("[+] Prüfe auf Sandbox-Umgebung (simuliert)")
        
        # Simuliere verschiedene Anti-Sandbox-Techniken
        techniques = {
            "user_interaction": random.choice([True, False]),  # Fehlende Benutzerinteraktion
            "system_uptime": random.choice([True, False]),     # System erst kürzlich gestartet
            "hardware_profile": random.choice([True, False]),  # Verdächtige Hardware-Konfiguration
            "system_resources": random.choice([True, False]),  # Zu wenig RAM/CPU
            "process_list": random.choice([True, False])       # Analyse-Tools laufen
        }
        
        # Protokolliere die Ergebnisse der einzelnen Techniken
        for tech_name, result in techniques.items():
            if result:
                logger.info(f"[+] Sandbox-Indikator '{tech_name}' erkannt (simuliert)")
        
        # Wenn mindestens zwei Techniken positiv sind, betrachten wir es als Sandbox
        is_sandbox = sum(techniques.values()) >= 2
        
        if is_sandbox:
            logger.info("[+] Sandbox-Umgebung erkannt (simuliert)")
        else:
            logger.info("[+] Keine Sandbox-Umgebung erkannt (simuliert)")
            
        return is_sandbox
    
    @staticmethod
    def check_analysis_tools():
        """Prüft, ob Analyse-Tools auf dem System laufen (simuliert)"""
        logger.info("[+] Prüfe auf laufende Analyse-Tools (simuliert)")
        
        # Simuliere die Erkennung verschiedener Analyse-Tools
        analysis_tools = [
            "Process Explorer", "Wireshark", "IDA Pro", "OllyDbg", 
            "Process Monitor", "Ghidra", "Debugger", "Sysinternals",
            "API Monitor", "Cuckoo Sandbox"
        ]
        
        # Simuliere, dass einige Tools erkannt werden
        detected_tools = []
        for tool in analysis_tools:
            if random.random() > 0.7:  # 30% Chance, ein Tool zu "erkennen"
                detected_tools.append(tool)
                logger.info(f"[+] Analyse-Tool erkannt: {tool} (simuliert)")
        
        return detected_tools
    
    @staticmethod
    def get_connected_devices():
        """Gibt eine Liste simulierter angeschlossener Geräte zurück"""
        devices = []
        
        # Simuliere verschiedene USB-Geräte
        usb_devices = [
            {"type": "storage", "name": "USB Stick", "size": "32GB"},
            {"type": "storage", "name": "External HDD", "size": "1TB"},
            {"type": "hid", "name": "Keyboard", "manufacturer": "Logitech"},
            {"type": "hid", "name": "Mouse", "manufacturer": "Microsoft"},
            {"type": "audio", "name": "Headset", "manufacturer": "Sennheiser"},
            {"type": "camera", "name": "Webcam", "manufacturer": "Logitech"}
        ]
        
        # Wähle zufällig 2-4 USB-Geräte aus
        num_usb = random.randint(2, 4)
        selected_usb = random.sample(usb_devices, num_usb)
        devices.extend(selected_usb)
        
        # Simuliere Bluetooth-Geräte
        bt_devices = [
            {"type": "audio", "name": "BT Speaker", "address": "00:11:22:33:44:55"},
            {"type": "audio", "name": "BT Headset", "address": "AA:BB:CC:DD:EE:FF"},
            {"type": "input", "name": "BT Keyboard", "address": "11:22:33:44:55:66"},
            {"type": "phone", "name": "Smartphone", "address": "22:33:44:55:66:77"}
        ]
        
        # Wähle zufällig 0-2 Bluetooth-Geräte aus
        num_bt = random.randint(0, 2)
        if num_bt > 0:
            selected_bt = random.sample(bt_devices, num_bt)
            devices.extend(selected_bt)
        
        logger.info(f"[+] {len(devices)} verbundene Geräte erkannt (simuliert)")
        return devices