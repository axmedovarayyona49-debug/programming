from dataclasses import dataclass , field
from typing import List 



@dataclass
class Member:
    name: str
    member_id: str
    sessions_attended: int = 0
    calories_burned : List[int] = field(default_factory= list)

    def log_session(self , calories: int):
        self.sessions_attended += 1
        self.calories_burned.append(calories)
    def avg_calories(self) -> float:
     if self.sessions_attended == 0:
            return 0.0
     return sum(self.calories_burned)   / self.sessions_attended
    
@dataclass
class FitnessClass:
    class_name : str
    instructor : str
    capacity: int
    members : List [Member] = field(default_factory = list)
    enrolled: int = field (init = False)
     
    def __post_init__(self):
        self._refresh()
    def _refresh(self):
        self.enrolled = len(self.members)

    def enroll(self , member: Member) -> bool:
            if self.enrolled >= self.capacity:
                return False
            self.members.append(member)
            self._refresh()
            return True
    def best_performer(self) -> str:
        if not self.members:
            return "No data "
        best = None
        best_avg = 0
        for m in self.members:
            avg = m.avg_calories()
            if avg > best_avg:
                best_avg = avg
                best = m 
        if best is None or best_avg == 0:
            return "No data"
            
        return best.name
    def class_stats(self) -> str:
        result = f"{self.class_name} ({self.instructor}):\n"
        for m in self.members:
            avg = m.avg_calories()
            result += f"{m.name} - {m.sessions_attended} sessions , avg{avg:.1f} cal\n"
        result += f"Enrolled:{self.enrolled}/{self.capacity}"
        return result
         
m1 = Member("Alice", "M001")
m2 = Member("Bob", "M002")
m3 = Member("Charlie", "M003")

m1.log_session(350)
m1.log_session(420)
m1.log_session(380)
m2.log_session(500)
m2.log_session(450)
m3.log_session(300)

fc = FitnessClass("HIIT", "Coach Dana", 3)
print(fc.enroll(m1))
print(fc.enroll(m2))
print(fc.enroll(m3))
print(fc.enroll(Member("Dave", "M004")))
print(fc.enrolled)
print(fc.best_performer())
print(fc.class_stats())
         
         
        
        

                 

