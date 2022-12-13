# Arkkitehtuurikuvaus
## Rakenne
<img src=./IMG_0055.jpeg width="350" height="300">

## Sovelluslogiikka

```mermaid
 classDiagram
 
      Main --> Merchant
      Main --> ui
 
      Merchant --> Database
      Merchant --> Tuote
 
      Database --> Tuote
      
      class Main{
      
      }
      
      class ui{
      root: pääikkuna
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


## Käyttäjän sisäänkirjautuminen
```mermaid
sequenceDiagram
  actor Asiakas
  
  participant main
  participant merchant
  participant database
  
  Asiakas ->> main: Valinta 1 (asiakas)
  main ->> merchant: start("asiakas")
  merchant ->> database: kirjaudu_sisaan("Yahia", 1234)
  
  database -->> merchant: Käyttäjän Yahia id
```

## Verkkokaupan datan pysyväistallennus
Verkkokaupan datan pysyväistallennuksesta huolehtii luokat merchant.py ja tieokanta backend.db.

Pysyväistallennuksessa on käytetty SQL-tietokantaa
