
# this python file to used for the run terraform command and create aws resouce creating
# import model in python
import os

# function 
def terrformCall():
    print('Now terrafrom resource creating')
    print('#'*80)
    input('do you want to continue Press Enter.. for init command')
    os.system('terraform init')
    print('#'*80)
    input('do you want to continue Press Enter.. for fmt command')
    os.system('terraform fmt')
    print('#'*80)
    input('do you want to continue Press Enter.. for validate command')
    os.system('terraform validate')
    print('#'*80)
    input('do you want to continue Press Enter.. for apply command')
    os.system('terraform apply -auto-approve')
    print('#'*80)
    print('Now all resoces is ready ')
    print('#'*80)
    print()
    print('plz go to aws console and check it')
    print()
    print('#'*80)
    input('do you want to continue Press Enter.. for destroy command')
    os.system('terraform destroy -auto-approve')
    print('#'*80)
    print('All resource destroy')
    print('plz go to AWS Console check it')
    print()
    print('#'*30,'!!!!..Thank you..!!!!','#'*30)
    print()

# function calling
terrformCall()