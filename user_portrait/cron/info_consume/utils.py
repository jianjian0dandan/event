# -*- coding: utf-8 -*-
import time
import datetime
import math, random
import collections
from math import *
import numpy as np
import sklearn

# from scipy.misc import comb

DAY = 24 * 60 * 60  # *1000
HOUR = 60 * 60


def trya():
    a = set()
    b = ['12', '3', '4', '5']
    for i in b:
        if i not in a:
            a.add(i)
    print a


def test(start_ts, end_ts):
    start = ts2datetime(float(start_ts))
    end = ts2datetime(float(end_ts))
    during = (end - start) / DAY
    end_time = time.localtime(int(end))[:3]
    end = datetime.date(*end_time)

    a = [str(end + datetime.timedelta(days=-i)) for i in range(int(during) + 1)]
    # a = [datetime.date(time.localtime(int(end))[:3] + datetime.timedelta(days=-i)) for i in range(int(during))]

    print a


def ts2datetime(ts):
    a = ts - ts % DAY + HOUR * 16  # 转为当天0点

    # a =  time.localtime(ts)[:3]
    return a
    # b = datetime.date(*a)


# return time.strftime('%Y-%m-%d', time.localtime(ts))

def test1(N):
    ep = 0.05 ** 2
    a = 2 * 100 * math.exp(-2 * ep * N)
    print a


def d_vc(N, d):
    ep = 0.05 ** 2
    a = math.exp(-(1. / 8) * ep * N)
    print a
    the = 4 * ((2 * N) ** d) * a
    print the


# homework5 No.4
def E_derivative_u(w, yita, u, v):
    delta = 2 * (math.exp(v) + 2 * v * math.exp(-u)) * (u * math.exp(v) - 2 * v * math.exp(-u))
    w_new = w - yita * delta
    return w_new


def zuhe(n, k):
    a = {'a': 2, 'b': 1}
    c = set([i for i in a.keys()])
    print c


def NMI(cluA, cluB):
    # 混淆矩阵
    vertices = 6
    cmat = [[0 for i in range(len(cluB))] for j in range(len(cluA))]
    i = 0
    j = 0
    for eacha in cluA:
        for eachb in cluB:
            print set(cluA[eacha]), set(cluB[eachb])
            cmat[i][j] = len(set(cluA[eacha]) & set(cluB[eachb]))
            j += 1
        i += 1
        j = 0
        # the nmi_numerator part
    print cmat
    print len(cluA), len(cluB)
    nmi_numerator = 0.0
    for i in range(len(cluA)):
        for j in range(len(cluB)):
            if (cmat[i][j] != 0):
                row = 0
                column = 0
                for k in range(len(cluB)):
                    row = row + cmat[i][k]
                for l in range(len(cluA)):
                    column = column + cmat[l][j]
                print cmat[i][j], vertices, row, column, cmat[i][j] * log((cmat[i][j] * vertices) / float(row * column),
                                                                          2)
                nmi_numerator = nmi_numerator + cmat[i][j] * log((cmat[i][j] * vertices) / float(row * column), 2)
    print '=============='
    nmi_numerator = -2 * nmi_numerator
    # the denominator part
    nmi_denominator1 = 0.0
    nmi_denominator2 = 0.0
    nmi = 0.0
    for i in range(len(cluA)):
        row = 0
        for k in range(len(cluB)):
            row = row + cmat[i][k]
        if (row != 0):
            nmi_denominator1 = nmi_denominator1 + row * log(row / float(vertices), 2)
            print row, vertices, row * log(row / float(vertices), 2)
    print '============='
    for j in range(len(cluB)):
        column = 0
        for l in range(len(cluA)):
            column = column + cmat[l][j];
        if (column != 0):
            nmi_denominator2 = nmi_denominator2 + column * log(column / float(vertices), 2)
            print column, vertices, column * log(column / float(vertices), 2)
    nmi_denominator = nmi_denominator1 + nmi_denominator2
    print nmi_numerator, nmi_denominator
    if (nmi_denominator != 0):
        nmi = nmi_numerator / float(nmi_denominator)
    print 'nmi', nmi
    return nmi


# #dict_a = {'a':[1,2,4],'b':[4,5,6],'c':[3]}
# #dict_b = {'q':[1,2,3],'w':[4,5,6]}

