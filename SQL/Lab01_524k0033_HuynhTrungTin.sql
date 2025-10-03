Create DATABASE TDT_SManage

ON PRIMARY (
	NAME = 'TDT_SManage',
	FILENAME = 'd:\database\TDT_SManage.mdf'
)

LOG ON (
	NAME = 'TDT_SManage.log',
	FILENAME='d:\database\TDT_Smanage_log.ldf'
)

create TABLE Department (
	Dep_ID VARCHAR(10),
	Dep_name NCHAR(20),
	year int,

	PRIMARY KEY(Dep_ID)
)

create table Student (
	name NCHAR(25),
	St_id VARCHAR(10),
	birth DATE,
	Dep_ID VARCHAR(10),

	PRIMARY KEY (St_id),
	FOREIGN KEY (Dep_ID) REFERENCES Department(Dep_ID)
)

create TABLE Courses (
	coursename NCHAR(30),
	course_id VARCHAR(10),
	credit int,
	dep_id VARCHAR(10),

	PRIMARY KEY(course_id),
	FOREIGN KEY(dep_id) REFERENCES Department(Dep_ID)
)

create TABLE Conditions (
	course_id VARCHAR(10),
	precourse_id VARCHAR(10),

	FOREIGN KEY(course_id) REFERENCES Courses(course_id),
	PRIMARY KEY(course_id,precourse_id)
)

Create table Results (
	St_id VARCHAR(10),
	course_id VARCHAR(10),
	mark FLOAT,

	FOREIGN KEY(course_id) REFERENCES Courses(course_id),
	FOREIGN KEY(St_id) REFERENCES Student(St_id),
	PRIMARY KEY(St_id,course_id)
)