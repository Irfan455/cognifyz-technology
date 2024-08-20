email = str(input(" Enter Email Address:"))

k,d,j=0,0,0

if len(email) >= 6:

    if email[0].isalpha():

      if ("@" in email) and (email.count("@") == 1):

       if (email[-4]==".") ^ (email[-3] == "."):

          for i in email:

             if i==i.isspace():

                k = 1

             elif i==i.isalpha():

               if i==i.isupper():

                 j=1

             elif i==i.isdigit():

                continue

             elif i == "_" or i== "." or i=="@":

                continue

             else:

                d =1

          if k == 1 and d==1 and j==1:

                 print("Invalid email")

          else:

                 print("Valid Email Address")

       else:

            print("Invalid email")

      else:

          print("Invalid email")

    else:

        print("Invalid email")

else:

    print("Invalid emaill")