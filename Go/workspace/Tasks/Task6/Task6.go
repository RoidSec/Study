package main

import (
	"html/template"
	"net/http"
)

type Contact struct {
	Email   string
	Subject string
	Message string
}

func main() {
	tmpl := template.Must(template.ParseFiles("form.html"))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			tmpl.Execute(w, nil)
			return
		}
		details := Contact{
			Email:   r.FormValue("email"),
			Subject: r.FormValue("subject"),