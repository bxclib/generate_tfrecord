matching_name={"0":0,
"1":1,
"2":2,
"3":3,
"4":4,
"5":5,
"6":6,
"7":7,
"8":8,
"9":9,
}       
'''
 This is the dictionary of the class to label
 For example, if you have 3 classes(dog,cat,fish), you put them in the root like this
 root/fish/your fish pictures
 root/cat/your cat pictures
 root/dog/your dog pictures
 And you want the fish label in Tfrecord is 0,the cat label in Tfrecord is 1,the dog label in Tfrecord is 2
 you should put matching_name like this:
matching_name={"fish":0,
"cat":1,
"dog":2,
}
'''
root = "./pic/"  # root is the place where you put your picture
tf_dir="./convert/"   #tf_dir is the place you will find your result(if the dir not exists, the program will make it)
tf_name="data.tfrecords"  #The name of the tfrecords
print_interval=1000           #The interval to print your result
shuffle_length=40000          
'''The length of shuffle.The shuffle will start and wrote picture to disk after the program load shuffle_length pictures in the program.
Please put this number less than the number of the whole images
'''
pre_process="img = img.convert('L')"
''' 
You can pre-process the picture before writing to data.This is the pre_process code that will execute before writing to disk
'''
