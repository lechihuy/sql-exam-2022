print('Chọn loại index?')
print('\t1. CLUSTERED INDEX (mặc định)')
print('\t2. UNIQUE NON-CLUSTERED INDEX')
index_type = input()
index_type = 'CLUSTERED INDEX' if index_type == '1' else 'UNIQUE NON-CLUSTERED INDEX'

print()
print('Tên index?')
index_name = input()

print()
print('Tên cột?')
column_name = input()

print()
print('Sắp xếp?')
print('\t0. Không (Mặc định)')
print('\t1. Tăng dần')
print('\t2. Giảm dần')
sort = input()
if sort == '1':
    column_name += ' ASC'
elif sort == '2':
    column_name += ' DESC'

print()
print('Tên bảng?')
table_name = input()

print()
print('Có option nếu đã có Index trùng tên này rồi thì xóa Index cũ trước đó? (y/n) [n]')
with_drop_existing = input()
with_drop_existing = with_drop_existing == 'y'

print()
sql = f"""
CREATE {index_type} {index_name}
ON {table_name} ({column_name})
{'WITH DROP_EXISTING' if with_drop_existing else ''}
"""

print(sql.strip())
