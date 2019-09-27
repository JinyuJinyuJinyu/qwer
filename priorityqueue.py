" simple iterable priority queue (version 1), has basic feature of queue, replace a node "
" if find there a better path by comparing priority, low performance. @Jinyu"

class priorityqueue:

    def __init__(self):
        self.queue = []

    def __repr__(self):
        string = ''
        for n in self.queue:
            string += str(n)
        return string

    def pop(self):
        "pop out highest priority node in queue"
        if self.queue:
            return self.find_first()
        else:
            return 'empty'

    def put(self,node):
        "put new node into queue, by checking whether there already a existing node, if not add the new node, else if "
        "existing node and new node are same but priority, will replace it with higher priority node"
        put = self.compare(node)
        if put:
            self.queue.extend([node])
        else:
            self.queue.extend([node])
        # print(self.queue)

    def compare(self,node):
        "'iterate the priority queue, replace original one if a shorter path to same dest'"
        # if not self.queue:
        #     self.queue.extend([node])

        # loop = True
        # l = len(self.queue) - 1
        # i = 0
        # # first_idx = 0
        # while loop:
        #     if self.queue[i][0] > node[0] and self.queue[i][1] == node[1]:
        #         self.queue.extend(node)
        #         self.queue.remove(self.queue[i])
        #     i += 1
        #     if i > l:
        #         loop = False
        find = False
        if self.queue:
            for n in self.queue:
                if int(n[0]) > int(node[0]) and str(n[1]) == str(node[1]):
                    # print(n)
                    self.queue.remove(n)
                    find = True
        # else:
        #     self.queue.extend([node])
        # if not find:
        #     self.queue.extend([node])
        return find

    def find_first(self):
        "find and pop out highest priority node"
        loop = True
        l = len(self.queue) - 1
        i = 0
        first_idx = 0
        "for LIFO, instead of FIFO when has same priority."
        self.queue = list(reversed(self.queue))
        while loop:
            if self.queue[first_idx][0] > self.queue[i][0]:
                first_idx = i
            i += 1
            if i > l:
                loop = False

        node = self.queue[first_idx]
        self.queue.remove(node)
        self.queue = list(reversed(self.queue))
        return node

    def is_empty(self):
        "return whether the queue is empty"
        if self.queue:
            return False
        else:
            return True



if __name__ == "__main__":
    q = priorityqueue()
    print(q.pop())
    q.put([1,'a'])
    print(q)


