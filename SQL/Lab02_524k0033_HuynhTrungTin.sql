Create DATABASE MovieDB;
Use MovieDB;
CREATE table Films
(
	film_id int PRIMARY KEY,
	title VARCHAR(50),
	year int,
	duration int
)
INSERT INTO Films (film_id, title, year, duration) VALUES
(1, 'Minority Report', 2002, 145),
(2, 'About A Boy', 2002, 101),
(3, 'Bourne Identity, The', 2002, 118),
(4, 'Notting Hill', 1999, 124),
(5, 'Nine Months', 1995, 103),
(6, 'Lola Rennt', 1998, 81);

create table Actors (
	actor_id int PRIMARY KEY,
	name VARCHAR(50),
	sex char(1)
)
INSERT INTO Actors (actor_id, name, sex) VALUES
(1, 'Damon, Matt', 'm'),
(2, 'Potente, Franka', 'f'),
(3, 'Cruise, Tom', 'm'),
(4, 'Grant, Hugh', 'm'),
(5, 'Roberts, Julia', 'f'),
(6, 'Moore, Julianne', 'f'),
(7, 'Bleibtreu, Moritz', 'm');

create table Act_Film (
	actor_id int FOREIGN KEY REFERENCES Actors(actor_id),
	film_id int FOREIGN KEY REFERENCES Films(film_id),
	role VARCHAR(50)
)
INSERT INTO Act_Film (actor_id, film_id, role) VALUES
(3, 1, 'Detective John Anderton'),
(4, 2, 'Will'),
(2, 3, 'Marie Kreutz'),
(1, 3, 'Jason Bourne'),
(4, 4, 'William Thacker'),
(5, 4, 'Anna Scott'),
(4, 5, 'Samuel ''Sam'' Faulkner, M.D., P.C.'),
(2, 6, 'Lola'),
(7, 6, 'Manni');

--2.a
Select title from Films;
--2.b
Select name from Actors where sex='f'
--2.c
Select name from Actors where Actors.actor_id in (
	Select actor_id from Act_Film, Films where Act_Film.film_id = Films.film_id and Films.title='Bourne Identity, The'
)
--2.d
Select title from Films where film_id IN (
	Select film_id from Act_Film where actor_id IN (
		Select actor_id from Actors where sex='f'
	)
) 
--2.e
Select title from Films where film_id NOT IN (
	Select film_id from Act_Film where actor_id  IN (
		Select actor_id from Actors where sex='f'
	)
)