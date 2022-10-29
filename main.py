import shape_calculator


rect=shape_calculator.Rectangle(10,5)
#x.print()
print(rect.get_area())
rect.set_height(3)
print(rect.get_area())
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

print()
sq=shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)	
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

