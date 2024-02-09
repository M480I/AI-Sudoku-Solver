class Arc:
    """ 
    each Arc has two cells "first" and "second"
    for every value in "first"'s domain
    there exits a value in "second"'s domain 
    that violates no constraints
    (second has it's domain changed)
    """
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second
        
        if self.first.cage is self.second.cage:
            self.cage = self.first.cage
        else:
            self.cage = None
        
        self.domain_changed = False
        self.domain_emptied = False
    

    def enforce_consistency(self):
        
        if self.first.number:
            new_domain = [self.first.number]
        
        else:
            new_domain = list(set(self.first.domain) & set(self.first.rcs_domain))
        
        if len(self.first.cage.cells) == 1:
            new_domain = list(set(new_domain)&{self.first.cage.goal_sum})
        
        new_domain_tmp = new_domain[:]
        
        can_not_same = False
        if self.first in self.second.connected_cells_rcs:
            can_not_same = True
        
        if self.cage is not None:
            for f_value in new_domain_tmp:
                
                valid = False
                
                for s_value in self.second.domain:
                    if ((not can_not_same or f_value != s_value)
                        and self.cage.is_valid_arc(
                        first=self.first,
                        first_value=f_value,
                        second=self.second,
                        second_value=s_value)):
                            valid = True
                        
                if not valid:
                    new_domain.remove(f_value)
        
                                
        if len(self.first.domain) == len(new_domain):
            return
        
        self.domain_changed = True
        
        self.first.domain = new_domain
        
        if len(new_domain) == 1:
            self.first.set_number(new_domain[0])
    
        elif not new_domain:
            self.domain_emptied = True
            