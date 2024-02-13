class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start):
	current = start
	if current is None:
		return
	print(current.data, end=' ')
	while current.link is not None:
		current = current.link
		print(current.data, end=' ')
	print()

def make_simple_linked_list(name_phone):
	global head, current, pre
	print_nodes(head)

	node = Node()
	node.data = name_phone
	if head is None:
		head = node
		return

	if head.data[0] > name_phone[0]:
		node.link = head
		head = node
		return


	current = head
	while current.link is not None:
		pre = current
		current = current.link
		if current.data[0] > name_phone[0]:
			pre.link = node
			node.link = current
			return

	current.link = node

head, current, pre = None, None, None
data_array = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]

if __name__ == "__main__":

	for data in data_array:
		make_simple_linked_list(data)

	print_nodes(head)