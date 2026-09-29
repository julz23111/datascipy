from pythonds3.basic import Stack

test_balanced = """<html>
   <head>
      <title> 
         Example 
      </title>
   </head>
 
   <body>
      <h1> Hello, world </h1>
   </body>
</html>
"""
   
test_mismatch ="""<html>
   <body>
      <h1> Hello, world </h2>
   </body>
</html>
"""

test_missingClose =  """<html>
   <head>
      <title> Example </title>
   </head>
   <body>
      <h1> Hello, world </h1>
</html>
"""

test_extraClose = """<html>
   <body>
   </body>
</html>
</div>
"""
#i = test_balanced.index('/')
#print(i)
class Tag:
   def __init__(self, tag):
      self.items = []
   def push(self, item):
      self.items.append(item)
   def pop(self):
      return self.items.pop()
   def is_empty(self):
      return self.items == []
def check_tags(htmlStr):
   s = Stack()
   matching_tags = {
      'html':'html',               
      'head':'head', 
      'title':'title', 
      'body':'body', 
      'h1':'h1'                       
   }
   for tag in htmlStr.split():
      if tag[0] == '<' and tag[1] != '/':
         s.push(tag)
      elif tag[0:2] == '</':
         if s.is_empty():
            return False
         else:
            top_tag = s.pop()
            if matching_tags[top_tag[1:-1]] != tag[2:-1]:
               return False
   return s.is_empty()

test_cases = [test_balanced, test_mismatch, test_missingClose, test_extraClose]
for i, test_case in enumerate(test_cases):
   result = check_tags(test_case)
   print(f"Test case {i+1}: {'Balanced' if result else 'Not Balanced'}")