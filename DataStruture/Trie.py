
class TrieNode(object):

  def __init__(self, char):
    self.char = char
    self.children = []
    self.word_finished = False
    self.counter = 1
  
def add(root, word):
  """
  Adding a word into the trie tree
  """
  node = root
  for char in word:
    foundInChild = False
    for child in node.children:
      if child.char == char:
        child.counter += 1
        node = child
        foundInChild = True
        break
    if not foundInChild:
      new_node = TrieNode(char)
      node.children.append(new_node)
      node = new_node
  # marked the last word as word finish(leaf)
  node.word_finished = True

def find_prefix(root, prefix):
  """
  """
  node = root
  if not node.children:
    return False, 0
  for char in prefix:
    charNotFound = True
    for child in node.children:
      if child.char == char:
        charNotFound = False
        node = child
        break
    if charNotFound:
      return False, 0
  return True, node.counter

if __name__ == "__main__":
  root = TrieNode('*')
  add(root, "hackathon")
  add(root, "hack")
  add(root, "hello")
  add(root, "hi")
  print(find_prefix(root, "he"))