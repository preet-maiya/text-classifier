import pickle

training_data = pickle.load(open("training_data.pkl", 'rb'))

class_name = ""
sentence = ""
new_data = {}
new_list = []
l = []
for data in training_data:
    if data['class'] not in l:
        #print data['class']
        l.append(data['class'])
print "CTRL + C to exit and save"
try:
    while(1):
        class_name = raw_input("Class Name: ")
        while class_name == "":
            class_name = raw_input("Class Name: ")
        new_data['class'] = class_name
        ch = "y"
        flag = 0
        if class_name not in l:
            print "New class detected".upper(),"...\nDo you want to create a new class \"",class_name,"\" ?(y or n)"
            flag = 1
            ch = raw_input()
        if ch == 'y':
            if flag == 1:
                print "New class created"
            sentence = raw_input("Sentence: ")
            new_data['sentence'] = sentence
            if flag == 1:
                training_data.extend(new_data)
            else:
                new_list.append(new_data)
            print new_data
        else:
            print "New class not created."
except KeyboardInterrupt:
    training_data.extend(new_list)
    #print training_data
    with open('training_data.pkl','w') as f:
        pickle.dump(training_data,f)
    print "\n\n\n\t\t\t\t*****EXIT*****\n"
