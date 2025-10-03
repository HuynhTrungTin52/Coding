Create DATABASE Employee;
use Employee;


CREATE TABLE Employee (
	FName VARCHAR(10),
	Minit VARCHAR(10),
	LName VARCHAR(10),
	SSN VARCHAR(15) PRIMARY KEY,
	BDate DATE,
	Address VARCHAR(25),
	Sex NVARCHAR(3),
	Salary INT,
	SuperSSN VARCHAR(15) FOREIGN KEY REFERENCES Employee(SSN)
)
CREATE TABLE Department (
	DName VARCHAR(20),
	DepNo VARCHAR(15) PRIMARY KEY,
	MgrSSN VARCHAR(15) FOREIGN KEY REFERENCES Employee(SSN),
	MgrSDate DATE
)

ALTER TABLE Employee ADD DepNo VARCHAR(15);

ALTER TABLE Employee ADD CONSTRAINT FK_DepNo FOREIGN KEY (DepNo) REFERENCES Department(DepNo);


CREATE TABLE Dept_Locations (
	DepNo VARCHAR(15) FOREIGN KEY REFERENCES Department(DepNo),
	DLocation VARCHAR(25) PRIMARY KEY 
)

CREATE TABLE Project (
	PName NVARCHAR(50),
	PNumber INT PRIMARY KEY,
	PLocation VARCHAR(25),
	DepNo VARCHAR(15) FOREIGN KEY REFERENCES Department(DepNo)
)

CREATE TABLE Works_On (
	ESSN VARCHAR(15) FOREIGN KEY REFERENCES Employee(SSN),
	PNo VARCHAR(15),
	Hours INT

	PRIMARY KEY(ESSN,PNo)
)

Create TABLE Dependent(
	ESSN VARCHAR(15) FOREIGN KEY REFERENCES Employee(SSN),
	Dependent_Name NVARCHAR(50) PRIMARY KEY,
	Sex VARCHAR(3),
	BDate Date,
	Relationship NVARCHAR(25)
)

insert into Department values('Information','D01', null,'2019-03-18')
insert into Department values('Security','D02', null,'2019-05-08')
insert into Department values('Administrative','D03',null,'2019-03-18')
insert into Department values('Bussiness','D04', null,'2022-06-17')
insert into Department values('Technical','D05', null,'2021-09-22')
insert into Department values('Consultant','D06',null,'2000-11-20')

insert into employee values('Tran','Van','Phuc','E01', '1990-2-20','Da Lat', 'Nam', 2000, null, 'D01')
insert into employee values('Nguyen','Minh','Hung','E02', '1992-4-07','Ca Mau', 'Nam', 1800, null, 'D02')
insert into employee values('Phan','Tuyet','Mai','E03','1991-8-28','Ninh Binh', N'Nữ', 2200, null, 'D02')
insert into employee values('Phan','Quoc','Dung','E04', '1995-4-13','Nha Trang', N'Nữ', 700, 'E01', 'D03')
insert into employee values('Le','Thi','Rieng','E05','1993-11-18','Ho Chi Minh', N'Nữ', 650, 'E02', 'D04')
insert into employee values('Pham','Van','Dong','E06', '1996-06-02','Ha Noi', 'Nam', 1250, 'E03', 'D04')
insert into employee values('Pham','Van','Minh','E07', '1996-06-02','Ha Noi', 'Nam', 1250, 'E03', 'D05')
insert into employee values('Doan','Minh','Khai','E08','2002-12-16','Ho Chi Minh','Nam',5000,null,'D05')

UPDATE Department SET MgrSSN = 'E01' WHERE depNo = 'D01'
UPDATE Department SET MgrSSN = 'E02' WHERE depNo = 'D02'
UPDATE Department SET MgrSSN = 'E03' WHERE depNo = 'D03'
UPDATE Department SET MgrSSN = 'E04' WHERE depNo = 'D04'
UPDATE Department SET MgrSSN = 'E05' WHERE depNo = 'D05'


insert into Dept_Locations values('D01','Ho Chi Minh')
insert into Dept_Locations values('D01','Da Nang')
insert into Dept_Locations values('D02','Binh Duong')
insert into Dept_Locations values('D03','Hai Phong')
insert into Dept_Locations values('D03','Ha Noi')
insert into Dept_Locations values('D03','Vu Han')
insert into Dept_Locations values('D04','Ukraine')
insert into Dept_Locations values('D05','Russia')

insert into project values(N'Website bán mỹ phẩm','06','Ha Noi','D02')
insert into project values(N'Website bán đồ điện tử','01','Binh Duong','D01')
insert into project values(N'Ứng dụng đặt món ăn','02','Vu Han','D03')
insert into project values(N'Ứng dụng giao hàng hóa','03','Hai Phong','D03')
insert into project values(N'Ứng dụng nhắn tin','04','Ho Chi Minh','D05')
insert into project values(N'Ứng dụng gọi điện','05','Dong Nai','D04')

