password = 'a123456'
enter = input('請輸入密碼： ')
i = 2
if password != enter :
	while i > 0:
		enter = input('密碼錯誤！還有'+str(i)+'次！')
		i = i - 1 
	print('密碼輸入錯誤3次，程式結束！')
else:
		print('輸入成功')
	