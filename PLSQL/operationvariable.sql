SET SERVEROUTPUT ON;
DECLARE
    no1 NUMBER(5);
    no2 NUMBER(5);
    s   NUMBER(5);
    d   NUMBER(5);
    p   NUMBER(5);
    q   NUMBER(5);
    rem NUMBER(5);
BEGIN
    no1 := &number1;
    no2 := &number2;

    s := no1 + no2;
    d := no1 - no2;
    p := no1 * no2;
    q := no1 / no2;
    rem := MOD(no1, no2);

    DBMS_OUTPUT.PUT_LINE('Sum=' || s);
    DBMS_OUTPUT.PUT_LINE('Difference=' || d);
    DBMS_OUTPUT.PUT_LINE('Product=' || p);
    DBMS_OUTPUT.PUT_LINE('Quotient=' || q);
    DBMS_OUTPUT.PUT_LINE('Remainder=' || rem);
END;
/