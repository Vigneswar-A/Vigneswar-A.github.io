SELECT USER_ID, USER_NAME, CREDIT, (CASE WHEN CREDIT >= 0 THEN 'No' ELSE 'Yes' END) as credit_limit_breached from (SELECT U.USER_ID, U.USER_NAME, U.CREDIT+SUM(CASE WHEN T.PAID_TO=U.USER_ID THEN T.AMOUNT ELSE 0 END) - SUM(CASE WHEN T.PAID_BY=U.USER_ID THEN T.AMOUNT ELSE 0 END) AS CREDIT FROM USERS U, TRANSACTIONS T GROUP BY U.USER_ID, U.CREDIT, U.USER_NAME)