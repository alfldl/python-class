# 인자로 받은 리스트를
# for 루프로 돌면서 i * i의 결과값으로
# 새로운 리스트를 만들고 리턴하는 함수

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print('my_nums->', my_nums)