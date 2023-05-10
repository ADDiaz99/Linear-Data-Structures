from node import Node
class LinkedList:
	def __init__(self):
		self.head=None

	def insert_at_begining(self, data):
		node=Node(data,self.head)
		self.head=node

	def insert_at_end(self, data):
		#caso de que sea el primero
		if self.head is None:
			self.head=Node(data, None)
			return
		itr =self.head
		while itr.next:
			itr=itr.next

		itr.next=Node(data, None)

	#de una Lista a una LinkedList
	def insert_value_from_list(self, data_list):
		self.head=None
		for data in data_list:
			self.insert_at_end(data)
def print(self):
		if self.head is None:
			print("Linked list is empty")
			return

		itr=self.head
		llstr=''
		
		while itr:
			llstr+=str(itr.data) + '-->'
			itr =itr.next

		print(llstr)
	
if __name__=="__main__":
	ll=LinkedList()
	ll.insert_value_from_list(["banana","mango","fresa"])
	ll.print()