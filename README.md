# Prueba
Prueba técnica para demostrar conocimientos en desarrollo backend. Los tres primeros puntos fueron desarrollados en el framework Django.

## Punto 1
A continuación se explicará el formato de los datos en los endpoints:
* registration/
```
    {
      username: '',
      email: '',
      password1: '',
      password2: ''
    }
```
Cuándo el usuario es creado exitosamente, se envía el access_token y refresh token como objeto json y, de igual manera, se envía el access_token como cookie al cliente.

* login/
```
    {
      username: '',
      email: '',
      password: ''
    }
```

Al autenticar correctamente el usuario, se envía el access_token y refresh token como objeto json y, de igual manera, se envía el access_token como cookie al cliente.
