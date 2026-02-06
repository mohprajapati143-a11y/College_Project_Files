DECLARE
   TYPE marks_varray IS VARRAY(5) OF NUMBER;
   marks marks_varray := marks_varray(85, 90, 78, 88, 92);
BEGIN
   FOR i IN 1 .. marks.COUNT LOOP
      DBMS_OUTPUT.PUT_LINE('Mark ' || i || ' = ' || marks(i));
   END LOOP;
END;
/
