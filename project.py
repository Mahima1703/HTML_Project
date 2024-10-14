print("NEWS PORTAL")
print("1-Admin Side")
print("2-Author Side")
side = int(input("Select a side:"))
categorieslist = []
subCategorylist = []
if side==1:
    print("Admin Side:")
    print("1-Category Management")
    print("2-SubCategory Management")
    print("3-Post Management")
    management = int(input("Select a management:"))
    while(management<=3):
        if management==1:
         print("Category Management:")
         print("1.Add New Category")
         print("2.List All Categories")
         print("3.Update Category Details")
         print("4.Delete Category")
         print("5.<--Exit-->")
         category = int(input("Select a menu:"))
         while(category<=5):
            if category==1:
             print("*Add New Category:")
             new_category1 = input("Category1:")
             #print(new_category1)
             new_category2 = input("Category2:")
             #print(new_category2)
             new_category3 = input("Category3:")
             #print(new_category3)
             break
             

            if category==2:  
             print("*List All Categories:")
             
             categorieslist.append(new_category1)
             categorieslist.append(new_category2)
             categorieslist.append(new_category3)
             for i in categorieslist:
              print(i)
             break
             

            if category==3:
             print("*Update Category Details")
             up_cat=input("Update a New Category:")
             categorieslist.append(up_cat)
             for show in categorieslist:
              print(show)
             break
             

            if category==4:      
             print("*Delete Category")
             delete_cat=input("Enter a Delete Category:")
             if delete_cat in categorieslist:
              categorieslist.remove(delete_cat)
              print("Category deleted:")
             else:
              print("Category not found:")
             for remaining in categorieslist: 
              print(remaining)
             break

            if category==5:
               print("Exit:")
            break
            
            
        if management==2:
         print("SubCategory Management:")
         print("1.Add New SubCategory")
         print("2.List All SubCategories")
         print("3.Update a New SubCategory")
         print("4.Delete SubCategory")
         sub_category = int(input("Select a menu:"))
         while(sub_category<=4):
            if sub_category==1:
             print("*Add New SubCategory:") 
             categorieslist.append(new_category1) 
             new_SubCategory1 = input("SubCategory1:")
             #print(new_SubCategory1)
             categorieslist.append(new_category2)
             new_SubCategory2 = input("SubCategory2:")
             #print(SubCategory2)
             categorieslist.append(new_category3)
             new_SubCategory3 = input("SubCategory3:")
             #print(SubCategory3)
             break

            if sub_category==2:
             print("*List All SubCategories:")
             
             subCategorylist.append(new_SubCategory1)
             subCategorylist.append(new_SubCategory2)
             subCategorylist.append(new_SubCategory3)
             for i in subCategorylist:
              print(i)
             break


            if sub_category==3:
             up_sub=input("*Update a New SubCategory:")
             subCategorylist.append(up_sub)
             for dis in subCategorylist:
              print(dis)
             break 
    
            if sub_category==4:
             print("*Delete SubCategory:")
             delete_sub=input("Enter a Delete SubCategory:")
             if delete_sub in subCategorylist:
              subCategorylist.remove(delete_sub)
              print("SubCategory deleted:")
             else:
              print("SubCategory not found:")
             for balance in subCategorylist:
              print(balance)
             break

       
        if management==3:
         print("Post Management:")
         print("1.Add New Post")
         print("2.List All Posts")
         print("3.Update a New Post")
         print("4.Delete Post")
         post = int(input("Select a menu:"))
         while(post<=4):
            if post==1:
               categorieslist.append(new_category1)
               subCategorylist.append(new_SubCategory1)
               print("*Add New Post:")
               new_post1 = input("Post1:")
               #print(new_post1)
               categorieslist.append(new_category2)
               subCategorylist.append(new_SubCategory2)
               new_post2 = input("Post2:")
               #print(new_post2)
               categorieslist.append(new_category3)
               subCategorylist.append(new_SubCategory3)
               new_post3 = input("Post3:")
               #print(new_post3)
               break

            if post==2:
               print("*List All Posts:")
               postslist = []
               postslist.append(new_post1)
               postslist.append(new_post2)
               postslist.append(new_post3)
               for j in postslist:
                  print(j)
               break

            if post==3:
               print("*Update a New Post:")
               up_pos=input("Update a New Post:")
               postslist.append(up_pos)
               for display in postslist:
                print(display)
               break
      
            if post==4:
               print("*Delete Post")
               delete_pos=input("Enter a Delete Post:")
               if delete_pos in postslist:
                 postslist.remove(delete_pos)
                 print("Post deleted:")
               else:
                 print("Post not found:")
               for minus in postslist:
                 print(minus)
               break


      
      

if side==2:
   
   print("Author Side:")
   print("User Management:")
   print("1.Add New Author")
   print("2.List All Authors")
   print("3.Update a New Author")
   print("4.Delete Author")
   author = int(input("Select a menu:"))
   while(author<=4):
      if author==1:
         print("*Add New Author:")
         new_Author1 = input("Author1:")
         #print(new_Author1)
         new_Author2 = input("Author2:")
         #print(new_Author2)
         new_Author3 = input("Author3:")
         #print(new_Author3)
         break
       

      if author==2: 
         print("*List All Authors:")
         authorslist = []
         authorslist.append(new_Author1)
         authorslist.append(new_Author2)
         authorslist.append(new_Author3)
         for i in authorslist:
            print(i)
         break

      if author==3:
         print("*Update a New Authors:")
         up_aut=input("Update a New Authors:")
         authorslist.append(up_aut)
         for dis in authorslist:
           print(dis)
         break

      if author==4: 
         print("*Delete Author")
         delete_aut=input("Enter a Delete Author:")
         if delete_aut in authorslist:
            authorslist.remove(delete_aut)
            print("Author deleted:")
         else:
            print("Author not found:")
         for balance in authorslist:
            print(balance)
         break

       