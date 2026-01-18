DECLARE
    num NUMBER(5);
BEGIN
    num := &number;

    IF MOD(num,3)=0 AND MOD(num,7)=0 THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is multiple of both 3 and 7');
    ELSIF MOD(num,3)=0 THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is multiple of only 3');
    ELSIF MOD(num,7)=0 THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is multiple of only 7');
    ELSE
        DBMS_OUTPUT.PUT_LINE(num || ' is multiple of neither 3 nor 7');
    END IF;
END;
/