WITH J AS (
    SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
)
SELECT FLAVOR
FROM FIRST_HALF AS H
JOIN J AS J
USING (FLAVOR)
ORDER BY (H.TOTAL_ORDER + J.TOTAL_ORDER) DESC
LIMIT 3;