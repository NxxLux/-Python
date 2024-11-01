def find_common_participants(group1, group2, sep=','):
    set1 = set(group1.split(sep))
    set2 = set(group2.split(sep))
    common_participants = sorted(set1 & set2)
    return common_participants


# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, sep='|')
print(result)
# TODO Провеьте работу функции с разделителем отличным от запятой
