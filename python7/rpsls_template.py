#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李志杰
日期：2020/11/22
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    if name=="石头":
        name=0
    if name=="史波克":
        name=1
    if name=="纸":
        name=2
    if name=="蜥蜴":
        name=3
    if name=="剪刀":
        name=4# 使用if/elif/else语句将各游戏对象对应到不同的整数
    return name# 不要忘记返回结果


    #编写执行代码,代码完成后将pass删除


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    if number==0:
        number="石头"
    if number==1:
        number="史波克"
    if number==2:
        number="纸"
    if number==3:
        number="蜥蜴"
    if number==4:
        number="剪刀"# 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    return number# 不要忘记返回结果

    #编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """


    print("-------- ")# 输出"-------- "进行分割
    player_choice=choice_name# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    player_choice_number=name_to_number(player_choice)# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    comp_number=random.randrange(0,5)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    result=number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    print("计算机选择了："+result)# 在屏幕上显示计算机选择的随机对象
    if player_choice=="石头" or player_choice=="史波克" or player_choice=="纸" or player_choice=="蜥蜴" or player_choice=="剪刀":
        if player_choice_number>comp_number:
            distance=player_choice_number-comp_number
        else:
            distance=player_choice_number-comp_number+5
            if distance==1 or distance==2:
                print("您赢了")
            elif distance==3 or distance==4:
                print("计算机赢了")
            else:
                print("您和计算机出的一样呢")
    else:
        print("Error: No Correct Name")
    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

     #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input("")
rpsls(choice_name)


