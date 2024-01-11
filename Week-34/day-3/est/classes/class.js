


class Car {
    constructor(model, name){
        this.model = model
        this.name = name
    }


    static makeClass(arr){
        const newCars = [];
        for(let car of arr){
            const {model, name} = car
            const newCar = new Car(model, name);
            newCars.push(newCar)
        }
        return newCars
    }
}


const civic = new Car("Honda", "civic")


// const newCarsToMake = [
//     {
//         model: "Nissan",
//         name: "Altima"
//     },
//     {
//         model: "Mercedes-Benz",
//         name: "CLA"
//     }
// ]

console.log(civic)

// const newCars = Car.makeClass(newCarsToMake)

// console.log(newCars)
