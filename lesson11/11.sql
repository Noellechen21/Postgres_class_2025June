SELECT t1.日期,  t2."stationName" AS 車站, t1.車站代碼, t1.進站人數, t1.出站人數
FROM "每日各站進出站人數" t1
JOIN "台鐵車站資訊" t2 ON t1.車站代碼 = t2."stationCode"
WHERE t1.日期 = '2023-01-05' AND t1.車站代碼 = 900;