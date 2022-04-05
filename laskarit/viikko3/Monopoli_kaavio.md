```mermaid
 classDiagram
	
	Noppa "2" --> Pelaaja
	Pelaaja "2..8" --> Pelilauta
	Ruutu "40" --> Pelilauta
	Pelinappula "1" --> Pelaaja
	Pelinappula --> Ruutu

	Aloitusruutu --> Ruutu
	Vankilaruutu --> Ruutu
	Sattuma --> Ruutu
	Yhteismaa --> Ruutu
	Asema --> Ruutu
	Laitos --> Ruutu
	Katu --> Ruutu
	

	class Noppa {
		luku
	}

        class Pelaaja {     
        }

	class Pelilauta {
	}

	class Ruutu {
	}
	
	class Pelinappula {
		ruutu
	}

	class Aloitusruutu {
	}

	class Vankilaruutu {
	}
		
	class Sattuma {
	}	
	
	class Yhteismaa {
	}
	
	class Asema {
	}
	
	class Laitos {
	}

	class Katu {
	}
	 
```
