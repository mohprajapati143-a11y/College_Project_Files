DECLARE
    no1 NUMBER(5);
    no2 NUMBER(5);
BEGIN
    no1 := &number1;
    no2 := &number2;

    IF no1 >= no2 THEN
        DBMS_OUTPUT.PUT_LINE(no1 || ' is greatest');
    ELSE
        DBMS_OUTPUT.PUT_LINE(no2 || ' is greatest');
    END IF;
END;
/