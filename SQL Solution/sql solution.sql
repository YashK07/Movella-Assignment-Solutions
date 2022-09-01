-- create table employee
CREATE TABLE employee (
  Emp_Id INTEGER PRIMARY KEY,
  Name VARCHAR(15) NOT NULL,
  Department TEXT NOT NULL,
  Grade INT NOT NULL,
  Salary INT,
  Gender TEXT
);
INSERT INTO employee (Emp_Id, Name, Department, Grade, Salary, Gender)
VALUES (1,'Robert', 'Computer Science', 100, 100000, 'M');
INSERT INTO employee (Emp_Id, Name, Department, Grade, Salary, Gender)
VALUES (2,'Ram', 'Information Technology', 101, 134000, 'M');
INSERT INTO employee (Emp_Id, Name, Department, Grade, Salary, Gender)
VALUES (3,'Alex', 'Computer Science', 200, 123456, 'M');
INSERT INTO employee (Emp_Id, Name, Department, Grade, Salary, Gender)
VALUES (4,'Radha', 'Information Technology', 201, 23456, 'F');
INSERT INTO employee (Emp_Id, Name, Department, Grade, Salary, Gender)
VALUES (5,'Santhi', 'Civil', 300, 234567, 'F');
INSERT INTO employee (Emp_Id, Name, Department, Grade, Salary, Gender)
VALUES (6,'Madhavi', 'BioTech', 301, 234567, 'F');


-- create table employee
CREATE TABLE student (
  Student_Id INTEGER PRIMARY KEY,
  Class_Teacher_Employee_Id INTEGER,
  Subject1 TEXT Not Null,
  Subject2 TEXT Not Null,
  Subject3 TEXT Not Null
);
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (1,1,'P', 'P','F');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (2,1,'P', 'F','P');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (3,2,'P', 'P','P');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (4,3,'F', 'F','F');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (5,4,'P', 'P','P');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (6,5,'P', 'P','F');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (7,4,'P', 'P','P');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (8,5,'P', 'P','P');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (9,4,'P', 'P','P');
INSERT INTO student(Student_Id, Class_Teacher_Employee_Id, Subject1, Subject2, Subject3)
VALUES (10,3,'F', 'F','F');



SELECT * FROM student;


/*Query Solutions*/
SELECT Name FROM employee WHERE Grade > 200;
SELECT Department FROM employee WHERE Gender = 'M';
SELECT * FROM employee ORDER BY Salary DESC  limit 1,1;
SELECT * FROM employee
WHERE
NOT EXISTS (SELECT * FROM student WHERE student.Class_Teacher_Employee_Id=employee.Emp_Id);

SELECT * FROM student WHERE Subject1='P' AND Subject2='P' AND Subject3='P';

SELECT employee.Emp_Id,employee.Name,employee.Department,employee.Grade,employee.Gender FROM employee
JOIN student ON student.Class_Teacher_Employee_Id=employee.Emp_Id
WHERE (student.Subject1='P') AND (student.Subject2='P') AND (student.Subject3='p');
