from tkinter import *
from tkinter import messagebox as message
import matplotlib.pyplot as plt
import random
import time
import numpy as np

window=Tk()
window.geometry("750x550")
window.title("Engineering Exploration")
window.configure(bg="#2b2b29")
f1=Frame(window,bg="#060108",borderwidth=6,relief=SUNKEN)
f1.pack(side=TOP,fill="x")
f2=Frame(window,bg="#060108",borderwidth=6,relief=SUNKEN)
f2.pack(side=LEFT,fill="y")
Label(f1,text="Fun With Algorithms",bg="#060108",fg="yellow",font=("Arial bold",20)).pack()
Label(f2,text="Algorithms",bg="yellow",width=10,font=("Arial bold",10)).pack(pady=5)
Label(f2,text="1.Selection",width=10,font=("Arial bold",10)).pack(pady=20)
Label(f2,text="2.Insertion",width=10,font=("Arial bold",10)).pack(pady=20)
Label(f2,text="3.Bubble",width=10,font=("Arial bold",10)).pack(pady=20)
Label(f2,text="4.Heap",width=10,font=("Arial bold",10)).pack(pady=20)
Label(f2,text="5.Merge",width=10,font=("Arial bold",10)).pack(pady=20)
Label(f2,text="6.Quick",width=10,font=("Arial bold",10)).pack(pady=20)
Label(f2,text="7.Radix",width=10,font=("Arial bold",10)).pack(pady=20)

