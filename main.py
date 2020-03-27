from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)[1:]


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
pattern_phone = re.compile(r'\+?(7|8)\s*\(?(\d{3})\)?\s*\-?(\d{3})-?\s*(\d{2})-?\s*(\d{2})\s*\(?(доб.)?\s*(\d*)\)?')
pattern_mail = re.compile(r'([\dA-Za-z\.]*)@([a-z]*)\.([a-z]*)')
pattern_name_job = re.compile(r'([А-Я][а-я]+)\s*,*([А-Я][а-я]+)\s*,*([А-Я]?[а-я]*)\s*,*([А-Я]*[а-я]*)\s*,*([^,\dA-Za-z+]*)')

sub_name_job = r'\1, \2, \3, \4, \5'
sub_phone = r' +7(\2)\3-\4-\5 \6\7'
sub_mail = r' \1@\2.\3'

phone_book = []

for contact in contacts_list:
    contact = ','.join(contact)
    record = pattern_name_job.sub(sub_name_job, contact)
    record = pattern_phone.sub(sub_phone, record)
    record = pattern_mail.sub(sub_mail, record)
    record = record.split(',')
    record = [x.strip() for x in record]
    phone_book.append(record)

res = []

while phone_book:
    single = phone_book.pop(0)
    for record in phone_book:
        if record[:2] == single[:2]:
            rec = []
            double = list(zip(record, single))
            for pair in double:
                if pair[0]:
                    rec.append(pair[0])
                else:
                    rec.append(pair[1])
            rec = [x for x in rec if x != '']
            res.append(rec)
        else:
            if not single in res:
                single = [x for x in single if x != '']
                res.append(single)


#print(phone_book)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(res)
