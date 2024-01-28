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
        # self.same_cage = first in second
        
        self.domain_changed = None
        self.domain_emptied = False
    
    # only needs to check for 'cage' part
    def enforce_consistency(self):
        
        if self.same_cage:
            for f_value in self.first.domain:
                is_valid = False
                for s_value in self.second.domain:
                    pass
                