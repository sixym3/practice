# def my_function():
#   print("Hello from a function")

# def function_A(child3, child2, child1): 
#   print("The youngest child is " + child3)

# function_A(child1 = "Emil", child2 = "Tobias", child3 = "Eric")


# def function_B(*kids): ## Pass in parameters as a tuple and access it with indexing
#   print("The youngest child is " + kids[2])

# function_B("Emil", "Tobias", "Linus")


def function_C(**kid): ## This way the function will receive a dictionary of arguments, and can access the items accordingly:
  print("His last name is " + kid["lname"])

function_C(fname = "Tobias", lname = "Refsnes")