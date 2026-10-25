# Kantine nettside

Dette er en nettside for skolekantina på Akademiet, laget med Flask.

## Sidene

- Hjem: velkomsttekst og lenker til de andre sidene.
- Meny: ukens meny fra mandag til fredag.
- Varer: faste varer med bilde, navn og pris.
- Kontakt: telefon, e-post og åpningstider.

## Om koden

I app.py har jeg en rute for hver side. Menyen og varene ligger som lister i kantinedata.py og vises med for-løkker. Alle sidene arver fra base.html, som har toppmenyen og bunnteksten. Designet ligger i static/style.css.

## Kjøre prosjektet

Installer Flask med pip install flask, kjør app.py og åpne http://127.0.0.1:5000 i nettleseren.

Laget av Marius
