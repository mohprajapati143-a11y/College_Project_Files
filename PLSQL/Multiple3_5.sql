SET SERVEROUTPUT ON;
DECLARE
    no NUMBER(4) := &no;
BEGIN
    IF MOD(no,3)=0 THEN
        IF MOD(no,5)=0 THEN
            DBMS_OUTPUT.PUT_LINE(no || ' is multiple of both 3 and 5');
        ELSE
            DBMS_OUTPUT.PUT_LINE(no || ' is multiple of only 3');
        END IF;
    ELSE
        IF MOD(no,5)=0 THEN
            DBMS_OUTPUT.PUT_LINE(no || ' is multiple of only 5');
        ELSE
            DBMS_OUTPUT.PUT_LINE(no || ' is multiple of none of 3 and 5');
        END IF;
    END IF;
END;
/