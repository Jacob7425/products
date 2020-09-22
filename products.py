import os # operating system 作業系統模組

#讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查是否有檔案
	with open('products.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line: # 不顯示標題
				continue  # 跳到下一迴
			name, price = line.strip().split(',') # strip清掉\n   split(',')用逗點分割
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')

# 使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = []
	p.append(name)  
	p.append(price)
	products.append(p)  # 23~26 可直接寫成 products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w') as f:
	f.write('商品,價格\n') # 如遇上亂碼 在34'w'後面加上, encoding= 'utf-8'
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')