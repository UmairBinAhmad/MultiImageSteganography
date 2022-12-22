import cv2
import csv 

def write_list_to_csv(mylist,filename):
    with open(filename, 'a', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(mylist)

frame = cv2.VideoCapture("fish.mp4")
success, image = frame.read()

result = cv2.VideoWriter('fish.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (128,128))
count = 1
frame_array = []
while success:
    
    success, image = frame.read()
    if success == False:
        break

    image = cv2.resize(image, (128, 128))
    frame_name = "frame%d.jpg" % count
    cv2.imwrite("dataset/"+frame_name, image)

    frame_array.append(frame_name)
    
    if count%4 ==0:
        print(frame_array)
        # write list to CSV File
        write_list_to_csv(frame_array, "dataset/frame_list.csv")

        # make array empty
        frame_array = []

    
    cv2.imshow("Frame", image)
    result.write(image)
    if cv2.waitKey(10) == 27:
        break
    count += 1
cv2.destroyAllWindows()
result.release()
frame.release()





# with open('list.csv', 'w') as csvfile: 
#     fieldnames = ['name', 'age'] 
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
#     writer.writeheader() 
#     writer.writerow({'name': 'John', 'age': 20}) 
#     writer.writerow({'name': 'Mary', 'age': 19}) 
#     writer.writerow({'name': 'Mike', 'age': 21})