SELECT EMP_ID, FIRSTNAME, LASTNAME, MAX(SALARY) as SALARY, DEPARTMENT_ID FROM SALARY GROUP BY EMP_ID,FIRSTNAME, LASTNAME, DEPARTMENT_ID ORDER BY EMP_ID