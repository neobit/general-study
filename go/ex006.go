package main

import "fmt"

type balance struct{
	saldo float64
	amountDebited float64
	amountDeposited float64
}

func (b balance) getBalance() float64 {
	return b.saldo
}

func (b * balance) depositValue(saldo float64){
	saldo = b.saldo + b.amountDebited
}

func (b * balance) debitValue(saldo float64){
	if b.saldo < b.amountDebited{
		fmt.Println("Saldo insuficiente")
	} else {
		saldo = b.saldo - b.amountDebited
	}
}

func main() {
	b1 := balance(100, 400, 300)
	fmt.Println(b1.getBalance())
}