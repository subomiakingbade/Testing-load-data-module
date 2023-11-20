# ECOR 1042 Lab 4 - Individual submission for test4 function

#import check module here
import check
#import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Subomi Akingbade"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101261502"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "1-147"

#==========================================#
#Do not modify the code alreayd provided.

def test_add_average():
    #Complete the function with your test cases
    
    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    lst = [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
    'Failures': 1, 'Health': 3, 'Absences': 7,
    'G1': 5, 'G2': 6, 'G3': 6},{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length = len(lst)
    lst2 = load_data.add_average(lst)
    check.equal(len(lst2), (old_length))
    
    lst3 = [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
    'Failures': 1, 'Health': 3, 'Absences': 7,
    'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length2 = len(lst3)
    lst4 = load_data.add_average(lst3)
    check.equal(len(lst4), (old_length2))
    
    lst5 = [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length3 = len(lst5)
    lst6 = load_data.add_average(lst5)
    check.equal(len(lst6), (old_length3))
    
    lst7 = [{'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length4 = len(lst7)
    lst8 = load_data.add_average(lst7)
    check.equal(len(lst8), (old_length4))
    
    lst9 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length5 = len(lst9)
    lst10 = load_data.add_average(lst9)
    check.equal(len(lst10), (old_length5))    
    #test that the function returns an empty list when it is called whith an empty list
    
    lst11 = []    
    old_length6 = len(lst11)
    lst12 = load_data.add_average(lst11)
    check.equal(len(lst12), (old_length6))    
    
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    lst14 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst14:
        nokeys1 = len(student)
    
    lst15 = load_data.add_average(lst14)
    for student in lst15:
        nokeys2 = len(student)    
    check.equal(nokeys1, (nokeys2-1))     
    
    
    
    lst18 = [{'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst18:
        nokeys3 = len(student)
    
    lst19 = load_data.add_average(lst18)
    for student in lst19:
        nokeys4 = len(student)    
    check.equal(nokeys3, (nokeys4-1))     
    
    
    
    lst20 = [{'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst20:
        nokeys5 = len(student)
    
    lst21 = load_data.add_average(lst20)
    for student in lst21:
        nokeys6 = len(student)    
    check.equal(nokeys5, (nokeys6-1))     
    
    
    
    lst22 = [{'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst22:
        nokeys7 = len(student)
    
    lst23 = load_data.add_average(lst22)
    for student in lst23:
        nokeys8 = len(student)    
    check.equal(nokeys7, (nokeys8-1))     
    
    
    
    lst24 = [{'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst24:
        nokeys9 = len(student)
    
    lst25 = load_data.add_average(lst24)
    for student in lst25:
        nokeys10 = len(student)    
    check.equal(nokeys9, (nokeys10-1))         
    
    #test that the G_Avg value is properly calculated  (5 different test cases required)
    lst16 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst16:
        gs = (student["G1"],student["G2"],student["G3"])
        newaverage = sum(gs) / 3
    lst17 = load_data.add_average(lst16)
    for student in lst17:
        gs2 = (student["G1"],student["G2"], student["G3"])
        newaverage2 = sum(gs2) / 3  
    check.equal(newaverage, newaverage2)
    
    

    lst26 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 13, 'G2': 14, 'G3': 15}]
    for student in lst26:
        gs3 = (student["G1"],student["G2"],student["G3"])
        newaverage3 = sum(gs3) / 3
    lst27 = load_data.add_average(lst26)
    for student in lst27:
        gs4 = (student["G1"],student["G2"], student["G3"])
        newaverage4 = sum(gs4) / 3  
    check.equal(newaverage3, newaverage4)
    
    
    
    lst28 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 14, 'G2': 15, 'G3': 16}]
    for student in lst28:
        gs5 = (student["G1"],student["G2"],student["G3"])
        newaverage5 = sum(gs5) / 3
    lst29 = load_data.add_average(lst28)
    for student in lst29:
        gs6 = (student["G1"],student["G2"], student["G3"])
        newaverage6 = sum(gs6) / 3  
    check.equal(newaverage5, newaverage6)
    
    
    
    lst30 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 15, 'G2': 16, 'G3': 17}]
    for student in lst30:
        gs7 = (student["G1"],student["G2"],student["G3"])
        newaverage7 = sum(gs7) / 3
    lst31 = load_data.add_average(lst30)
    for student in lst31:
        gs8 = (student["G1"],student["G2"], student["G3"])
        newaverage8 = sum(gs8) / 3  
    check.equal(newaverage7, newaverage8)
    
    
    
    lst32 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 16, 'G2': 17, 'G3': 18}]
    for student in lst32:
        gs9 = (student["G1"],student["G2"],student["G3"])
        newaverage9 = sum(gs9) / 3
    lst33 = load_data.add_average(lst32)
    for student in lst33:
        gs10 = (student["G1"],student["G2"], student["G3"])
        newaverage10 = sum(gs10) / 3  
    check.equal(newaverage9, newaverage10)    
    
   
test_add_average()    
check.summary()


# Do NOT include a main script in your submission
