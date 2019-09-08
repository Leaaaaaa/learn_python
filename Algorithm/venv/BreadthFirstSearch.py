from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire" ]
graph["bob"] = ["anju", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anju"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]#注意这里是[]而不是（）!!!
    searched =[]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + "is a mango seller")
                return True
            else:
                search_queue += graph[person]  #注意这里是[]而不是（）!!!
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search("you")