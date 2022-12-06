stack = [   ['S','L','W'],
            ['J','T','N','Q'],
            ['S','C','H','F','J'],
            ['T','R','M','W','N','G','B'],
            ['T','R','L','S','D','H','Q','B'],
            ['D','W','R','N','J','M'],
            ['B','Z','T','F','H','N','D','J'],
            ['H','L','Q','N','B','F','T']]

with open('dayfiveinput.txt','r') as file:
    instructions = file.read().split('\n')
    for i in range(len(instructions)):
        instructions[i] = instructions[i].split()
        num_moves = int(instructions[i][1])
        from_stack = int(instructions[i][3])-1
        to_stack = int(instructions[i][5])-1
        j = len(stack[from_stack])-1
        while j > to_stack:
            stack[to_stack].append(stack[from_stack][j])
            j -= 1