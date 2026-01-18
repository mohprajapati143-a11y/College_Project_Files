DECLARE
    no1 NUMBER(4);
    no2 NUMBER(4);
    no3 NUMBER(4);
BEGIN
    no1 := &number1;
    no2 := &number2;
    no3 := &number3;

    IF no1 > no2 AND no1 > no3 THEN
        DBMS_OUTPUT.PUT_LINE(no1 || ' is the greatest');
    ELSIF no2 > no3 AND no2 > no1 THEN
        DBMS_OUTPUT.PUT_LINE(no2 || ' is the greatest');
    ELSE
        DBMS_OUTPUT.PUT_LINE(no3 || ' is the greatest');
    END IF;
END;
/