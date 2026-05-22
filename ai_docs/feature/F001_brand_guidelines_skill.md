# F001 — Brand-Guidelines-Skill für Gollnick Data

**Status:** Geplant
**Erstellt:** 2026-05-20

## Kontext und Problemstellung

Für Gollnick Data Solutions sollen konsistente Brand-Guidelines jederzeit abrufbar sein. Aktuell existiert kein automatisierter Prozess, um auf Basis der Website-Inhalte strukturierte Vorgaben (Mission, Tone of Voice, Farbwelt, Bildsprache, Produkt-Portfolio, Logo-Regeln) zu erzeugen. Das neue Skill soll diese Informationen in streng formatiertem Markdown bündeln, damit Designer:innen und Autor:innen schnell verbindliche Leitplanken erhalten.

## Anforderungen

### Funktional
- Skill verarbeitet Eingaben des/der Nutzer:in und erzeugt immer ein Markdown-Dokument mit festen Kapiteln (Mission, Tone of Voice, Farbwelt & Typografie, Bildsprache, Produktspektrum, Logo Usage, ggf. weitere definierte Abschnitte).
- Standard-Ausgabe auf Deutsch; das Skill akzeptiert explizite Sprachwechsel, bleibt sonst deutsch.
- Farb- und Typografieabschnitt enthält konkrete Hex-Codes (#1e2328, #222535, #2a2530, #2c2c54, #c05c37/#bf5c36, #f7f5f9, #faf8f6, #fff500, #e5e2e3) sowie die Fonts Roboto (UI/Text) und Lora (Headlines/Zitate) mit Hinweisen zu Verwendung.
- Tone-of-Voice-Abschnitt beschreibt Claim „Deine KI-Zukunft, trainiert von uns“, liefert Do’s & Don’ts und Anwendungsbeispiele (z. B. Newsletter, Kursseite, Social Copy falls angefordert).
- Bildsprache-Abschnitt erklärt Motivwelt (Tech-/Lern-Kontexte, Portraits, warme Farbübergänge, Vertrauen & Expertise) inklusive Vorgaben zu Licht, Komposition, Icon-Stil.
- Produktspektrum-Abschnitt nennt die Hauptangebote (Bildungsurlaubkurse, AZAV-/BILDUNGSGUTSCHEIN-Programme, Bücher, Onlinekurse, Consulting) mit kurzen Beschreibungen und typischen Kennzahlen (z. B. 5 Tage / 40 UE remote).
- Logo Usage liefert feste Regeln (Primärlogo auf Weiß oder sehr helle Hintergründe, Negativversion auf #1e2328/#2a2530, Mindestschutzraum = 1× Höhe des Schriftzugs, keine Platzierung auf Verlauf, kein Verzerren/Drehen, Skalierungsgrenzen für Digital/Print).
- Skill bezieht bei Bedarf aktuelle Inhalte (z. B. Kursnamen, Testimonials) per Webfetch/Recherche, sofern erreichbar, und fällt ansonsten auf hinterlegte Defaults zurück.
- Ergebnis enthält optional einen Abschnitt „Verbote“ (Farben/Tone-of-Voice-Verfehlungen) wenn vom Input gefordert.

### Nicht-funktional
- Strikte Einhaltung des strukturierten Markdown-Templates (Überschriften-Hierarchie, Tabellen falls definiert).
- Quellenangabe bzw. Hinweis, falls Informationen automatisch von gollnickdata.de bezogen wurden.
- Ausgaben sollen deterministisch sein: gleiche Eingabe ⇒ gleiches Layout & Reihenfolge.
- Skill darf nur die im Brief genannten Farben/Fonts als verbindlich markieren; Erweiterungen nur nach expliziter Nutzeranfrage.

## Akzeptanzkriterien

- [ ] Ausgabe erfolgt standardmäßig vollständig auf Deutsch, es sei denn, der Prompt fordert eine andere Sprache.
- [ ] Jede Response enthält alle Pflichtkapitel (Tone of Voice, Bildsprache, Produktspektrum, Logo Usage, Farb- & Typografie-Regeln) und füllt sie mit Inhalten.
- [ ] Farb- und Typografie-Abschnitt listet mindestens die Hex-Werte #1e2328, #222535, #2a2530, #2c2c54, #c05c37 (bzw. #bf5c36), #f7f5f9, #faf8f6 und #fff500 sowie die Fonts Roboto & Lora samt Einsatzempfehlung.
- [ ] Tone-of-Voice-Kapitel enthält Claim „Deine KI-Zukunft, trainiert von uns“ plus mindestens drei Do’s und drei Don’ts.
- [ ] Produktspektrum führt die wichtigsten Kurs/Dienstleistungs-Kategorien inklusive kurzer Beschreibungen der Formate (z. B. 5 Tage / 40 UE, Remote, Bildungsurlaub) auf.
- [ ] Logo Usage beschreibt Mindestschutzraum, erlaubte Hintergründe und verbotene Anwendungen.
- [ ] Wenn Webdaten nicht erreichbar sind, weist das Skill darauf hin und nutzt definierte Default-Werte.

## Definition of Done

- [ ] Skillordner (z. B. `.opencode/skills/brand-guidelines`) angelegt und SKILL.md fertiggestellt.
- [ ] Alle referenzierten Ressourcen (z. B. Farb-/Fonttabellen, Beispiel-Markdown-Template) im Skill-Verzeichnis vorhanden.
- [ ] Beispiel-Evals (mind. zwei) erstellt und dokumentiert.
- [ ] Tests/Evals ausgeführt und dokumentierte Ergebnisse vorhanden.
- [ ] README bzw. Hinweis im Repo aktualisiert (falls nötig) und Nutzer informiert.
- [ ] Manuelle Stichprobe einer Skill-Ausgabe geprüft.

## Betroffene Bereiche im Code

- `.opencode/skills/brand-guidelines/` — neues Skill mit SKILL.md, ggf. Referenzdateien.
- `ai_docs/` — enthält dieses Planungsdokument; keine weiteren Änderungen geplant.
- (Optional) `scripts/` oder Hilfsdateien, falls Helper-Skripte für Farbtabellen benötigt werden *(zu verifizieren)*.

## Umsetzungshinweise (optional)

- Mögliches Template für jede Response vorbereiten (Markdown mit H2/H3-Struktur, Tabellen für Farben/Typografie). 
- Farbwerte und Fonts direkt im Skill als Konstanten hinterlegen, inklusive Beschreibungen (Primär, Sekundär, Akzent, Neutrals). 
- Tone-of-Voice-Do’s/Don’ts aus Website-Tonalität ableiten (freundlich, kompetent, praxisnah, keine Buzzword-Inflation). 
- Logo-Regeln anhand des SVGs und Manifest-Farben präzisieren; ggf. Mindestgröße Digital (120 px Breite) und Print (25 mm) definieren.

## Out of Scope

- Automatisierte Generierung von visuellen Assets (Mockups, Logos, Templates).
- Dynamische Aktualisierung per API (Skill arbeitet auf statisch hinterlegten + optional live abgefragten Daten, aber ohne Persistenz).
- Vollständige Social-Media-Guidelines (nur falls explizit angefordert, sonst nicht Bestandteil).

## Abhängigkeiten

- Zugriff auf die öffentliche Website https://www.gollnickdata.de/ für aktuelle Inhalte.
- Bestehende Skill-Infrastruktur (.opencode/skills/, Eval-Tools). Keine weiteren externen Libs geplant.

## Risiken

- Website-Inhalte können sich ändern → regelmäßige Aktualisierung der Defaults nötig.
- Fehlende offiziellen Angaben zu Logo-Schutzraum/Mindestgrößen könnten zu Annahmen führen; Nutzer-Validierung notwendig.
- Strikte Regeln können für ungeplante Use Cases zu unflexibel sein; ggf. Erweiterungsmechanismus nötig.

## Offene Fragen

- [ ] Gibt es offizielle Vorgaben für Schutzraum/Mindestgröße des Logos oder müssen wir Annahmen treffen?
- [ ] Sollen Social-Media-spezifische Textregeln integriert werden oder bleiben sie außen vor?
- [ ] Gibt es interne Dateien (z. B. PDFs) mit detaillierteren Farb-/Typo-Spezifikationen, die eingebunden werden sollen?
