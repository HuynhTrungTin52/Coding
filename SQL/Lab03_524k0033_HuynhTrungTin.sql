create DATABASE EmployeeManage;
use EmployeeManage;
create table DEPARTMENT (
	Dept_ID CHAR(3) PRIMARY KEY,
	Dept_Name NVARCHAR(40),
	Address NVARCHAR(50),
	TEL char(10)
)
CREATE TABLE LANGUAGE (
	Lang_ID char(2) PRIMARY KEY,
	Language NVARCHAR(20)
)
Create table EMPLOYEE(
	Emp_ID char(5) PRIMARY KEY,
	Name NVARCHAR(40),
	Gender char(3),
	Bdate DATETIME,
	Salary int,
	Dept_ID char(3) FOREIGN KEY REFERENCES DEPARTMENT(Dept_ID),
	Tel char(10),
	BeRegular DATETIME
)
Create table SKILLS(
	Emp_ID char(5) FOREIGN KEY REFERENCES EMPLOYEE(Emp_id),
	Lang_ID char(2) FOREIGN KEY REFERENCES LANGUAGE(Lang_ID),
	Skill CHAR(1),
	PRIMARY KEY(Emp_ID,Lang_ID)
)

INSERT into DEPARTMENT VALUES
	('HCA','Personel Administration','19 Nguyen Huu Tho, HCM','04 8585793'),
	('KDA','Marketing','19 Nguyen Huu Tho, HCM','04 8574943'),
	('KTA','Technical','19 Nguyen Huu Tho, HCM','04 9480485'),
	('QTA','Equipment','19 Nguyen Huu Tho, HCM','04 8508585');
Insert into LANGUAGE VALUES 
	(01,'English'),
	(02,'Russian'),
	(03,'French'),
	(04,'Japanese'),
	(05,'Chinese'),
	(06,'Korean');
INSERT INTO EMPLOYEE VALUES 
('HC001', N'Nguyễn Thị Hà', N'Nữ', '1950-08-27', 2500000, 'HCA', '9892358765', '1975-02-08'),
('HC002', N'Trần Văn Nam', 'Nam', '1975-06-12', 3000000, 'HCA', '9728416395', '1997-06-08'),
('HC003', N'Nguyễn Thanh Huyền', N'Nữ', '1978-07-03', 1500000, 'HCA', '9615748203', '1999-09-24'),
('KD001', N'Lê Tuyết Anh', N'Nữ', '1977-02-03', 2500000, 'KDA', '9248596713', '2001-10-02'),
('KD002', N'Nguyễn Anh Tú', 'Nam', '1942-07-04', 2600000, 'KDA', '9301284567', '1999-09-24'),
('KD003', N'Phạm An Thái', 'Nam', '1977-05-09', 1600000, 'KDA', '9574839201', '1999-09-24'),
('KD004', N'Lê Văn Hải', 'Nam', '1976-01-02', 2700000, 'KDA', '9103467589', '1997-06-08'),
('KD005', N'Nguyễn Phương Minh', 'Nam', '1980-01-02', 2000000, 'KDA', '9429506178', '2001-10-02'),
('KT001', N'Trần Đình Khảm', 'Nam', '1981-12-02', 2700000, 'KTA', '9687391024', '2005-01-01'),
('KT002', N'Nguyễn Mạnh Hùng', 'Nam', '1980-08-16', 2300000, 'KTA', '9534672189', '2005-01-01'),
('KT003', N'Phạm Thanh Sơn', 'Nam', '1984-08-20', 2000000, 'KTA', '9982756410', '2005-01-01'),
('KT004', N'Vũ Thị Hoài', N'Nữ', '1980-12-05', 2500000, 'KTA', '9045187632', '2001-10-02'),
('KT005', N'Nguyễn Thu Lan', N'Nữ', '1977-10-05', 3000000, 'KTA', '9173645890', '2001-10-02'),
('KT006', N'Trần Hoài Nam', 'Nam', '1978-07-02', 2800000, 'KTA', '9708912345', '1997-06-08'),
('KT007', N'Hoàng Nam Sơn', 'Nam', '1940-12-03', 3000000, 'KTA', '9856237410', '1965-07-02'),
('KT008', N'Lê Thu Trang', N'Nữ', '1950-07-06', 2500000, 'KTA', '9435108627', '1968-08-02'),
('KT009', N'Khúc Nam Hải', 'Nam', '1980-07-22', 2000000, 'KTA', '9768923451', '2005-01-01'),
('KT010', N'Phùng Trung Dũng', 'Nam', '1978-08-28', 2200000, 'KTA', '9214567890', '1999-09-24');
Insert into SKILLS values 
('HC001', 01, 'A'), 
('KD004', 05, 'A'),
('HC001', 02, 'B'), 
('KD005', 01, 'B'),
('HC002', 01, 'C'), 
('KD005', 02, 'D'),
('HC002', 03, 'C'), 
('KD005', 03, 'B'),
('HC003', 01, 'D'), 
('KD005', 04, 'B'),
('KD001', 01, 'C'), 
('KT001', 01, 'D'),
('KD001', 02, 'B'), 
('KT001', 04, 'E'),
('KD002', 01, 'D'),
('KT002', 01, 'C'),
('KD002', 02, 'A'), 
('KT002', 02, 'B'),
('KD003', 01, 'B'), 
('KT003', 01, 'D'),
('KD003', 02, 'C'), 
('KT003', 03, 'C'),
('KD004', 01, 'C'), 
('KT004', 01, 'D'),
('KD004', 04, 'A'), 
('KT005', 01, 'C')

insert into EMPLOYEE values (
	'QT001',N'Huỳnh Trung Tín','Nam','2006-10-04',150000,'QTA','1234567890','2026-10-04'
);

-- 1)List employee information with KT001 code
Select Name from EMPLOYEE where Emp_ID='KT001'
-- 2)Please correct the name of the employee on the Vietnamese character (Unicode)
-- 3)Give a list of female employees?
Select Name from EMPLOYEE where Gender like 'Nữ'
-- 4)Look for employees with last name ' Nguyễn '
Select Name from EMPLOYEE where Name like N'Nguyễn %'
-- 5)Give the list of employees with a name that contains the word ' Văn ' 
Select Name from EMPLOYEE where Name like N'% Văn %'
-- 6)Take out employees who are under 30?
Select Name FROM Employee WHERE DATEDIFF(year,Bdate,GETDATE())<30
-- 7) Give the list of employees aged between 25 and 30 years old?
Select Name FROM Employee WHERE DATEDIFF(year,Bdate,GETDATE())<30 AND DATEDIFF(year,Bdate,GETDATE())>25
-- 8)Give the staff id that have studied foreign languages 01 at level C or higher?
SELECT Emp_ID FROM SKILLS WHERE Lang_ID=01 AND Skill<='C'
-- 9)Give the list of employees to be the regular employees before 2000? 
SELECT Name 
from EMPLOYEE 
WHERE YEAR(BeRegular)<2000
-- 10)Given the list of employees who have been regular employees for more than 10 years?
Select NAME 
FROM Employee 
WHERE YEAR(GETDATE()) - YEAR(BeRegular)>=10