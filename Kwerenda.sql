CREATE TABLE Info 
	(id AUTO_INCREMENT PRIMARY KEY,
	numer_telefonu VARCHAR(11) NOT NULL,
	HASH VARCHAR(64) NOT NULL,
	TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	kraj VARCHAR(50) NOT NULL);

-- dodawanie rekordów (id i timestamp dodają się automatycznie, więc ich nie wpisujemy): 	

INSERT INTO Info (numer_telefonu, HASH, kraj)
VALUES ()