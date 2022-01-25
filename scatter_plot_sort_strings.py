#import libraries to build a scatter plot
#import matplotlib.pyplot as plt
#import numpy as np
#from datetime import datetime


#Quick sort function
def quickSort(array):
	quickSortHelper(array, 0, len(array)-1)
	return array	       

def quickSortHelper(array,start_indx,end_indx):			
	pivot = start_indx
	left_indx = start_indx + 1
	right_indx = end_indx	
	if start_indx >= end_indx:
		return
	#iterate the array until the condition met
	while left_indx <= right_indx:
		 #check if the left element to the pivot is less than the pivot value 
			if array[left_indx] <= array[pivot]:
				left_indx += 1		
			if array[right_indx] >= array[pivot]:
				right_indx -= 1
			if left_indx < right_indx:
				swap(left_indx,right_indx,array)
	if left_indx > right_indx: # when the left index is greater than right index 
		swap(pivot,right_indx,array) #call swap function
		quickSortHelper(array, start_indx, right_indx-1) #call the quick sort with the left part of the sorted element
		quickSortHelper(array, right_indx+1 , end_indx) #call the quick sort with the right part of the sorted elemenmt
	
# Swaps the array elements when conditions are met	
def swap(i, j, array):
	array[i],array[j] = array[j],array[i]

# main function 
def main():
# Data used to sort 

	decision = "y" # decision variable to continue the while loop


	while decision == "y" or decision == "Y":
		list_srt = []
		input1 = input("Please enter a string:")
		if len(input1) == 0:
			print("Empty String !!!! Please enter a string with length min of length 1")
			break
	
		list1 = input1.split(" ")
	#	list1 = list(dict.fromkeys(list1)) # to remove dupilicates from the string
		print(f'length of List : {len(list1)}')
		print(f'Before sort :{list1}')
		for i in list1:		
			array = list(i) # coverts list to string
			quickSort(array)
			str = ""
			list_srt.append(str.join(array)) # joins the list to a string and then append to the sorted list
		print(f'After sort :{list_srt}')
		'''
		for i in list_srt:
			x = list_srt.index(i);y=len(i); #preparing x and y values for plot
			sc = plt.scatter(x,y,s=len(i)*2)

		
		# Add title and axis names
		plt.title('Dispersion of sorted list(Length of String)')
		plt.xlabel('Index of String')
		plt.ylabel('Length of String')

		
		# Save the figure
	#	now = datetime.now()
	#	timestamp = datetime.timestamp(now)
	#	plt.savefig(f"/content/drive/MyDrive/Images/Scatter_plot_quicksort_{timestamp}.png"); # save the figure in the given location
		plt.show(block=False) # Code will continue execution irrespective of picture window '''
		decision = input("Do you want to continue(Y/N):")


	print("Thank you !!!")


if __name__ == "__main__":
    main()
