from arc import Arc
from queue import Queue


INF = 10000000


def enforce_consistency(arcs):
    while not arcs.empty():
        arc = arcs.get()
        
        arc.enforce_consistency()
        
        if arc.domain_emptied:
            return False
        
        if arc.domain_changes:
            first = arc.first
            for cell in first.connected_cells:
                
                if cell.number is not None:
                    continue
                
                arc = Arc(first=cell,
                        second=first,
                        )
                arcs.put(arc)
    return True        