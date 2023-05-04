# Taller-pytest
###PRUEBAS ENDPOINTS
~~~
Endpoint Hello:
curl -X 'GET' \
  'http://127.0.0.1:8000/hello' \
  -H 'accept: application/json'
~~~  
~~~
Endpoint Is_prime respuesta False:
curl -X 'GET' \
  'http://127.0.0.1:8000/IsPrime/4' \
  -H 'accept: application/json'
  ~~~
  ~~~
Endpoint Is_prime respuesta True:
curl -X 'GET' \
  'http://127.0.0.1:8000/IsPrime/2' \
  -H 'accept: application/json' 
 ~~~
 ~~~
  Endpoint Fibonacci correcto:

  curl -X 'GET' \
  'http://127.0.0.1:8000/fibonacci/11' \
  -H 'accept: application/json'
  ~~~
