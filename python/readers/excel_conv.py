from openpyxl import Workbook
from openpyxl import load_workbook


def remove_formating(cell):
	cell.style.alignment.wrap_text = False
	result = ""
	if cell.value == None:
		result = ""
	else:
		result = "%s"%cell.value

		replace_chars = {'\n': ' ', '\r': ' '}

		for k in replace_chars.keys():
			result = result.replace(k, replace_chars[k])
		
	return result

def display_sheets(book):
	worksheet_names = book.get_sheet_names()

	for worksheet_name in worksheet_names:
		ws = book.get_sheet_by_name(worksheet_name)
	
		rows = ws.rows

		disp_object(ws.get_cell_collection())

		print ("\n".join(["="*50,"worksheet title -> " + ws.title,"worksheet highest row -> %s"%ws.get_highest_row(), "worksheet highest coloum -> %s"%ws.get_highest_column(),"="*50]))

		cells = []
		for row in rows:
			cells.append([remove_formating(cell) for cell in row ])

		for c in cells:
			print ("~".join(c))

def disp_object(obj):
	v = dir(obj)
	for i in v:
		if not i[0] == '_':
			print (i)


if __name__ == "__main__":
	delim = "~"
	book = load_workbook('test_book.xlsx')

	display_sheets(book)
