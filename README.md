# BLEM: A dynamic module!
## setup (dynamic)
1. download the required packages (poetry.sh in the install directory for poetry install)
2. go to install.py in the install directory
3. download blemDynamic.py from the install directory
4. add the blemDynamic.py to the same directory as the file that will import it
5. add the contents from blemDynamic.txt to the top of the importing file
## setup (static)
1. download the required packages (poetry.sh in the install directory for poetry install)
2. download blemStatic.py from the install directory
3. add "import blem" to the top of the importing file
## dynamic advantages
1. automatic updates
2. extremely low size on disk (just from the import and the small file
## dynamic disadventages
1. slow start (needs to fetch the functions)
## extra
1. check the cmd folder for the functions (add blem. to the start and replace the .py with a .x)
2. there is an extra cmd built into the package file used in the dynamic module code itself
3. some functions have every line of code accompanied by a comment explaining every step (go to cmd directory)
4. static does NOT have comments, only the dynamic cmd folder has them
