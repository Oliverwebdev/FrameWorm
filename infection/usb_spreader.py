"""
USB-basierte Infektionsmechanismen
"""
import os
import random
import threading
import time
from datetime import datetime

from ..core.logger import logger
from ..core.config import SIMULATION_MODE
from ..utils.system_info import SystemInfo

class USBSpreader:
    """Klasse zur Verbreitung über USB-Geräte"""
    
    def __init__(self):
        self.running = False
        self.infected_devices = []
        self.monitoring_thread = None
        logger.info("[+] USBSpreader initialisiert")
    
    def execute(self):
        """Startet die USB-Überwachung und Infektion"""
        self.running = True
        logger.info("[+] USBSpreader gestartet")
        
        # Starte den Überwachungs-Thread
        self.monitoring_thread = threading.Thread(target=self._monitor_usb_devices)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()
        
        return True
    
    def _monitor_usb_devices(self):
        """Kontinuierliche Überwachung von USB-Geräten"""
        last_devices = []
        
        while self.running:
            try:
                # Simuliere das Sammeln aktuell angeschlossener Geräte
                current_devices = SystemInfo.get_connected_devices()
                
                # Identifiziere neu angeschlossene Geräte
                new_devices = [d for d in current_devices if d not in last_devices]
                
                # Verarbeite neue Geräte
                for device in new_devices:
                    self._process_new_device(device)
                
                # Aktualisiere Geräteliste für den nächsten Durchlauf
                last_devices = current_devices.copy()
                
                # Kurze Pause zwischen den Überprüfungen
                time.sleep(2)
                
            except Exception as e:
                logger.error(f"[-] Fehler bei der USB-Überwachung: {e}")
                time.sleep(5)
    
    def _process_new_device(self, device):
        """Verarbeitet ein neu angeschlossenes USB-Gerät"""
        device_type = device.get("type", "unknown")
        device_name = device.get("name", "Unbekanntes Gerät")
        
        logger.info(f"[+] Neues USB-Gerät erkannt: {device_name} (Typ: {device_type})")
        
        if SIMULATION_MODE:
            # Überprüfe, ob das Gerät für Infektion geeignet ist
            if device_type == "storage":
                # Simuliere Infektion eines Speichergeräts
                success = self._infect_storage_device(device)
                if success:
                    self.infected_devices.append(device)
            elif device_type == "hid":
                # Für HID-Geräte (Tastatur/Maus) andere Techniken
                logger.info(f"[+] HID-Gerät erkannt, nutze HID-spezifische Techniken (simuliert)")
                # Hier könnte HID-spezifischer Code stehen
        else:
            logger.warning(f"[!] Echte Infektionen sind deaktiviert. Setze SIMULATION_MODE=True in config.py")
    
    def _infect_storage_device(self, device):
        """Simuliert die Infektion eines USB-Speichergeräts"""
        device_name = device.get("name", "Unbekanntes Gerät")
        logger.info(f"[+] Simuliere Infektion von USB-Speichergerät: {device_name}")
        
        # Simuliere Autorun.inf-Erstellung
        logger.info(f"[+] Erstelle Autorun.inf auf {device_name} (simuliert)")
        
        # Simuliere Kopieren des Payloads
        logger.info(f"[+] Kopiere Payload auf {device_name} (simuliert)")
        
        # Simuliere Verstecken der Dateien
        logger.info(f"[+] Verstecke Infektionsdateien auf {device_name} (simuliert)")
        
        # Simuliere zufälligen Erfolg/Misserfolg
        success = random.random() > 0.2  # 80% Erfolgswahrscheinlichkeit
        
        if success:
            logger.info(f"[+] Infektion von {device_name} erfolgreich (simuliert)")
        else:
            logger.info(f"[-] Infektion von {device_name} fehlgeschlagen (simuliert)")
        
        return success
    
    def stop(self):
        """Stoppt den USB-Spreader"""
        self.running = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=1.0)
        logger.info("[-] USBSpreader gestoppt")