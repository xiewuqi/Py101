formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) 
print formatter % ("noe", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (    
	"I had this thing.",
	"That you could type up right.",
	"But it did't sing.",
	"So I said goodnight."
)