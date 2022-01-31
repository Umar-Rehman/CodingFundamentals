-- 1.1 Create tables and populate with sample data (MySQL)

--DROP DATABASE IF EXISTS qastore;

--CREATE DATABASE qastore;

--USE qastore;

CREATE TABLE company
	(
    company_no INT NOT NULL,
	company_name VARCHAR(20) NOT NULL,
	tel VARCHAR(15) NULL,
	county VARCHAR(15) NULL,
	post_code CHAR(8) NULL,
    CONSTRAINT PK_company_no PRIMARY KEY (company_no)
    );
     
INSERT INTO company (company_no,company_name,tel,county,post_code)
    VALUES (1000,'Xander Radiators Ltd','01254 987766','Devon','PL4 9RT');
INSERT INTO company (company_no,company_name,tel,county,post_code)
    VALUES (2000,'Arctic plc','0181-987-1265','London','N1 4LH');
INSERT INTO company (company_no,company_name,tel,county,post_code)
    VALUES (3000,'Hadron Heating Ltd','(01306) 345672','London','SE3 89L');
INSERT INTO company (company_no,company_name,tel,county,post_code)
    VALUES (4000,'Yellow Electrics Ltd','0171 478 2990','London','N9 2FG');

CREATE TABLE contact
	(
	company_no INT NOT NULL,
	contact_code CHAR(2) NOT NULL,
	contact_name VARCHAR(20) NOT NULL,
	job_title VARCHAR(30) NULL,
	tel VARCHAR(25) NULL,
	notes VARCHAR(60) NULL,
    CONSTRAINT PK_company_no_contact_code PRIMARY KEY (company_no,contact_code),
    CONSTRAINT FK_company_no FOREIGN KEY(company_no) REFERENCES company (company_no)
    );

/*









*/

INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (1000,'MM','Elizabeth Simmonsa','Bought Ledger Manager','(0207)223-9887','We first visited her in January 1988');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (2000,'NN','Tom Vincent','Electrical Manager','01546-456566 Ext 22','Works only on Monday and Wednesdays');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (2000,'OO','Niamh Dickinson','Accounts Officer','0207-341-566670 ext 10','');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (3000,'PP','Ella Fraser','Accounts Officer','0131 324545 ext 213','Insists on personally signing all orders');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (3000,'QQ','Samantha Forster','Development Director','01456 801711 ext 44','Has been in his job a long time');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (3000,'RR','Rebecca Mason','Federal Reporting Officer','0208-111-11111','Has a preference for Apple Macintosh systems');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (4000,'SS','Ben Pratt','Head of Inter Office Systems','0207-988-0777','');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes)
    VALUES (4000,'TT','Leah Weston','Chief Executive Officer','05673-476878 ext 221','Is listed in Whos Who 1988 onwards');
INSERT INTO contact (company_no,contact_code,contact_name,job_title,tel,notes) 
    VALUES (4000,'UU','Jacob Byrne','Gourmet Foods Purchaser','0823-598494 ext 1','Is upset becuase he is not chief executive!');
    
CREATE TABLE dept
	(
	dept_no INT NOT NULL,
	dept_name VARCHAR(20) NOT NULL,
	manager VARCHAR(20) NULL,
	sales_target DECIMAL(12, 4) NULL,
    CONSTRAINT PK_dept_no PRIMARY KEY (dept_no)
    );

INSERT INTO dept (dept_no,dept_name, manager,sales_target)
    VALUES (1,'Credit Control','Jade Fleming',25.0000);
INSERT INTO dept (dept_no,dept_name,manager,sales_target)
    VALUES (2,'Advanced Products','Max Norton',5.0000);
INSERT INTO dept (dept_no,dept_name,manager,sales_target)
    VALUES (3,'Business Systems','Joel Moss',15.0000);
INSERT INTO dept (dept_no,dept_name,manager,sales_target)
    VALUES (4,'Electrical Repairs','Tegan Turnbull',45.0000);
INSERT INTO dept (dept_no,dept_name, manager,sales_target) 
    VALUES (5,'Desktop Systems','Rebecca Roberts',5.0000);

