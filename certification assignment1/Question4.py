# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    highest=arr[0]
    second_highest=arr[0]
    for i in arr:
        if highest<i:
            second_highest=highest
            highest=i
        if highest>i and second_highest<i:
            second_highest=i
    print(second_highest)
