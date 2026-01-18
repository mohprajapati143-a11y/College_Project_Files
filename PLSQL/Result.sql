SET SERVEROUTPUT ON;

DECLARE
    r   NUMBER(3);
    s1  NUMBER(2);
    s2  NUMBER(2);
    s3  NUMBER(2);
    t   NUMBER(3);
    a   NUMBER(5,2);
    re  VARCHAR2(6);
    d   VARCHAR2(8);
BEGIN
    r := &no;

    SELECT sub1, sub2, sub3
    INTO s1, s2, s3
    FROM stud
    WHERE sno = r;

    t := s1 + s2 + s3;
    a := ROUND(t / 3, 2);

    IF s1 >= 35 AND s2 >= 35 AND s3 >= 35 THEN
        re := 'pass';
    ELSE
        re := 'fail';
    END IF;

    IF re = 'pass' AND a >= 60 THEN
        d := 'first';
    ELSIF re = 'pass' AND a >= 50 THEN
        d := 'second';
    ELSIF re = 'pass' AND a >= 35 THEN
        d := 'third';
    ELSE
        d := 'nill';
    END IF;

    UPDATE stud
    SET tot = t,
        avr = a,
        res = re,
        div = d
    WHERE sno = r;

    COMMIT;

    DBMS_OUTPUT.PUT_LINE('Total = ' || t);
    DBMS_OUTPUT.PUT_LINE('Average = ' || a);
    DBMS_OUTPUT.PUT_LINE('Result = ' || re);
    DBMS_OUTPUT.PUT_LINE('Division = ' || d);

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Student number not found');
END;
/
