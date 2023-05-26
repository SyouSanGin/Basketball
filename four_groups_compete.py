from group import Group
import random
"""
usage:
abstraction of the first stage
"""
class FourGroups:
    
    static_order:tuple = (
        (0,0,3,1),
        (0,1,3,0),
        (1,0,2,1),
        (1,1,2,0)
        )
    
    """
    usage:
    construct the FourGroups object
    
    para:
    group: list[Group] => the winner in the four groups
    
    attention:
    the length of groups must be four
    """
    def __init__(self, groups_winner: list):
        assert len(groups_winner) == 4
        self.groups_winner:list = groups_winner
        self.info :list[str] = list()
        
    """
    usage:
    simulate the competitions
    
    ret:
    tuple[str, list]
    
    the first one is the final winner
    the second one is the record process
    """
    def compete(self):
        idx_q_winner : list[int]= [0,0,0,0]
        for idx, order in enumerate(FourGroups.static_order):
            scale:float = self.groups_winner[order[0]][0][order[1]][1] /(self.groups_winner[order[0]][0][order[1]][1] + self.groups_winner[order[2]][0][order[3]][1])
            if random.random() < scale:
                idx_q_winner[idx] =100 + order[0]*10+order[1]
                self.info.append((self.groups_winner[order[0]][0][order[1]][0], self.groups_winner[order[2]][0][order[3]][0]))
            else:
                idx_q_winner[idx] = 100 + order[2] * 10 + order[3]
                self.info.append((self.groups_winner[order[2]][0][order[3]][0], self.groups_winner[order[0]][0][order[1]][0]))
        
        idx_s_winner : list[int] = [0,0]
        for i in range(2):
            cpt1 = idx_q_winner[i]
            cpt2 = idx_q_winner[i+2]
            
            mainid1 = (cpt1 // 10) % 10
            mainid2 = (cpt2 // 10) % 10
            subid1 = cpt1 % 10
            subid2 = cpt2 % 10
            
            scale: float = self.groups_winner[mainid1][0][subid1][1] / (self.groups_winner[mainid1][0][subid1][1] + self.groups_winner[mainid2][0][subid2][1])

            if random.random() < scale:
                idx_s_winner[i] = cpt1
                self.info.append((self.groups_winner[mainid1][0][subid1][0],self.groups_winner[mainid2][0][subid2][0]))
            else:
                idx_s_winner[i] = cpt2
                self.info.append((self.groups_winner[mainid2][0][subid2][0], self.groups_winner[mainid1][0][subid1][0]))
        mainid1 = (idx_s_winner[0] // 10) % 10
        mainid2 = (idx_s_winner[1] // 10) % 10
        subid1 = idx_s_winner[0] % 10
        subid2 = idx_s_winner[1] % 10
        scale: float = self.groups_winner[mainid1][0][subid1][1] / (self.groups_winner[mainid1][0][subid1][1] + self.groups_winner[mainid2][0][subid2][1])
        if random.random() < scale:
            self.info.append(f"{self.groups_winner[mainid1][0][subid1][0]} > {self.groups_winner[mainid2][0][subid2][0]}")
            return self.groups_winner[mainid1][0][subid1][0], self.info
        else:
            self.info.append((self.groups_winner[mainid2][0][subid2][0], self.groups_winner[mainid1][0][subid1][0]))
            return self.groups_winner[mainid2][0][subid2][0], self.info
        
        

            