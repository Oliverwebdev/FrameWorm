"""
Konfigurationsdatei für das FrameWorm Framework
"""

# Simulationseinstellungen
SIMULATION_MODE = True  # True = Sandbox-Modus ohne echte Infektion
LOG_LEVEL = "INFO"      # Logging-Level (DEBUG, INFO, WARNING, ERROR)

# Netzwerk-Konfiguration
DEFAULT_SUBNET = "192.168.1.0/24"  # Standard-Subnetz für Netzwerk-Scans
SCAN_TIMEOUT = 1.0                 # Timeout für Netzwerk-Scans in Sekunden

# Evasion-Konfiguration
SANDBOX_DETECTION_ENABLED = True   # Erkennung von Sandbox-Umgebungen
ANTI_VM_CHECKS_ENABLED = True      # Erkennung von virtuellen Maschinen
ANTI_ANALYSIS_ENABLED = True       # Anti-Analyse-Techniken

# Payload-Konfiguration 
DEFAULT_ENCRYPTION_STRENGTH = 256  # Stärke der Verschlüsselung in Bits

# Command & Control Konfiguration
C2_COMMUNICATION_INTERVAL = 60     # Kommunikationsintervall in Sekunden
STEALTH_MODE = True                # Aktivierung des Stealth-Modus

# Verbreitungseinstellungen
MAX_INFECTION_TARGETS = 10         # Maximale Anzahl gleichzeitiger Infektionsziele