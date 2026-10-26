# Collection of properties or methods.
# Collection of attributes or methods.

# attributes    :   variablename = variablevalue   / key+value
# methods : function


# Create Empty Dict : 
# my_dict = {}
# print(my_dict,type(my_dict))

# user = {
#     # keys          values
#     "firstname" : "Raj",         # attribute
#     "lastname" : "shah"
# }

# print(user,type(user))  :


product = {
    "brand" : "vivo",
    "price" : 19999.0,
    "category" : "Mobile",
    "quantity" : 11
}

# Attribute/property : pair -> key (str) + value(any)

# How to Print Dict : 
# print(product)


# How to Print Property value : 
#1. get method : return  : property value / None
# print(product.get("category"))
# print(product.get("price"))
# print(product.get("model"))


# Add new Property or Modify Property value : 

# product.update
# product.update("model","xyz")      # error
# Add : 
# product.update({"model":"xyz"})
# Modify : 
# product.update({"quantity":10})

# product.update(["model","xyz"])      # error

# print(product)


# product.setdefault
# Add : 
# product.setdefault("model")      # model : None

# product.setdefault("model",12)

# product.setdefault("quantity",100)

# print(product)

# Add : 
# product.__setitem__("model","xyz")
# Modify :
# product.__setitem__("quantity",[11,12])


# print(product)

# product.pop("quantity")


# print(product)


# product.clear()
# print(product)

# product.fromkeys
# product.items
# product.keys
# product.values