insert into works_on values('E01','01',100)
insert into works_on values('E01','02',150)
insert into works_on values('E02','03',50)
insert into works_on values('E02','04',200)
insert into works_on values('E04','03',100)
insert into works_on values('E04','04',120)
insert into works_on values('E05','04',100)
insert into works_on values('E03','05',300)
insert into works_on values('E06','05',100)
insert into works_on values('E06','06',400)

insert into Dependent values('E01',N'Trần Phương Thảo',N'Nữ','2004-02-14',N'Con')
insert into Dependent values('E02',N'Phạm Ngọc Phương',N'Nữ','1993-05-14',N'Vợ')
insert into Dependent values('E02',N'Võ Văn Dũng','Nam','2008-02-19',N'Con')
insert into Dependent values('E03',N'Nguyễn Quốc Tuấn',N'Nữ','1984-06-08',N'Chồng')
insert into Dependent values('E04',N'Phan Thị Phương',N'Nữ','2006-08-1',N'Con')
insert into Dependent values('E05',N'Lê Quốc Tuấn','Nam','1971-04-28',N'Bố')
insert into Dependent values('E06',N'Võ Thị Xuân',N'Nữ','2976-11-16',N'Mẹ')

-- 1)
SELECT
    D.DepNo,
    D.DName,
    COUNT(E.SSN) AS NumberOfEmployees
FROM
    Department AS D
LEFT JOIN
    Employee AS E ON D.DepNo = E.DepNo
GROUP BY
    D.DepNo, D.DName
ORDER BY
    NumberOfEmployees;
-- 2)
SELECT
    D.DepNo,
    D.DName,
    COUNT(E.SSN) AS NumberOfEmployees
FROM
    Department AS D
INNER JOIN
    Employee AS E ON D.DepNo = E.DepNo
GROUP BY
    D.DepNo, D.DName
HAVING
    COUNT(E.SSN) > 2
ORDER BY
    D.DepNo;
--3)
SELECT
    D.DName,
    DL.DLocation
FROM
    Department AS D
JOIN
    Dept_Locations AS DL ON D.DepNo = DL.DepNo
WHERE
    D.DepNo IN ('D01', 'DO3', 'DO5');
--4)
SELECT
    E.FName,
    E.LName,
    P.PName,
    P.PNumber
FROM
    Employee AS E
JOIN
    Works_On AS W ON E.SSN = W.ESSN
JOIN
    Project AS P ON W.PNo = P.PNumber
WHERE
    E.Sex = N'Nữ';
--5)
SELECT
    E.FName,
    E.LName
FROM
    Employee AS E
JOIN
    Dependent AS D ON E.SSN = D.ESSN
WHERE
    E.Sex = D.Sex;
--6)
SELECT
    DISTINCT E.FName, E.LName
FROM
    Employee AS E
JOIN
    Works_On AS W ON E.SSN = W.ESSN
JOIN
    Project AS P ON W.PNo = P.PNumber
WHERE
    P.DepNo = 'D05';
--7)
SELECT
    E.FName, E.LName
FROM
    Employee AS E
LEFT JOIN
    Works_On AS W ON E.SSN = W.ESSN
WHERE
    W.ESSN IS NULL;
--8)
SELECT
    DepNo,
    COUNT(SSN) AS NumberOfEmployees,
    AVG(Salary) AS AverageSalary
FROM
    Employee
GROUP BY
    DepNo;
--9)
SELECT
    D.DName,
    D.DepNo
FROM
    Department AS D
JOIN
    Employee AS E ON D.DepNo = E.DepNo
GROUP BY
    D.DName, D.DepNo
HAVING
    AVG(E.Salary) BETWEEN 30000 AND 60000;
--10)
SELECT
    E.FName, E.LName
FROM
    Employee AS E
LEFT JOIN
    Dependent AS D ON E.SSN = D.ESSN
WHERE
    D.ESSN IS NULL;
--11)
SELECT
    E.FName, E.LName
FROM
    Employee AS E
JOIN
    Works_On AS W ON E.SSN = W.ESSN
WHERE
    W.PNo IN (3388, 1945)
GROUP BY
    E.SSN, E.FName, E.LName
HAVING
    COUNT(DISTINCT W.PNo) = 2;
--12)
SELECT
    DepNo,
    PNumber
FROM
    Project
ORDER BY
    PNumber;
--13)
SELECT
    E.FName,
    E.LName,
    SUM(W.Hours) AS TotalHoursWorked
FROM
    Employee AS E
LEFT JOIN
    Works_On AS W ON E.SSN = W.ESSN
GROUP BY
    E.SSN, E.FName, E.LName;
--14)
SELECT
    E.FName,
    E.LName
FROM
    Employee AS E
JOIN
    Employee AS S ON E.SuperSSN = S.SSN
WHERE
    S.SuperSSN IS NULL;	
--15)
SELECT
    E.FName,
    E.LName
FROM
    Employee AS E
JOIN
    Dept_Locations AS DL ON E.DepNo = DL.DepNo
WHERE
    E.Address LIKE '%Salt Lake City%' 
    AND DL.DLocation = 'Salt Lake City';
--16)
SELECT
    E.FName,
    E.LName
FROM
    Employee AS E
JOIN
    Department AS D ON E.SSN = D.MgrSSN
WHERE
    D.MgrSDate < '1976-09-20';