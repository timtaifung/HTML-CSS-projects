class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_next_node(self, link_node):
    self.link_node = link_node
    
  def get_next_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))

#programming of hanoi application using command interval
stacks=[]
left_pillar=Stack('LEFT')
middle_pillar=Stack('MIDDLE')
right_pillar=Stack('RIGHT')
stacks.append(left_pillar)
stacks.append(middle_pillar)
stacks.append(right_pillar)

# recieving total number of disk for game setup and placing them into left-most pillar
num_disks=int(input('\n\nHow many disks do you want to be challended: '))
while(num_disks<3):
    print('\ndisk number must be more than 3, Try again!')
    num_disks=int(input('\n\nHow many disks do you want to be challended: '))
print('The most effective number of steps you need to solve this is {0}'.format((2**num_disks-1)))
for i in range(num_disks):
    swapped=num_disks-i
    left_pillar.push(swapped)

#fuction for user input
#illustrate the choices which the user have ideally (L/M/R) where each letter input is associated to the pillars
#if user_input===choices, it will return the specific stack(pillar)
def get_input():
    choices=[stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(choices)):
            name=stacks[i].get_name() ; choice=choices[i]
            print('\nEnter {0} for {1}'.format(choice,name))
        user_input=input('')
        if user_input in choices:
            for i in range(len(choices)):
                if user_input==choices[i]:
                    return stacks[i]

#gameplay mechenism
num_user_moves=0
while right_pillar.has_space():
    print('Current Stack:')
    for stack in stacks:
        stack.print_items()
    while True:
        print('\nWhich stack do you want to move from?')
        from_stack=get_input()
        print('\nWhich stack to you want to move to')
        to_stack=get_input()
        #checking in from stack/to stack has space/empty respectively
        if from_stack.is_empty():
            print('Stack is empty! try again')
        elif to_stack.has_space() or from_stack.peek()<to_stack.peek():
            disk=from_stack.pop()
            to_stack.push(disk)
            num_user_moves +=1
            break
        else:
            print('\nInvalid Move, Try again!')

print('GAme Complete! You finished the game in {0} number of steps.'.format(num_user_moves))