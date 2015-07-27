# Bubble Sort
def bubble_sort(seq):
    changed = True
    while True:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq

if __name__ == "__main__":
   n=int(raw_input())
   seq=[]
   for i in range (0,n):
      seq.append(int(raw_input()))
   seq=bubble_sort(seq)
   for x in seq:
      print(x)
