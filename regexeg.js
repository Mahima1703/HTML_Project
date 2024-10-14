//const pattern = /a{3,}/
//const text = "aaaaaa"
//console.log(text.search(pattern))

const myset =  new Set(['Apple','Orange','Mango',1,'Apple'])
console.log(myset)
myset.add('Getin')
console.log(myset)
//myset.clear()
//console.log(myset)
myset.delete('Mango')
console.log(myset)
console.log(myset.entries())
console.log(myset.keys())
console.log(myset.values())

myset.forEach(function(value,key,myset){
    console.log(key)
})