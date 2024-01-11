
// This is a closure in javascript

function outter(func){
    function inner(num){
        return num * 2
    }
    return inner
}


inner = outter()

console.log(inner(2))