CREATE TABLE salesperson
	(
	emp_no INT NOT NULL,
	first_name VARCHAR(15) NOT NULL,
	last_name VARCHAR(15) NOT NULL,
	dept_no INT NULL,
	salary DECIMAL(12,4) NULL,
    sales_target DECIMAL(12,4) NULL,
	county VARCHAR(15) NULL,
	post_code CHAR(8) NULL,
	tel VARCHAR(25) NULL,
	notes VARCHAR(50) NULL,
    CONSTRAINT PK_emp_no PRIMARY KEY (emp_no),
    CONSTRAINT FK_dept_no FOREIGN KEY (dept_no) REFERENCES dept (dept_no)
    );

INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes)
    VALUES (10,'Aiden','Peacock',1,10.0000,9.0000,'Surrey','RT8 8LP','0171-908-8765','Joined in Sept 1996');
INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes)
    VALUES (20,'Peter','Potts',2,11.0000,14.0000,'Hampshire','RF3 9UD','(0306)7871','Bright Prospect');
INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes)
    VALUES (30,'Isabella','Flynn',2,12.0000,7.0000,'Hampshire','W45 TY3','(0908)922211','Should be promoted within the next 4 months');
INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes)
    VALUES (40,'Edward','Quinn',3, 13.0000,11.0000,'London',NULL,'0171-898-9656',NULL);
INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes)
    VALUES (50,'Christopher','Farmer',3,14.0000,12.0000,'Surrey','CR1 2GH','0181-898-1126',NULL);
INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county, post_code,tel,notes)
    VALUES (60,'Melissa','Khan',3,15.0000,13.0000,'Surrey',NULL,'0181-877-0123','Dislikes international travel');
INSERT salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes)
    VALUES (100,'George','Bull',NULL,20.0000,29.0000, 'Essex','IG3 8AT','01708-776688','No Department');

CREATE TABLE sale
	(
	order_no INT NOT NULL,
	emp_no INT NULL,
	company_order_no VARCHAR(15) NULL,
	company_no INT NOT NULL,
	contact_code CHAR(2) NOT NULL,
	order_value DECIMAL(12,2) NULL,
	order_date DATETIME NULL,
	description VARCHAR(140) NULL,
    CONSTRAINT PK_order_no PRIMARY KEY (order_no),
    CONSTRAINT FK_company_no_contact_code FOREIGN KEY(company_no, contact_code) REFERENCES contact (company_no, contact_code)
    );
    
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description)
    VALUES (100,60,'AA1',1000,'MM',7.11,'2000-06-24 10:20:30','IBM Thinkpad 755CE');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description) 
    VALUES (200, 60,'Ord34',3000,'QQ',6.22,'2000-05-01 11:21:31','MS Office Professional * 30');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description)
    VALUES (300, 60,'Ord39',2000,'OO',12.33,'2000-07-14 12:22:32','25 ScanPRO 4800 Scanner');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description) 
    VALUES (400,10,'DGG5',1000,'MM',5.44,'2000-08-09 13:23:33','Modems and Cables etc');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description) 
    VALUES (500, 60,'DPF78',4000,'TT',2.55,'2000-07-23 14:24:34','Laser printer');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description) 
    VALUES (600, 50,'AC12',3000,'PP',27.66,'2000-05-23 15:25:35','Complete Desktop Publishing System');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description) 
    VALUES (700,10,'23',2000,'OO',3.77,'2000-01-23 16:26:36','SQL Server 7.0 20 user licence');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description) 
    VALUES (800, 60,'B-123E',3000,'RR',3.88,'2000-12-15 17:27:37','Printer cartridges');
INSERT sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value, order_date,description)
    VALUES (900,NULL,'AA2',1000,'MM',9.99,'2000-06-25 12:21:19', 'Toshiba Portage R30-A-15D');
INSERT INTO sale (order_no,emp_no,company_order_no,company_no,contact_code,order_value,order_date,description)
    VALUES (1000,120,'AA3',1000,'MM',19.99,'2000-06-26 16:11:41', 'HP Compaq LA 1956x');

-- 1.2 Check contents of qastore database

SELECT * FROM company;
SELECT * FROM contact;
SELECT * FROM dept;
SELECT * FROM salesperson;
SELECT * FROM sale;