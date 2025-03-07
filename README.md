# FrameWorm Framework

[![Simuliertes Framework](https://img.shields.io/badge/Framework-Simulation-blue)](https://github.com/yourusername/FrameWorm)
[![Nur für Bildung](https://img.shields.io/badge/Zweck-Bildung%20%26%20Forschung-green)](https://github.com/yourusername/FrameWorm)
[![Keine reale Infektion](https://img.shields.io/badge/Funktion-Simulation-orange)](https://github.com/yourusername/FrameWorm)

**WICHTIGER HINWEIS**: Dieses Framework ist ausschließlich für Bildungs- und Forschungszwecke konzipiert. Es führt KEINE realen schädlichen Operationen aus, sondern simuliert lediglich das Verhalten von Malware in einer kontrollierten Umgebung.


=== Malware Simulation Framework ===
=== NUR FÜR BILDUNGS- UND FORSCHUNGSZWECKE ===
=== ALLE AKTIONEN WERDEN NUR SIMULIERT ===
```

## Überblick

Das FrameWorm Framework ist ein modular aufgebautes Malware-Simulationssystem, das entwickelt wurde, um die Funktionsweise moderner Malware zu studieren und zu verstehen. Es ermöglicht das Erforschen verschiedener Infektions-, Persistenz-, Evasions- und Command & Control-Techniken in einer sicheren Umgebung, ohne tatsächlichen Schaden zu verursachen.

Alle Funktionen werden lediglich simuliert und protokolliert, ohne tatsächliche schädliche Aktionen durchzuführen. Das Framework läuft standardmäßig im `SIMULATION_MODE`, was sicherstellt, dass keine echten Systeme gefährdet werden.

## Hauptmerkmale

- **Modular**: Verschiedene Komponenten können unabhängig voneinander aktiviert und kombiniert werden
- **Bildungszweck**: Demonstriert Techniken moderner Malware für Sicherheitsspezialisten, Forscher und Studierende
- **Simulationsmodus**: Führt keine realen schädlichen Aktionen aus, sondern simuliert und protokolliert nur das Verhalten
- **Erweiterbar**: Kann um neue Module und Techniken erweitert werden
- **Protokollierung**: Detaillierte Logs aller (simulierten) Aktivitäten

## Komponenten/Module

### Core

- **MasterOrchestrator (`core/worm.py`)**: Zentrale Steuerungslogik, die alle Module koordiniert
- **Konfiguration (`core/config.py`)**: Einstellungen für das Framework
- **Logger (`core/logger.py`)**: Protokollierungssystem

### Infektion

- **NetworkWorm (`infection/network_spreader.py`)**: Simuliert netzwerkbasierte Verbreitung
- **USBSpreader (`infection/usb_spreader.py`)**: Simuliert Verbreitung über USB-Medien
- **PhishingAttack (`infection/phishing.py`)**: Simuliert Phishing-Angriffe

### Command & Control

- **C2Server (`command_control/c2_server.py`)**: Simuliert einen Command & Control Server
- **P2PCommunication (`command_control/peer2peer.py`)**: Simuliert dezentrales P2P-Netzwerk
- **SteganographyModule (`command_control/steganography.py`)**: Simuliert verdeckte Kommunikation mittels Steganographie

### Evasion

- **SandboxDetector (`evasion/sandbox_detection.py`)**: Techniken zur Erkennung von Analyseumgebungen
- **CodeObfuscator (`evasion/obfuscation.py`)**: Simuliert Code-Verschleierung
- **AVBypass (`evasion/av_bypass.py`)**: Simuliert Techniken zur Umgehung von Antivirenlösungen
- **VulnerabilityExploiter (`evasion/vulnerability_exploiter.py`)**: Simuliert das Ausnutzen von Schwachstellen

### Payloads

- **KeyloggerPayload (`payloads/keylogger.py`)**: Simuliert einen Keylogger
- **RansomwarePayload (`payloads/ransomware.py`)**: Simuliert einen Ransomware-Angriff
- **BotnetClient (`payloads/botnet.py`)**: Simuliert einen Botnet-Client

### Utilities

- **SystemInfo (`utils/system_info.py`)**: Sammelt (simuliert) Systeminformationen
- **EncryptionModule (`utils/crypto.py`)**: Kryptographie-Funktionen für simulierte Verschlüsselung

## Installation

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/yourusername/FrameWorm.git
   cd FrameWorm
   ```

2. Stellen Sie sicher, dass Python 3.6+ installiert ist.

3. Installieren Sie die eventuell benötigten Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

### Grundlegende Ausführung

Um das Framework mit den Standardmodulen zu starten:

```bash
python main.py
```

### Ausführung mit spezifischen Modulen

Sie können spezifische Module beim Start angeben:

```bash
python main.py --modules network keylogger c2
```

### Verfügbare Befehlszeilenoptionen

```
-m, --modules   Module zum Laden (z.B. 'network usb')
-s, --simulate  Simulationsmodus aktivieren (Standard: aktiviert)
-v, --verbose   Ausführliche Protokollierung
```

### Beispiele

1. Starten des Frameworks mit Netzwerk- und USB-Verbreitung:
   ```bash
   python main.py --modules network usb
   ```

2. Starten des Frameworks mit Ransomware-Simulation:
   ```bash
   python main.py --modules ransomware
   ```

3. Starten des Frameworks mit C2-Server und Botnet-Client:
   ```bash
   python main.py --modules c2 botnet
   ```

## Konfiguration

Die Hauptkonfiguration erfolgt in der Datei `core/config.py`. Hier können Sie verschiedene Parameter anpassen:

- `SIMULATION_MODE`: Sollte immer auf `True` gesetzt sein, um sicherzustellen, dass keine echten Infektionen stattfinden
- `LOG_LEVEL`: Protokollierungsebene (DEBUG, INFO, WARNING, ERROR)
- `DEFAULT_SUBNET`: Standard-Subnetz für Netzwerk-Scans
- `C2_COMMUNICATION_INTERVAL`: Kommunikationsintervall in Sekunden
- `MAX_INFECTION_TARGETS`: Maximale Anzahl gleichzeitiger Infektionsziele

## Struktur der Ausgaben

Das Framework erzeugt detaillierte Protokolle aller simulierten Aktivitäten. Diese werden sowohl in der Konsole angezeigt als auch in der Datei `worm_simulator.log` gespeichert.

Beispielausgabe:
```
[+] Initialisiere Master-Orchestrator
[+] System erkannt: Windows 10.0.19042
[+] Hostname: DESKTOP-ABC123
[+] Architektur: AMD64
[+] Lade Standardmodule...
[+] Modul hinzugefügt: Network
[+] Modul hinzugefügt: Keylogger
[+] Modul hinzugefügt: Sandbox Detection
[+] Starte Master-Orchestrator
[+] Ausführung im Simulationsmodus - Keine echte Infektion
[+] Starte Modul: Network
[+] Starte Modul: Keylogger
[+] Starte Modul: Sandbox Detection
[+] Framework läuft. Drücken Sie Ctrl+C zum Beenden.
```

## Sicherheitshinweise

- **Nutzungszweck**: Dieses Framework ist ausschließlich für Bildungs- und Forschungszwecke konzipiert.
- **Simulationsmodus**: Alle Operationen werden simuliert, keine echten schädlichen Aktionen werden ausgeführt.
- **Verantwortung**: Der Einsatz dieser Techniken gegen reale Systeme ohne Erlaubnis ist illegal und unethisch.
- **Lehrzweck**: Ziel ist es, Sicherheitsexperten zu schulen und ihnen zu helfen, Bedrohungen besser zu verstehen.
- **Keine reale Infektion**: Dieses Framework führt keine echten Infektionen durch, sondern protokolliert nur, was in einer realen Infektion passieren würde.

## Best Practices

1. **Ausführungsumgebung**: Führen Sie das Framework idealerweise in einer isolierten Umgebung (z.B. virtuelle Maschine) aus, obwohl es nur simuliert.
2. **Simulationsmodus**: Vergewissern Sie sich, dass der `SIMULATION_MODE` in der Konfigurationsdatei immer auf `True` gesetzt ist.
3. **Ethischer Einsatz**: Nutzen Sie die gewonnenen Kenntnisse nur zu defensiven und bildungsbezogenen Zwecken.
4. **Code-Überprüfung**: Wenn Sie eigene Module hinzufügen, stellen Sie sicher, dass diese ebenfalls nur simulieren und keine realen Aktionen ausführen.

## Erweiterung des Frameworks

Um neue Module hinzuzufügen:

1. Erstellen Sie eine neue Python-Datei im entsprechenden Verzeichnis (z.B. `infection/`, `evasion/`, `payloads/`).
2. Implementieren Sie eine Klasse mit mindestens einer `execute()`-Methode.
3. Achten Sie darauf, dass alle Aktionen nur simuliert werden (`SIMULATION_MODE` beachten).
4. Registrieren Sie das neue Modul im `main.py` skript.

## Häufige Fragen

**F: Ist dieses Framework gefährlich?**  
A: Nein. Das Framework simuliert nur das Verhalten von Malware und führt keine realen schädlichen Aktionen aus.

**F: Kann ich es für Pentests nutzen?**  
A: Das Framework ist für Bildungszwecke konzipiert. Für professionelle Penetrationstests sollten spezialisierte und lizenzierte Tools verwendet werden.

**F: Werden reale Dateien verschlüsselt oder Systeme infiziert?**  
A: Nein. Alle Aktionen werden nur simuliert und protokolliert. Es findet keine tatsächliche Verschlüsselung oder Infektion statt.

**F: Kann ich eigene Module hinzufügen?**  
A: Ja, das Framework ist modular aufgebaut und kann um eigene Module erweitert werden.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

## Haftungsausschluss

Dieses Tool ist nur für Bildungs- und Forschungszwecke gedacht. Der Missbrauch dieses Tools für böswillige Zwecke ist illegal und unethisch. Der Autor übernimmt keine Verantwortung für Schäden, die durch den Missbrauch dieses Frameworks entstehen könnten.

---

*Hinweis: Dieses Framework ist ein Simulationstool und führt keine realen Malware-Aktionen aus.*