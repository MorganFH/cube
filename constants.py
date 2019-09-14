"""
          / \ 
         /   \ 
        /     \ 
   G   /       \   O
      /         \ 
     /     W     \ 
    | \         / |
    |  \       /  |
    |   \     /   |
    |    \   /    |
    |     \ /     |
    |      |      |
    |   R  |   B  |
     \     |      /
      \    |     /
       \   |    /
        \  |   /
         \ |  /  
          \|/
        
           Y

"""

SIDES = {
    "red": 0,
    "green": 1,
    "orange": 2,
    "blue": 3,
    "white": 4,
    "yellow": 5,
}  # Mapping from center color to side number
OPPOSITES = {
    "white": "yellow",
    "yellow": "white",
    "red": "orange",
    "orange": "red",
    "blue": "green",
    "green": "blue",
}  # remove?
CORNERS = [
    ("white", "blue", "red"),
    ("white", "blue", "orange"),
    ("white", "orange", "green"),
    ("white", "green", "red"),
    ("yellow", "red", "green"),
    ("yellow", "red", "blue"),
    ("yellow", "blue", "orange"),
    ("yellow", "orange", "green"),
]
PIECETYPES = {"center": 0, "edge": 1, "corner": 2}
