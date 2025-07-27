/*將車站名稱改為唯一值*/

ALTER TABLE "台鐵車站資訊" ADD PRIMARY KEY("stationCode") ;


/*有中文字時最好加上雙引號*/

/*單寫stationCode執行後會變成小寫，老師發現要加上""*/