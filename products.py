import os # operating system 作業系統模組

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line: # 不顯示標題
				continue  # 跳到下一迴
			name, price = line.strip().split(',') # strip清掉\n   split(',')用逗點分割
			products.append([name, price])
	return products

# 使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		p = []
		p.append(name)  
		p.append(price)
		products.append(p)  # 22~25 可直接寫成 products.append([name, price])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('商品,價格\n') # 如遇上亂碼 在36'w'後面加上, encoding= 'utf-8'
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查是否有檔案
		products = read_file(filename)
	else:
		print('找不到檔案')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()