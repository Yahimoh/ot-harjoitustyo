```mermaid
 classDiagram
	
	Noppa "2" --> Pelaaja
	Pelaaja "2..8" --> "1" Pelilauta

	class Noppa {
		luku
	}

        class Pelaaja {     
        }

	class Pelilauta {
	}

	class Tontti {
	}
```
