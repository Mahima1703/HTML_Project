try{
   // console.log(a);
   throw new Error("This is an Error")
  
}
catch(e){
  console.log(e.message);
}

finally{
    console.log("hi");
    console.log("Inside Finally")
}

/*a = [1,2,3,4]
console.log(a[4])
b= "hi"
console.log(b+2)*/
