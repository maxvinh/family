database = {
	'home': 'ngoi nha',
	'baby': 'em be'
}
def show_menu():
	print("-----------------------------------")
	print("CHUONG TRINH TU DIEN")
	print("1. Them tu")
	print("2. Tim tu")
	print("3. Xoa tu")
	print("4. Xem tat ca tu")
	print("An 0 de thoat chuong trinh")

show_menu()

choice = input("Ban muon lam gi")

while  choice != 0:
	if choice == 0:
		break
	elif choice == 1:
		add()
	elif choice == 2:
		find()
	elif choice == 3:
		delete()
	elif choice == 4:
		view_all()
else:
		print("Khong co lua chon nao")

	