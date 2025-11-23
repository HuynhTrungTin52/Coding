Create Database HousingDB;
USE HousingDB;
--2)

CREATE TABLE House_0033 (
    HAddr NVARCHAR(100) PRIMARY KEY,
    Bedrooms INT,
    Bathrooms INT
);

CREATE TABLE Owner_0033 (
    OName NVARCHAR(50),
    OPhone VARCHAR(15),
    CONSTRAINT PK_Owner_0033 PRIMARY KEY (OName, OPhone)
);

CREATE TABLE Renter_0033 (
    RName NVARCHAR(50),
    RPhone VARCHAR(15),
    CONSTRAINT PK_Renter_0033 PRIMARY KEY (RName, RPhone)
);

CREATE TABLE House_Owner_0033 (
    HAddr NVARCHAR(100),
    OName NVARCHAR(50),
    OPhone VARCHAR(15),
    PercentageOwned DECIMAL(5, 2) CHECK (PercentageOwned <= 100),
    
    CONSTRAINT PK_House_Owner_0033 PRIMARY KEY (HAddr, OName, OPhone),
    CONSTRAINT FK_HO_House FOREIGN KEY (HAddr) REFERENCES House_0033(HAddr),
    CONSTRAINT FK_HO_Owner FOREIGN KEY (OName, OPhone) REFERENCES Owner_0033(OName, OPhone)
);

CREATE TABLE House_Renter_0033 (
    HAddr NVARCHAR(100),
    RName NVARCHAR(50),
    RPhone VARCHAR(15),
    
    CONSTRAINT PK_House_Renter_0033 PRIMARY KEY (HAddr, RName, RPhone),
    CONSTRAINT FK_HR_House FOREIGN KEY (HAddr) REFERENCES House_0033(HAddr),
    CONSTRAINT FK_HR_Renter FOREIGN KEY (RName, RPhone) REFERENCES Renter_0033(RName, RPhone)
);

INSERT INTO House_0033 (HAddr, Bedrooms, Bathrooms) VALUES 
('123 Nguyen Van Linh', 3, 2),
('456 Ton Duc Thang', 2, 1),
('789 Le Duan', 4, 3),
('101 Nguyen Huu Tho', 1, 1),
('202 Nguyen Trai', 5, 4);

INSERT INTO Owner_0033 (OName, OPhone) VALUES 
('Huynh Trung Tin', '0901230033'), 
('Nguyen Van A', '0909998888'),
('Tran Thi B', '0907776666'),
('Le Van C', '0905554444'),
('Pham Thi D', '0903332222');

INSERT INTO Renter_0033 (RName, RPhone) VALUES 
('Alice Smith', '0911111111'),
('Bob Jones', '0922222222'),
('Charlie Brown', '0933333333'),
('David White', '0944444444'),
('Eve Black', '0955555555');

INSERT INTO House_Owner_0033 (HAddr, OName, OPhone, PercentageOwned) VALUES 
('123 Nguyen Van Linh', 'Huynh Trung Tin', '0901230033', 100.00),
('456 Ton Duc Thang', 'Nguyen Van A', '0909998888', 50.00),
('456 Ton Duc Thang', 'Tran Thi B', '0907776666', 50.00), 
('789 Le Duan', 'Le Van C', '0905554444', 100.00),
('101 Nguyen Huu Tho', 'Pham Thi D', '0903332222', 100.00);

INSERT INTO House_Renter_0033 (HAddr, RName, RPhone) VALUES 
('456 Ton Duc Thang', 'Alice Smith', '0911111111'),
('456 Ton Duc Thang', 'Bob Jones', '0922222222'), 
('789 Le Duan', 'Charlie Brown', '0933333333'),
('101 Nguyen Huu Tho', 'David White', '0944444444'),
('123 Nguyen Van Linh', 'Eve Black', '0955555555');

--1) Find the address and number of bedrooms of all houses owned by 'Student Name'.
SELECT h.HAddr, h.Bedrooms 
FROM House_0033 h
JOIN House_Owner_0033 ho ON h.HAddr = ho.HAddr
WHERE ho.OName = 'Student Name';

-- 2) List all houses that have more than 2 bedrooms but are currently NOT rented by anyone.
SELECT HAddr, Bedrooms 
FROM House_0033 
WHERE Bedrooms > 2 
AND HAddr NOT IN (SELECT HAddr FROM House_Renter_0033);

-- 3) Who are the renters currently living in the house at '456 Ton Duc Thang'?
SELECT r.RName, r.RPhone
FROM Renter_0033 r
JOIN House_Renter_0033 hr ON r.RName = hr.RName AND r.RPhone = hr.RPhone
WHERE hr.HAddr = '456 Ton Duc Thang';

-- 4) Calculate the total number of bathrooms across all houses owned by 'Nguyen Van A'.
SELECT SUM(h.Bathrooms) as TotalBathrooms
FROM House_0033 h
JOIN House_Owner_0033 ho ON h.HAddr = ho.HAddr
WHERE ho.OName = 'Nguyen Van A';

-- 5) Find owners who own less than 100% of a house (Shared Ownership).
SELECT OName, OPhone, HAddr, PercentageOwned
FROM House_Owner_0033
WHERE PercentageOwned < 100;


-- View 1) Full Property Details
CREATE VIEW View_HouseOwners_0033 AS
SELECT h.HAddr, h.Bedrooms, h.Bathrooms, ho.OName, ho.PercentageOwned
FROM House_0033 h
JOIN House_Owner_0033 ho ON h.HAddr = ho.HAddr;

-- View 2) Shows houses that currently have no renters recorded
CREATE VIEW View_VacantHouses_0033 AS
SELECT h.HAddr, h.Bedrooms, h.Bathrooms
FROM House_0033 h
LEFT JOIN House_Renter_0033 hr ON h.HAddr = hr.HAddr
WHERE hr.RName IS NULL;

-- Procedure 1) Get All Renters (No Parameter)
CREATE PROCEDURE GetAllRenters_0033
AS
BEGIN
    SELECT * FROM Renter_0033;
END;

-- Procedure 2) Get House Details by Owner Name (With Input Parameter)
CREATE PROCEDURE GetHousesByOwner_0033
    @OwnerName NVARCHAR(50)
AS
BEGIN
    SELECT h.HAddr, h.Bedrooms, h.Bathrooms, ho.PercentageOwned
    FROM House_0033 h
    JOIN House_Owner_0033 ho ON h.HAddr = ho.HAddr
    WHERE ho.OName = @OwnerName;
END;