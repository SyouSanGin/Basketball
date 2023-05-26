import random
"""
usage:
abstraction of the first stage
"""
class Group:
    
    """
    usage:
    construct the Group object
    
    para:
    name_list: the names of different teams, a list
    ability: the ability teams, a list
    """    
    def __init__(self, name_list : list[str], ability : list[float]):
        self.name_list = name_list
        self.ability = ability
        self.rec : list[int] = [int(0) for _ in range(len(self.name_list))]
        self.info : list = list()
        
        
    """
    usage:
    generate the qualifier
    
    para:
    n_qualifier: the number of qualifiers to generate
    
    ret:
    tuple[list, list, list]
    the first one is the qualifiers
    the second one is the record of the process
    the third one is the record
    """
    
    def get_qualifier(self, n_qualifier: int)->tuple[list, list]:
        for i in range(len(self.name_list)):
            for j in range(i+1, len(self.name_list)):
                scale : float = self.ability[i] / (self.ability[i] + self.ability[j])
                if random.random() < scale:
                    self.rec[i] += 1
                    self.info.append((self.name_list[i] , self.name_list[j]))
                else:
                    self.rec[j] += 1
                    self.info.append((self.name_list[j] ,self.name_list[i]))
        idx_rec_sorted = sorted(list(zip([i for i in range(len(self.name_list))], self.rec)), key = lambda x: x[1], reverse=True)
        res = [(self.name_list[idx_rec_sorted[i][0]], self.ability[idx_rec_sorted[i][0]]) for i in range(n_qualifier)]        
        return res, self.info, idx_rec_sorted
        
        