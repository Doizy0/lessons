#В одном из государств все решения традиционно принимались простым большинством голосов на общем собрании граждан, которых, к счастью, было не очень много. Одна из местных партий, стремясь прийти к власти как можно более законным путем, смогла добиться некоторой реформы избирательной системы. Главным аргументом было то, что население острова в последнее время значительно возросло, и проведение общих собраний перестало быть легкой задачей.

#Суть реформы состояла в следующем: с момента введения ее в действие все избиратели острова делились на K групп (необязательно равных по численности). Голосование по любому вопросу теперь следовало проводить отдельно в каждой группе, причем считалось, что группа высказывается "за", если "за" голосует более половины людей в этой группе, а в противном случае считалось, что группа высказывается "против". После проведения голосования в группах подсчитывалось количество групп, высказавшихся "за" и "против", и вопрос решался положительно в том и только том случае, когда групп, высказавшихся "за", оказывалось более половины общего количества групп.

#Эта система вначале была с радостью принята жителями острова. Когда первые восторги рассеялись, очевидны стали, однако, некоторые недостатки новой системы. Оказалось, что сторонники партии, предложившей систему, смогли оказать некоторое влияние на формирование групп избирателей. Благодаря этому, они получили возможность проводить некоторые решения, не обладая при этом реальным большинством голосов.

#Пусть, например, на острове были сформированы три группы избирателей, численностью в 5, 5 и 7 человек соответственно. Тогда партии достаточно иметь по три сторонника в каждой из первых двух групп, и она сможет провести решение всего 6-ю голосами "за", вместо 9-и, необходимых при общем голосовании.

#Требуется написать программу, которая по заданному разбиению избирателей на группы определит минимальное количество сторонников партии, достаточное для принятия любого решения.
#https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=729

k = int(input())
groups = list(map(int, input().split()))
if k % 2 != 0:
    half = k // 2 + 1
else:
    half = k // 2

supporters = 0
for i in groups:
    if i % 2 != 0:
        s = i // 2 + 1
    else:
        s = i//2
    supporters += s

print(supporters)
