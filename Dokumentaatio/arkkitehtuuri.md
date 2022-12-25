# Arkkitehtuurikuvaus
## Rakenne
<img src=./IMG_0055.jpeg width="350" height="300">
Hakemisto **ui** sisältää tekstikäyttöliittymälle koodia, hakemisto **services** sisältää sovelluksen toiminnalle ja kontrollille tarvittavia koodia, **entities** sisältää koodi- tiedostomalleja ja hakemisto **repositories** sisältää sovelluksen tietokannalle tarvittavia toiminnallisuuksia. **main.py** hoitaa sovelluksen alustukselle ja käynnistämiselle tarvittavia toimintoja. 

## Sovelluslogiikka

```mermaid
 classDiagram
 
      Main --> TUI
 
      Merchant --> Database
      Merchant --> Tuote
 
      Database --> Tuote
      
      TUI --> AsiakkaanTUI
      TUI --> KauppiaanTUI
      
      AsiakkaanTUI --> Merchant
      KauppiaanTUI --> Merchant
      
      class Main{
      
      }
      
      class AsiakkaanTUI {
      -asiakkaan_id: Int
      -merchant: Merchant
      }
      
      class KauppiaanTUI {
      -merchant: Merchant
      }
      
      class TUI{
      asiakkaan_tui: AsiakkaanTUI
      kauppiaan_tui: KauppiaanTUI
      }
      
      class Merchant{
      db: Database
      tuote: Tuote
      }
      
      class Database{
      tuote: Tuote
      }
      
      class Tuote {
      nimi: string
      hinta: int
      }  
```
## Käyttöliittymä
Tekstikäyttöliittymiä ovat:
- Kaupan käynnistys ja roolin (asiakas / kauppias) valinta
- Kauppiaan näkymä ja toiminnot
- Asiakkaan sisäänkirjautumisen / rekisteröinnin näkymä
- Asiakkaan näkymä ja toiminnot

## Käyttäjän sisäänkirjautuminen
```mermaid
sequenceDiagram
  actor Asiakas
  
  participant main
  participant tui
  participant merchant
  participant database
  participant asiakas_tui
  
  main ->> tui: start()
  Asiakas ->> tui: Valinta 1 (asiakas)
  tui ->> asiakas_tui: asiakkaan_sisaankirjautuminen_tui()
  asiakas_tui ->> merchant: asiakkaan_sisaankirjautuminen()
  merchant ->> database: kirjaudu_sisaan("Yahia", 1234)
  
  
  database -->> merchant: Käyttäjän Yahia id
```

## Verkkokaupan datan pysyväistallennus
Verkkokaupan datan pysyväistallennuksesta huolehtii luokat merchant.py ja tieokanta backend.db.

Pysyväistallennuksessa on käytetty SQL-tietokantaa
