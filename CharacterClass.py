# Make a sub classes of Mario video game characters
        # Mario     # Luigi     # Toad      # Princess
# Speed     4           3           5           2
# Jump      4           5           2           3
# Power     4           3           5           2
# Skill     None        None        None      Float Jump
import random
import time

class Character:
    def __init__(self, speed, jump, power, skill):
        self.speed = speed
        self.jump = jump
        self.power = power
        self.skill = skill
        self.xpos = 0
        self.ypos = 0
    
    def run(self, steps):
        time = steps * self.speed 
        x = self.xpos + steps
        self.xpos = x
        return f"Time:{time} Xpos: {self.xpos}" # in seconds
    
    def try_jump(self):
       y = self.ypos + self.jump
       self.ypos = y
       print(self.ypos)
       y = self.ypos - self.jump
       self.ypos = y
       time.sleep(0.5)
       return self.ypos

    def lose_power(self):
        new_val = self.power - 1
        self.power = new_val
        if self.power < 0:
            raise ValueError("Dead")
    
    def gain_power(self, amount):
        new_val = self.power + amount
        self.power = new_val
        if self.power > self.max_power or self.power < 0:
            raise ValueError("Power too high")
    
    def apply_skill(self):
        if self.skill is not None:
            return f"Used Skill {self.skill} and killed {random.randint(1,100)}"

class Mario(Character):
    max_power = 4
    def __init__(self,speed, jump, power, skill):
        super().__init__(speed, jump, power, skill)

class Luigi(Character):
    max_power = 3
    def __init__(self,speed, jump, power, skill):
        super().__init__(speed, jump, power, skill)

class Toad(Character):
    max_power = 5 
    def __init__(self,speed, jump, power, skill):
        super().__init__(speed, jump, power, skill)

class PrincessToadStool(Character):
    max_power = 2
    def __init__(self,speed, jump, power, skill):
        super().__init__(speed, jump, power, skill)

# Instances
mario_1 = Mario(4, 4, 4, None)
luigi_1 = Luigi(3,5,3, None)
toad_1 = Toad(5,2,5, None)
princess_1 = PrincessToadStool(2,3,3, "Float Jump")
