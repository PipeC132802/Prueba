# Prueba

Prueba técnica para demostrar conocimientos en desarrollo backend. Los tres primeros puntos fueron desarrollados en el
framework Django.

## Punto 1

A continuación se explicará el formato de los datos en los endpoints:

* registration/

Para crear un usuario se hace una petición POST
```
    {
      username: '',
      email: '',
      password1: '',
      password2: ''
    }
```

Cuándo el usuario es creado exitosamente, se envía el access_token y refresh token como objeto json y, de igual manera,
se envía el access_token como cookie al cliente.

* login/
Para autenticar el usuario, se hace por medio de peticiones POST.
```
    {
      username: '',
      email: '',
      password: ''
    }
```

Al autenticar correctamente el usuario, se envía el access_token y refresh token como objeto json y, de igual manera, se
envía el access_token como cookie al cliente.

* user/

Para este edpoint, solamente se debe enviar el access_token en el header de la petición de tipo GET.

```
    headers : {
      Authorization: 'Bearer <access_token>'
    }
```

y la respuesta tiene la forma:

```
    {
      pk: 1,
      username: "username",
      email: "user@mail.com",
      first_name: "Firstname",
      last_name: "Lastname"
    }
```

* update-account-info/

Para actualizar la información del usuario, se debe enviar el token en el encabezado y los datos en una solicitud PUT y
con el siguiente formato:

```
    {
        username: "",
        first_name: "",
        last_name: ""
    }
```

* deactivate-account/
  
Para desactivar la cuenta, se hace una petición PUT a este endpoint con el token en el encabezado. Como respuesta se
obtiene un mensaje confirmando la desactivación.

* activate-account/ 
  
Para desactivar la cuenta, se hace una petición PUT a este endpoint.

```
    {
      username: "",
      password: ""
    }
```

* delete-account/

Para eliminar la cuenta se envía el access_token en el encabezado y por medio de una petición DELETE.

