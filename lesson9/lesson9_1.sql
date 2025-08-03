SELECT *
FROM "台鐵車站資訊"

SELECT count (*) AS "筆數"
FROM "台鐵車站資訊"

/* 值用單引號，有大小寫但不想要動的要用雙引號*/
/*選擇地址中包含臺北的*/
SELECT *
FROM "台鐵車站資訊"
WHERE "stationAddrTw" LIKE '%臺北%'

SELECT count(name) AS "臺北車站數"
FROM "台鐵車站資訊"
WHERE "stationAddrTw" LIKE '%臺北%'

/*將兩個表結合*/
SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "stationName" = '基隆'

/*執行join後，車站代碼，站點可能會重複*/

SELECT count(*)
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "stationName" = '基隆'
/*看一下基隆有幾筆，得到 1714筆*/

/*寫清楚是哪個表的什麼去join*/
SELECT count(*)
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE "stationName" = '基隆'

/*全台各站點2022年進站總人數*/
SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
GROUP BY "name"
/*使用group by時 Select那裏需要使用聚合函式，否則會報錯，以上是錯誤示範*/

/*使用group by時需要使用聚合函式，否則會報錯*/
SELECT count("name")
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
GROUP BY "name"

SELECT "stationName" AS 站名, count("name") AS 筆數
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
GROUP BY "name"
/*上面是錯誤示範，使用group by時，欄位名稱要用group by有選擇到的欄位*/

SELECT "name" AS 站名, count("name") AS 筆數
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
GROUP BY "name"
/*更新後就對了*/

SELECT "name" AS 站名, count("name") AS 筆數, AVG("進站人數")AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
GROUP BY "name"
/*("進站人數")AS "進站人數"* 這是平均每天的進站人數*/

/*加入條件*/
SELECT "name" AS 站名, count("name") AS 筆數, AVG("進站人數")AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name"

/*取出date,年份的function : date_part *//*這是錯誤示範，因為group by沒有年份*/
SELECT "name" AS 站名,date_part('year',"日期" ) AS 年份 ,count("name") AS 筆數, AVG("進站人數")AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name"

/*更新後就對了*/
SELECT "name" AS 站名,date_part('year',"日期" ) AS 年份 ,count("name") AS 筆數, AVG("進站人數")AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name", "年份"

/*不選擇年份*/
SELECT "name" AS 站名,date_part('year',"日期" ) AS 年份 ,count("name") AS 筆數, AVG("進站人數")AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
GROUP BY "name", "年份"

/*加入條件*/
SELECT "name" AS 站名,date_part('year',"日期" ) AS 年份 ,count("name") AS 筆數, AVG("進站人數")AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "name" = '基隆'
GROUP BY "name", "年份"

SELECT "name" AS 站名,date_part('year',"日期" ) AS 年份 ,count("name") AS 筆數, AVG("進站人數")AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "name" = '基隆'
GROUP BY "name", "年份"
ORDER BY "進站人數" DESC; 