import subprocess
import glob
import os
import shlex

currentFile = 'Project_3_Tester'#Name of script file
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath) 

labname = 'NetworkDestruction'

# Take the name of all the .zip files into a list
submissions=glob.glob(dirPath  + "/*.zip")
print("Here " , submissions)
output_case_directory = '/output/'

out_file_extension = '.out'
ans_file_extension = '.ans'

#removes leftover files. FNULL serves to suppress output
FNULL = open(os.devnull, 'w')
subprocess.call('rm *.java', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
subprocess.call('rm *.class', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

# Run the test case of the given number
def runTestCase(command, test_out, test_ans):
    subprocess.call('java ' + labname + ' ' + command + ' ' + '>' + '\"output/' + test_out + '\"', shell=True)

    # Compare compressed and the decompressed output file with the original file
    compare_command = 'diff -w -B ' + '\"ans/' + test_ans + '\"' + ' ' + '\"output/' + test_out + '\"'
    compare_command = shlex.split(compare_command)
    compare_result = subprocess.Popen(compare_command, stdout=subprocess.PIPE).communicate()[0].rstrip().decode(
        'ascii')

    # If both files are identical, test case passed
    if compare_result == '':
        return True
    return False

def testSubmission(submission, output_case_directory):
    print("I am here ", submission)
    subprocess.call(['unzip', '-o', ''+submission])

    # Extract student_id out of zip filename
    list_of_basename_elements = submission.split('_', 1)
    student_id = list_of_basename_elements[0]

    # Compile java files and run the test

    subprocess.call('javac *.java', shell = True)

    correctCases = 0
    totalCases = 0

    test_cases = glob.glob(dirPath  + output_case_directory + '*.ans')
    test_cases.sort()

    commands = ["-r 2 4 destruction_example_1.txt", "-d 4 destruction_example_1.txt", "-d 6 destruction_example_2.txt", 
    "-r 2 6 destruction_example_2.txt", "-c 10 destruction_example_3.txt", "-r 3 10 destruction_example_3.txt"]
    case_numbers = [item for item in range(1, len(commands)+1)]

    # Run tests on each ouput directory file
    for (command, case_no) in zip(commands, case_numbers):

        print("Testing Project 3, case #"+str(case_no))
        ans_file = "0"+str(case_no)+ans_file_extension
        out_file = "0"+str(case_no)+out_file_extension

        if runTestCase(command, out_file, ans_file) is True:
            print("SUCCESS!")
            correctCases += 1
        else:
            print("WRONG! Error ")

        totalCases += 1

    return student_id, correctCases, totalCases

# Iterate on every .zip file
for currentZip in submissions:
    # Extract file name from path
    name_of_file = os.path.basename(currentZip) 

    student_id, correct, total = testSubmission(name_of_file, output_case_directory)

    # Record grade in the TestResult text file
    gradebook = open('TestResult.txt', 'a')
    gradebook.write("NetId: " + student_id + "    Evaluation Result: " + str(correct) + '/' + str(total) + "\n")
    gradebook.flush()

    # removes leftover files again for good measures. FOR EVERY STUDENT. -Akira. FNULL serves to suppress output
    FNULL = open(os.devnull, 'w')
    subprocess.call('rm *.java', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm *.class', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    # subprocess.call('rm output/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)