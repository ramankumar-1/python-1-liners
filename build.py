# Code to build the HTML page containing the problems & its solutions

start="""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Python 1 liners</title>
        <meta name="description" content="Solve interesting problems using single line Python code">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Python 1 Liners</h1>
        <h2>Enjoy the coding !!</h2>
"""

end = """</body>
</html>
"""

try:
    # opening the HTML file to write
    html=open("index.html","w")

    # opening the Problems and solutions text file to read
    prob=open("problems.txt","r")
    sol=open("solutions.txt","r")

    # writing the contents to the HTML file
    html.write(start)
    q,a=prob.readline(),sol.readline()

    while q and a:
        html.write(f"<p>{q}<br>")
        html.write(f"<code>{a[3:]}</code></p>")
        q,a=prob.readline(), sol.readline()
    
    html.write(end)

    # close the HTML file
    html.close()

except FileNotFoundError as err:
    print(err)