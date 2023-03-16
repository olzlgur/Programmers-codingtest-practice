-- 코드를 입력하세요
select id as "가게 ID", NAME, (c - s) as "결제 횟수" from (SELECT id, NAME from merchants where NAME like "%논현%" or name like "%강남%") as b left outer join 
(select merchant_id, count(*) as c, sum(category) as s from card_usages group by merchant_id) as a 
on a.merchant_id = b.id order by id