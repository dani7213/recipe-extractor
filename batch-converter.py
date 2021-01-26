from bs4 import BeautifulSoup
import os
import glob


dir_path = r"/home/daniel/nemlig/Ind/"
results_dir = r"/home/daniel/nemlig/Ud/"

for file_name in glob.glob((dir_path+ "*.html")):
    with open(file_name) as html_file:
        soup = BeautifulSoup(html_file, "html.parser")
        results_file = "%s%s.txt"%(results_dir, os.path.splitext(os.path.basename(file_name))[0])
        tmp = soup.find('section', class_="recipe__main")
        with open(results_file, 'w') as html_file:
            recipe = soup.find('section', class_="recipe__main")
            print("<html>", file=html_file)
            print(recipe.prettify(), file=html_file)
            print("</html>", file=html_file)
            print("done")
            
        
