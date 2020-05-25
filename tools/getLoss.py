# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 

  
# Function to rename multiple files 
def main(): 
    f = open("output3014.txt", "r") 
    output = open("output.csv", "w")
    output.write('iteration,d_loss, g_loss\n')
    count = 1
    for l in f:
	if (l[0:8] != "Epoch: ["):
	    continue
	pos_d_loss_start = l.find('d_loss: ') + 8
	pos_d_loss_end = l.find(', g_loss:')
	pos_g_loss_start = pos_d_loss_end + 10
        pos_g_loss_end = -1
	# print(l[pos_d_loss_start: pos_d_loss_end])
	# print(l[pos_g_loss_start: pos_g_loss_end])
	output.write(str(count) + ',' + l[pos_d_loss_start: pos_d_loss_end] + ',' + l[pos_g_loss_start: pos_g_loss_end] + '\n')
	count += 1
    f.close()
    output.close()

        

  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
