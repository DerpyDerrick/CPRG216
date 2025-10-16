names = ["John", "Sam", "Cassandra", "Tom", "Sarah", "Michael"]
GPA = [3.4,3.6,3.1,3.6,3.8,4.0]
print(f"{'GPA Table':^22}")
print(f"{'Name':>10s}{'GPA':>6s}")
print(f"{'====':>10s}{'====':>6s}")
for i,j in zip(names, GPA):
    print(f"{i:>10s}{j:>6.0f}")