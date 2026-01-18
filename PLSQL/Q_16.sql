------------------------------ Create table to store clerks--------------------------------
CREATE TABLE cl_table (
  empno  NUMBER(4),
  ename  VARCHAR2(20),
  sal    NUMBER(8,2),
  job    VARCHAR2(15),
  deptno NUMBER(3)
);

----------------------------- Create table to log operations-------------------------------
CREATE TABLE cursor_ret (
  mess        VARCHAR2(50),
  update_date DATE,
  time        VARCHAR2(10),
  deptno      NUMBER(3),
  name        VARCHAR2(20)
);

------------------- PL/SQL block to insert clerks and log the operation--------------------
DECLARE
  eno    NUMBER(4);
  ename  VARCHAR2(20);
  salary NUMBER(8,2);
  dno    NUMBER(3);
  j      VARCHAR2(15);

  x      NUMBER := 0;
  m      VARCHAR2(50);
  t      VARCHAR2(10);
  uname  VARCHAR2(20);

  CURSOR c1 IS
    SELECT empno, ename, sal, job, deptno
    FROM employee
    WHERE job = 'CLERK';
BEGIN
  uname := '&your_name';

  OPEN c1;
  LOOP
    FETCH c1 INTO eno, ename, salary, j, dno;
    EXIT WHEN c1%NOTFOUND;

    INSERT INTO cl_table VALUES (eno, ename, salary, j, dno);
    x := x + 1;
  END LOOP;
  CLOSE c1;

  DBMS_OUTPUT.PUT_LINE(x || ' clerks inserted into cl_table');

  m := x || ' clerks inserted';
  t := TO_CHAR(SYSDATE, 'HH24:MI');

  INSERT INTO cursor_ret
  VALUES (m, SYSDATE, t, NULL, uname);
END;
/
