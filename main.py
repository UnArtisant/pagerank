'''
Jorge Rodrigo Colín Rubio           | A01662960
Raphaël Marc Joseph Barriet	 	    | A01763686
Nicole Kapellmann Lepine		    | A01664563
'''

def crete_graph():
    return {"to": [], "from": [], "result": 0.0}


def read_file(file):
    matrix = {}
    with open(file) as f:
        lines = f.readlines()
    for item in lines:
        # Remove newline and parentheses
        cleaned_item = item.strip().replace('(', '').replace(')', '')

        # Split the string into two elements and convert to integers
        row = list(map(int, cleaned_item.split(',')))

        # Append the row to the matrix
        if matrix.get(row[0]) is None:
            matrix[row[0]] = crete_graph()
        matrix[row[0]]['to'].append(row[1])

        if matrix.get(row[1]) is None:
            matrix[row[1]] = crete_graph()
        matrix[row[1]]['from'].append(row[0])
    return matrix


def page_rank():
    file = "analysis.txt"
    matrix = read_file(file)
    n = len(matrix)  # length of the matrix
    for i in range(0, 5):
        print(f"Round.{i}\n")
        for r in matrix:
            if i == 0:
                matrix[r]["result"] = 1 / n
            else:
                matrix[r]["result"] = sum(
                    matrix[j]["result"] / len(matrix[j]["to"]) if len(matrix[j]["to"]) > 0 else 0 for j in
                    matrix[r]["from"])
            print(f"P{r} is {matrix[r]["result"]}")
    print("\n")


page_rank()