# dict_a = {'1': [0, 1, 2, 3, 4, 5], '3': [12, 13, 14, 15, 16], '2': [6, 7, 8, 9, 10, 11]}
# dict_b = {'1': [0, 2, 3, 4, 5, 6, 12, 13], '3': [11, 14, 15, 16], '2': [1, 7, 8, 9, 10]}

def na_nmi(a, b, vertics):
    info = 0
    for i in a.keys():
        for j in b.keys():
            inter = len(set(a[i]) & set(b[j]))
            if inter != 0:
                info += (float(inter) / vertics) * log((float(inter) * vertics) / (len(a[i]) * len(b[j])), 2)
    h = 0.0
    for dicts in [a, b]:
        for k in dicts.keys():
            p = float(len(dicts[k])) / vertics
            h += - p * log(p, 2)
    nmi = info * 2 / h
    return round(nmi, 3)


def try_nmi():
    dict_a = {'a': [1, 2], 'b': [4, 5, 6], 'c': [3]}
    dict_b = {'q': [1, 2, 3], 'w': [4, 5, 6]}
    print na_nmi(dict_a, dict_b, 6)
    dict_a = {'1': [0, 1, 2, 3, 4, 5], '3': [12, 13, 14, 15, 16], '2': [6, 7, 8, 9, 10, 11]}
    dict_b = {'1': [0, 2, 3, 4, 5, 6, 12, 13], '3': [11, 14, 15, 16], '2': [1, 7, 8, 9, 10]}
    print na_nmi(dict_a, dict_b, 17)
    # NMI(dict_a,dict_b)

    # f = open('a.txt','r')
    # print f.readlines()
    # f = open('a.txt','w')
    # for i in ['a','b','c']:
    #     f.write(i+'\n')
    a = [540, 560, 610, 890, 1050, 900, 650, 850, 1020, 1220, 1780, 2100, 1800, 1300, 540, 560, 610, 890, 1050]
    b = [180, 161, 180, 286, 310, 260, 180]  # 中性
    d = [240, 260, 280, 410, 530, 460, 340]  # 消极

    print [i * 1.2 for i in a]

    a = ['11.03', '11.04', '11.05', '11.06', '11.07', '11.08', '11.09', '11.10', '11.11', '11.12', '11.13', '11.14',
         '11.15', '11.16', '11.17', '11.18', '11.19', '11.20', '11.21']

    print len(a)


def path_sort(list, start_index, end_index):
    flag = list[end_index]
    i = start_index - 1
    print flag, i
    for j in range(start_index, end_index):
        print 'j:', j, '    i:', i
        if list[j] > flag:
            pass
        else:
            i += 1
            print 'list[j]:', list[j], '    flag:', flag, '    list[i]:', list[i]
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp
        print l
    tmp = l[end_index]
    l[end_index] = l[i + 1]
    l[i + 1] = tmp
    print list, i + 1
    return i + 1


def Quick_sort(list, start_index, end_index):
    if start_index >= end_index:
        return
    middle = path_sort(list, start_index, end_index)
    Quick_sort(list, start_index, middle - 1)
    Quick_sort(list, middle + 1, end_index)
    return l


def fast_sort(l, first, last):
    temp = l[first]
    if first < last:
        key_index = sub_sort(l, first, last)
        fast_sort(l, first, key_index)
        fast_sort(l, key_index, last)
    return l


def sub_sort(l, i, j):
    key = l[j]
    for k in range(i, j):
        if l[k] > j:
            pass
        temp = l[k]
        l[i] = l[j]
        i += 1
        l[j] = temp
    return i


