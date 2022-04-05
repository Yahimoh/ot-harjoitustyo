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
	
	Hotelli "1" --> Katu
	Talo "1..4" --> Katu
	

	class Noppa {
		luku
	}

        class Pelaaja {
		rahaa
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
	
	class Hotelli {
	}
	
	class Talo {
	}
	 
```
