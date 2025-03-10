
class MaximalFlow:

    def __init__(self):
        
        self.network = []
        with open("./network.txt", "r") as file: 
            for line in file:
                self.network.append([int(num) for num in line.split()])

        self.source = 0
        self.sink = len(self.network) - 1
        

    def bfs(self, source, sink, network): 
        # enqueue the the source
        queue = [source]
        marked = []
        parent = [-1] * len(network)
        saturating_flow = 10**8

        while len(queue) > 0: 
            current = queue.pop(0)
            if current not in marked:
                marked.append(current)

            # enqueue neighbors
            for i, neighbor in enumerate(network[current]):

                if neighbor > 0 and i not in marked: 
                    queue.append(i)
                    parent[i] = current
                    
                    # find the path if we reach the sink
                    if i == sink: 
                        path = []
                        current = sink
                        while current != source:
                            path.append(current)
                            current = parent[current]
                        path.append(source) 
                        path.reverse()

                        # get the max slow in the path
                        for j in range(len(path) - 1):
                            curr, next = path[j], path[j + 1]
                            saturating_flow = min(saturating_flow, network[curr][next])

                        return path, saturating_flow
                    
        return None, None
                
    def maximal_flow_algorithm(self): 
        print("Initial Network:", self.network)
        
        max_flow = 0

        # get a path from source to sink
        path, saturating_flow = self.bfs(self.source, self.sink, self.network)

        print("Saturating Path:", path, "Flow:", saturating_flow)

        while path: 
            # update max_flow
            max_flow += saturating_flow
            
            # reverse units of capacity used by the path
            for i in range(len(path) - 1):
                curr, next = path[i], path[i + 1]
                self.network[curr][next] -= saturating_flow
                self.network[next][curr] += saturating_flow

            print("Updated Network", self.network)

            # get the new path
            path, saturating_flow = self.bfs(self.source, self.sink, self.network)

            print("Saturating Path:", path, "Flow:", saturating_flow)

        return max_flow, self.network


def main(): 
    algo = MaximalFlow()
    max_flow, network = algo.maximal_flow_algorithm()
    print("Maximal Flow:", max_flow)
    print("Flow:", network)

if __name__ == "__main__": 
    main()