```mermaid
 classDiagram
	
	Noppa "2" --> Pelaaja
	Pelaaja "2..8" --> Pelilauta
	Ruutu "40" --> Pelilauta

	class Noppa {
		luku
	}

        class Pelaaja {     
        }

	class Pelilauta {
	}

	class Ruutu {
	}
```
