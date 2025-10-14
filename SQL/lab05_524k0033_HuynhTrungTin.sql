Create database QLSV
use QLSV


create table student
(
	snum numeric(9,0) primary key,
	sname varchar(30),
	major varchar(25),
	standing varchar(2),
	age numeric(3,0)
);
create table faculty
(
	fid numeric(9,0) primary key,
	fname varchar(30),
	deptid numeric(2,0)
);
create table class
(
	name varchar(40) primary key,
	meets_at varchar(20),
	room varchar(10),
	fid numeric(9,0),
	foreign key(fid) references faculty
);
create table enrolled
(
	snum numeric(9,0),
	cname varchar(40),
	primary key(snum,cname),
	foreign key(snum) references student,
	foreign key(cname) references class(name)
);


--1)Find the names of all Juniors (level = JR) who are enrolled in a class taught by I. Teach. 
SELECT DISTINCT s.sname
FROM student S, enrolled E
WHERE s.standing = 'JR' AND s.snum IN (
	--Find all of the students enrolled in I.Teach's class
	SELECT DISTINCT e.snum
	FROM enrolled E, faculty F, class C
	WHERE f.fid = c.fid AND e.cname IN (
		--Find the class I.Teach is teaching
		SELECT C.name
		FROM faculty F, class C
		WHERE f.fname='Ivana Teach' and c.fid =f.fid
	)
)

-- 2)Find the age of the oldest student who is either a History major or enrolled in a course taught by I.Teach

SELECT MAX(s.age) as oldest_age
FROM student S
WHERE s.major='History' OR s.snum IN (
	--Find all of the students enrolled in I.Teach's class
	SELECT DISTINCT e.snum
	FROM enrolled E, faculty F, class C
	WHERE f.fid = c.fid AND e.cname IN (
		--Find the class I.Teach is teaching
		SELECT C.name
		FROM faculty F, class C
		WHERE f.fname='Ivana Teach' and c.fid =f.fid
	)
)

-- 3)Find the names of all classes that either meet in room R128 or have five or more students enrolled
SELECT c.name
FROM class C
WHERE c.room='R128' OR c.name IN (
	SELECT c.name
	FROM class C, enrolled E
	WHERE c.name=e.cname
	GROUP BY c.name
	HAVING COUNT(e.snum)>=5
	
)

--4)Find the names of all students who are enrolled in two classes that meet at the same time
SELECT student.sname
FROM student
WHERE student.snum
IN(
    SELECT e1.snum
FROM enrolled e1
	JOIN class c1 ON c1.name = e1.cname
WHERE c1.meets_at IN (
    SELECT c2.meets_at
FROM class c2
WHERE c1.name <> c2.name
    )
)

-- 5)Find the names of faculty members who teach in every room in which some class is taught.
SELECT f.fname
FROM faculty f
JOIN class c ON c.fid = f.fid
GROUP BY f.fid, f.fname
HAVING COUNT(DISTINCT c.room) = (SELECT COUNT(DISTINCT room) FROM class);

-- 6)Find the names of faculty members for whom the combined enrollment of the courses that they teach is less than five.
SELECT f.fname
FROM faculty f
LEFT JOIN class c ON c.fid = f.fid
LEFT JOIN enrolled e ON e.cname = c.name
GROUP BY f.fid, f.fname
HAVING COUNT(e.snum) < 5;

-- 7)For each level, print the level and the average age of students for that level. 
SELECT standing AS level,
	ROUND(AVG(CAST(age AS FLOAT)), 2) AS avg_age
FROM student
GROUP BY standing
ORDER BY standing;

-- 8)For all levels except JR, print the level and the average age of students for that level. 
SELECT standing AS level,
	ROUND(AVG(CAST(age AS FLOAT)), 2) AS avg_age
FROM student
WHERE standing <> 'JR'
GROUP BY standing
ORDER BY standing;
-- 9)For each faculty member that has taught classes only in room R128, print the faculty member’s name and the total number of classes she or he has taught. 
SELECT f.fname,
	COUNT(c.name) AS total_classes
FROM faculty f
JOIN class c ON c.fid = f.fid
GROUP BY f.fid, f.fname
HAVING COUNT(*) > 0
   AND SUM(CASE WHEN c.room <> 'R128' THEN 1 ELSE 0 END) = 0;

-- 10)Find the names of students enrolled in the maximum number of classes. 
SELECT s.sname
FROM student s
JOIN (
	SELECT snum, COUNT(*) AS class_count,
				 RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
	FROM enrolled
	GROUP BY snum
) ec ON s.snum = ec.snum
WHERE ec.rnk = 1;

-- 11)Find the names of students not enrolled in any class. 
SELECT s.sname
FROM student s
LEFT JOIN enrolled e ON s.snum = e.snum
WHERE e.snum IS NULL;

-- 12) For each age value that appears in Students, find the level value that appears most often. For example, if there are more FR level students aged 18 than SR, JR, or SO students aged 18, you should print the pair (18, FR).
SELECT age, standing
FROM (
	SELECT age, standing, COUNT(*) AS cnt,
				 RANK() OVER (PARTITION BY age ORDER BY COUNT(*) DESC) AS rnk
	FROM student
	GROUP BY age, standing
) t
WHERE rnk = 1
ORDER BY age;
