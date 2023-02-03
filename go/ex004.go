package main

import (
	"fmt"
)

func main(){
	var idade float64
	fmt.Print("Insira a idade do nadador: ")
	fmt.Scanln(&idade)

	var categoria string
	if idade <= 9{
		categoria = fmt.Sprintf("Esse nadador é da categoria MIRIM, visto que ele tem %.0f anos.", idade)
	}else if idade > 9 && idade <= 14 {
		categoria = fmt.Sprintf("Esse nadador é da categoria INFANTIL, visto que ele tem %.0f anos.", idade)
	}else if idade > 14 && idade <= 19 {
		categoria = fmt.Sprintf("Esse nadador é da categoria JUNIOR, visto que ele tem %.0f anos.", idade)
	}else if idade > 19 && idade <= 20 {
		categoria = fmt.Sprintf("Esse nadador é da categoria SÊNIOR, visto que ele tem %.0f anos.", idade)
	}else if idade > 20 {
		categoria = fmt.Sprintf("Esse nadador é da categoria MASTER, visto que ele tem %.0f anos.", idade)
	}

	fmt.Println(categoria)
}