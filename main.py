#!/usr/bin/env python3
"""
FrameWorm Framework - Ein modulares Malware-Simulationsframework

Wichtiger Hinweis: Dieses Framework ist rein für Forschungs- und Bildungszwecke.
Es dient zur Analyse und zum Verständnis moderner Malware-Techniken in einer
kontrollierten Umgebung ohne tatsächliche Schadfunktionalität.

KEINE der Funktionen in diesem Framework führt tatsächliche schädliche Aktionen aus -
alle Aktivitäten werden nur simuliert und protokolliert.
"""

import os
import sys
import time
import argparse
from datetime import datetime

# Füge das Hauptverzeichnis dem Python-Pfad hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importe aus dem Framework
from FrameWorm.core.logger import logger
from FrameWorm.core.worm import MasterOrchestrator
from FrameWorm.core.config import SIMULATION_MODE

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="FrameWorm - Malware Simulation Framework")
    parser.add_argument("-m", "--modules", nargs="+", help="Module zum Laden (z.B. 'network usb')")
    parser.add_argument("-s", "--simulate", action="store_true", help="Simulationsmodus aktivieren")
    parser.add_argument("-v", "--verbose", action="store_true", help="Ausführliche Protokollierung")
    return parser.parse_args()

def print_banner():
    """Print the framework banner"""
    banner = """
    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ███╗   ███╗
    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗████╗ ████║
    █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝██╔████╔██║
    ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██║╚██╔╝██║
    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
    
    === Malware Simulation Framework ===
    === NUR FÜR BILDUNGS- UND FORSCHUNGSZWECKE ===
    === ALLE AKTIONEN WERDEN NUR SIMULIERT ===
    
    Ausführungszeitpunkt: {datetime}
    Simulationsmodus: {simulation}
    """
    
    print(banner.format(
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        simulation="AKTIV" if SIMULATION_MODE else "INAKTIV"
    ))

def main():
    """Main function to run the framework"""
    args = parse_arguments()
    print_banner()
    
    # Initialisiere den Master-Orchestrator
    orchestrator = MasterOrchestrator()
    
    # Lade Module basierend auf Befehlszeilenargumenten
    if args.modules:
        for module_name in args.modules:
            if module_name.lower() == "network":
                from FrameWorm.infection.network_spreader import NetworkWorm
                orchestrator.add_module("Network", NetworkWorm())
            elif module_name.lower() == "usb":
                from FrameWorm.infection.usb_spreader import USBSpreader
                orchestrator.add_module("USB", USBSpreader())
            elif module_name.lower() == "keylogger":
                from FrameWorm.payloads.keylogger import KeyloggerPayload
                orchestrator.add_module("Keylogger", KeyloggerPayload())
            elif module_name.lower() == "ransomware":
                from FrameWorm.payloads.ransomware import RansomwarePayload
                orchestrator.add_module("Ransomware", RansomwarePayload())
            elif module_name.lower() == "c2":
                from FrameWorm.command_control.c2_server import C2Server
                orchestrator.add_module("C2", C2Server())
    else:
        # Standardmodule laden
        logger.info("[+] Lade Standardmodule...")
        from FrameWorm.infection.network_spreader import NetworkWorm
        from FrameWorm.payloads.keylogger import KeyloggerPayload
        from FrameWorm.evasion.sandbox_detection import SandboxDetector
        
        orchestrator.add_module("Network", NetworkWorm())
        orchestrator.add_module("Keylogger", KeyloggerPayload())
        orchestrator.add_module("Sandbox Detection", SandboxDetector())
    
    # Starte den Orchestrator
    try:
        orchestrator.execute()
        
        # Warte eine Weile, damit die Threads starten können
        time.sleep(2)
        
        # Adaptive Strategie anwenden
        orchestrator.adapt_strategy()
        
        # Simuliere laufende Aktivität
        logger.info("[+] Framework läuft. Drücken Sie Ctrl+C zum Beenden.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("[-] Benutzerabbruch erkannt. Fahre Framework herunter...")
        orchestrator.shutdown()
    except Exception as e:
        logger.error(f"[-] Unerwarteter Fehler: {e}")
        orchestrator.shutdown()

if __name__ == "__main__":
    main()