Label(window,text="Hellow, Let us play with algorithms and graphs.",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",13)).place(x=100,y=50)
Label(window,text="Here we plot time complexity of an algorithm with respective to size of input data.",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",13)).place(x=100,y=80)
Label(window,text="Enter any number in between one to hundred.",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",13)).place(x=100,y=110)
Label(window,text="Note:Make sure that array size do not overload.",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=100)
e=Entry(window,width=30,borderwidth=6)
e.pack()
sx_coordinate=[]
sy_b_coordinate=[]
sy_a_coordinate=[]
sy_w_coordinate=[]
ix_coordinate=[]
iy_b_coordinate=[]
iy_a_coordinate=[]
iy_w_coordinate=[]
bx_coordinate=[]
by_b_coordinate=[]
by_a_coordinate=[]
by_w_coordinate=[]
hx_coordinate=[]
hy_b_coordinate=[]
hy_a_coordinate=[]
hy_w_coordinate=[]
mx_coordinate=[]
my_b_coordinate=[]
my_a_coordinate=[]
my_w_coordinate=[]
qx_coordinate=[]
qy_b_coordinate=[]
qy_a_coordinate=[]
qy_w_coordinate=[]
rx_coordinate=[]
ry_b_coordinate=[]
ry_a_coordinate=[]
ry_w_coordinate=[]


def event():  
    n=int(e.get())
    Label(window,text="Time complexity when array size is "+str(n*10),bg="#2b2b29",fg="yellow",font=("Arial bold",10)).pack(pady=10)
    Label(window,text="Name_of_Algorithm     Best_case     Average_case     Worst_case",bg="#2b2b29",fg="yellow",font=("Arial bold",10)).pack()
    if n>=1000:
        message.showwarning("Overload","Data should not exceed 1000.")
        return
    def selection_sort(list):
        for i in range(len(list)):
            min=i
            for j in range(i+1,len(list)):
                if list[min]>list[j]:
                    min=j
            list[min],list[i]=list[i],list[min]

    for k in range(1,500,1):
        list=[random.randint(1,1000) for i in range(k)]
        sx_coordinate.append(k)
        start=end=0
        start=time.time()
        selection_sort(list)
        end=time.time()
        sy_a_coordinate.append(np.longdouble(end - start))
        list.sort()
        start=end=0
        start=time.time()
        selection_sort(list)
        end=time.time()
        sy_b_coordinate.append(np.longdouble(end - start))
        start=end=0
        list.sort(reverse=True)
        start=time.time()
        selection_sort(list)
        end=time.time()
        sy_w_coordinate.append(np.longdouble(end - start))

    Label(window,text="Selection sort   "+str(sy_b_coordinate[n-1])+"    "+str(sy_a_coordinate[n-1])+"    "+str(sy_w_coordinate[n-1])+" seconds",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=5)
    plt.subplot(7,3,1)
    plt.plot(sx_coordinate,sy_b_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("Selection Sort")
    plt.subplot(7,3,2)
    plt.plot(sx_coordinate,sy_a_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("Selection Sort")
    plt.subplot(7,3,3)
    plt.plot(sx_coordinate,sy_w_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("Selection Sort")
    def insertion_sort(list):
        for i in range(len(list)):
            j=i 
            while list[j-1]>list[j] and j>0:
                list[j-1],list[j]=list[j],list[j-1]
                j=j-1

    for k in range(1,100,1):
        list=[random.randint(1,1000) for i in range(k*10)]
        ix_coordinate.append(k*10)
        start=end=0
        start=time.time()
        insertion_sort(list)
        end=time.time()
        iy_a_coordinate.append(np.longdouble(end - start))
        list.sort()
        start=end=0
        start=time.time()
        insertion_sort(list)
        end=time.time()
        iy_b_coordinate.append(np.longdouble(end - start))
        start=end=0
        list.sort(reverse=True)
        start=time.time()
        insertion_sort(list)
        end=time.time()
        iy_w_coordinate.append(np.longdouble(end - start))

    Label(window,text="Insertion sort    "+str(iy_b_coordinate[n-1])+"     "+str(iy_a_coordinate[n-1])+"     "+str(iy_w_coordinate[n-1])+" seconds",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=5)
    plt.subplot(7,3,4)
    plt.plot(ix_coordinate,iy_b_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("insertion Sort")
    plt.subplot(7,3,5)
    plt.plot(ix_coordinate,iy_a_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("insertion Sort")
    plt.subplot(7,3,6)
    plt.plot(ix_coordinate,iy_w_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("insertion Sort")
    
    def bubble_sort(list):
        for i in range(0,len(list)-1):  
            for j in range(len(list)-1):  
                if(list[j]>list[j+1]):  
                    temp = list[j]  
                    list[j] = list[j+1]  
                    list[j+1] = temp

    for k in range(1,100,1):
        list=[random.randint(1,1000) for i in range(k*10)]
        bx_coordinate.append(k*10)
        start=end=0
        start=time.time()
        bubble_sort(list)
        end=time.time()
        by_a_coordinate.append(np.longdouble(end - start))
        list.sort()
        start=end=0
        start=time.time()
        bubble_sort(list)
        end=time.time()
        by_b_coordinate.append(np.longdouble(end - start))
        start=end=0
        list.sort(reverse=True)
        start=time.time()
        bubble_sort(list)
        end=time.time()
        by_w_coordinate.append(np.longdouble(end - start))

    Label(window,text="Bubble sort    "+str(by_b_coordinate[n-1])+"     "+str(by_a_coordinate[n-1])+"     "+str(by_w_coordinate[n-1])+" seconds",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=5)
    plt.subplot(7,3,7)
    plt.plot(bx_coordinate,by_b_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("bubble Sort")
    plt.subplot(7,3,8)
    plt.plot(bx_coordinate,by_a_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("bubble Sort")
    plt.subplot(7,3,9)
    plt.plot(bx_coordinate,by_w_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("bubble Sort")

    def heapify(list,i,l):
        largest=i
        left=2*i+1
        right=2*i+2

        if left<l and list[largest]<list[left]:
            largest=left
    
        if right<l and list[largest]<list[right]:
            largest=right
    
        if largest!=i:
            list[i],list[largest]=list[largest],list[i]
            heapify(list,l,largest)
    
    def heap_sort(list,l):
        for i in range(l//2-1,-1,-1):
            heapify(list,i,l)

        for i in range(l-1,0,-1):
            list[i],list[0]=list[0],list[i]
            heapify(list,0,i)
    
    for k in range(1,100,1):
        list=[random.randint(1,1000) for i in range(k*10)]
        hx_coordinate.append(k*10)
        start=end=0
        start=time.time()
        heap_sort(list,len(list))
        end=time.time()
        hy_a_coordinate.append(np.longdouble(end - start))
        list.sort()
        start=end=0
        start=time.time()
        heap_sort(list,len(list))
        end=time.time()
        hy_b_coordinate.append(np.longdouble(end - start))
        start=end=0
        list.sort(reverse=True)
        start=time.time()
        heap_sort(list,len(list))
        end=time.time()
        hy_w_coordinate.append(np.longdouble(end - start))

    Label(window,text="Heap sort   "+str(hy_b_coordinate[n-1])+"    "+str(hy_a_coordinate[n-1])+"    "+str(hy_w_coordinate[n-1])+" seconds",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=5)
    plt.subplot(7,3,10)
    plt.plot(hx_coordinate,hy_b_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("heap Sort")
    plt.subplot(7,3,11)
    plt.plot(hx_coordinate,hy_a_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("heap Sort")
    plt.subplot(7,3,12)
    plt.plot(hx_coordinate,hy_w_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("heap Sort")

    def merge_sort(list):
        if len(list)>1:
            mid=len(list)//2
            left_list=list[:mid]
            right_list=list[mid:]

            merge_sort(left_list)
            merge_sort(right_list)

            i=0
            j=0
            k=0
            while i<len(left_list) and j<len(right_list):
                if left_list[i]<right_list[j]:
                    list[k]=left_list[i]
                    i+=1
                    k+=1

                else:
                    list[k]=right_list[j]
                    j+=1
                    k+=1

            while i<len(left_list):
                list[k]=left_list[i]
                i+=1
                k+=1

            while j<len(right_list):
                list[k]=right_list[j]
                j+=1
                k+=1
    
    for k in range(1,100,1):
        list=[random.randint(1,1000) for i in range(k*10)]
        mx_coordinate.append(k*10)
        start=end=0
        start=time.time()
        merge_sort(list)
        end=time.time()
        my_a_coordinate.append(np.longdouble(end - start))
        list.sort()
        start=end=0
        start=time.time()
        merge_sort(list)
        end=time.time()
        my_b_coordinate.append(np.longdouble(end - start))
        start=end=0
        list.sort(reverse=True)
        start=time.time()
        merge_sort(list)
        end=time.time()
        my_w_coordinate.append(np.longdouble(end - start))

    Label(window,text="Merge sort   "+str(my_b_coordinate[n-1])+"    "+str(my_a_coordinate[n-1])+"    "+str(my_w_coordinate[n-1])+" seconds",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=5)
    plt.subplot(7,3,13)
    plt.plot(mx_coordinate,my_b_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("merge Sort")
    plt.subplot(7,3,14)
    plt.plot(mx_coordinate,my_a_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("merge Sort")
    plt.subplot(7,3,15)
    plt.plot(mx_coordinate,my_w_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("merge Sort")

    def pivot_position(list,first,last):
        pivot=list[first]
        left=first+1
        right=last
        
        while True:
            while left<=right and list[left]<=list[first]:
                left+=1

            while left<=right and list[first]<=list[right]:
                right-=1

            if right<left:
                break
            else:
                list[left],list[right]=list[right],list[left]
        list[right],list[first]=list[first],list[right]
        return right

    def quick_sort(list,low,high):
        if low<high:
            p=pivot_position(list,low,high)  
            quick_sort(list,low,p-1)
            quick_sort(list,p+1,high)

    for k in range(1,100,1):
        list=[random.randint(1,1000) for i in range(k*10)]
        qx_coordinate.append(k*10)
        start=end=0
        start=time.time()
        quick_sort(list,0,len(list)-1)
        end=time.time()
        qy_a_coordinate.append(np.longdouble(end - start))
        list.sort()
        start=end=0
        start=time.time()
        quick_sort(list,0,len(list)-1)
        end=time.time()
        qy_b_coordinate.append(np.longdouble(end - start))
        start=end=0
        list.sort(reverse=True)
        start=time.time()
        quick_sort(list,0,len(list)-1)
        end=time.time()
        qy_w_coordinate.append(np.longdouble(end - start))

    Label(window,text="Quick sort   "+str(qy_b_coordinate[n-1])+"    "+str(qy_a_coordinate[n-1])+"    "+str(qy_w_coordinate[n-1])+" seconds",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=5)
    plt.subplot(7,3,16)
    plt.plot(qx_coordinate,qy_b_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("quick Sort")
    plt.subplot(7,3,17)
    plt.plot(qx_coordinate,qy_a_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("quick Sort")
    plt.subplot(7,3,18)
    plt.plot(qx_coordinate,qy_w_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("quick Sort")

    def counting(list,place):
        size=len(list)
        count=[0]*10
        output=[0]*size

        for i in range(size):
            index=list[i]//place
            count[index%10]+=1

        for i in range(1,10):
            count[i]+=count[i-1]
        
        i=size-1
        while i>=0:
            index=list[i]//place
            output[count[index%10]-1]=list[i]
            i-=1

        for i in range(size):
            list[i]=output[i]

    def radix_sort(array):
        place=1
        max_element=max(array)
        
        while max_element//place>0:
            counting(array,place)
            place*=10

    for k in range(1,100,1):
        list=[random.randint(1,1000) for i in range(k*10)]
        rx_coordinate.append(k*10)
        start=end=0
        start=time.time()
        radix_sort(list)
        end=time.time()
        ry_a_coordinate.append(np.longdouble(end - start))
        list.sort()
        start=end=0
        start=time.time()
        radix_sort(list)
        end=time.time()
        ry_b_coordinate.append(np.longdouble(end - start))
        start=end=0
        list.sort(reverse=True)
        start=time.time()
        radix_sort(list)
        end=time.time()
        ry_w_coordinate.append(np.longdouble(end - start))

    Label(window,text="Radix sort   "+str(ry_b_coordinate[n-1])+"    "+str(ry_a_coordinate[n-1])+"    "+str(ry_w_coordinate[n-1])+" seconds",bg="#2b2b29",fg="#18fa0c",font=("Arial bold",10)).pack(pady=5)
    plt.subplot(7,3,19)
    plt.plot(rx_coordinate,ry_b_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("radix Sort")
    plt.subplot(7,3,20)
    plt.plot(rx_coordinate,ry_a_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("radix Sort")
    plt.subplot(7,3,21)
    plt.plot(rx_coordinate,ry_w_coordinate,"r-*",markersize=2,alpha=1,linewidth=1)
    plt.xlabel("Size of input",color="green",labelpad=10)
    plt.ylabel("Time complexity",color="green")
    plt.title("radix Sort")
    plt.show()
b=Button(window,bg="green",fg="white",text="submit",width=10,height=1,command=event)
b.pack(pady=5)
window.mainloop()