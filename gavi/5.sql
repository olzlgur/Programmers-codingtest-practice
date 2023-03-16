-- 코드를 입력하세요
select owner, (abs(x-cX) + abs(y-cY)) as distance from (select * from house_locations) as b inner join 
(select x as cX, y as cY from house_locations where owner = "Carlos") as a
order by distance desc, owner limit 1