---------------------------------------------------------------------------------------------CREATE TABLE cursor_ret (
    mess        VARCHAR2(30),
    update_date DATE,
    time        VARCHAR2(10),
    deptno      NUMBER(3),
    name        VARCHAR2(10)
);



DECLARE
    x       NUMBER(4);
    m       VARCHAR2(30);
    t       VARCHAR2(10);
    d       NUMBER(3);
    v_name  VARCHAR2(10);
BEGIN
    d      := &DNO;
    v_name := '&your_name';

    UPDATE employee 
    SET sal = sal + 1000
    WHERE deptno = d;

    IF SQL%FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Some rows are updated by the query');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Query did not update any row');
    END IF;

    x := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE(x || ' number of rows updated');

    m := x || ' rows updated on';
    t := TO_CHAR(SYSDATE, 'HH24:MI');

    INSERT INTO cursor_ret (mess, update_date, time, deptno, name)
    VALUES (m, SYSDATE, t, d, v_name);
END;
/