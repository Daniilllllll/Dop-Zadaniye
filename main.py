grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a = list(sorted(students))

sred1 = sum(grades[0])/len(grades[0])
sred2 = sum(grades[1])/len(grades[1])
sred3 = sum(grades[2])/len(grades[2])
sred4= sum(grades[3])/len(grades[3])
sred5 = sum(grades[4])/len(grades[4])
sredOB = sred1,sred2,sred3,sred4,sred5

itog = dict(zip(a,sredOB))
print(itog)