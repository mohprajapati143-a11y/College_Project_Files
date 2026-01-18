DECLARE
    ch VARCHAR2(1);
BEGIN
    ch := '&char';

    IF ch IN ('a','e','i','o','u','A','E','I','O','U') THEN
        DBMS_OUTPUT.PUT_LINE(ch || ' is a vowel');
    ELSE
        DBMS_OUTPUT.PUT_LINE(ch || ' is a consonant');
    END IF;
END;
/