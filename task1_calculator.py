import math 
while 1:
# - 2 modes [Seintific(add , sub, div,mul,mod,exp,) - programming(bin,hex,dec,oct operations)]

    mode= input("\nchoose calculator mode (1 or 2)\n\n1=scientific mode\n2=programmer mode\n")
    mode=int(mode)
    if mode == 1:
        print("scientific mode is selected")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. MODULUS")
        print("6. SQUARE ROOT")
        print("7. POWER")
        print("8. LOGARITHMIC")
        print("9. FACTORIAL")
        num_neededforop=input("Select an operation to perform:\n")
        num_neededforop=int(num_neededforop)
        
        ##2numneeded
        if num_neededforop ==1 or num_neededforop == 2 or num_neededforop== 3 or num_neededforop == 4 or num_neededforop == 5 or num_neededforop == 7 or num_neededforop == 8:
            first_num=input("Insert the first number: ")
            second_num=input("Insert the second number: ")
            if num_neededforop == 1:
                sum=float(first_num)+float(second_num);
                print(str(first_num) + "+"+ str(second_num) + "=" + str(sum))
                continue;
            if num_neededforop == 2:
                sub=float(first_num)-float(second_num);
                print(str(first_num) + "-"+ str(second_num) + "=" + str(sub))
                continue;
            if num_neededforop == 3:
                mult=float(first_num)*float(second_num);
                print(str(first_num) + "x"+ str(second_num) + "=" + str(mult))
                continue;
            if num_neededforop == 4:
                div=float(first_num)/float(second_num);
                print(str(first_num) + "/"+ str(second_num) + "=" + str(div))
                continue;
            if num_neededforop == 5:
                mod=float(first_num)%float(second_num);
                print(str(first_num) + "+"+ str(second_num) + "=" + str(mod))
                continue;
            if num_neededforop == 7:
                ppow=float(first_num)**float(second_num);
                print(str(first_num) + "^"+ str(second_num) + "=" + str(ppow))
                continue;
            if num_neededforop == 8:
                print("log of "+str(first_num) + " to the base"+ str(second_num) + "=" + str((math.log(float(first_num),float(second_num)))))
                continue;
       
       ##1numneeded
        
        if num_neededforop ==6 or num_neededforop== 9:
            one_s_num=input("Insert the number: ")
            continue;
            if num_neededforop == 6:
                print("√" + str(one_s_num )+"=" + str(math.sqrt(float(one_s_num))))
                continue;
            if num_neededforop == 9:
                facto=math.factorial(int(one_s_num))
                print( str(one_s_num )+ "! " +"=" + str(facto))
                continue;
            
        
    ##bin,hex,dec,oct operations,and , or shift
    if mode == 2:
        print("programmer mode is selected")
        print("1. convert decimal to binary")
        print("2. convert to decimal to binary;")
        print("3. convert decimal to hexadecimal")
        print("4. convert decimal to octal")
        print("5. Bitwise AND x & y ")
        print("6. Bitwise OR  x | y")
        print("7. Bitwise right shift  x>> ")
        print("8. Bitwise left shift  x<<  ")
        num_neededforop=input("Select an operation to perform:\n")
        num_neededforop=int(num_neededforop)
        ##num1 needed
        if num_neededforop ==1 or num_neededforop == 2 or num_neededforop== 3 or num_neededforop == 4:
            one_s_num=input("Insert the number: ")
            if num_neededforop == 1:
                print("Binary representation", str(bin(int(one_s_num))))
            if num_neededforop == 2:
                print("decimal representation", str(int(one_s_num,2)))
            if num_neededforop == 3:
                print("hexadecimal representation", str(hex(int(one_s_num))))
            if num_neededforop == 4:
                print("octal representation", str(oct(int(one_s_num))))
        ##2num needed
        
        if num_neededforop ==5 or num_neededforop == 6 or num_neededforop== 7 or num_neededforop == 8:
            first_num=input("Insert the first number: ")
            second_num=input("Insert the second number: ")
            if num_neededforop == 5:

                print(str(first_num) + "&"+ str(second_num) + "=" + str(int(first_num)&int(second_num)))
            if num_neededforop == 6:
                print(str(first_num) + "|"+ str(second_num) + "=" + str(int(first_num)|int(second_num)))
            if num_neededforop == 7:
                print(str(first_num) ," >> ",str(second_num)," = ", str(int(first_num)>>int(second_num)))
            if num_neededforop == 8:
                print(str(first_num) ," << ",str(second_num)," = ", str(int(first_num)<<int(second_num)))


    else:
        print("!!! invalid input please press 1 or 2 to select modes")







