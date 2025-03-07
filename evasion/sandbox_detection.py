"""
Sandbox-Erkennungstechniken
"""
import os
import random
import platform
import time
from datetime import datetime

from ..core.logger import logger
from ..utils.system_info import SystemInfo

class SandboxDetector:
    """Klasse zur Erkennung von Sandbox-/Analyseumgebungen"""
    
    def __init__(self):
        self.detection_results = {}
        logger.info("[+] SandboxDetector initialisiert")
    
    def execute(self):
        """Führt alle Erkennungsmethoden aus"""
        logger.info("[+] Führe Sandbox-Erkennung aus")
        
        # Führe verschiedene Sandbox-Erkennungstechniken aus
        self.detection_results["virtualization"] = SystemInfo.check_virtualization()
        self.detection_results["sandbox"] = SystemInfo.check_sandbox()
        self.detection_results["analysis_tools"] = len(SystemInfo.check_analysis_tools()) > 0
        
        # Zusätzliche Erkennungsmethoden
        self.detection_results["sleep_acceleration"] = self._check_sleep_acceleration()
        self.detection_results["mouse_movement"] = self._check_mouse_movement()
        self.detection_results["memory_size"] = self._check_memory_size()
        
        # Auswertung der Ergebnisse
        detected = sum(1 for result in self.detection_results.values() if result)
        total = len(self.detection_results)
        
        detection_ratio = detected / total if total > 0 else 0
        is_sandbox = detection_ratio > 0.4  # Wenn mehr als 40% der Checks positiv sind
        
        logger.info(f"[+] Sandbox-Erkennung abgeschlossen: {detected}/{total} Indikatoren erkannt")
        logger.info(f"[+] Sandbox-Erkennung Ergebnis: {'Sandbox erkannt' if is_sandbox else 'Keine Sandbox erkannt'}")
        
        return is_sandbox
    
    def is_running_in_sandbox(self):
        """Prüft, ob die Anwendung in einer Sandbox läuft"""
        # Falls noch keine Erkennungen durchgeführt wurden, führe sie aus
        if not self.detection_results:
            return self.execute()
        
        # Auswertung der Ergebnisse
        detected = sum(1 for result in self.detection_results.values() if result)
        total = len(self.detection_results)
        
        detection_ratio = detected / total if total > 0 else 0
        return detection_ratio > 0.4  # Wenn mehr als 40% der Checks positiv sind
    
    def _check_sleep_acceleration(self):
        """Überprüft, ob Sleep-Funktionen beschleunigt werden (Indikator für Sandbox)"""
        logger.info("[+] Prüfe auf Sleep-Beschleunigung (simuliert)")
        
        # Startzeit merken
        start_time = time.time()
        
        # Eine kurze Pause machen
        time.sleep(2)
        
        # Endzeit berechnen
        elapsed = time.time() - start_time
        
        # Wenn deutlich weniger als 2 Sekunden vergangen sind, wurde Sleep beschleunigt
        is_accelerated = elapsed < 1.8
        
        if is_accelerated:
            logger.info("[+] Sleep-Beschleunigung erkannt (simuliert)")
        else:
            logger.info("[+] Keine Sleep-Beschleunigung erkannt (simuliert)")
        
        return is_accelerated
    
    def _check_mouse_movement(self):
        """Überprüft, ob Mausbewegungen erkannt werden (Sandboxes haben oft keine)"""
        logger.info("[+] Prüfe auf Mausbewegungen (simuliert)")
        
        # In einer echten Implementierung würde man tatsächliche Mausbewegungen überprüfen
        # Hier simulieren wir das Ergebnis
        has_mouse_movement = random.random() > 0.7  # 30% Chance, keine Mausbewegung zu "erkennen"
        
        if has_mouse_movement:
            logger.info("[+] Mausbewegungen erkannt (simuliert)")
        else:
            logger.info("[+] Keine Mausbewegungen erkannt (simuliert)")
        
        return not has_mouse_movement  # Keine Mausbewegung ist ein Indikator für Sandbox
    
    def _check_memory_size(self):
        """Überprüft, ob der verfügbare Speicher typisch für eine Sandbox ist"""
        logger.info("[+] Prüfe auf verdächtige Speichergröße (simuliert)")
        
        # In einer echten Implementierung würde man den tatsächlichen Speicher überprüfen
        # Hier simulieren wir das Ergebnis
        memory_size_gb = random.uniform(1.0, 8.0)  # Simulierte Speichergröße in GB
        
        # Typischerweise haben Sandboxes weniger Speicher
        is_suspicious = memory_size_gb < 2.0
        
        logger.info(f"[+] Speichergröße: {memory_size_gb:.2f} GB (simuliert)")
        if is_suspicious:
            logger.info("[+] Verdächtig niedrige Speichergröße erkannt (simuliert)")
        else:
            logger.info("[+] Speichergröße erscheint normal (simuliert)")
        
        return is_suspicious