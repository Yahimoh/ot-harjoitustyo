# Verkkokauppa #

Verkkokauppa sovelluksen avulla kauppias voi laittaa myyntiin kauppiaan tarjoamia tuotteita ja palveluita. Kauppias voi laatia tuotteile toistaiseksi nimen ja hinnan. Verkkokaupassa asiakas voi rekisteröityä / kirjautua sisään tililleen ja sitten asiakas voi katsoa ja lisää tai poistaa kauppiaan tarjoamia tuotteita ostoskoriin.

## Verkkokauppan laajemmat toiminnallisuudet ovat työn alla.. ##

## Dokumentaatio ##
[Vaatimuusmäärittely](https://github.com/Yahimoh/ot-harjoitustyo/blob/main/Dokumentaatio/Vaatimuusmaarittely.md)

[Työaikakirjakirjanpito](https://github.com/Yahimoh/ot-harjoitustyo/blob/main/Dokumentaatio/Tyoaikakirjanpito.md)

[Changelog](https://github.com/Yahimoh/ot-harjoitustyo/blob/main/Dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/Yahimoh/ot-harjoitustyo/blob/main/Dokumentaatio/arkkitehtuuri.md)

## Release 1.0
[Verkkokauppa v1.0](https://github.com/Yahimoh/ot-harjoitustyo/releases/tag/1.0)

## Asennus
Asenna projektin riippuvuudet komennolla:
```bash
poetry install
```

## Käynnistys
Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

## Testaus
Käynnistä testit komennolla:
```bash
poetry run invoke test
```

Käynnistä testikattavuus komennolla:
```bash
poetry run invoke coverage-report
```

## Kooditarkistukset
Käynnistä kooditarkastukset *pylint* avulla komennolla:
```bash
poetry run invoke lint
```
