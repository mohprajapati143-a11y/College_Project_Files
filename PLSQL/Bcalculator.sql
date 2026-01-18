DECLARE
    msal   NUMBER(7,2) := &msal;
    annsal NUMBER(9,2);
    bonus  NUMBER(7,2);
    doj    DATE := TO_DATE('&date_of_join', 'DD-MM-YYYY');
    exp    NUMBER(5,2);
    totsal NUMBER(9,2);
BEGIN
    exp := ROUND(MONTHS_BETWEEN(SYSDATE, doj) / 12, 2);
    annsal := msal * 12;

    IF exp > 3 THEN
        bonus := annsal * 12 / 100;
    ELSE
        bonus := 1000;
    END IF;

    totsal := msal + bonus;

    DBMS_OUTPUT.PUT_LINE('Annual salary = Rs. ' || annsal);
    DBMS_OUTPUT.PUT_LINE('Experience = ' || exp || ' years');
    DBMS_OUTPUT.PUT_LINE('Bonus amount = Rs. ' || bonus);
    DBMS_OUTPUT.PUT_LINE('Total salary drawn = Rs. ' || totsal);
END;
/
