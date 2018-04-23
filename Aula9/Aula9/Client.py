import requests as Req 

Req.api.post("http://localhost/Alunos/add", json={"Id":"1", "Nome":"Tenis" , "Status":"Ativo"})
Req.api.post("http://localhost/Alunos/add", json={"Id":"2", "Nome":"Martelo", "Status":"Ativo"})
Req.api.delete("http://localhost/Alunos/del/1")
Req.api.put("http://localhost/Alunos/alter", json={"Id":"1", "Nome":"Sapato" , "Status":"Ativo"})
print("Ok")
