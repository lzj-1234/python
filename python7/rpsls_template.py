#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���־��
���ڣ�2020/11/22
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    if name=="ʯͷ":
        name=0
    if name=="ʷ����":
        name=1
    if name=="ֽ":
        name=2
    if name=="����":
        name=3
    if name=="����":
        name=4# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    return name# ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    if number==0:
        number="ʯͷ"
    if number==1:
        number="ʷ����"
    if number==2:
        number="ֽ"
    if number==3:
        number="����"
    if number==4:
        number="����"# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    return number# ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    print("-------- ")# ���"-------- "���зָ�
    player_choice=choice_name# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    comp_number=random.randrange(0,5)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    result=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("�����ѡ���ˣ�"+result)# ����Ļ����ʾ�����ѡ����������
    if player_choice=="ʯͷ" or player_choice=="ʷ����" or player_choice=="ֽ" or player_choice=="����" or player_choice=="����":
        if player_choice_number>comp_number:
            distance=player_choice_number-comp_number
        else:
            distance=player_choice_number-comp_number+5
            if distance==1 or distance==2:
                print("��Ӯ��")
            elif distance==3 or distance==4:
                print("�����Ӯ��")
            else:
                print("���ͼ��������һ����")
    else:
        print("Error: No Correct Name")
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input("")
rpsls(choice_name)


