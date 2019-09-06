import multiplythread
import numpy as np
import timeit


def main():
    print("Prueba3!!")
    result_dict={}
    num_hilos=3

    tmp_a = open("./data/ex1.txt", "r").read().split("\n", 2)[2].replace("   ", ",").replace("\n", ";")
    #tmp_b = open("./data/ex1.txt", "r").read().split("\n", 2)[2].replace("   ", ",").replace("\n", ";")
    tmp_b=tmp_a

    matrix_a=np.matrix(tmp_a)
    matrix_b=np.matrix(tmp_b)

    #print("Main! \nA=\n{}\nB=\n{}\n".format(matrix_a,matrix_b))
    #print("AxB=\n{}\n".format(matrix_a*matrix_b))

    #print(matrix_a.shape)
    #print(matrix_b.shape)

    if matrix_a.shape[1] != matrix_b.shape[0]:
        exit()
    
    result_matrix = np.zeros((0, matrix_b.shape[1]))

    #print("result=\n{}".format(result_matrix))

    thread_tab = []

    step = int(matrix_a.shape[0] / num_hilos)
    rest = int(matrix_a.shape[0] % num_hilos)
    start = 0

    #print("multiplicando matrices de orden {}x{}".format(matrix_a.shape[0],matrix_a.shape[1]))

    for i in range(num_hilos):
        if i < rest:
            x=timeit.default_timer()
            print("Thread start:{} end:{}".format(start, start+step+1))
            thread_tab.append(
                multiplythread.Multiplythread(
                    i, matrix_a[start: start+step+1], matrix_b , result_dict))
            start += 1
            y=timeit.default_timer() - x #SE ALMACENA EN Y EL TIEMPO DE EJECUCIoN
        else:
            #print("Thread start:{} end:{}".format(start, start + step ))
            thread_tab.append(
                multiplythread.Multiplythread(
                i, matrix_a[start:start+step:], matrix_b, result_dict))
        start += step

    pass


if __name__=='__main__':
    main()


