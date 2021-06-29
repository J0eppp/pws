package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type Subject string

type Name string

type Group struct {
	Subjects []Subject

}



type Availability [][]uint8

type Teacher struct {
	Name Name `json:"name"`
	Subject Subject `json:"subject"`
	Availability Availability `json:"availability"`
}

func main() {
	file, err := os.Open("../../test_data/dsatur_test_data.json")

	if err != nil {
		panic(err)
	}

	byteValue, err := ioutil.ReadAll(file)

	data := struct {
		Subjects []Subject `json:"subjects"`
		Groups []Group `json:"groups"`
		Teachers []Teacher `json:"teachers"`
	}{}

	json.Unmarshal(byteValue, &data)

	fmt.Printf("%+v\n", data)
}
