package main

import "fmt"

func main() {
	var num1, num2 float64
	fmt.Print("Digite o primeiro valor: ")
	fmt.Scanln(&num1)
	fmt.Print("Digite o segundo valor: ")
	fmt.Scanln(&num2)

	sum := num1 + num2
	fmt.Println("A soma dos dois valores é igual a:", sum)
}
