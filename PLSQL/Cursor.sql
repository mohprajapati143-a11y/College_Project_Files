CREATE TABLE cursor_ret (
    mess        VARCHAR2(30),
    update_date DATE,
    time        VARCHAR2(10),
    deptno      NUMBER(3),
    name        VARCHAR2(10)
);

SET SERVEROUTPUT ON;
DECLARE
    x    NUMBER(4);
    m    VARCHAR2(30);
    t    CHAR(6);
    d    NUMBER(3);
    name VARCHAR2(10) := '';
BEGIN
    d := &DNO;
    name := '&your_name';

    UPDATE employ SET sal = sal + 1000 WHERE dno = d;

    IF SQL%FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Some rows are retrieved by the query');
    ELSIF SQL%NOTFOUND THEN
        DBMS_OUTPUT.PUT_LINE('Query is not able to retrieve any row');
    END IF;

    x := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE(x || ' no. of rows updated');

    m := CONCAT(TO_CHAR(x), ' no of rows updated on');
    t := TO_CHAR(SYSDATE, 'hh24:mi');

    INSERT INTO cursor_ret VALUES(m, SYSDATE, t, d, name);
END;
/