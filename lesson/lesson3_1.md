

---

## 建立資料表的語法 test

```sql
CREATE TABLE [IF NOT EXISTS] table_name ( 
    column1 datatype(length) column_constraint, 
    column2 datatype(length) column_constraint, 
    ... 
    table_constraints
    );
```
## 建立一個名為student的資料表
```sql
CREATE TABLE IF NOT EXISTS student(
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE

);

##刪除表格


```sql
DROP TABLE student;
```

## 新增1筆資料

```sql
INSERT INTO student (name, major)
VALUES ('呂郁君','歷史');

```


## 新增多筆資料

```sql
INSERT INTO student (name, major)
VALUES ('小柱','生物'),('信忠','英語');

```