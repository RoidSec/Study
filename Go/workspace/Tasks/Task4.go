package main

import (
	"fmt"
)

type Person struct {
	name string
	age int
	job string
	salary int
}

func main() {
	var pers1 Person
	var pers2 Person
	
	pers1.name = "John"
	pers1.age = 30
	pers1.job = "Carpenter"
	pers1.salary = 55000

	pers2.name = "Jane"
	pers2.age = 25
	pers2.job = "Teacher"
	pers2.salary = 65000

	fmt.Println("Name: ", pers1.name)
	fmt.Println("Age: " , pers1.age)
	fmt.Println("Job: " , pers1.job)
	fmt.Println("Salary: " , pers1.salary)

	fmt.Println("Name: ", pers2.name)
	fmt.Println("Age: " , pers2.age)
	fmt.Println("Job: " , pers2.job)
	fmt.Println("Salary: " , pers2.salary)	

}