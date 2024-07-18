SELECT USER1_ID, USER2_ID
FROM (
        SELECT R1.USER_ID AS USER1_ID, R2.USER_ID AS USER2_ID, COUNT(DISTINCT R1.FOLLOWER_ID) AS COMMONFOLLOWERS
        FROM RELATIONS R1, RELATIONS R2
        WHERE R1.USER_ID < R2.USER_ID AND R1.FOLLOWER_ID = R2.FOLLOWER_ID
        GROUP BY R1.USER_ID, R2.USER_ID
    )
WHERE COMMONFOLLOWERS = (
        SELECT MAX(COUNT(DISTINCT R1.FOLLOWER_ID))
        FROM RELATIONS R1, RELATIONS R2
        WHERE R1.USER_ID < R2.USER_ID AND R1.FOLLOWER_ID = R2.FOLLOWER_ID
        GROUP BY R1.USER_ID, R2.USER_ID
    )