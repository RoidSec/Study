package main
import ("fmt")

func main() {
  var cars = [4]string{"Volvo", "BMW", "Ford", "Mazda"}
  cars[0]= "Opel"
  fmt.Print(cars)
}