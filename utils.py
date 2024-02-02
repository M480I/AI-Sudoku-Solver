from arc import Arc


INF = 10000000


def enforce_consistency(arcs: list):
    while arcs:
        arc = arcs.pop()
        
        arc.enforce_consistency()
        
        if arc.domain_emptied:
            return False
        
        if arc.domain_changed:
            first = arc.first
            for cell in first.connected_cells:
                
                if cell.number is not None:
                    continue
                
                new_arc = Arc(first=cell,
                        second=first,
                        )
                arcs.append(new_arc)
    return True        