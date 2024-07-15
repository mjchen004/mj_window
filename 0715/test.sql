SELECT * 
FROM youbike


SELECT DISTINCT sarea
FROM youbike

SELECT sna as 站点,total as 总车辆数,rent_bikes as 可惜,return_bikes as 可借,mayday as 
FROM youbike
WHERE (updatetime,sna) IN (
    SELECT MAX(updatetime),sna
    FROM youbike
    WHERE sarea = '士林区'
    GROUP BY sna
)