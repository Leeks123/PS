from math import factorial
n, k = map(int,input().split())

# factoArr = [0 for _ in range(n+1)]

# for i in range(n+1):
#     if i==0:
#         factoArr[i]=1
#         continue
#     if factoArr[i]==0:
#         factoArr[i] = factoArr[i-1]*i
        
# # print(factoArr)
# # print(int(factoArr[n]/(factoArr[k]*factoArr[n-k])))
# 이것 저것 꽤를 부렸지만 결국은 라이브러리
print(factorial(n)//(factorial(k)*factorial(n-k)))