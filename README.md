Project 3 Tester
Pratistha Maharjan
Bartlomiej Jezierski

Description for Project 3 Tester 
The tester file compares the output file generated from the running the script and compares with the .ans file in ans folder. The output file generated from running the script will be placed in the output folder. 

To run tests for a lab on student' submisson: 
1) Place the zipped files in Project3_tester-main. 
//TODO: change the name of the labname in line 10 depending on the name given in the project 3 handout 

2) From the terminal, run the script inside the folder (Project3_tester-main):
    python Project_3_Tester.py 

**DO not unzip the files and place in the folder"


//OPTIONAL*****
Currently the tester contains output folder that collects the output file generated after running the script . However, to save space this can be removed: To remove the output files
1) uncommenting out line 94: 
#subprocess.call('rm output/*.out', shell = True, stdout=FNULL, stderr=subprocess.STDOUT)
2) Run the program again. 


Brief desciption of the NetworkDestruction.java - test functionality


Test Case 1:

java NetworkDestruction -r 2 4 destruction_example_1.txt

10 63
16 51
20 30
6 9


Test Case 2:

java NetworkDestruction -d 4 destruction_example_1.txt

25 6
5 5
12 5
6 4


Test Case 3:

java NetworkDestruction -d 6 destruction_example_2.txt

66 148
12 72
77 64
26 60
47 48
37 45


Test Case 4:

java NetworkDestruction -r 2 6 destruction_example_2.txt

7 5
12 5
26 5
31 5
36 5
42 5


Test Case 5:

java NetworkDestruction -c 10 destruction_example_3.txt

114 7
105 6
112 6
125 6
6 4
23 4
34 4
65 4
107 4
124 4


Test Case 6:

java NetworkDestruction -r 3 10 destruction_example_3.txt

114 270
105 125
112 75
118 39
125 25
11 24
65 21
138 21
36 15
37 8
