SET SERVEROUTPUT ON;
DECLARE
    n NUMBER(3);
    x NUMBER(2) := 1;
    f NUMBER(5) := 1;
BEGIN
    n := &number;
    LOOP
        f := f * x;
        x := x + 1;
        EXIT WHEN x > n;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Factorial of ' || n || ' is = ' || f);
END;
/