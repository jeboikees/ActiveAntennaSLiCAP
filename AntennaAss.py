from SLiCAP import *

# Initialize a project
prj = initProject('Active antenna assignment')

htmlPage('Environmental factors')
file2html('environmental.txt')

htmlPage('Cost factors')
file2html('cost.txt')

htmlPage('Functional factors')
file2html('functional.txt')

htmlPage('Performance factors')
file2html('performance.txt')
