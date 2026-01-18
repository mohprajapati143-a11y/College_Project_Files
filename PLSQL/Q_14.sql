-----------------------------------------Create Employee-------------------------------------DECLARE
    x NUMBER(4);
BEGIN
    UPDATE emp
    SET sal = sal + 1000
    WHERE deptno = 10;

    x := SQL%ROWCOUNT;

    DBMS_OUTPUT.PUT_LINE(x || ' number of rows updated');
END;
/
-------------------------------------RUN---------------------------------------------------
DECLARE
    x NUMBER(4);
BEGIN
    DELETE FROM employee
    WHERE job = '&job';

    x := SQL%ROWCOUNT;

    DBMS_OUTPUT.PUT_LINE(x || ' number of rows deleted');
END;
/
---------------------------------ROW UPDATE------------------------------------------------
DECLARE
    x NUMBER(4);
BEGIN
    UPDATE employee
    SET sal = sal + 1000
    WHERE deptno = &dno;

    IF SQL%FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Some rows are updated by the query');
    ELSIF SQL%NOTFOUND THEN
        DBMS_OUTPUT.PUT_LINE('Query did not update any row');
    END IF;

    x := SQL%ROWCOUNT;

    DBMS_OUTPUT.PUT_LINE(x || ' number of rows updated');
END;
/
