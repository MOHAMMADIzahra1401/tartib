print(" pleas adad ra ba (((,))) vared konid")
input_string = input('enter your numbers:')
# print("\n")
user_list = input_string.split(",")
print('list: ', user_list)

n=len(user_list)

for i in range(1,n):
    if user_list[i-1]<user_list[i]:
        print("kalamat   betartib hastan")
        
    else:
        print("no")
        print("if no in result :dar natige be tartib (((( nist  ))))!!!!!!!!!")


    