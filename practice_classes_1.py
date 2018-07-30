class Clothing(object):
	def __init__(self, color, kind, length, style):
		self.color = color
		self.kind = kind
		self.length = length
		self.style = style



shirt_1 = Clothing("Blue", "Shirt", "Short", "Casual")

print shirt_1.color
