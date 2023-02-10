import re
import pymysql

import requests
from bs4 import BeautifulSoup as bs

conn = pymysql.connect(host='goeasy-db.clvgcrbhh40l.ap-northeast-2.rds.amazonaws.com',
                       user='admin',
                       password='rhdlwl123!',
                       db='pansoriDB',
                       charset='utf8')

# ids = [64437, 64438, 64439, 64440, 64441, 64442, 64443, 64444, 64445, 64446, 64447, 64448, 64449, 64450, 64451, 64452, 64453, 64454, 64455, 64456, 64457, 64458, 64459, 64460, 64461, 64462, 64463, 64464, 64465, 64466, 64467, 64468, 64469, 64470, 64472, 64473, 64474, 64475, 64476, 64477, 64478, 64481, 64493, 64494, 64495, 64496, 64497, 64498, 64499, 64500,
#        64501, 64502, 64503, 64504, 64506, 64507, 64508, 64509, 64510, 64511, 64512, 64513, 64514, 64515, 64516, 64517, 64518, 64519, 64520, 64521, 64522, 64523, 64524, 64525, 64526, 64527, 64528, 64529, 64530, 64532, 64539, 64541, 64542, 64543, 64544, 64545, 64546, 64547, 64548, 64549, 64550, 64551, 64552, 64555, 64556, 64557, 64558, 64559, 64560, 64561]

sql1 = "select precedent_id from detail_table where content = ''"
sql2 = "insert into detail_table (precedent_id, content) values (%s, %s)"
sql3 = "delete from simple_precedent where precedent_id = %s ;"
# sql = "INSERT INTO user (name, email) VALUES (%s, %s)"

if __name__ == "__main__":
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql1)
            ids = cur.fetchall()
            for index in range(2597, len(ids)):
                print(ids[index][0])
                cur.execute(sql3, ids[index][0])
                conn.commit()
            #     if index[0] == 220261:
            #         data = requests.get(
            #             f"https://www.law.go.kr/LSW/precInfoP.do?precSeq={index[0]}&amp;mode=0")
            #         soup = bs(data.text, "html.parser")
            #         title = soup.select_one('#contentBody > h2')
            #         sub_title = soup.select_one('#contentBody > div.subtit1')
            #         content_elements = soup.select('#conScroll > *')
            #         temp = ""
            #         for elements in content_elements:
            #             test = bs(str(elements).replace("<br/>", "\n"), "html.parser")
            #             p = re.compile('(?<=\【)(.*?)(?=】)')
            #             items = p.findall(test.text)
            #             if len(items) != 0:
            #                 temp += items[0] + "##"
            #             else:
            #                 temp += test.text + "|"
            #         print(index, temp)
                    # cur.execute(sql2, (ids[index][0], temp))
                    # conn.commit()