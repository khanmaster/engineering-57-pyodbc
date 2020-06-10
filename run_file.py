from db_products_oop import DBProduct_table


product_table = DBProduct_table()

print(product_table.get_by_id(1))

print(product_table.get_all())

print(product_table.get_all('Chef'))