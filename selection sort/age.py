# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
ml=[{
    "name":"dhanush",
    "age" :18,
    "mark":596},
    { "name":"madan",
    "age":18,
    "mark":516},
    { "name":"dhanush",
    "age":19,
    "mark":596},
    { "name":"thanush",
    "age":18,
    "mark":526},
    { "name":"andhar",
    "age":16,
    "mark":516}
    ]
    
for el in range(len(ml)):
    small=el
  
    for swap in range(el,len(ml)):
        if ml[small]["mark"]<ml[swap]["mark"]:
            small=swap
            
    if ml[el]["mark"]==ml[small]["mark"]:
        if ml[el]["age"]>ml[small]["age"]:
            ml[el],ml[small]=ml[small],ml[el] 
            
    else:
        ml[el],ml[small]=ml[small],ml[el]
print(ml)
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    