
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for message in f:
			lines.append(message.strip())
	return lines
# .strip()用來去除換行符號 \n

def convert(lines):
	new = []
	# 如果對話非人名開頭程式碼會找不到person當掉=>需給default值
	# 但此時確實沒人名 此情況適合用python特殊的default:None
	person = None 

	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
		# 如果person有值才執行
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for message in lines:
			f.write(message + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()


#1.寫良好的程式碼架構
#2.轉換好的function中,使用了continue來跳到下一行
#3.None適合用來當預設值