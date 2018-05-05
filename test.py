import re
import datetime
# pattern1 = "ngày ([0-9]{1,2}) (.*)"
# pattern2 = "ngày ([0-9]{1,2}) tháng ([0-9]{1,2})"
# pattern3 = "ngày ([0-9]{1,2}/[0-9]{1,2})"
# pattern4 = "(ngày |)(([0-9]{1,2})|([0-9]{1,2}/[0-9]{1,2})|([0-9]{1,2}/[0-9]{1,2}/[0-9]{4}))"
# pattern5 = "(2|3|4)"
#
# str = "3"
#
# b = re.match(pattern5,str)
#
# if b :
#     print(b.group(0))
#     print(b.group(1))
#
#
#     print(True)
# else :
#     print(False)
# patterns1 ="(?:nd|st|rd|th)?"
# s = re.match(patterns1,"st")
# print(s.group(0))
# msg = " 17:17:12 va 20:56"
# patterns2 = re.findall(r'\D(?:(00|[0]?[2-9]|[0]?1[0-9]?|2[0-3]):([0-5]?[0-9]))', msg)
# patterns3 = re.findall('\D(0?[0-9]|1[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9])', msg)
#
# # for pattern in patterns2:
# #     print(pattern)\D
# print(patterns2)
# print(patterns3)

# big_pattern1 = r'([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)/(?:\s*)(1[0-2]|0?[1-9])|' + \
        #                r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)tháng(?:\s*)(1[0-2]|0?[1-9])(?:\s*)năm(?:\s*)(2[0-9]{3})|' + \
        #                r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)tháng(?:\s*)(1[0-2]|0?[1-9])|' + \
        #                r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])|' + \
        #                r'(?:[^0-9\w]|^)tháng(?:\s*)(1[0-2]|0?[1-9])(?:\s*)năm(?:\s*)(2[0-9]{3})|' + \
        #                r'(?:[^0-9\w]|^)tháng(?:\s*)(1[0-2]|0?[1-9])|' + \
        #                r'(?:[^0-9\w]|^)năm(?:\s*)(2[0-9]{3})'
# msg ="11 giờ hoăc 23 gi"
# patterns4 = re.findall(r'(?:(?:[^0-9\w]|^)([0:1]?[0-9]|2[0-3])(?:\s*)giờ)',msg)
# print(patterns4)
#
# a = {"1":1,"2":3}
# b = {"1":3,"4":4}
# c = {}
# c.update(a)
# c.update(b)
# print("3" in a.keys())
#
# a = [{"1":1,"2":2},{"1":2,"2":4}]
# b = [{"1":1,"2":2},{"1":3,"2":5}]
# print({"1":2,"2":4} in a)
# print(a)
# a.remove({"1":1,"2":2})
# print(a)
#
# c = a.copy()
# print(c)
# c.append("4")
# print(a)
# print(c)
#
# for i in range(100):
#     if i != 10:
#         print(i)
#     else:
#         break


# cur = datetime.datetime.now()
# day_week = cur.weekday()
# fu = cur + datetime.timedelta(6)
# a = cur - datetime.timedelta(day_week)
# print(cur + datetime.timedelta(-3))
# for i in range(7):
#     print(a + datetime.timedelta(i))

# print(fu)

# a = {}
# a["a"] = 1
# print("a1" in a)
#
# for i in range(10,20):
#     print(i)

import datetime

a= datetime.datetime.now()
print(a)
print(type(a))


