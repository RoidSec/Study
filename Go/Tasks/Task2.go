package main

import (
	"errors"
	"fmt"
)

func f1(arg int) (int, error) {
if arg == 42 {

// `errors.New` constructs a basic `error` value
// with the given error message.
return -1, errors.New("cant work with 42")

}

// error value of nil means no error
return arg + 3, nil
}

func main() {
for _, i := range []int{7, 42} {
if r, e := f1(i); e != nil {
fmt.Println("f1 failed:", e)
} else {
fmt.Println("f1 worked:", r)
}
}
}