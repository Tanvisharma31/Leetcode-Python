# Last updated: 02/03/2026, 13:56:28
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = []
        self.valid = {}

        for user, task, priority in tasks:
            t = (-priority, -task, user)
            self.tasks.append(t)
            self.valid[-task] = t
        
        heapify(self.tasks)
       

    def add(self, userId: int, taskId: int, priority: int) -> None:
        t = (-priority, -taskId, userId)
        self.valid[-taskId] = t
        heappush(self.tasks, t)
        

    def edit(self, taskId: int, newPriority: int) -> None:
        old_pri, old_task, old_user = self.valid[-taskId]
        t = (-newPriority, old_task, old_user)
        self.valid[-taskId] = t
        heappush(self.tasks, t)

    def rmv(self, taskId: int) -> None:
        del self.valid[-taskId]

    def execTop(self) -> int:
        # print(self.tasks)
        # print(self.valid)
        while self.tasks:
            pri, tsk, usr = heappop(self.tasks)

            if tsk not in self.valid:
                continue
            
           
            if self.valid[tsk][0] != pri or self.valid[tsk][2] != usr:
                continue
            
            del self.valid[tsk]
            return usr
            
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
# class TaskManager:

#     def __init__(self, tasks: List[List[int]]):
#         self.tasks_dict = defaultdict(list)
#         self.tasks = []
#         for userId, taskId, priority in tasks:
#             self.tasks_dict[-taskId] = [userId, -priority]
#             self.tasks.append([-priority, -taskId, userId])
        
#         heapify(self.tasks)

#     def add(self, userId: int, taskId: int, priority: int) -> None:
#         self.tasks_dict[-taskId] = [userId, -priority]
#         heappush(self.tasks, [-priority, -taskId, userId])
        
        
#     def edit(self, taskId: int, newPriority: int) -> None:
#         self.tasks_dict[-taskId][1] = -newPriority
#         heappush(self.tasks, [-newPriority, -taskId, self.tasks_dict[-taskId][0]])
        

#     def rmv(self, taskId: int) -> None:
#         del self.tasks_dict[-taskId]
        

#     def execTop(self) -> int:
#         while self.tasks:
#             priority, taskId, userId = heappop(self.tasks)
            
#             if taskId not in self.tasks_dict: continue
#             if self.tasks_dict[taskId][1] != priority or self.tasks_dict[taskId][0]!=userId: continue

#             del self.tasks_dict[taskId]      
#             return userId
        
#         return -1
        

"""  
0: TaskManager - [[[1, 101, 10], [2, 102, 20], [3, 103, 15]]]       -> None  
1: add - [4, 104, 5]                                                -> None  
2: edit - [102, 8]                                                  -> None  
3: execTop - []                                                     -> 3  
4: rmv - [101]                                                      -> None  
5: add - [5, 105, 15]                                               -> None  
6: execTop - []                                                     -> 5  


cmd = 
var = 
out = 
mine = []
for i in range(len(cmd)):
    print(f'{i}: {cmd[i]} - {var[i]}        -> {out[i]}  ') #vs {mine[i]}
    # if out[i] != mine[i]: print('THIS ONE ^^') 
"""

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()