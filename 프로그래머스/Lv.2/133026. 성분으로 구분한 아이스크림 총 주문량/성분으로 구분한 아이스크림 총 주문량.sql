/*Date
- 241111
*/
SELECT
    b.INGREDIENT_TYPE
    , SUM(a.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF a
INNER JOIN ICECREAM_INFO b ON a.FLAVOR = b.FLAVOR
GROUP BY b.INGREDIENT_TYPE
ORDER BY a.TOTAL_ORDER;