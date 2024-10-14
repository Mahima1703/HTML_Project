let modules = {

	frontend: ["HTML","CSS"],
	backend: ["Java","Python"],
	tools: ["git","Jenkins"]
};


let is_ins_open = true;


let course = (time,work) => {

	return new Promise( (resolve,reject) => {
		
		/*if(is_ins_open){
			
			resolve(work())
		}*/
        
if(is_ins_open){

	setTimeout(()=> {resolve(work())},time);
}
		else{
			
			reject(console.log(" Closed"));
		}
    });
}


//now we need to create a relationship with time also..




course(2000, () => console.log(`${modules.frontend[0]} was selected`))


.then (()=>{
    return course(1000,()=>{console.log("Front End Selected")});
})

.then(()=>{
    return course(1000,()=>{console.log(" Back End Selected")});
})

.catch(()=>{

    console.log(" Closed !!!!")
})

.finally(()=>{

    console.log("Thank you");
})