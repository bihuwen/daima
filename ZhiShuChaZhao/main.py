# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'毕煳炆 {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    string2="请输入查找质数的范围（例如1 换行 100）";
    print(string2);
    # 存放质数
    a = [];
    # 存放初始数
    qss = int(input())
    # 存放终止数
    zzs = int(input())
    # 循环起始数到终止数
    for num in range(qss, zzs):
        # 循环计算2到num里能被整除的数
        for i in range(2, num):
            if (num % i == 0): break
        else:a.append(num)
string = str(qss)+"~" + str(zzs) + "的质数有"
print(string)
print(a)

