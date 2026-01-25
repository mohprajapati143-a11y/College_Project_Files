CREATE TABLE employ (
    empno NUMBER(4),
    ename VARCHAR2(20),
    job   VARCHAR2(20),
    sal   NUMBER(7,2)
);
-------------------------------------------------------------
INSERT INTO employ VALUES (101, 'RAM',   'CLERK', 3000);
INSERT INTO employ VALUES (102, 'SAM',   'MANAGER', 8000);
INSERT INTO employ VALUES (103, 'RAJ',   'CLERK', 3200);
INSERT INTO employ VALUES (104, 'ANU',   'ANALYST', 7000);

COMMIT;
-------------------------------------------------------------
DECLARE
    no NUMBER(3);
BEGIN
    DELETE FROM employ
    WHERE job = '&job';

    IF SQL%ROWCOUNT = 0 THEN
        DBMS_OUTPUT.PUT_LINE('There is no employee doing the job');
    ELSE
        no := SQL%ROWCOUNT;
        DBMS_OUTPUT.PUT_LINE('Employee records deleted successfully');
        DBMS_OUTPUT.PUT_LINE('No of records deleted = ' || no);
    END IF;
END;
/
