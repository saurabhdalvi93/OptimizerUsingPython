
# import openpyxl module 
import openpyxl 
  
# Call a Workbook() function of openpyxl  
# to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
# Get workbook active sheet   
# from the active attribute. 
sheet = wb.active 
  
# writing to the cell of an excel sheet 
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = 400
sheet['A4'] = 500
sheet['A5'] = 600
  
# The value in cell A7 is set to a formula  
# that sums the values in A1, A2, A3, A4, A5 . 
sheet['A7'] = '= SUM(A1:A5)'
  
# save the file 
wb.save("sum.xlsx") 
