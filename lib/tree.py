class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    
    def depth_search(node):
      if node['id'] == id:
        return node
      
      for child in node.get('children', []):
        result = depth_search(child)
        if result:
            return result 
    
      return None
    
    if self.root:
      return depth_search(self.root)
    else: 
      return None