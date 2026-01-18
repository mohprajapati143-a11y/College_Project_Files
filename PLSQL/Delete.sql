SET SERVEROUTPUT ON;
DECLARE
    no NUMBER(3);
BEGIN
    DELETE FROM employ WHERE job = '&job';

    IF SQL%NOTFOUND THEN
        DBMS_OUTPUT.PUT_LINE('There is no employee doing the job');
    ELSIF SQL%FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Some data has been retrieved by the cursor');
    END IF;

    no := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE('No of records deleted = ' || no);
END;
/