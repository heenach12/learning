def SearchTool(tools, length, start_index, target):
    i = start_index
    steps = 0

    while i < length + start_index:

        if target == (tools[(i % length)]):
            print(steps)
            return steps
        steps += 1

        i = i + 1

Tools = ['hammer', 'mallet',
'file', 'saw', 'ladder', 'scissor']

length = len(Tools)
target = "saw"
start_index = 6

SearchTool(tools=Tools, length=length, start_index=start_index, target=target)
