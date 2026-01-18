DECLARE
    num NUMBER(5);
BEGIN
    num := &number;

    IF num > 0 THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is positive');
    ELSIF num < 0 THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is negative');
    ELSE
        DBMS_OUTPUT.PUT_LINE(num || ' is equal to zero');
    END IF;
END;
/