if __name__ == '__main__':
    # l=[66,61,4,83,2,96,33]

    # print Quick_sort(l,0,len(l)-1)
    # print '1'
    # test('1468789200','1468875600')
    # d_vc(460000,10)
    '''
    u,v,yita=1,1,0.1
    w=0
    i = 0 
    while True:
        w_new = E_derivative_u(w,yita,u,v)
        error = w - w_new
        i += 1
        print error
        if error < math.pow(10,-14):
            print i
        w = w_new
    '''
    # result= {0: [10, 11, 14, 17, 32, 33, 34, 36, 41, 42, 46, 48, 51, 60, 69, 73, 80, 89, 96, 113, 119, 123, 137, 144, 152, 153, 154, 156, 159, 163, 178, 181, 182, 189, 191, 197, 204, 205, 208, 209, 214, 215, 232, 233, 239, 240, 243, 246, 252, 254, 255, 266, 278, 281, 285, 286, 291, 293, 300, 304, 315, 334], 66: [0, 2, 4, 6, 8, 9, 12, 15, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 35, 37, 38, 39, 44, 47, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 68, 71, 72, 74, 75, 76, 78, 79, 81, 82, 83, 84, 86, 87, 91, 93, 95, 97, 99, 100, 102, 103, 104, 105, 106, 107, 108, 112, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 138, 140, 141, 145, 147, 149, 155, 157, 158, 160, 162, 164, 167, 168, 169, 170, 171, 175, 177, 179, 183, 184, 185, 186, 187, 188, 190, 193, 195, 196, 198, 199, 202, 203, 206, 207, 210, 211, 212, 216, 220, 221, 222, 223, 227, 228, 230, 231, 234, 235, 236, 237, 238, 241, 245, 247, 248, 249, 250, 251, 253, 256, 257, 259, 260, 264, 265, 267, 268, 269, 270, 271, 273, 275, 276, 279, 280, 282, 283, 284, 287, 289, 290, 294, 296, 297, 298, 299, 301, 302, 303, 307, 308, 310, 312, 313, 314, 316, 317, 319, 321, 322, 323, 324, 328, 329, 330, 331, 333, 335, 337, 338, 339, 340, 341, 343, 344, 345, 346], 201: [201, 172, 165], 311: [1, 13, 16, 18, 19, 22, 27, 31, 40, 43, 70, 92, 110, 111, 114, 115, 136, 139, 143, 148, 150, 161, 166, 173, 213, 219, 225, 229, 242, 261, 288, 292, 306, 309, 311, 325, 332, 336, 342], 226: [22, 45, 67, 85, 98, 101, 130, 142, 174, 176, 224, 226, 262, 277, 295, 320], 274: [3, 77, 151, 180, 194, 217, 272, 274, 305, 327], 172: [], 258: [7, 90, 109, 192, 200, 244, 258, 263], 318: [5, 88, 94, 146, 218, 318, 326]}
    real_c = {'circle3': [51, 83, 237], 'circle2': [155, 99, 327, 140, 116, 147, 144, 150, 270], 'circle1': [173],
              'circle0': [71, 215, 54, 61, 298, 229, 81, 253, 193, 97, 264, 29, 132, 110, 163, 259, 183, 334, 245, 222],
              'circle7': [225, 46],
              'circle6': [337, 289, 93, 17, 111, 52, 137, 343, 192, 35, 326, 310, 214, 32, 115, 321, 209, 312, 41, 20],
              'circle5': [23],
              'circle4': [125, 344, 295, 257, 55, 122, 223, 59, 268, 280, 84, 156, 258, 236, 250, 239, 69],
              'circle9': [336, 204, 74, 206, 292, 146, 154, 164, 279, 73], 'circle8': [282], 'circle22': [267],
              'circle23': [28, 149, 162], 'circle20': [244, 282, 262, 293, 220, 174], 'circle21': [12],
              'circle17': [90, 52, 172, 126, 294, 179, 145, 105, 210],
              'circle16': [251, 94, 330, 5, 34, 299, 254, 24, 180, 194, 281, 101, 266, 135, 197, 173, 36, 9, 85, 57, 37,
                           258, 309, 80, 139, 202, 187, 249, 58, 127, 48, 92],
              'circle15': [108, 208, 251, 125, 325, 176, 133, 276, 198, 271, 288, 316, 96, 246, 347, 121, 7, 3, 170,
                           323, 56, 338, 23, 109, 141, 67, 345, 55, 114, 122, 50, 304, 318, 65, 15, 45, 317, 322, 26,
                           31, 168, 124, 285, 255, 129, 40, 172, 274, 95, 207, 128, 339, 233, 1, 294, 280, 224, 269,
                           256, 60, 328, 189, 146, 77, 196, 64, 286, 89, 22, 39, 190, 281, 117, 38, 213, 135, 197, 291,
                           21, 315, 261, 47, 36, 186, 169, 342, 49, 9, 16, 185, 219, 123, 72, 309, 103, 157, 277, 105,
                           139, 148, 248, 341, 62, 98, 63, 297, 242, 10, 152, 236, 308, 82, 87, 136, 200, 183, 247, 290,
                           303, 319, 6, 314, 104, 127, 25, 69, 171, 119, 79, 340, 301, 188, 142],
              'circle14': [175, 227], 'circle13': [138, 131, 68, 143, 86], 'circle12': [278],
              'circle11': [324, 265, 54, 161, 298, 76, 165, 199, 203, 13, 66, 113, 97, 252, 313, 238, 158, 240, 331,
                           332, 134, 218, 118, 235, 311, 151, 308, 212, 70, 211], 'circle10': [42, 14, 216, 2],
              'circle19': [93, 33, 333, 17, 137, 44, 343, 326, 214, 115, 312, 41, 20], 'circle18': [177]}
    # d = {'circle3': [51, 83,155], 'circle2': [155, 99, 327, 140, 116, 147, 144, 150, 270], 'circle0': [71, 215, 54, 61, 298, 229, 81, 253, 193, 97, 264, 29, 132, 110, 163, 259, 183, 334, 245, 222], 'circle6': [337, 289, 93, 17, 111, 52, 137, 343, 192, 35, 326, 310, 214, 32, 115, 321, 209, 312, 41, 20], 'circle4': [125, 344, 295, 257, 55, 122, 223, 59, 268, 280, 84, 156, 258, 236, 250, 239, 69], 'circle23': [28, 149, 162], 'circle9': [336, 204, 74, 206, 292, 146, 154, 164, 279, 73], 'extra': [173, 225, 46, 23, 282, 267, 12, 175, 227, 278, 177], 'circle17': [90, 52, 172, 126, 294, 179, 145, 105, 210], 'circle16': [251, 94, 330, 5, 34, 299, 254, 24, 180, 194, 281, 101, 266, 135, 197, 173, 36, 9, 85, 57, 37, 258, 309, 80, 139, 202, 187, 249, 58, 127, 48, 92], 'circle15': [108, 208, 251, 125, 325, 176, 133, 276, 198, 271, 288, 316, 96, 246, 347, 121, 7, 3, 170, 323, 56, 338, 23, 109, 141, 67, 345, 55, 114, 122, 50, 304, 318, 65, 15, 45, 317, 322, 26, 31, 168, 124, 285, 255, 129, 40, 172, 274, 95, 207, 128, 339, 233, 1, 294, 280, 224, 269, 256, 60, 328, 189, 146, 77, 196, 64, 286, 89, 22, 39, 190, 281, 117, 38, 213, 135, 197, 291, 21, 315, 261, 47, 36, 186, 169, 342, 49, 9, 16, 185, 219, 123, 72, 309, 103, 157, 277, 105, 139, 148, 248, 341, 62, 98, 63, 297, 242, 10, 152, 236, 308, 82, 87, 136, 200, 183, 247, 290, 303, 319, 6, 314, 104, 127, 25, 69, 171, 119, 79, 340, 301, 188, 142], 'circle13': [138, 131, 68, 143, 86], 'circle11': [324, 265, 54, 161, 298, 76, 165, 199, 203, 13, 66, 113, 97, 252, 313, 238, 158, 240, 331, 332, 134, 218, 118, 235, 311, 151, 308, 212, 70, 211], 'circle10': [42, 14, 216, 2], 'circle20': [244, 282, 262, 293, 220, 174], 'circle19': [93, 33, 333, 17, 137, 44, 343, 326, 214, 115, 312, 41, 20]}
    a = {'circle2': [5, 8, 2], 'circle3': [51, 83, 237], 'circle4': [35, 67, 89], 'circle5': [43, 65, 97]}
    b = {'circle1': [1], 'circle4': [3], 'circle5': [7], 'circle2': [5], 'circle6': [8], 'circle7': [2],
         'circle3': [51, 83, 237], 'circle11': [43], 'circle12': [65], 'circle13': [97], 'circle14': [35],
         'circle15': [67], 'circle16': [89]}
    # print na_nmi(a, b, 15)
    sort_rel = [1, 2, 3, 4, 5, 6, 7]
    c_list = [2, 7, 5]
    new_rel = [i for i in sort_rel if i in c_list]
    print new_rel
    a = np.array([1,2,4])
    print a